
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

### Sync loal repo with GitHub repo
```
git switch -c main
git add .
git commit -m "first commit"
git add remote origin https://github.com/<your username>/MLOpsDemo.git
```

### Install dependencies using Poetry

```
poetry init
poetry add scikit-learn pandas pydantic uvicorn fastapi
```