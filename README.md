# poetry-api
Restful poetry is a minimalistic server under development that provides restful API to power my language-based generative AI projects.  

# <h2>Current API endpoints </h2>

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