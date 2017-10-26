#!/bin/bash

while [ 1 ]
do
    read -n1 c

    if [ 'q' == "$c" ]; then
        exit 0
    fi
    if [[ "$c" =~ ^[0-9a-zA-Z]$ ]];then
        echo "normor"
    elif [[ "$c" =~ ^[!@#$%^\&*()_+\-=|\\:\"\;\'\<\>,\./]$ ]];then
        echo "not generel"
    elif [[ "$c" =~ ^\?$ ]];then
        echo "is ear"
    elif [[ "$c" =~ ^[\{\}]$ ]];then
        echo "da kuohao "
    elif [[ "$c" =~ ^\[$ ]];then
        echo "zhong kuohao zuo"
    elif [[ "$c" =~ ^\]$ ]];then
        echo "zhong kuohao you"
    else
        echo "ctrl key"
        read -n1 ch
        if [[ "$ch" =~ ^\[$ ]];then
            read -n1 cha
            case $cha in
                'A') echo "up arrow" ;;
                'B') echo "down arrow" ;;
                'C') echo "right arrow" ;;
                'D') echo "left arrow" ;;
                *)   echo "$cha" ;;
            esac
        elif [[ "$ch =~ ^O$" ]]; then
            read -n1 cha
            case $cha in
                'P' ) echo "F1" ;;
                'Q' ) echo "F2" ;;
                'R' ) echo "F3" ;;
                'S' ) echo "F4" ;;
                'T' ) echo "F5" ;;
            esac
        fi
    fi
done
