#!/usr/bin/python

# masterHandle.py
# Runs the show.

# sys.argv[1] -- project directory
# sys.argv[2] -- indicator for which structure alignment algorithm to use

import sys, os, commands

scripts = '/home/kylem/BIMM185/scripts/'

os.chdir( sys.argv[1] )

# Run the sequence-based tree calculation
res = commands.getoutput( 'python '+scripts+'handleSeqTree.py mylist' )

# Run the structure alignment to produce a distance matrix
algo = sys.argv[2]
distmat = ''
if algo == 'deep':
  res = commands.getoutput( 'python '+scripts+'runDeepAlign.py mylist '+sys.argv[1]+'/' )
  distmat = 'deepAlignTM.out'
elif algo == 'tm':
  res = commands.getoutput( 'python '+scripts+'runTMAlign.py mylist '+sys.argv[1]+'/' )
  distmat = 'TMAlignTM.out'
elif algo == 'fat':
  res = commands.getoutput( 'python '+scripts+'runFatcat.py mylist '+sys.argv[1]+'/' )
  distmat = 'fatcatScore.out'
elif algo == 'matt':
  res = commands.getoutput( 'python '+scripts+'runMatt.py mylist '+sys.argv[1]+'/' )
  distmat = 'mattScore.out'
elif algo == 'click':
  res = commands.getoutput( 'python '+scripts+'runClick.py mylist '+sys.argv[1] )
  distmat = 'clickRMSD.out'
else:
  print "Error occured!"

# Calculate the structure tree file from the distance matrix
res = commands.getoutput( 'mv '+distmat+' infile' )
res = commands.getoutput( 'sh '+scripts+'neighborjoin.sh ../optfile' )

# Adjust newick tree file names
pname = os.path.basename( sys.argv[1] )
seqtree = pname + '_seq'
structtree = pname + '_struct'
res = commands.getoutput( 'mv allseqs.ph ' + seqtree )
res = commands.getoutput( 'mv outtree ' + structtree )

# Translate the newick files to .gifs
res = commands.getoutput( 'python '+scripts+'printunrooted.py '+seqtree )
res = commands.getoutput( 'python '+scripts+'printunrooted.py '+structtree )

# Move .gifs to temp file so rest of the files can be deleted
res = commands.getoutput( 'mv '+seqtree+'.gif'+' /home/kylem/public_html/temp/. ' )
res = commands.getoutput( 'mv '+structtree+'.gif'+' /home/kylem/public_html/temp/. ' )
