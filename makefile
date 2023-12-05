# Consistent set of make tasks.
.DEFAULT_GOAL:= help  # because it's is a safe task.

clean:  # Remove all build, test, coverage and Python artifacts.
	rm -rf .venv
	find . -name "*.pyc" -exec rm -f {} \;
	find . -type f -name "*.py[co]" -delete -or -type d -name "__pycache__" -delete

compile:  # Compile the requirements files using pip-tools.
	rm -f requirements.*
	.venv/bin/pip-compile --output-file=requirements.txt && echo "-e ." >> requirements.txt

.PHONY: help
help: # Show help for each of the makefile recipes.
	@grep -E '^[a-zA-Z0-9 -]+:.*#'  makefile | sort | while read -r l; do printf "\033[1;32m$$(echo $$l | cut -f 1 -d':')\033[00m:$$(echo $$l | cut -f 2- -d'#')\n"; done

survey-prep:
	. .venv/bin/activate; python ./src/data/add_id_to_waypoints.py

dataset:  # Prepare the datasets for analysis
	. .venv/bin/activate; python ./python_src/make_observations_dataset.py

gitpod-before:  # Customize the terminal and install global project dependencies.
	# Move the R library to where we can see it.
	mkdir -p $(GITPOD_REPO_ROOT)/.R/library
	sudo bash -c "echo R_LIBS_USER=$$GITPOD_REPO_ROOT/.R/library > /home/gitpod/.Renviron"
	# https://stackoverflow.com/questions/47541007/how-to-i-bypass-the-login-page-on-rstudio
	sudo usermod -a -G sudo gitpod
	sudo bash -c "echo 'server-user=gitpod' >> /etc/rstudio/rserver.conf"
	sudo bash -c "echo 'auth-none=1' >> /etc/rstudio/rserver.conf"
	# Ensure the pyenv is configured for the user.
	echo 'eval ""$(pyenv init - --no-rehash)""' >> ~/.bashrc
	sudo chmod -R 777 ${PYENV_ROOT}

gitpod-init:  # Downloading dependencies and compiling source code.
	$(MAKE) venv

gitpod-command:  # Ensure that the rserver is available.
	ln -s $(GITPOD_REPO_ROOT) $(HOME)/atlanta-shore
	# Restart the rserver with sudo otherwise it won't run for the gitpod user (dunno why)
	sudo rserver
	sudo pkill rserver

report:  # Report the python version and pip list.
	.venv/bin/python --version
	.venv/bin/python -m pip list -v

venv:  # Install the requirements for Python and R.
	-pyenv install --skip-existing
	python -m venv .venv
	.venv/bin/python -m pip install --upgrade pip setuptools
	.venv/bin/python -m pip install -r requirements.txt
	Rscript "setup.R"

test:  # Run the tests.
	. .venv/bin/python -m pytest ./tests/pytest
	Rscript -e ".libPaths('.R/library'); devtools::install()"
	Rscript -e "testthat::test_dir('tests')"

shit:
	echo 'eval "$$(pyenv init - --no-rehash)"' >> ~/.bashrc