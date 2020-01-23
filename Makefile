# Makefile
# *remember to use tabs as separator*

survey-prep:
	python	./src/data/add_id_to_waypoints.py

dataset:
	python	./src/data/make_dataset.py
