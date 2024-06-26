# Get a Rocker image with LaTeX already installed.
FROM rocker/verse:4.3.2

# Add Starship because I like it
RUN sh -c "$(curl -fsSL https://starship.rs/install.sh)" -- --yes \
 && echo 'eval "$(starship init bash)"' >> ~/.bashrc

# Build the Python virtual environment and R library so they are available for other users.
RUN apt-get --quiet update
RUN sudo apt-get install --assume-yes python3.10-dev python3.10-venv lsof sqlite3
WORKDIR /app
RUN mkdir -p /app/.R/library
COPY pyproject.toml requirements.txt setup.R Makefile /app/
RUN make venv

# Add a few LaTeX packages that aren't already installed.
## User is rstudio because they are to be used in Rstudio.
USER rstudio
RUN tlmgr update --self
RUN tlmgr install isodate beamer substr babel-english sectsty float
