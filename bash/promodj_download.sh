#!/bin/bash

base_url="https://promodj.com/djyura/groups/17664/efiri_programmi_intelligent_Sound_tolko_muzika?page=%s"

#grep tool__downloads | grep -o 'href=\"[^\"]\+"'

begin=$1
end=$2
if [[ -z $end ]];then
    echo "Empty range"
    exit 1
fi

for p in $(seq $begin $end);do
    url=$(printf $base_url $p)
    wget -q $url -O - | grep tool__downloads | grep -o 'href=\"[^\"]\+"' | cut -d= -f2 | tr -d \" | sort
done

