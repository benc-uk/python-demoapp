# Python Flask - Demo Web Application
This is a simple Python Flask web application. The app provides system information and a realtime monitoring screen with dials showing CPU, memory, IO and process information.

The app has been designed with cloud native demos & containers in mind, in order to provide a real working application for deployment, something more than "hello-world" but with the minimum of pre-reqs. It is not intended as a complete example of a fully functioning architecture or complex software design.

Typical uses would be deployment to Kubernetes, demos of Docker, CI/CD (build pipelines are provided), deployment to cloud (Azure) monitoring, auto-scaling

## Screenshot
![screen](https://user-images.githubusercontent.com/14982936/30533171-db17fccc-9c4f-11e7-8862-eb8c148fedea.png)

## Locally via Python
Python 3.6+ is required and has been tested on Windows and Linux (Ubuntu 18.04)

Simply run with `python run.py` the script should start the app, and set Flask listening on port 5000, you can change the port with the environmental variable `PORT`.  
Go to `http://localhost:5000` to view the app.  

## Running as Docker Container
The image is publicly available on [GitHub Container Registry](https://hub.docker.com/r/bencuk/python-demoapp/) so running it in Docker is simple `docker run --rm -it -p 5000:5000 ghcr.io/benc-uk/python-demoapp`

The container runs on Debian Linux and is configured to use the latest version of Python (3.6.2 at the time of writing)


# GitHub Actions CI/CD 
A working set of CI and CD release GitHub Actions workflows are provided `.github/workflows/`, automated builds are run in GitHub hosted runners

### [GitHub Actions](https://github.com/benc-uk/python-demoapp/actions)

[![](https://img.shields.io/github/workflow/status/benc-uk/python-demoapp/CI%20Build%20App)](https://github.com/benc-uk/python-demoapp/actions?query=workflow%3A%22CI+Build+App%22)

[![](https://img.shields.io/github/workflow/status/benc-uk/python-demoapp/CD%20Release%20-%20AKS?label=release-kubernetes)](https://github.com/benc-uk/python-demoapp/actions?query=workflow%3A%22CD+Release+-+AKS%22)

[![](https://img.shields.io/github/workflow/status/benc-uk/python-demoapp/CD%20Release%20-%20Webapp?label=release-azure)](https://github.com/benc-uk/python-demoapp/actions?query=workflow%3A%22CD+Release+-+Webapp%22)

[![](https://img.shields.io/github/last-commit/benc-uk/python-demoapp)](https://github.com/benc-uk/python-demoapp/commits/master)


## Running in Azure App Service (Linux)

If you want to deploy to an Azure Web App as a container (aka Linux Web App), a Bicep template is provided in the [infrastructure as code](infra/) directory

You can also very quickly deploy to Azure App Service directly with the [Azure CLI](https://docs.microsoft.com/en-us/cli/azure/) and `az webapp up`. Note. `<app-name>` must be globally unique. Change the sku to a larger size, e.g. `P1V2` for a much faster deployment
```
az webapp up --sku F1 --name <app-name>
```

## Running in Azure App Service (Windows)
Just don't, it's awful
