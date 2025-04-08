# Get a simple base image
FROM mcr.microsoft.com/devcontainers/base:bullseye

# Install LaTeX because it is not included in the Rocker image.
RUN apt-get --quiet update \
    && apt-get install --assume-yes texlive-latex-extra texlive-extra-utils latexmk \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Add some labels so it looks nice in Github packages.
LABEL org.opencontainers.image.source=https://github.com/joejcollins/atlanta-shore/
LABEL org.opencontainers.image.description="Data editing image for atlanta-shore"
LABEL org.opencontainers.image.version="0.0.1"
LABEL org.opencontainers.image.authors="Joe J Collins <joejcollins@gmail.com>"
