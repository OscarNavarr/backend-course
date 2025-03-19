from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi import Request
import psycopg2
import uvicorn

# Fonction pour créer une connexion à la base de données
def get_db_connection():
    return psycopg2.connect(database="val_max_alex_oscar", user="postgres", password="Aucun66", host="localhost", port=5432)

app = FastAPI()

# Configuration des templates et fichiers statiques
templates = Jinja2Templates(directory="src/main")
app.mount("/static", StaticFiles(directory="src/main/static"), name="static")

# Récupération dynamique des données
def fetch_data(query):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute(query)
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return data

# Création des routes
@app.get("/", response_class=HTMLResponse)  # Cette route gèrera la page d'acceuil/index
async def read_root(request: Request):      # Request est spécifique à Jinja2
    return templates.TemplateResponse({
            "request": request,
            "consultations": fetch_data("SELECT * FROM public.consultations"),
            "enseignants": fetch_data("SELECT * FROM public.enseignants"),
            "cours": fetch_data("SELECT * FROM public.cours"),
            "promotions": fetch_data("SELECT * FROM public.promotions"),
            "utilisateurs": fetch_data("SELECT * FROM public.utilisateurs"),
            "salles": fetch_data("SELECT * FROM public.salles"),
        }, "index.html")

@app.get("/consultations")
def read_consultations():
    return {"consultations" : fetch_data("SELECT * FROM public.consultations")}

@app.get("/enseignants")
def read_enseignants():
    return {"enseignants" : fetch_data("SELECT * FROM public.enseignants")}

@app.get("/cours")
def read_cours():
    return {"cours" : fetch_data("SELECT * FROM public.cours")}

@app.get("/promotions")
def read_promotions():
    return {"promotions" : fetch_data("SELECT * FROM public.promotions")}

@app.get("/utilisateurs")
def read_utilisateurs():
    return {"utilisateurs" : fetch_data("SELECT * FROM public.utilisateurs")}

@app.get("/salles")
def read_salles():
    return {"salles" : fetch_data("SELECT * FROM public.salles")}

# Code éxecuté au lancement de l'application
if __name__ == "__main__":
    uvicorn.run(app, host='127.0.0.1', port=8000) # Lancement du server

