# Consistent set of make tasks.
.DEFAULT_GOAL:= help  # because it's is a safe task.

clean:  # Remove all build, test, coverage and Python artifacts.
	rm -rf .venv
	find . -name "*.pyc" -exec rm -f {} \;
	find . -type f -name "*.py[co]" -delete -or -type d -name "__pycache__" -delete

compile:  # Compile the requirements files using pip-tools.
	. .venv/bin/activate; python -m pip install pip-tools
	. .venv/bin/activate; python -m piptools compile -o requirements.txt pyproject.toml && echo "-e ." >> requirements.txt

.PHONY: help
help: # Show help for each of the makefile recipes.
	@grep -E '^[a-zA-Z0-9 -]+:.*#'  makefile | sort | while read -r l; do printf "\033[1;32m$$(echo $$l | cut -f 1 -d':')\033[00m:$$(echo $$l | cut -f 2- -d'#')\n"; done

survey-prep:
	. .venv/bin/activate; python ./src/data/add_id_to_waypoints.py

dataset:
	. .venv/bin/activate; python ./src/data/make_dataset.py

report:  # Report the python version and pip list.
	.venv/bin/python --version
	.venv/bin/python -m pip list -v

requirements:  # Install the requirements for Python and R.
	python3 -m venv .venv
	. .venv/bin/activate; python -m pip install --upgrade pip setuptools
	. .venv/bin/activate; python -m pip install -r requirements.txt
	Rscript "setup.R"
	Rscript -e ".libPaths('.R/library'); devtools::install()"

test:  # Run the tests.
	. .venv/bin/activate; python -m pytest ./tests/pytest
	Rscript -e "testthat::test_dir('tests')"
