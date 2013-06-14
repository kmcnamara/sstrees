#!/usr/bin/python

# getStructures.py
# Read pdb ids coming in as command line args and download their .pdb files
# from the PDB. If there is an error in downloading the file, print an error
# message.

# sys.argv[1] -- directory name to save the .pdb files in
# sys.argv[2] -- pdb id 1
# sys.argv[3] -- pdb id 2
# ...

import sys, os, commands

# Target directory
target = '/home/kylem/BIMM185/pdbs/' + sys.argv[1] + '/'


# Read PDB codes from sys.argv
for id in range(len(sys.argv))[2:] :
  if len(sys.argv[id]) != 4:
    print sys.argv[id]
    continue

  res = commands.getoutput( 'wget -P '+target+' www.rcsb.org/pdb/files/'\
                            +sys.argv[id]+'.pdb' )
  res = res.split('\n')
  if "ERROR" in res[-2]:
    print sys.argv[id]
