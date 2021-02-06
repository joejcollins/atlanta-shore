FROM gitpod/workspace-full

# Arbitary choice of python version
RUN pyenv install 3.7.7

# Also install R
RUN brew install R
