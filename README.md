# Funzioni Inefficienti

Questa repository contiene un insieme di funzioni Python che verranno utilizzate per esercizi di ottimizzazione e green coding. L'obiettivo è migliorare l'efficienza delle funzioni esistenti e verificare le modifiche tramite Docker e GitHub Actions.

## Struttura della Repository

- `python.py`: Contiene le funzioni Python da ottimizzare.
- `Dockerfile`: Definisce l'ambiente Docker per eseguire il programma.
- `.github/workflows/python_workflow.yml`: Configura un workflow GitHub Actions per eseguire il programma e catturare l'output.

## Prerequisiti

- Docker
- Git
- Python 3.8 o superiore
- Pip (gestore di pacchetti per Python)

## Installazione di Python e Pip

### Installazione di Python

#### Windows

1. Scarica l'installer di Python dal sito ufficiale: [Python.org](https://www.python.org/downloads/).
2. Esegui l'installer e segui le istruzioni. Assicurati di selezionare l'opzione "Add Python to PATH" durante l'installazione.

#### macOS

1. Apri il Terminale.
2. Installa Homebrew se non lo hai già installato seguendo le istruzioni su [brew.sh](https://brew.sh/).
3. Esegui il seguente comando per installare Python:

```
brew install python
```


### Installazione di Pip
Se non hai pip installato, puoi installarlo utilizzando il seguente comando:

```
python -m ensurepip --upgrade
```


## Istruzioni

### Clonare la Repository

Per clonare la repository, eseguire il seguente comando:

```
git clone https://github.com/tiziano093/funzioni_inefficienti.git
cd funzioni_inefficienti
```


### Creare un Branch
Prima di apportare modifiche, crea un nuovo branch utilizzando il tuo nome e cognome. Ad esempio, se il tuo nome è Mario Rossi, esegui:

```
git checkout -b mario-rossi
```



### Installare le Dipendenze
Per eseguire il codice in locale, è necessario installare le dipendenze:
```
pip install psutil memory_profiler
```

### Eseguire il Programma in Locale
Per eseguire il programma in locale, utilizzare il seguente comando:
```
python python.py
```


### Costruire e Eseguire il Programma con Docker 
Per costruire l'immagine Docker ed eseguire il programma, eseguire i seguenti comandi:
```
docker build -t funzioni_inefficienti .
docker run funzioni_inefficienti
```


### Pushare le Modifiche
Dopo aver apportato le modifiche e verificato che funzionano correttamente, puoi pushare le modifiche al tuo branch:

```
git add .
git commit -m "Descrizione delle modifiche"
git push origin nome-del-branch
```


Ad esempio, se il tuo branch si chiama mario-rossi, esegui:
```
git push origin mario-rossi
```


### Eseguire il Workflow GitHub Actions
Il workflow GitHub Actions verrà eseguito automaticamente quando pushi le modifiche. Questo workflow esegue il programma e carica il file output.log come artefatto.

### Differenze tra Esecuzioni
Questo esercizio dimostra la differenza nell'eseguire lo stesso codice su diverse macchine e sistemi:

- Locale: Eseguendo il codice sulla tua macchina locale, le prestazioni possono variare a seconda delle specifiche hardware e del sistema operativo. Questo ti permette di vedere come il codice si comporta nel tuo ambiente di sviluppo, confronta i risultati con i tuoi compagni.
- Docker: Docker fornisce un ambiente isolato e coerente, indipendente dalla macchina host. Questo può aiutare a eliminare le variabili legate all'hardware e al sistema operativo, ma può introdurre un sovraccarico dovuto alla virtualizzazione.
- GitHub Actions: Eseguire il codice su GitHub Actions permette di automatizzare i test e le verifiche in un ambiente server. Questo è utile per garantire che il codice funzioni correttamente in un ambiente standardizzato e per confrontare le prestazioni con altri ambienti.

### Impatto del Linguaggio
Anche il linguaggio di programmazione può influire sull'uso delle risorse e sulle prestazioni. Python, ad esempio, è noto per essere facile da leggere e scrivere, ma può essere meno efficiente in termini di uso della CPU e della memoria rispetto a linguaggi compilati come C++ o Go.

# Obiettivo dell'Esercizio
L'obiettivo di questo esercizio è migliorare l'efficienza delle funzioni nel file python.py e verificare che le modifiche rispettino le pratiche di green coding. Utilizza Docker per garantire che l'ambiente di esecuzione sia coerente e GitHub Actions per automatizzare la verifica delle modifiche.

# Buon lavoro!