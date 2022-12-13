# --- THIS IS PART OF GLOBAL MAKEFILE ---

# Coverage reports for Python
# Locally, use html report. In CI, xml:some/path
PYTHON_COVERAGE_REPORT ?= html

POETRY_WRAPPER_IMAGE_NAME ?= $(PROJECT_NAME)_poetry_wrapper


.PHONY:
poetry-lock:  ## Recreate Poetry lock file after any changes to pyproject.toml file
	make _run-poetry-helper cmd="poetry lock $(args)"


.PHONY:
poetry-add: ## Add package to poetry: make poetry-add cmd=package
	make _run-poetry-helper cmd="poetry add $(cmd)"


.PHONY:
fmt-py: autoflake black isort  ## Format all Python code


.PHONY:
lint-py: black-check isort-check flake8 pylint mypy  ## Lint all Python code


.PHONY:
quality-py: ## Run all Python code formatters and quality tools
	make -k fmt-py flake8 pylint mypy


.PHONY:
test-py:  ## Run tests on Python code
	docker-compose run python pytest $(args)

.PHONY:
test-loc:
	psql -c "DROP DATABASE IF EXISTS $(POSTGRES_TEST_DATABASE_NAME);"
	psql -c "CREATE DATABASE $(POSTGRES_TEST_DATABASE_NAME);"
	#export PICCOLO_CONF="piccolo_conf_test"
	piccolo migrations forwards all
	piccolo tester run

.PHONY:
coverage-py:  ## Runs python/django test coverage calculation
	docker-compose run --rm -e COVERAGE_FILE=/home/user/.coverage python \
		pytest --cov=. --cov-report $(PYTHON_COVERAGE_REPORT) --cov-report term-missing $(cmd)


.PHONY:
patch-coverage-py-paths:
	sed -i -e "s|<source>.|<source>${CI_PROJECT_DIR}/${PROJECT_NAME}/|" $(PYTHON_COVERAGE_REPORT)


.PHONY:
autoflake:  args ?= .
autoflake:  ## Run autoflake (fix unused imports and variables) on Python code
	make -s run-python cmd="autoflake -r -i --remove-all-unused-imports --remove-unused-variables $(args)"


.PHONY:
black-check: args ?= .
black-check:
	make run-python cmd="black --check --diff $(args)"


.PHONY:
black: args ?= .
black: ## Format Python code with Black
	make -s run-python cmd="black $(args)"


.PHONY:
flake8: args ?= .
flake8: ## Run Python code style checks
	make -s run-python cmd='flake8 $(args)'


.PHONY:
pylint: ## Run Python code style checks
ifdef args
	make -s run-python cmd='pylint ${PROJECT_NAME} $(args)'
else
	make -s run-python cmd='pylint ${PROJECT_NAME}'
endif

.PHONY:
mypy: args ?= .
mypy:  ## Check Python types
	echo -e "$(CYAN)Checking types$(COFF)"
	make -s run-python cmd="mypy $(args)"


.PHONY:
isort-check:
	echo -e "$(CYAN)Checking imports with isort$(COFF)"
	make -s run-python cmd='isort tests $(PROJECT_NAME) --check --diff'


.PHONY:
isort: args ?= .
isort: ## Fix imports automatically with isort
	echo -e "$(CYAN)Fixing imports with isort$(COFF)"
	make -s run-python cmd="isort $(args) --skip-glob='*/site-packages/*'"


.PHONY:
makemigrations: ## Make piccolo migrations
	docker-compose run --rm python piccolo migrations new $(PROJECT_NAME) --auto --trace $(cmd)
	UNCOMMITTED_MIGRATIONS=`git ls-files --exclude-standard -o . | grep migrations`; \
	if [ "x$$UNCOMMITTED_MIGRATIONS" != "x" ]; then \
		make fmt-py; \
		echo -e "$(CYAN)Don't forget to add these files to git:$(COFF)"; \
		echo "$$UNCOMMITTED_MIGRATIONS"; \
	fi


.PHONY:
migrate: ## Apply piccolo migrations
	docker-compose run --rm python piccolo migrations forwards $(PROJECT_NAME) $(cmd)

.PHONY:
psql:
	docker-compose exec postgres psql --user $(POSTGRES_USER) --dbname $(POSTGRES_DATABASE_NAME)


.PHONY:
run:
	docker-compose run --rm --no-deps --entrypoint "sh -c" python "$(cmd)"


.PHONY:
poetry-check: poetry-lock-check
	make _run-poetry-helper cmd="poetry check"
	make run-python cmd="poetry run safety check"

.PHONY:
poetry-add-dev:  ## Add a development package to poetry: make poetry-add-dev cmd=package
	make _run-poetry-helper cmd="poetry add --dev $(cmd)"


# --- Internal commands ---

.PHONY:
_build-poetry-helper:
	docker build -q $(PROJECT_ROOT) \
	    -f Dockerfile --target poetry \
	    --tag $(POETRY_WRAPPER_IMAGE_NAME) > /dev/null


.PHONY:
_run-poetry-helper: make-dirs _build-poetry-helper
	docker run -t --rm --name $(POETRY_WRAPPER_IMAGE_NAME) \
	-v $(PWD)/scripts:/scripts \
	-v $(PWD):/src \
	-v $(CACHE_DIR):/home/user/.cache \
	$(POETRY_WRAPPER_IMAGE_NAME) $(cmd)


.PHONY:
run-python:
	docker-compose run --rm --no-deps --entrypoint "sh -c" python "$(cmd)"



poetry.lock:
	make poetry-lock


$(BACKEND_DIR)/locale:
	mkdir -p $(BACKEND_DIR)/locale

