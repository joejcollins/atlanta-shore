FROM gitpod/workspace-full

# Arbitary choice of python version
RUN pyenv install 3.7.7

# Also install R
RUN brew install R

# Install LaTeX
RUN sudo apt-get -q update && \
    sudo apt-get install -yq texlive-full inotify-tools && \
    sudo rm -rf /var/lib/apt/lists/*
