# Python Flask - Demo app for Azure
This is a simple Python Flask web application designed for demos, to be used with Azure and DevOps scenarios. The app provides system information and a realtime monitoring screen with dials showing CPU, memory, IO and process information.

Deployment to Azure App Service is possible as Kudu deployment scripts and supporting files are provided to run as a HttpPlatformModule. Dockerfile is provided and public images are on Dockerhub to allow this to be run in a range of container services (Azure Web App for Containers, Azure Container Instance etc.)

The app can of course be run directly via Python.  
Python 3.6+ is required and has been tested on Windows and Linux (Ubuntu 18.04)

## Screenshot
![screen](https://user-images.githubusercontent.com/14982936/30533171-db17fccc-9c4f-11e7-8862-eb8c148fedea.png)

## Locally via Python
Simply run with `python run.py` the script should start the app, and set Flask listening on port 5000, you can change the port with the environmental variable `PORT`.  
Go to `http://localhost:5000` to view the app.

## Running as Docker Container
The image is publicly available on [Dockerhub here](https://hub.docker.com/r/bencuk/python-demoapp/) so running it in Docker is simple `docker run -d -p 5000:5000 bencuk/python-demoapp`

The container runs on Debian Linux and is configured to use the latest version of Python (3.6.2 at the time of writing)

If you want to deploy to an Azure Container Instance, a working template & quick deploy button is provided in the [azure deploy directory](azure-deploy/)

## Running in Azure App Service (Linux)

If you want to deploy to an Azure Web App for Containers (aka Linux Web App), a template is provided in the [azure deploy directory](azure-deploy/)

## Running in Azure App Service (Windows)
Just don't