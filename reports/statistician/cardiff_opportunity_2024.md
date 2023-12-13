---
title: "Using Image Analysis and Machine Learning for Biodiversity Monitoring"
date: "13 December 2023"
author: "Joe Collins"
email: "j.collins@zengenti.com"

output:
  pdf_document:
    template: ../markdown_template.ltx
---
# Background

In 2019, the Spains Hall Estate, Essex,
initiated a nature recovery and natural flood management program by introducing beavers, widely regarded as bioengineers,
into a fenced enclosure.
Comprehensive monitoring of the hydrology, canopy cover, and botanical species composition has been conducted
each year (2019-2023) to assess the impact of beavers within the enclosure.
Two standardised geolocated full colour images were taken at each survey point
capturing canopy cover (light) and ground cover of vegetatio, bare ground and/or open water.

In the summer of 2023, more beavers were introduced into two further enclosures.
Survey data from the first enclosure will be utilized
to predict the timeline for impacts on woodland cover, changes in water levels and botanical changes in the new enclosures.
The objective is to deploy machine learning techniques on the geolocated images
to predict Ellenberg indicator values (EIVs) and changes in light levels (L) and moisture levels (M), resulting from the beaver activity.
 
The model will be truthed against the real survey data and aims to predict changes in biodiversity, which will enable the utilisation of beavers as bioengineers within Biodiversity Net Gain calculations and Ecosystem Services. 

# Objective

Utilize machine learning techniques to predict Ellenberg indicator values (EIVs)
from geolocated images.
The focus is on automatically extracting features,
such as shape descriptors and leaf area index,
to generate a model predicting EIVs for images from the two additional enclosures.

# Collaborative Team

Whilst the Spains Hall estate is a commercial enterprise,
this is a volunteer lead study
run by a collaborative team consisting of:

* Sarah Brockless - Ecologist [LinkedIn](https://www.linkedin.com/in/sarah-brockless-833291a7/).
* Joe Collins - Software Engineer [LinkedIn](https://www.linkedin.com/in/joejcollins/).
* Mags Cousins - Botanist [ResearchGate](https://www.researchgate.net/profile/Mags-Cousins).
* Dave Gasca - Hydrologist [LinkedIn](https://www.linkedin.com/in/david-gasca-7830537/).

The team would welcome input from a data scientist.

# Opportunity Details

* **Data Availability** This is an open source project
and the data thus far is available on [Github](https://github.com/joejcollins/atlanta-shore).
* **Tools** The project uses both R and Python for data preparation and statistical analysis.
Some familiarity with Git is needed but training can be given.
* **Survey Assistance** There will be an opportunity to assist with the botanical survey and data collection on site
at the Spains Hall Estate,
20-24 June 2024.
* **Contact** For further information contact Joe Collins at <j.collins@zengenti.com>.
