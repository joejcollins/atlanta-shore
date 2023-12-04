FROM docker pull rocker/verse:4.3.2

RUN sudo apt -q update \
 && sudo apt install --assume-yes python3.10-venv
