#!/usr/bin/python

# drawunrooted.py
# Use ete2 to render an unrooted tree from an input Newick formatted tree file.

# sys.argv[1] -- filename for tree file
# sys.argv[2] -- filename for output .png file

import sys
from ete2 import Tree, TreeStyle

if( len(sys.argv) != 3 ):
  print "Usage: python drawunrooted.py <Newick_file> <Tree_png>"
  exit(-1)

t = Tree(sys.argv[1])

r = TreeStyle()
r.mode = "r"
r.scale = 50

t.render(sys.argv[2], w=720, units="px", tree_style=r)
