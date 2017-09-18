# Python Flask - Demo app for Azure
This is a simple Python Flask web application designed for demos, to be used with Azure and DevOps scenarios. The app provides system information and a realtime monitoring screen with dials showing, CPU, memory, IO and process information.

Deployment to Azure App Service is possibl,e as Kudu deployment scripts and supporting files are provided to run as a HttpPlatformModule. Dockerfile is provided also and public images are on Dockerhub to allow this to be run in a range of container services (Azure Web App for Containers, Azure Container Instance etc.)

The app can of course be run directly via Python. Python 3.x is required and has been tested on 3.5 and 3.6

## Screenshot
![screen](https://user-images.githubusercontent.com/14982936/30533171-db17fccc-9c4f-11e7-8862-eb8c148fedea.png)

## Locally via Python

## Running as Docker Container

[![deploy](https://raw.githubusercontent.com/benc-uk/azure-arm/master/etc/azuredeploy.png)](https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2Fbenc-uk%2Fpython-demoapp%2Fmaster%2Fazure-deploy%2Fcontainer-instance%2Fazuredeploy.json)  

## Running in Azure App Service (Windows)

[![deploy](https://raw.githubusercontent.com/benc-uk/azure-arm/master/etc/azuredeploy.png)](https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2Fbenc-uk%2Fpython-demoapp%2Fmaster%2Fazure-deploy%2Fweb-app%2Fazuredeploy.json)  

## Running in Azure App Service (Linux)

[![deploy](https://raw.githubusercontent.com/benc-uk/azure-arm/master/etc/azuredeploy.png)](https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2Fbenc-uk%2Fpython-demoapp%2Fmaster%2Fazure-deploy%2Fweb-app-container%2Fazuredeploy.json)  