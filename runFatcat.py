#!/usr/bin/python

# runFatcat.py
# Use FATCAT to determine distance scores between all pairs of proteins
# in a given set.

# sys.argv[1] -- input list of .pdb file names to align
# sys.argv[2] -- project directory

import sys
import os
import commands

from kmutils import fileToList, splitLines, scaleFakeTM

### Setup ###

fatcat = 'sh /home/kyle/BIMM185/scripts/Fatcat.sh'
#fatcat_dir = '/home/kyle/BIMM185/jfatcat/'
pdb_dir = sys.argv[2]
fatcat_opt = ' -pdbFilePath '+pdb_dir+' -flexible true -printFatCat true'

### Functions ###

# runAlignment
# input: 'xxxx.pdb', 'yyyy.pdb'
# return: string Score
# Run structure alignment on the two input structures and return the Score
def runAlignment(pdb1, pdb2):
    Score = 0
    length = -1
    align = fatcat+' -file1 '+pdb_dir+pdb1+' -file2 '+pdb_dir+pdb2+fatcat_opt
    result = commands.getoutput(align)
    # Parse for the score line
    result = result.split('\n')            # result is now a list of lines
    for i in range( len( result ) ):
      line = result[i].split()             # line is a list of words
      if( line[0] == 'Twists' ):           # Looking for first word == Twists
        break
    for i in range( len( line ) ):
      if( line[i] == 'Score' ):            # Looking for word == Score
        Score = float(line[i+1])           # Store Score
        length = float(line[i+3])          # Store align-len
        break
    Score = Score / length
    # Return the Score
    return str(Score)
# End of runAlignment

### End of Functions ###

### Main ###

print '\nRunning runFatcat.py...'

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

outfile = open('fatcatScore.out', 'w')
# Follow PHYLIP distance matrix format
outfile.write( str(len(pdbs)) )
# Send distance matrix numbers to output file
for row in range( len(Score_matrix) ):
    outfile.write( '\n' + pdbs[row][0][:-4] + '         ' )
    for col in range( len(Score_matrix[0]) ):
        outfile.write( ' ' + Score_matrix[row][col]  )
outfile.write( '\n' )
outfile.close()

print 'Distance matrix written to fatcatScore.out\n'

#### End of Main ###
