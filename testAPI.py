import openai
import pandas as pd
import os
from dotenv import load_dotenv
from openai import OpenAI
import re
# Carica le variabili d'ambiente dal file .env
load_dotenv()

# Configurazione di OpenAI
openai.api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI()

# Percorso del file CSV che contiene i dati sui film
CSV_PATH = 'movies.csv'  # O usa 'movies.xlsx' per un file Excel

# Carica il file CSV in un DataFrame Pandas
df = pd.read_csv(CSV_PATH)  # Usa pd.read_excel(CSV_PATH) se hai un file Excel

# Input dell'utente (esempio)
genre = "Action"  # esempio di input
user_score_min = 7.0
user_score_max = 10.0
release_date_min = 2000
release_date_max = 2020

# Limita il numero di film nel prompt per evitare di superare i limiti di token
movie_list = df[['title', 'genres', 'user_score', 'release_date']].head(20).to_string(index=False)

stream = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": f"""
            Consider the following list of movies with details (title, genres, user_score, release_date):
            {movie_list}

            The user has provided the following preferences:
            - Genre: {genre}
            - User Score: {user_score_min} to {user_score_max}
            - Release Date: {release_date_min} to {release_date_max}

            Please recommend a few movies that match the user's preferences.
            """
            }],
    stream=True,
)

# Estrai e formatta i risultati
for chunk in stream:
    if chunk.choices[0].delta.content is not None:
         print(chunk.choices[0].delta.content, end="")

