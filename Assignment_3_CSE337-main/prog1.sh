#!/bin/bash

# if the number of arguments is not 2, print error and terminate
if [ $# -ne 2 ];
    then
    echo "src and dest dirs missing"
    exit 0
fi

# check if the source directory exists
if [ ! -e $1 ] 
then
    echo “<src-dir> not found
    exit 0
fi

# check if the destination directory exists
if [ ! -e $2 ]
    then
    mkdir -p $2
fi

SOURCE_DIRECTORY="$1"
DESTINATION_DIRECTORY="$2"

find "$SOURCE_DIRECTORY" -type d -print0 | while read -d '' -r DIRECTORY || [[  -n $DIRECTORY  ]]; do
    FILE_COUNT=$(find $DIRECTORY -maxdepth 1 -name '*.c' | wc -l)
    if [ $FILE_COUNT -gt 3 ]; then
        find $DIRECTORY -maxdepth 1 -name '*.c' -print0 | while read -d '' -r FILE || [[ -n $FILE ]]; do
            FILE_DIRECTORY=$(dirname $FILE)
            FILE_NAME=$(basename $FILE)
            RELATIVE_PATH=$(realpath --relative-to="$SOURCE_DIRECTORY" "$FILE_DIRECTORY")
            NEW_PATH="$DESTINATION_DIRECTORY/$RELATIVE_PATH"



            echo -e "DO YOU WANT $FILE TO $NEW_PATH ? (y/n)"
            read -r RESPONSE </dev/tty

            if [ "$RESPONSE" == "y" ] || [ "$RESPONSE" == 'Y' ]; then
                if [ ! -e "$NEW_PATH" ]; then
                  mkdir -p "$NEW_PATH"
                fi
                mv "$FILE" "$NEW_PATH"
                else
                    echo "SKIPPING $FILE"
            fi
        done
    else
        find $DIRECTORY -maxdepth 1 -name '*.c' -print0 | while read -d '' -r FILE || [[ -n $FILE ]]; do
            FILE_DIRECTORY=$(dirname $FILE)
            FILE_NAME=$(basename $FILE)
            RELATIVE_PATH=$(realpath --relative-to="$SOURCE_DIRECTORY" "$FILE_DIRECTORY")
            NEW_PATH="$DESTINATION_DIRECTORY/$RELATIVE_PATH"

            if [ ! -e $NEW_PATH ]; then
                mkdir -p "$NEW_PATH"
            fi

            mv "$FILE" "$NEW_PATH" 
        done
    fi
done