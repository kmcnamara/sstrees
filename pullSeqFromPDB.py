#!/usr/bin/python

# pullSeqFromPDB.py
# Given an input .pdb file, output the .fa file that corresponds to the
# residues that are represented in the ATOM entries of the structure.

# sys.argv[1] -- .pdb file

import sys

from kmutils import fileToList, splitLines, threeToOneLetterAA

# Grab the .pdb file
pdb_lines = []
fileToList( sys.argv[1], pdb_lines )

# Open a .fa file
fa = open( sys.argv[1][:-4] + '.fa', 'w' )
# Add a header line
fa.write( '>' + sys.argv[1][:-4] )

# Go through ATOM entries to find residues
seq = ''
index = -99
count = 0
for line in pdb_lines:
  if( line[:4] == 'ATOM' ):
    num = int( line[22:26] )
    if( num > index ):
      # New residue found
      if( num != index+1 and count != 0 ):
        # Add amino acid 'X' for each missing residue
        for missing in range( num - index - 1 ):
          seq += 'X'
          count += 1
        # Add new amino acid
        seq += threeToOneLetterAA[ line[17:20] ]
        index = num
        count += 1
      else:
        # Add new amino acid
        seq += threeToOneLetterAA[ line[17:20] ]
        index = num
        count += 1

# Write seq to .fa file
for i in range( len(seq) ):
  if( i % 80 == 0 ):
    fa.write( '\n' )
  fa.write( seq[i] )

fa.close()

# End of pullSeqFromPDB.py
