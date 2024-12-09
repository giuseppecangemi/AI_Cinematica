# Documentazione App "AI Cinematica"

Questa applicazione web consiglia film basati sui criteri selezionati dall'utente, utilizzando un modello **GPT-4o-mini** per generare suggerimenti personalizzati.

## Descrizione

L'applicazione è costruita con Flask e utilizza OpenAI GPT-4o-mini per consigliare film in base a:
- Genere
- Punteggio IMDb
- Data di uscita

L'utente inserisce i suoi criteri e l'intelligenza artificiale fornisce una lista di film che corrispondono a questi parametri.

## Tecnologie Utilizzate
- **Flask**: Framework web in Python per la gestione delle richieste HTTP.
- **OpenAI GPT-4o-mini**: Modello di intelligenza artificiale per generare risposte personalizzate.
- **Pandas**: Per la gestione e manipolazione dei dati (CSV).
- **Python-dotenv**: Per la gestione delle variabili d'ambiente (API Key di OpenAI).
- **HTML & CSS**: Per la creazione dell'interfaccia utente.


## Utilizzo

Accedi all'app dal browser. Seleziona il genere, il punteggio IMDb minimo e massimo e l'intervallo di anni di uscita. Clicca su "Trova Film" per ottenere i suggerimenti personalizzati basati sui criteri selezionati.

## Funzionamento

Quando l'utente invia il modulo, l'app:
1. Filtra un campione di 500 film casuali dal dataset.
2. Invia i dati a OpenAI **GPT-4o-mini** per generare raccomandazioni basate sui criteri specificati.
3. Mostra i film consigliati, insieme a una breve descrizione per ogni film.

## Perché perferirlo a ChatGPT?

Sebbene ChatGPT possa essere utile per rispondere a domande generali, l'app di raccomandazione di film offre una serie di vantaggi specifici che migliorano l'esperienza dell'utente:

### 1. **Personalizzazione Avanzata**
L'app permette all'utente di definire criteri specifici, come il genere, il punteggio IMDb e l'intervallo di data di uscita. Questo approccio consente di ottenere raccomandazioni molto più mirate e adatte ai gusti personali dell'utente, senza dover chiedere più volte o fornire dettagli extra ogni volta.

### 2. **Raccomandazioni Basate su Dati**
L'app utilizza un dataset di film reali, che può essere facilmente aggiornato. In questo modo, le raccomandazioni non sono solo teoriche, ma si basano su dati concreti e su un algoritmo che filtra i film in modo sistematico. ChatGPT, al contrario, potrebbe non avere accesso agli stessi dati specifici o essere limitato nel fornire suggerimenti accurati e dettagliati.

### 3. **Automazione e Rapidità**
Con l'app, tutto il processo di selezione dei film avviene in modo automatizzato e istantaneo. L'utente non ha bisogno di formulare ogni volta richieste dettagliate a ChatGPT, che potrebbe richiedere più tempo per generare risposte. In questo caso, l'intelligenza artificiale risponde immediatamente con una lista di film, senza che l'utente debba fare più passaggi.

### 4. **Accesso Continuo e Scalabilità**
L'applicazione è accessibile 24/7 online tramite **Render**. ChatGPT, invece, può essere soggetto a limitazioni di accesso o di capacità di risposta, specialmente in situazioni ad alto traffico o per utenti con limiti nell'uso delle API.


## Versione Online

L'applicazione è anche disponibile online all'indirizzo:  
[https://ml-ai-webservice.onrender.com](https://ml-ai-webservice.onrender.com)

Questa versione è stata pubblicata su **Render**, una piattaforma che permette di eseguire e distribuire applicazioni web in modo semplice e scalabile. Render offre un'infrastruttura cloud che automatizza il deployment e la gestione delle applicazioni, consentendo agli sviluppatori di concentrarsi sul codice senza preoccuparsi della gestione dei server.

## Contribuire

Forka questo repository, crea un branch per la tua funzionalità, aggiungi i tuoi cambiamenti, e invia una pull request.

## Licenza

Questo progetto è sotto la [MIT License](LICENSE).
