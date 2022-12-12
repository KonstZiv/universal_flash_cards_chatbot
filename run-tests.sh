#!/bin/bash
psql -c "DROP DATABASE IF EXISTS my_test_db;"
psql -c "CREATE DATABASE my_test_db;"
export PICCOLO_CONF="piccolo_conf_test"
piccolo migrations forwards all
python -m pytest tests/