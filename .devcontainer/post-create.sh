# Ensure the latest version, make the virtual env and initialize the precommit hooks.
git pull
make venv
.venv/bin/pre-commit run --all-files
