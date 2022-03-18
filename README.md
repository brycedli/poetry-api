# poetry-api
Restful poetry is a minimalistic server under development that provides restful API to power my language-based generative AI projects.  

# <h2>Current API endpoints </h2>

<b> /generate (WIP) </b>:
Generates text based on existing model of poetry (currently Edgar Allen Poe) 

<b> /emotion</b>:
Assigns emotional scores to text.

<br> 

# <h2>Deploying project </h2>

Submit image
```
gcloud builds submit --tag gcr.io/<PROJECT_ID>/poetryapp
```
Deploy
```
gcloud run deploy --image gcr.io/<PROJECT_ID>/poetryapp
```
# <h2>Flask CLI reference </h2>
```
export FLASK_APP=main
flask run
```
