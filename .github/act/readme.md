# Act

Act is an amazing command line local runner for GitHub Actions  
https://github.com/nektos/act

Install with

```bash
curl https://raw.githubusercontent.com/nektos/act/master/install.sh | sudo bash
```

To run the workflows for this repo, example commands are given below

The `.secrets` file must be created first, see the sample file for a reference.

### Run CI

```bash
act push --secret-file .github/act/.secrets --platform ubuntu-latest=ghcr.io/benc-uk/devcontainers/python:root
```

### Run a deployment

```bash
act workflow_dispatch --eventpath .github/act/workflow_dispatch.json --secret-file .github/act/.secrets --platform ubuntu-latest=ghcr.io/benc-uk/devcontainers/python:root
```
