# Make the virtual environment and initialize the precommit hooks.
make venv
.venv/bin/pre-commit run --all-files
