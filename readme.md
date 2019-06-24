# Python Flask - Demo app for Azure
This is a simple Python Flask web application designed for demos, to be used with Azure and DevOps scenarios. The app provides system information and a realtime monitoring screen with dials showing CPU, memory, IO and process information.

Deployment to Azure App Service is possible as Kudu deployment scripts and supporting files are provided to run as a HttpPlatformModule. Dockerfile is provided and public images are on Dockerhub to allow this to be run in a range of container services (Azure Web App for Containers, Azure Container Instance etc.)

The app can of course be run directly via Python.  
Python 3.5+ is required and has been tested on Windows with versions 3.5.2, 3.5.3 and 3.5.4. Under Linux 3.5.2 and 3.6.2 have been tested. Running under Linux subsystem for Windows (aka Bash for Windows) also works

## Screenshot
![screen](https://user-images.githubusercontent.com/14982936/30533171-db17fccc-9c4f-11e7-8862-eb8c148fedea.png)

## Locally via Python
Simply run with `python run.py` the script should start the app, and set Flask listening on port 5000, you can change the port with the environmental variable `PORT`.  
Go to `http://localhost:5000` to view the app.

## Running as Docker Container
The image is publicly available on [Dockerhub here](https://hub.docker.com/r/bencuk/python-demoapp/) so running it in Docker is simple `docker run -d -p 5000:5000 bencuk/python-demoapp`

The container runs on Debian Linux and is configured to use the latest version of Python (3.6.2 at the time of writing)

If you want to deploy to an Azure Container Instance, a working template & quick deploy button is provided in the [azure deploy directory](azure-deploy/)

## Running in Azure App Service (Windows)
When running in a Windows App Service (Web App), there's a few things to note:
- Python 3.5 is required. The default python versions (2.7 or 3.4) will not work, to install 3.5 use one of the standard [Python Site Extensions](https://www.siteextensions.net/packages?q=python+3.5), Version 3.5.4 x64 is expected by the deployment script.

- Kudu deploy scripts (`.deployment` & `kududeploy.cmd`) are provided, these expect to find Python in `D:\home\python354x64\` if you install a different version, then `kududeploy.cmd` will require modification. The script will install all required modules using pip and the `requirements.txt` file

- The app is configured to run under the IIS HttpPlatformHandler, the supplied `web.config` does this using the [Waitress WSGI server](https://docs.pylonsproject.org/projects/waitress/en/latest/) for Python. The `run_waitress_server.py` is the main entrypoint in this case which acts as a wrapper and starts the Flask app running, `web.config` is configured to run `run_waitress_server.py`.  
  - Note, the `HTTP_PLATFORM_PORT` environmental variable is picked up directly by `run_waitress_server.py`, this variable is dynamically populated  by the HttpPlatformHandler, this is **not** the same port as when running via `run.py` (port 5000)  
  - More information on running Flask apps in Azure via WSGI can be found in [this blog post](https://prmadi.com/running-flask-app-with-httpplatformhandler-in-azure-app-services/), but some of the information is out of date

If you want to deploy to an Azure Web App, a working template & quick deploy button is provided in the [azure deploy directory](azure-deploy/)
 

## Running in Azure App Service (Linux)

If you want to deploy to an Azure Web App for Containers (aka Linux Web App), a template is provided in the [azure deploy directory](azure-deploy/)