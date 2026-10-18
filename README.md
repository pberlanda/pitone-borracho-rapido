# pitone-borracho-rapido

1. crea l'ambiente virtuale, attivalo e installa le dipendenze (fastapi uvicorn)
- {python -m venv venv}
- {source venv/bin/activate}
- {pip install fastapi uvicorn}

2. scrivi il codice
3. avvio del server
{uvicorn app:app --reload}
4. test API
- tutti i libri http://127.0.0.1:8000/libri
- un libro http://127.0.0.1/libro/2
- aggiungi un libro: usa un JSON
{
    "id": 3,
    "titolo": "Ti con zero",
    "autore": "Italo Calvino"
}
5. FastAPI cre la documentazione automatica
- http://127.0.0.1:8000/docs
- http://127.0.0.1:8000/redocs