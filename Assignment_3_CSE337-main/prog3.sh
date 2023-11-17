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
        result = 0
    }
    {
        student[$1] = 0
        weight_summation = 0
        for (i=2; i <=NF; i++) {
            if (args[i] == "") {
                args[i] = 1
            }
            weight_summation+=args[i]
            student[$1]+=($i*args[i])
    }
        result+=student[$1]/weight_summation
}
END {
    answer = result/NR
    floor_value = int(answer)
    if (answer < 0 && answer != floor_value) {
        floor_value -= 1
    }
    print floor_value
}' "$INPUT_FILE"