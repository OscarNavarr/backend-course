from typing import Annotated

from fastapi import Depends, FastAPI, HTTPException, Query
from sqlmodel import Field, Session, SQLModel, create_engine, select


class Planning(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    age: int | None = Field(default=None, index=True)
    secret_name: str


sqlite_file_name = "database.db"
# sqlite_url = f"sqlite:///{sqlite_file_name}"
sqlite_url = "postgrsql://postgre:Aucun66000!@localhost:5432/val_max_alex_oscar"

connect_args = {"echo": True}
engine = create_engine(sqlite_url, connect_args=connect_args)


# def create_db_and_tables():
#     SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session


SessionDep = Annotated[Session, Depends(get_session)]

app = FastAPI()

# @app.on_event("startup")
# def on_startup():
#     create_db_and_tables()

# @app.post("/heroes/")
# def create_hero(hero: Hero, session: SessionDep) -> Hero:
#     session.add(hero)
#     session.commit()
#     session.refresh(hero)
#     return hero


@app.get("/planning/")
def read_plannings(
    session: SessionDep,
    offset: int = 0,
    limit: Annotated[int, Query(le=100)] = 100,
) -> list[Planning]:
    plannings = session.exec(select(Planning).offset(offset).limit(limit)).all()
    return plannings


@app.get("/planning/{planning_id}")
def read_planning(planning_id: int, session: SessionDep) -> Planning:
    planning = session.get(Planning, planning_id)
    if not planning:
        raise HTTPException(status_code=404, detail="Planning not found")
    return planning