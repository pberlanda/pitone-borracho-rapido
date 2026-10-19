# pitone-borracho-rapido

1. crea l'ambiente virtuale, attivalo e installa le dipendenze (fastapi uvicorn)

       python -m venv venv
       source venv/bin/activate
       pip install fastapi uvicorn

2. scrivi il codice
3. avvio del server

        uvicorn app:app --reload --host 0.0.0.0

4. test API
- tutti i libri /libri
- un libro /libro/2
- aggiungi un libro: usa un JSON

        {
            "id": 3,
            "titolo": "Ti con zero",
            "autore": "Italo Calvino"
        }
  oppure usa il form /form
 
5. FastAPI cre la documentazione automatica
- /docs
- /redocs


qui per [altro](https://chatgpt.com/share/6ad6474c-77d8-83ed-8d77-99d2a3040750)