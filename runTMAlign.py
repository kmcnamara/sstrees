#!/usr/bin/python

# runTMAlign.py
# Use TMAlign to determine TM-score values between all pairs of proteins
# in a given set.

# sys.argv[1] -- input list of .pdb file names to align

import sys
import os
import commands

from kmutils import fileToList, splitLines

### Setup ###

tmalign = '/home/kyle/BIMM185/TMAlign/TMalign'
pdb_dir = '/home/kyle/BIMM185/pdbs/test/'

### Functions ###

# runAlignment
# input: 'xxxx.pdb', 'yyyy.pdb'
# return: string TM-Score
# Run structure alignment on the two input structures and return the TM-Score
def runAlignment(pdb1, pdb2):
    align = tmalign+' '+pdb_dir+pdb1+' '+pdb_dir+pdb2+' -a'
    result = commands.getoutput(align)
    lines = result.split('\n')
    line = lines[15].split()
    TMS = line[1]
    # Return the TM-Score
    return TMS
# End of runAlignment

### End of Functions ###

### Main ###

# Usage
if(len(sys.argv) != 2):
    sys.stderr.write('\nUsage: '+ sys.argv[0] + ' <PDBList>\n\n')
    sys.exit(1)

print '\nRunning runTMAlign.py...'

# Read in the .pdb file names
pdbs = splitLines(sys.argv[1])

# Initialize distance matrix with zeros
TM_matrix = []
for row in range( len(pdbs) ):
    TM_matrix.append([])
    for col in range( len(pdbs) ):
        TM_matrix[row].append('0.0')

# Enter distance scores as 1 - TM Score
for A in range( len(pdbs) ):
    for B in range( len(pdbs) ):
        if(B < A):
            # Fill in matrix[A][B] and matrix[B][A] with TM-Score
            myTM = runAlignment(pdbs[A][0], pdbs[B][0])
            myTM = 1.00 - float(myTM)
            myTM = str(myTM)
            TM_matrix[A][B] = myTM
            TM_matrix[B][A] = myTM


outfile = open('TMAlignTM.out', 'w')
# Follow PHYLIP distance matrix format
outfile.write( str(len(pdbs)) )
# Send distance matrix numbers to output file
for row in range( len(TM_matrix) ):
    outfile.write( '\n' + pdbs[row][0][:-4] + '         ' )
    for col in range( len(TM_matrix[0]) ):
        outfile.write( ' ' + TM_matrix[row][col]  )
outfile.write( '\n' )
outfile.close()

print 'Distance matrix written to TMAlignTM.out\n'

#### End of Main ###
