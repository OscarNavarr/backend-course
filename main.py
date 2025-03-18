from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi import Request
import psycopg2
import uvicorn

# from pyngrok import ngrok

connection = psycopg2.connect(database="val_max_alex_oscar", user="postgres", password="Aucun66", host="localhost", port=5432)

cursor = connection.cursor()

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

# config html templates
templates = Jinja2Templates(directory="src/main")

# config static files
app.mount("/static", StaticFiles(directory="src/main/static"), name="static")

# public_url = ngrok.connect(8000)
# print(f"🔗 Public URL: {public_url}")


@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {
            "request": request,
            "consultations" : cons_record,
            "enseignants" : ens_record,
            "cours" : cours_record,
            "promotions" : promo_record,
            "utilisateurs" : users_record,
            "salles" : salles_record
        })

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


if __name__ == "__main__":
    uvicorn.run(app, host='127.0.0.1', port=8000)

