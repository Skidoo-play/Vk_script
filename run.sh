#!/bin/bash

for bash_script in .env/*.sh; do
	source $bash_script
done

./main.py $@