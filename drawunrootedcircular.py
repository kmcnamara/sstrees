#!/usr/bin/python

# drawunrootedcircular.py
# Use ete2 to render an unrooted tree from an input Newick formatted tree file.
# Render the tree as circular.

# sys.argv[1] -- filename for tree file
# sys.argv[2] -- filename for output .png file

import sys
from ete2 import Tree, TreeStyle

if( len(sys.argv) != 3 ):
  print "Usage: python drawunrootedcircular.py <Newick_file> <Tree_png>"
  exit(-1)

t = Tree(sys.argv[1])
c = TreeStyle()
c.mode = "c"
c.scale = 50
c.arc_start = -90
c.arc_span = 360

t.render(sys.argv[2], w=720, units="px", tree_style=c)
