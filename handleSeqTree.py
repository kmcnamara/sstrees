#!/usr/bin/python

# handleSeqTree.py
# Handle all the business involved in produced the sequence-based phylogenetic
# tree. Use pullSeqFromPDB.py to get all the needed .fa files. Then use
# runClustal.sh to produce the newick tree file.

# sys.argv[1] -- list of .pdb files

import sys, os, commands
from kmutils import fileToList, splitLines

scripts = '/home/kylem/BIMM185/scripts/'

files = splitLines( sys.argv[1] )

cat = 'cat '
for f in range( len(files) ):
  res = commands.getoutput( 'python '+scripts+'pullSeqFromPDB.py '+files[f][0] )
  cat += files[f][0][:-4] + '.fa '

res = commands.getoutput( cat + ' > allseqs.fa' )

res = commands.getoutput( 'sh '+scripts+'runClustal.sh allseqs.fa seqtree' )
