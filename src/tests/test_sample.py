import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert "text/html" in response.headers["content-type"]

def test_read_consultations():
    response = client.get("/consultations")
    assert response.status_code == 200
    assert "consultations" in response.json()

def test_read_enseignants():
    response = client.get("/enseignants")
    assert response.status_code == 200
    assert "enseignants" in response.json()

def test_read_cours():
    response = client.get("/cours")
    assert response.status_code == 200
    assert "cours" in response.json()

def test_read_promotions():
    response = client.get("/promotions")
    assert response.status_code == 200
    assert "promotions" in response.json()

def test_read_utilisateurs():
    response = client.get("/utilisateurs")
    assert response.status_code == 200
    assert "utilisateurs" in response.json()

def test_read_salles():
    response = client.get("/salles")
    assert response.status_code == 200
    assert "salles" in response.json()
