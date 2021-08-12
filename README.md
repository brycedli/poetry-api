# restful-poetry
Restful poetry is a minimalistic server that provides restful API to power my language-based generative AI projects.  

Submit
```
gcloud builds submit --tag gcr.io/<PROJECT_ID>/poetryapp
```
Build
```
gcloud run deploy --image gcr.io/<PROJECT_ID>/poetryapp
```