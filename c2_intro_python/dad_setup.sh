#!/bin/bash

#
# I found these scripts online. I added a little debugging that's commented out.
# I also don't like the fact that pathadd doesn't alert you if the path you add
#   isn't a directory. I'll leave that to someone else to add
#
pathadd() {
    if [ -d "$1" ] && ! echo $PATH | grep -E -q "(^|:)$1($|:)" ; then
        if [ "$2" = "after" ] ; then
            PATH="$PATH:${1%/}"
        else                               
            PATH="${1%/}:$PATH"            
        fi                         
    fi
#    echo "New PATH:"
#    printenv PATH | sed 's/:/\n/g'
}

#
# This is ugly sed code but it works.
#
pathrm() {
    PATH="$(echo $PATH | sed -e "s;\(^\|:\)${1%/}\(:\|\$\);\1\2;g" -e 's;^:\|:$;;g' -e 's;::;:;g')"        
#    echo "New PATH:"
#    printenv PATH | sed 's/:/\n/g'
}

#
# I added this to help understand the search order for commands
#
path() {
    printenv PATH | sed 's/:/\n/g'
}

#
# This establishes aliases relative to my root for the assignment directories. To override these
# just go back and issues the following command: source ~/.profile
#
base=`pwd`    # this establishes the root of my repository

for i in `seq 1 7`; do
    alias a$i="cd $base/assignment_$i"
done

#
# Insert the current directory in PATH so you can just type the name of executable scripts in the current directory
#
pathadd .
