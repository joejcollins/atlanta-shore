# Consistent set of make tasks.
.DEFAULT_GOAL:= help  # because it's is a safe task.

clean:  # Remove all build, test, coverage and Python artifacts.
	rm -rf .venv
	rm -rf atlanta_shore.egg-info
	find . -name "*.pyc" -exec rm -f {} \;
	find . -type f -name "*.py[co]" -delete -or -type d -name "__pycache__" -delete
	rm -rf .R

lock:  # Compile the requirements files using pip-tools.
	rm -f requirements.*
	.venv/bin/pip-compile --output-file=requirements.txt

.PHONY: help
help: # Show help for each of the makefile recipes.
	@grep -E '^[a-zA-Z0-9 -]+:.*#'  Makefile | sort | while read -r l; do printf "\033[1;32m$$(echo $$l | cut -f 1 -d':')\033[00m:$$(echo $$l | cut -f 2- -d'#')\n"; done

survey-prep:
	.venv/bin/python ./src/data/add_id_to_waypoints.py

.PHONY: docs  # because there is a directory called docs.
docs:  # Build the mkdocs documentation.
	.venv/bin/python -m mkdocs build --clean

gitpod-before:  # Customize the terminal and install global project dependencies.
	# Move the R library to where the developers can see it like the .venv.
	mkdir -p .R/library
	# And ensure that R is aware of the new location.
	echo '.libPaths(c("'"${GITPOD_REPO_ROOT}/.R/library"'", .libPaths()))' > $(HOME)/.Rprofile
	sudo bash -c "echo R_LIBS_USER=$$GITPOD_REPO_ROOT/.R/library > $(HOME)/.Renviron"
	# https://stackoverflow.com/questions/47541007/how-to-i-bypass-the-login-page-on-rstudio
	-if id -u gitpod &>/dev/null; then sudo usermod -aG sudo gitpod; fi
	sudo bash -c "echo 'server-user=gitpod' >> /etc/rstudio/rserver.conf"
	sudo bash -c "echo 'auth-none=1' >> /etc/rstudio/rserver.conf"
	# For convenience open up the permissions on the TexLive directory
	-sudo chmod -R 777 /usr/local/texlive
	# Set the git merge strategy
	-git config pull.rebase false
	# Get Starship running.
	echo 'eval "$$(starship init bash)"' >> ~/.bashrc
	# Remove the .bash_profile so the .bashrc gets sourced.
	rm -f ~/.bash_profile

gitpod-init:  # Copy accross the pre-built .venv and the .R libraries.
	cp -r /app/.venv .venv
	cp -r /app/atlanta_shore.egg-info atlanta_shore.egg-info
	.venv/bin/python -m pip install -e .
	cp -r /app/.R/library/* .R/library

gitpod-command:  # Ensure that the rserver is available.
	# Ensure that the Rproject is available in the users home directory.
	ln -s $(GITPOD_REPO_ROOT) $(HOME)/atlanta-shore
	# Restart the rserver with sudo otherwise it won't run for the gitpod user (dunno why).
	sudo rserver
	sudo pkill rserver

lint:  # Lint the code with ruff and sourcery.
	.venv/bin/python -m ruff check ./python_src ./tests
	.venv/bin/sourcery login --token $$SOURCERY_TOKEN
	.venv/bin/sourcery review ./python_src ./tests --check --no-summary
	.venv/bin/python -m mypy ./python_src ./tests

report:  # Report the python version and pip list.
	whoami
	.venv/bin/python --version
	.venv/bin/python -m pip list -v
	Rscript -e "installed_packages <- as.data.frame(installed.packages()); \
		print(installed_packages[c('Package', 'LibPath')])"

rserver:  # Run Rstudio server
	@echo "https://127.0.0.1:8787/"
	@echo "User=rstudio Password=rstudio"
	sudo rstudio-server restart

venv:  # Install the requirements for Python and R.
	python3 -m venv .venv
	.venv/bin/python -m pip install --upgrade pip setuptools
	.venv/bin/python -m pip install -r requirements.txt
	-.venv/bin/python -m pip install --editable .
	mkdir --parents .R/library
	Rscript "setup.R"

test:  # Run the tests (tests in Github Actions are run as 'root' so add .libPaths)
	.venv/bin/python -m pytest ./tests/pytest
	Rscript -e ".libPaths('.R/library'); devtools::test()"
