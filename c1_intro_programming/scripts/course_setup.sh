#!/bin/bash


# this is the name of the repository you created on github for your assignment
gitProject="intro-programming"

# the username for the account you created on github
gitUser="mgoblues"

# this combines the earlier two variables in the URL for git commands
gitRepo="https://github.com/$gitUser/$gitProject.git"

# replace instructor information with your own before running script
git config --global user.name "Joel Elster"
git config --global user.email je60@nyu.edu

# these will silence some errors and use our familiar vim by default
git config --global core.editor vim
git config --global push.default simple

# make sure git project is checked out
if [ ! -d "$HOME/$gitProject" ]; then
    cd $HOME
    git clone $gitRepo
fi

# create assignment_3 dir if it doesn't exist
if [ ! -d "$HOME/$gitProject/assignment_3" ]; then
    echo "Attempting to run \`mkdir assignment_3\`"
    mkdir $HOME/$gitProject/assignment_3
fi
