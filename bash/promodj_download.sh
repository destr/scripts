#!/bin/bash

base_url="https://promodj.com/djyura/groups/17664/efiri_programmi_intelligent_Sound_tolko_muzika?page=%s"

#grep tool__downloads | grep -o 'href=\"[^\"]\+"'


for p in $(seq 1 2);do
    url=$(printf $base_url $p)
    wget -q $url -O - | grep tool__downloads | grep -o 'href=\"[^\"]\+"' | cut -d= -f2 | tr -d \"
done

