FROM gitpod/workspace-full:latest

# Install LaTeX and R Server
RUN sudo apt-get -q update \
 && sudo apt-get install -yq texlive-latex-extra  \
 && sudo apt-get install -y r-base gdebi-core \
 && wget https://download2.rstudio.org/server/bionic/amd64/rstudio-server-1.4.1103-amd64.deb \
 && sudo gdebi -n rstudio-server-1.4.1103-amd64.deb \
 && sudo rm rstudio-server-1.4.1103-amd64.deb \
 && sudo groupadd rstudio-users \
 && sudo touch /etc/rstudio/rserver.conf \
 && sudo bash -c "echo auth-required-user-group=rstudio-users >> /etc/rstudio/rserver.conf"

# Install starship because I like it
RUN curl -fsSL https://starship.rs/install.sh | bash -s -- --yes
