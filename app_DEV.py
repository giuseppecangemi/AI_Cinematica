from flask import Flask, request, render_template
import openai
import pandas as pd
import os
from dotenv import load_dotenv
from openai import OpenAI
from datetime import datetime

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY") 
client = OpenAI()

CSV_PATH = 'movies.csv'  
df = pd.read_csv(CSV_PATH)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    genre = request.form.get('genre')
    user_score_min = float(request.form.get('user_score_min'))
    user_score_max = float(request.form.get('user_score_max'))
    release_date_min = int(request.form.get('release_date_min'))
    release_date_max = int(request.form.get('release_date_max'))

    movie_list = df[['title', 'user_score', 'release_date']].sample(n=500).to_dict(orient='records')
    movie_list_str = "\n".join([f"{m['title']} ({m['release_date']}, Punteggio: {m['user_score']})" for m in movie_list])

    #shuffled_movies = df.sample(frac=1).head(500)
    #movie_list = shuffled_movies.to_string(index=False)
    #timestamp = datetime.now().isoformat()

    #prompt
    response_text = ""
    stream = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": f"""
                Considera la seguente lista di film con i dettagli (titolo, generi, punteggio utente, data di uscita):
                {movie_list_str}

                L'utente ha fornito i seguenti criteri:
                - Genere: {genre}
                - Punteggio Utente: {user_score_min} a {user_score_max}
                - Anno di Uscita: {release_date_min} a {release_date_max}

                Si prega di consigliare alcuni film che corrispondano ai criteri dell'utente. Fai in seguenza anche una brevissima descrizione per ogni film consigliato.
                Questo output che generi deve contenere il titolo, il punteggio utente, la data di uscita (in formato yyyy-mm-dd) e la descrizione richiesta.
                """
                }],
        stream=True,
    )


    for chunk in stream:
        if chunk.choices[0].delta.content is not None:
            response_text += chunk.choices[0].delta.content

    #per andare a capo (lasciare spazio)
    response_text = response_text.replace("\n", "<br>")

    return render_template('predict.html', 
                           response_text=response_text, 
                           genre=genre,
                           user_score_min=user_score_min,
                           user_score_max=user_score_max,
                           release_date_min=release_date_min,
                           release_date_max=release_date_max)


if __name__ == '__main__':
    app.run(debug=True)