FROM gitpod/workspace-full

RUN sudo apt-get update \
    && pyenv install 3.7.7 \
    && curl -fsSL https://starship.rs/install.sh | bash -s -- --yes \
    && sudo apt-get install -y r-base gdebi-core \
    && wget https://download2.rstudio.org/server/bionic/amd64/rstudio-server-1.4.1103-amd64.deb \
    && sudo gdebi -n rstudio-server-1.4.1103-amd64.deb \
    && sudo groupadd rstudio-users \
    && sudo touch /etc/rstudio/rserver.conf \
    && sudo bash -c "echo auth-required-user-group=rstudio-users >> /etc/rstudio/rserver.conf" \
    && sudo bash -c "echo R_LIBS=/workspace/R/library >> /etc/R/Renviron.site" \
    && sudo bash -c "echo R_LIBS_USER=/workspace/R/library >> /etc/R/Renviron.site" \
    && sudo mkdir -p /workspace/R/library \
    && sudo R -e "install.packages(\"tinytex\", lib=\"/workspace/R/library\")" \
    && sudo mkdir -p /home/gitpod/.TinyTeX \
    && sudo R -e "tinytex::install_tinytex(force=TRUE, dir=\"/home/gitpod/.TinyTeX\")" \
    && sudo bash -c "echo 'setwd(\"/workspace/atlanta-shore\")' >> /etc/R/Rprofile.site"
