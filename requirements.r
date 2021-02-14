# Package list
dir.create(".R/")
install.packages(c(
    "base64enc", 
    "digest", 
    "evaluate", 
    "glue", 
    "highr", 
    "htmltools", 
    "jsonlite", 
    "knitr", 
    "magrittr", 
    "markdown", 
    "mime", 
    "rlang", 
    "rmarkdown", 
    "stringi", 
    "stringr", 
    "tinytex", 
    "xfun"), lib=".R/")
tinytex::install_tinytex(force=TRUE, dir="/home/gitpod/.TinyTeX")
