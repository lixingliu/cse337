#!/bin/bash

# if the number of arguments is not 2, print error and terminate
if [ $# -ne 2 ];
    then
    echo "data file or output file not found"
    exit 0
fi

INPUT_FILE="$1"
OUTPUT_FILE="$2"

if [ ! -f "$INPUT_FILE" ]; then
    echo "$INPUT_FILE not found"
    exit 0
fi

> "$OUTPUT_FILE"

while IFS= read -r line; do
echo "l"
done < "$INPUT_FILE"