# Get a Rocker image with LaTeX already installed.
FROM rocker/verse:4.3.2

# Install the Pyenv pre-requisites.
RUN apt-get --quiet update
RUN sudo apt-get install --assume-yes build-essential libssl-dev zlib1g-dev \
libbz2-dev libreadline-dev libsqlite3-dev curl \
libncursesw5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev

# Get pyenv but put it in /opt/pyenv rather that the user's home directory
# so it can be used in different dev containers which have different users.
ENV PYENV_ROOT="/opt/pyenv"
ENV PATH="${PYENV_ROOT}/bin:${PATH}"
RUN apt-get install --assume-yes git sudo \
 && git clone https://github.com/pyenv/pyenv.git ${PYENV_ROOT} \
 && sudo chmod -R 777 ${PYENV_ROOT}

# Install Python 3.11.6 using pyenv
RUN apt-get -y install locales
ENV PYENV_VERSION=3.11.6
RUN ${PYENV_ROOT}/bin/pyenv install ${PYENV_VERSION}
RUN pyenv global ${PYENV_VERSION}
RUN pyenv rehash

# Update alternatives so that the pyenv Python is the default Python.
# We can't use an alias because the container's entrypoint is a shell script and .bashrc is not sourced.
RUN update-alternatives --install /usr/bin/python python ${PYENV_ROOT}/versions/${PYENV_VERSION}/bin/python 1

# Add a few LaTeX packages that aren't already installed.
USER rstudio
RUN tlmgr update --self
RUN tlmgr install isodate beamer substr babel-english sectsty float

RUN sh -c "$(curl -fsSL https://starship.rs/install.sh)" -- --yes \
 && echo 'eval "$(starship init bash)"' > .bashrc

# Build the Python virtual environment and R library so they are available for other users.
WORKDIR /app
RUN mkdir -p /app/.R/library
COPY pyproject.toml requirements.txt setup.R makefile /app/
RUN eval "$(pyenv init -)" \
  && make venv
