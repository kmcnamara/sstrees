#!/usr/bin/python

# runMatt.py
# Use Matt to determine distance scores between all pairs of proteins
# in a given set.

# sys.argv[1] -- input list of .pdb file names to align
# sys.argv[2] -- project directory

import sys
import os
import commands

from kmutils import fileToList, splitLines, scaleFakeTM

### Setup ###

matt = '/home/kylem/BIMM185/Matt-src-1.00/bin/Matt'
pdb_dir = sys.argv[2]

### Functions ###

# runAlignment
# input: 'xxxx.pdb', 'yyyy.pdb'
# return: string Score
# Run structure alignment on the two input structures and return the Score
def runAlignment(pdb1, pdb2):
    Score = 0
    length = -1
    align = matt+' '+pdb_dir+pdb1+':'+pdb1[-5]+' '+pdb_dir+pdb2+':'+pdb2[-5]
    result = commands.getoutput(align)
    # Parse for the score and alignment length 
    result = splitLines('MattAlignment.txt')
    Score = float(result[3][2])
    length = float(result[1][2])
    Score = Score / length
    # Remove output files
    toremove = 'MattAlignment.fasta MattAlignment.pdb MattAlignment.spt '+\
               'MattAlignment.txt'
    removed = commands.getoutput('rm '+toremove)
    # Return the Score
    return str(Score)
# End of runAlignment

### End of Functions ###

### Main ###

print '\nRunning runMatt.py...'

# Read in the .pdb file names
pdbs = splitLines(sys.argv[1])

# Initialize distance matrix with zeros
Score_matrix = []
for row in range( len(pdbs) ):
    Score_matrix.append([])
    for col in range( len(pdbs) ):
        Score_matrix[row].append('0.0')

maxval = -1.0
for A in range( len(pdbs) ):
    for B in range( len(pdbs) ):
        if(B < A):
            # Fill in matrix[A][B] and matrix[B][A] with RMSD value
            Score_matrix[A][B] = runAlignment(pdbs[A][0], pdbs[B][0])
            Score_matrix[B][A] = Score_matrix[A][B]
            if( float(Score_matrix[A][B]) > maxval ):
              maxval = float(Score_matrix[A][B])

# Scale the RMSD matrix
maxval += 0.1
Score_matrix[:] = scaleFakeTM( Score_matrix, maxval )

outfile = open('mattScore.out', 'w')
# Follow PHYLIP distance matrix format
outfile.write( str(len(pdbs)) )
# Send distance matrix numbers to output file
for row in range( len(Score_matrix) ):
    outfile.write( '\n' + pdbs[row][0][:-6] + '         ' )
    for col in range( len(Score_matrix[0]) ):
        outfile.write( ' ' + Score_matrix[row][col]  )
outfile.write( '\n' )
outfile.close()

print 'Distance matrix written to mattScore.out\n'

#### End of Main ###
