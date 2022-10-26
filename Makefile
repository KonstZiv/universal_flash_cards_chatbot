# Project name
PROJECT_NAME ?= app

# Get root dir and project dir
PROJECT_ROOT ?= $(CURDIR)
BACKEND_DIR ?= $(PROJECT_ROOT)/$(PROJECT_NAME)
#FRONTEND_DIR ?= $(PROJECT_ROOT)/frontend

CACHE_DIR ?= $(PROJECT_ROOT)/.data/cache
NODE_MODULES_DIR ?= $(PROJECT_ROOT)/.data/node_modules

BLACK ?= \033[0;30m
RED ?= \033[0;31m
GREEN ?= \033[0;32m
YELLOW ?= \033[0;33m
BLUE ?= \033[0;34m
PURPLE ?= \033[0;35m
CYAN ?= \033[0;36m
GRAY ?= \033[0;37m
COFF ?= \033[0m

# Omit some noise.
MAKEFLAGS += --silent --no-print-directory


.PHONY:
all: help


.PHONY:
help:
	echo -e "Available make commands:"
	echo -e ""
	grep --no-filename -E '^[a-zA-Z_%-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
	echo -e ""


.PHONY:
docker-rebuild:
	docker-compose rm -asf
	make docker


.PHONY:
docker: settings
	docker-compose build
	docker-compose up -d
	docker-compose logs -f


.PHONY:
setup: pycharm settings ## Sets up the project in your local machine. Might take a while.
	echo -e "$(CYAN)Creating Docker images$(COFF)"
	make make-dirs
	make poetry.lock
	docker-compose build
	#echo -e "$(CYAN)Running migrations$(COFF)"
	#make migrate
	echo -e "$(CYAN)Installing node modules$(COFF)"
	echo -e "$(CYAN)===================================================================="
	echo -e "SETUP SUCCEEDED"
	echo -e "Run 'make docker' to start dockers.(COFF)"


.PHONY:
pycharm: $(PROJECT_ROOT)/.idea ## Copies default PyCharm settings (unless they already exist)



$(PROJECT_ROOT)/.idea:
	echo -e "$(CYAN)Creating pycharm settings from template$(COFF)"
	mkdir -p $(PROJECT_ROOT)/.idea && cp -R $(PROJECT_ROOT)/.idea_template/* $(PROJECT_ROOT)/.idea/


$(PROJECT_ROOT)/.env:
	echo -e "$(CYAN)Copying .env file$(COFF)"
	cp $(PROJECT_ROOT)/.env.example $(PROJECT_ROOT)/.env


.PHONY:
settings: $(PROJECT_ROOT)/.env

.PHONY:
coverage: coverage-py  ## Runs all tests with coverage

.PHONY:
test: test-py ## Runs automatic tests on all code

.PHONY:
lint: lint-py  ## Lint all Python

.PHONY:
fmt: fmt-py  ## Format all Python (alias: format)

.PHONY:
format: fmt  ## Format all Python  (alias: fmt)

.PHONY:
make-dirs:
	mkdir -p $(CACHE_DIR) $(NODE_MODULES_DIR)


include $(BACKEND_DIR)/Makefile

# Currently, no cypress installed
# include Makefile-cypress

