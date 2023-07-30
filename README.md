
## This is an MLOps demo using Azure Function Apps
This demo illustrates how to use MLOps principles to deploy machine learning models in Azure. The models are deployed using fastapi as well as
Azure function app.


### Install Poetry
For macOS install poetry following [this link](https://formulae.brew.sh/formula/poetry). For other OS please use this [link](https://python-poetry.org/docs/)


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

In the generated *pyproject.toml* file, please remove the line *packages = [{include = "model_deploy"}]*

### Make the following directories:
```
mkdir -p .github/workflows
mkdir src
mkdir model
```
Inside the **.github/workflows** directory, add the following workflows/piplines:

IaC.yml \
acr.yml \
functionapp.yml \
cleanup.yml

Inside the **model** directory, simply include your saved model *model.pkl*.

Inside the **src** directory, add the following: \
app.py

### Include Service Principal in your repo
1. Generate a service principal using [here](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-setup-authentication?view=azureml-api-2&tabs=sdk#configure-a-service-principal) to connect your repo with Azure.
2. Save the generated json output as AZURE_CREDENTIALS by going to your repo (MLOpsDemo) *settings >> secrets and variables >> actions >> new repository secret*

### Run workflows
1. Start by running workflow *IaC*.
2. Go to Azure Portal and see your created resource group *RG*, in that resource group try, you will see an azure container registry named *modelcontainerxd*.
3. Open *modelcontainerxd* in Azure portal and go to Access Keys, you will see the username and password.
4. Copy the username and password and save them as DOCKER_USERNAME and DOCKER_PASSWORD under secrets in your GitHub repo, respectively.
5. Run the workflow *acr*.
6. Run the workflow *functionapp*.

### Cleanup
1. Once all your workflows run succesfully, go to your Azure portal.
2. Under your resource group *RG*, you will see a function app called *modeldeployxd*.
3. In your function app, you will see the URL *https://modeldeployxd.azurewebsites.net*.
4. Copy and paste the URL in your browser, you should see a message "Welcome to the API". If you don't get that message try to debug the error.
5. To interact with the model go to *https://modeldeployxd.azurewebsites.net/docs*, you will see a fastapi with GET and POST methods.
6. In your *app.py*, there is an example of the input for the POST method, please use that example and click execute.
7. **Once happy, please run the workflow cleanup to remove all the resource in Azure.**





