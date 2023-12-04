FROM rocker/rstudio:latest

RUN sudo apt -q update \
 && sudo apt install --assume-yes python3.10-venv

# Install TinyTex for all users.
RUN wget -qO- "https://yihui.org/tinytex/install-unx.sh" | sh -s - --admin --no-path

# Expose the port for RStudio
EXPOSE 8787
