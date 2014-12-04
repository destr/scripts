#!/bin/bash

musicdir="$1"
musicmanager=`realpath $(dirname "$0")`/../python/musicmanager.py

function renameBad() {
    find "$musicdir" -regextype posix-extended -regex ".*[?:<>*\"\|].*" -type $1 \
        -exec rename "s/[?:<>*\"\|]//g" {} \;
}

renameBad d
renameBad f

#find "$musicdir" -regextype posix-extended -regex ".*[?:<>*\"\|].*" -type d | \
