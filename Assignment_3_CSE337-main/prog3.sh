#!/bin/bash

if [ ! -f "$1" ]; then
    echo "missing data file"
fi

INPUT_FILE="$1"

position=0;
for weight in "$@"; do
    weights[position]=$weight
    ((position++))
done

weights_string=$(IFS=,; echo "${weights[*]}")

escaped_weights_string=$(echo "$weights_string" | awk '{ gsub(/\\/, "\\\\"); print }')


awk -F'[,]' '
    BEGIN {
        weights="'"$escaped_weights_string"'"
        split(weights, args, ",")
    }
    {
        student[$1] = 0
        for (i=2; i <=NF; i++) {
            if (args[i] == "") {
                args[i] = 1
            }
            student[$1]+=($i*args[i])/
    }
        print student[$1]
        print "new line"
}' "$INPUT_FILE"