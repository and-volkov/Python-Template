# Python-Template
### Template repository for new python projects

### Description

* This repository contains a template for new python projects
* It contains a `Makefile` with the following commands:
  * `make help` - show all available commands
  * `make init` - initialize poetry. You should run this command before all others
  * `make install` - Create `.venv` inside project folder and install all requirements 
  * `make test` - run tests
  * `make clean` - clean up
  * And several other commands for managing docker containers and images.
* It contains simple github actions for testing.

### Comments
* Default package manager - `poetry`. You can see official documentation [here](https://python-poetry.org/docs/).
* Default linter - `ruff`. You can see official documentation [here](https://github.com/charliermarsh/ruff).
* You should create `.env` file with your environment variables. You can see example in `.env.example` file.