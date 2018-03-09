#!/usr/local/bin/python3

#def printFile(filePath): f = file(filePath) contents = f.read() printContents()
#def printContents(): print("Contents of " + filePath) print(contents)

import sys

def printFile(filePath):
    f = open(filePath,'r')
    contents = f.read()
    print("Contents of " + filePath);
    print(contents)

#================================================================================
#printFile( "/home/vagrant/intro-programming/assignment_7/homemade-cat.py" )

if __name__ == "__main__":
    file = __file__
    if len(sys.argv) > 1:
        file = sys.argv[1]

    printFile( file )

