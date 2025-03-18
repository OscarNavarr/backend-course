from typing import Union
from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
# from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import psycopg2
import pytest

connection = psycopg2.connect(database="val_max_alex_oscar", user="postgres", password="Aucun66", host="localhost", port=5432)

cursor = connection.cursor()

# cursor.execute("""
#     SELECT * from public.consultations
#     SELECT * from public.enseignants;"
#     SELECT * from public.cours;" +
#     SELECT * from public.promotions;" 
#     SELECT * from public.utilisateurs;
#     SELECT * from public.salles;"""
# )

cursor.execute("SELECT * from public.consultations;")
cons_record = cursor.fetchall()
cursor.execute("SELECT * from public.enseignants;")
ens_record = cursor.fetchall()
cursor.execute("SELECT * from public.cours;")
cours_record = cursor.fetchall()
cursor.execute("SELECT * from public.promotions;")
promo_record = cursor.fetchall()
cursor.execute("SELECT * from public.utilisateurs;")
users_record = cursor.fetchall()
cursor.execute("SELECT * from public.salles;")
salles_record = cursor.fetchall()

print("Data from Database:- ", cons_record)

app = FastAPI()


@app.get("/")
def read_root():
    return {
            "consultations" : cons_record,
            "enseignants" : ens_record,
            "cours" : cours_record,
            "promotions" : promo_record,
            "utilisateurs" : users_record,
            "salles" : salles_record
        }

@app.get("/consultations")
def read_cons():
    return {"consultations" : cons_record}

@app.get("/enseignants")
def read_cons():
    return {"enseignants" : ens_record}

@app.get("/cours")
def read_cons():
    return {"cours" : cours_record}

@app.get("/promotions")
def read_cons():
    return {"promotions" : promo_record}

@app.get("/utilisateurs")
def read_cons():
    return {"utilisateurs" : users_record}

@app.get("/salles")
def read_cons():
    return {"salles" : salles_record}

# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}

app.mount("/src", StaticFiles(directory="src", html=True), name="src")


# You can add additional URLs to this list, for example, the frontend's production domain, or other frontends.
# allowed_origins = [
#     "http://localhost:5500"
# ]

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=allowed_origins,
#     allow_credentials=True,
#     allow_methods=["GET", "POST", "PUT", "DELETE"],
#     allow_headers=["X-Requested-With", "Content-Type"],
# )


if __name__ == "__main__":
    uvicorn.run(app, host='127.0.0.1', port=8000)

