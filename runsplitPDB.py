#!/usr/bin/python

# runsplitPDB.py
# Run the script splitPDB.py on every .pdb file in the directory, then
# delete that parent file.

import sys, os, commands

os.chdir( "/home/kylem/BIMM185/pdbs/"+sys.argv[1] )

res = commands.getoutput( 'ls *.pdb' )

pdbs = res.split('\n')

for f in pdbs:
  res = commands.getoutput( 'python /home/kylem/BIMM185/scripts/splitPDB.py '+f )
  res = commands.getoutput( 'rm '+f )
