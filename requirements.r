# R package list
dir.create(".R/library")
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
    "xfun"), lib=".R/library")
# TinyTex for documents
dir.create(".R/.TinyTex")
tinytex::install_tinytex(force=TRUE, dir=".R/.TinyTex")
