from fastapi import FastAPI
from fastapi.responses import FileResponse
from pydantic import BaseModel

# inzializzo l'app
app = FastAPI()

# modello dei ati (schema del libro)
class Libro(BaseModel):
    id: int
    titolo: str
    autore: str

# dati di esempio
libri = [
    {"id": 1, "titolo": "L'uomo invisibile", "autore": "H.G. Wells"},
    {"id": 2, "titolo": "Il fu Mattia Pascal", "autore": "Luigi Pirandello"},
    {"id": 3, "titolo": "Ti con zero", "autore": "Italo Calvino"}
]

# GET: tutti i libri
@app.get("/libri")
def get_libri():
    return libri

# GET: un libro
@app.get("/libro/{id}")
def get_libro(id: int):
    for libro in libri:
        if libro["id"] == id:
            return libro
    return {"errore":"libro non trovato"}

# POST: aggiunge un libro
@app.post("/libri")
def add_libri(libro: Libro):
    libri.append(libro.dict()) # converte l'oggetto libro in un dizionario
    return libro

# form HTML
@app.get("/form")
def showForm():
    return FileResponse("static/form.html")