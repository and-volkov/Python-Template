# Python-Template
### Template repository for new python projects

* This repository contains a template for new python projects
* It contains a `Makefile` with the following commands:
  * `make help` - show all available commands
  * `make init` - initialize venv and install requirements
  * `make install` - install development requirments
  * `make freeze` - freeze requirements to `requirements.txt
  * `make test` - run tests
  * `make clean` - clean up
  * And several other commands for managing docker containers and images.
* It contains simple github actions for testing.

### Comments
* Default linter - `ruff`. You can see official documentation [here](https://github.com/charliermarsh/ruff).
* You should create `.env` file with your environment variables. You can see example in `.env.example` file.