#!/usr/bin/python

# makeChainFile.py
# Take in .pdb file names as command line arguments and print the file names
# to a 'mylist' file at a location specified by the first command line arg.

# sys.argv[1] -- directory to save the file
# sys.argv[2] -- .pdb file 1
# sys.argv[3] -- .pdb file 2
# ...

import sys, os

os.chdir( sys.argv[1] )

file = open( 'mylist', 'w' )

for f in range( len(sys.argv) )[2:] :
  file.write( sys.argv[f] + '\n' )

file.close()
