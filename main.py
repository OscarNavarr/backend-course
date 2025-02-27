from typing import Union
from fastapi import FastAPI, HTTPException
import uvicorn
import psycopg2

connection = psycopg2.connect(database="val_max_alex_oscar", user="postgres", password="Aucun66", host="localhost", port=5432)

cursor = connection.cursor()

cursor.execute("SELECT * from public.salles;")

# Fetch all rows from database
record = cursor.fetchall()

print("Data from Database:- ", record)

app = FastAPI()

if __name__ == "__main__":
    uvicorn.run(app, host='0.0.0.0', port=8000)

@app.get("/")
def read_root():
    return record

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}