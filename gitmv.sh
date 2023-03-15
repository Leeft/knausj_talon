#!/usr/bin/env bash

for dir in "$@"
do
    echo "processing ${dir}:"

    find ${dir} -type f -regextype egrep -regex ".*/[^.].*\.(py|talon)" -print0 | while IFS= read -r -d $'\0' file;
    do
    echo "---- $file"
        f="$(basename -- $file)"
        echo ">>> $f -> .$f";
        `git mv "${dir}/${f}" "${dir}/.${f}"`
    done
done
