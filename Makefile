VENV = $VENV
PYTHON = $(VENV)/bin/python3
PIP = $(VENV)/bin/pip
ENVIRONMENT_VARIABLE_FILE='.env'
DOCKER_NAME=$DOCKER_NAME
DOCKER_TAG=$DOCKER_TAG

define find.functions
	@fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's/##//'
endef

help:
	@echo 'The following commands can be used.'
	@echo ''
	$(call find.functions)

init: ## sets up environment and installs requirements
init:
	poetry init

install: ## Installs development requirments
install:
	poetry config virtualenvs.in-project true
	poetry install

clean: ## Remove build and cache files
clean:
	rm -rf *.egg-info
	rm -rf build
	rm -rf dist
	rm -rf .pytest_cache
	# Remove all pycache
	find . | grep -E "(__pycache__|\.pyc|\.pyo$)" | xargs rm -rf

test: ## Run tests
test:
	pytest

build: ## Build docker image
build:
	docker build -t $(DOCKER_NAME):$(DOCKER_TAG) -f docker/Dockerfile .

create: ## Create docker image
create: build
	docker create -it --name $(DOCKER_NAME) $(DOCKER_NAME):$(DOCKER_TAG)

start: ## Build and start docker image
start: build
	docker start $(DOCKER_NAME)

run: ## build, start and run docker image
run: start
	docker run -it $(DOCKER_NAME):$(DOCKER_TAG)

exec: ## build, start and exec into docker image
exec: start
	docker exec -it $(DOCKER_NAME) python
