#!/usr/bin/sh

# neighborjoin.sh
# Run PHYLIP's neighbor joining clustering algorithm on an input phylip
# formatted distance matrix.

# This script takes two arguments, both filenames for the distance matrix
# file and the file containing options to use in neighbor.

# $1 -- options file

echo `/home/kylem/BIMM185/phylip*/exe/neighbor < $1 `
