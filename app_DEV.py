from flask import Flask, request, render_template
import openai
import pandas as pd
import os
from dotenv import load_dotenv
from openai import OpenAI

# Carica le variabili d'ambiente dal file .env
load_dotenv()

# Configurazione di OpenAI
openai.api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI()

# Percorso del file CSV che contiene i dati sui film
CSV_PATH = 'movies.csv'  # Modifica il percorso se necessario

# Carica il file CSV in un DataFrame Pandas
df = pd.read_csv(CSV_PATH)

# Inizializza l'app Flask
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Recupera i dati dal form
    genre = request.form.get('genre')
    user_score_min = float(request.form.get('user_score_min'))
    user_score_max = float(request.form.get('user_score_max'))
    release_date_min = int(request.form.get('release_date_min'))
    release_date_max = int(request.form.get('release_date_max'))

    # Limita il numero di film nel prompt per evitare di superare i limiti di token
    movie_list = df[['title', 'genres', 'user_score', 'release_date']].head(20).to_string(index=False)

    # Richiesta di completamento della chat con OpenAI (streaming)
    response_text = ""
    stream = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": f"""
                Consider the following list of movies with details (title, genres, user_score, release_date):
                {movie_list}

                The user has provided the following preferences:
                - Genre: {genre}
                - User Score: {user_score_min} to {user_score_max}
                - Release Date: {release_date_min} to {release_date_max}

                Please recommend a few movies that match the user's preferences. Each movie should be listed on a new line, with details such as title, genre, user score, and release date.
                """
                }],
        stream=True,
    )

    # Estrai e formatta i risultati dallo stream
    for chunk in stream:
        if chunk.choices[0].delta.content is not None:
            response_text += chunk.choices[0].delta.content

    # Sostituire i ritorni a capo con <br> per visualizzare ogni film su una nuova riga
    response_text = response_text.replace("\n", "<br>")

    return f"<h1>Recommended Movies:</h1><p>{response_text}</p>"

if __name__ == '__main__':
    app.run(debug=True)
