#!/bin/bash

for bash_script in .env/*.sh; do
	source $bash_script
done

# ./test.py $@
./menu.py $@