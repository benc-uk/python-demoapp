# Python Flask - Demo Web Application

This is a simple Python Flask web application forked from benc-uk with the purpose on this fork being the demonstration of ci workflows (see [GitHub Actions CI/CD](#github-actions-cicd))

# Status

![](https://img.shields.io/github/last-commit/marios-r/python-demoapp) 

Live instances:

[![](https://img.shields.io/website?label=Hosted%3A%20Digital%20Ocean&up_message=online&url=http%3A%2F%2F64.227.114.131%3A5080%2F)](http://64.227.114.131:5080/)  

## Building & Running Locally

### Pre-reqs

- Be using Linux, WSL or MacOS, with bash, make etc
- [Python 3.8+](https://www.python.org/downloads/) - for running locally, linting, running tests etc
- [Docker](https://docs.docker.com/get-docker/) - for running as a container, or image build and push

Clone the project to any directory where you do development work

```
git clone https://github.com/marios-r/python-demoapp.git
```

### Makefile

A standard GNU Make file is provided to help with running and building locally.

```text
help                 💬 This help message
lint                 🔎 Lint & format, will not fix but sets exit code on error
lint-fix             📜 Lint & format, will try to fix errors and modify code
image                🔨 Build container image from Dockerfile
push                 📤 Push container image to registry
run                  🏃 Run the server locally using Python & Flask
test                 🎯 Unit tests for Flask app
test-report          🎯 Unit tests for Flask app (with report output)
test-api             🚦 Run integration API tests, server must be running
clean                🧹 Clean up project
```

Make file variables and default values, pass these in when calling `make`, e.g. `make image IMAGE_REPO=blah/foo`

| Makefile Variable | Default                   |
| ----------------- | ------------------------- |
| TEST_HOST         | localhost:5008            |
| IMAGE_REPO        | m219raptis/python-demoapp |
| IMAGE_TAG         | latest                    |

Getting weird errors? You have the option to use the [dev container on vsCode](https://code.visualstudio.com/docs/devcontainers/create-dev-container). 

# Containers

Public container image is [available on Docker Hub](https://hub.docker.com/r/m219raptis/python-demoapp)

Run in a container with:

```bash
docker container run -dp 5008:5008 -t m219raptis/python-demoapp:latest
```
This should make the app available on http://localhost:5008/

Should you want to build your own container, use `make image` and the above variables to customise the name & tag.

# GitHub Actions CI/CD

A working set of CI and CD release GitHub Actions workflows are provided `.github/workflows/`, automated builds are run in GitHub hosted runners.

It is assumed that PRs are deployed on a QA enironment and default branch is deployed on a staging environment.

In the case you fork this repo, please note that there are some secret variables you need to add.
| Secret Variable | Description                                                             |
| --------------- | ----------------------------------------------------------------------- |
| D_REG_USER      | Docker Hub username                                                     |
| D_REG_PW        | Docker Hub password                                                     |
| D_SSH_KEY       | SSH private key to deployment server                                    |
| D_SSH_USER      | Username too login with SSH                                             |
| GHA_TOKEN       | GitHub token with permission to access your repo (public if it's public)|

Additionally, you need to add the below repository variables.
| Variable     | Description                                            |
| ------------ | ------------------------------------------------------ |
| QA_HOST      | Host for the QA deployment (domain|ip)                 |
| QA_PORT      | Port where the deployed app can be accessed on QA      |
| STAGING_HOST | Host for the staging deployment (domain|ip)            |
| STAGING_PORT | Port where the deployed app can be accessed on staging |

The workflows are designed to be extended and support a following working procedure:
1. Workflow on file ci-deploy-qa will get triggered when a PR gets opened and will execute lower level tests like unit tests as well as any linting.
If those checks proceed, the branch will get deployed to QA and become available for manual testing and UAT.
2. Workflow on file ci-deploy-staging will get triggered when the PR gets merged to default branch and will deploy the newer version to staging. It will imediately after that trigger higher level tests like api tests and e2e tests. On our example implementation the API tests are being triggered with workflow dispatch.

This should allow us to have fully tested staging environments that can be deployed to production when necessary. 
Depending the situation, e2e regression tests, which are more time consuming, can run on a schedule on staging instead and limit the testing on every merge to smoke tests. Current implementation is just for demonstration but can be extended as necessary.

![CICD](https://github.com/marios-r/python-demoapp/assets/18104126/65c21d83-e33f-468d-8cd2-d2e1091c1f96)
