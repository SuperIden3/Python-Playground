PR = python3
RFLAGS = 
FILE = main.py

.PHONY: all run time

all: run

run: $(FILE)
	python3 $(FILE)

time: $(FILE)
	bash -c "time python3 $(FILE)"
