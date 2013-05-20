#!/usr/bin/python

# splitPDB.py
# Given an input .pdb file, create new .pdb files that have only one chain
# per file. XXXX.pdb with chains A, B, and C will spawn XXXX_A.pdb,
# XXXX_B.pdb, and XXXX_C.pdb.

# sys.argv[1] -- the filename of the .pdb file
# sys.argv[2] -- the desired prefix name for the output chain files

import sys

from kmutils import fileToList, splitLines

if( len(sys.argv) != 3 ):
  print "Usage: " + sys.argv[0] + " <.pdb file> <name>"
  exit(0)

pdb_lines = []
fileToList( sys.argv[1], pdb_lines )

# Find the chain names
chains = []
for line in pdb_lines:
  if( line[:4] == 'ATOM'):
    chain = line[21]
    if chain not in chains:
      chains.append( chain )

# Output a file for each chain
for chain in chains:
  out_pdb = open( sys.argv[2]+'_'+chain+'.pdb', 'w' )

  for line in pdb_lines:
    if( line[:4] == 'ATOM' ):
      if( line[21] != chain ):
        continue
    elif( line[:6] == 'ANISOU' ):
      if( line[21] != chain ):
        continue
    elif( line[:6] == 'HETATM' ):
      if( line[21] != chain ):
        continue
    elif( line[:3] == 'TER' ):
      if( line[21] != chain ):
        continue

    out_pdb.write( line )

  out_pdb.close()

# End of splitPDB.py
