
## This is an MLOps demo using Azure Function Apps
This demo illustrates on how to use MLOps principles to deploy machine learning models in Azure. The models are deployed using fastapi as well as
Azure function app.


### Install Poetry
For macOS install poetry following [this link](https://formulae.brew.sh/formula/poetry).


### Create a repo in GitHub and name it MLOpsDemo

### Create a repo on your machine
```
mkdir model-deploy
cd /model-deploy
git init
```

### Sync local repo with GitHub repo
```
git switch -c main
git add .
git commit -m "first commit"
git add remote origin https://github.com/<your username>/MLOpsDemo.git
```

### Install dependencies using Poetry

```
poetry init
poetry add scikit-learn pandas pydantic uvicorn fastapi requests
```
When initializing poetry ensure that you change python ^3.11 to ^3.8.

### Make the following directories:
```
mkdir -p .github/workflows
mkdir src
mkdir model
```
Inside the *.github/workflows* directory, add the following workflows/piplines:

IaC.yml \
acr.yml \
functionapp.yml \
cleanup.yml

Inside the *model* directory, simply include your saved model model.pkl.

Inside the *src* directory, add the following:
app.py

### Include Service Principal in your repo
1. Generate a service principal using [here](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-setup-authentication?view=azureml-api-2&tabs=sdk#configure-a-service-principal) to connect your repo with Azure.
2. Save the generated json output as AZURE_CREDENTIALS by going to settings>>secrets and variables>>actions>>new repository secret





