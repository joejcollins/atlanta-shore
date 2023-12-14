% Class Identification
\NeedsTeXFormat{LaTeX2e}[1995/06/01]
\ProvidesClass{./roles}
              [2023/12/25 v1.0 roles]

% Base Class
\LoadClass[12pt, a4paper, twoside, british]{article}

% Packages
\usepackage[british]{babel}
\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage{hyperref}  % Required for hyperlinks
\usepackage[english]{isodate}
\usepackage{graphicx}
\usepackage{float}

% Make it look kind of like Word
\usepackage[margin=1in]{geometry}
\providecommand{\tightlist}{%  This command is in the pandoc template
  \setlength{\itemsep}{0pt}\setlength{\parskip}{0pt}}
\raggedright
\renewcommand{\familydefault}{\sfdefault}  
\setlength{\parindent}{0pt}  % No indentation for paragraphs
\setlength{\parskip}{1em}  % Add space between paragraphs
