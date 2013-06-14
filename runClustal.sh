#!/usr/bin/sh

# runClustal.sh
# Do multiple sequence alignment plus neighbor joining using ClustalW.

# $1 -- multi-fasta file
# $2 -- output tree filename

echo `/home/kylem/BIMM185/clustalw-2.1/clustalw2 -tree -INFILE=$1 -outfile=$2 -output=PHYLIP`
