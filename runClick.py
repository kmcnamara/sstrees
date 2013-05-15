#!/usr/bin/python
import sys
import os
import commands

# # # # # # #
# runClick.py
# Kyle McNamara
# Script to use Click to determine RMSD values between all pairs of proteins
# in a given set.
# # # # # # #

### Setup ###

click = '/home/kyle/BIMM185/Click/click.py'
click_dir = '/home/kyle/BIMM185/Click'
pdb_dir = '/home/kyle/BIMM185/pdbs'

### Functions ###

# fileToList
# input: 'filename', filecontents[]
# return: none
# Open a file and use readlines() to transfer its lines to a list
def fileToList(filename, filecontents):
  file = open(filename, 'r')
  filecontents[:] = file.readlines()
  file.close()
  return
# End of fileToList

# splitLines
# input: 'filename'
# return: filecontents[[]]
# Use fileToList to put the file contents into a list and then use split()
# on each line and return the file contents as a 2D list
def splitLines(filename):
  myList_init = []
  fileToList(filename, myList_init)
  myList = []
  for i in range(len(myList_init)):
    myList.append(myList_init[i].split())
  return myList
# End of splitLines

# runAlignment
# input: 'xxxx.pdb', 'yyyy.pdb'
# return: float RMSD
# Run structure alignment on the two input structures and return the RMSD
def runAlignment(pdb1, pdb2):
    align = click +' '+ pdb_dir +'/'+ pdb1 +' '+ pdb_dir +'/'+ pdb2
    result = commands.getoutput(align)
    # Output clique file looks like "XXXX-YYYY.pdb.1.clique"
    clique = pdb_dir +'/'+ pdb1[:-4] +'-'+ pdb2 +'.1.clique'
    # Output the first 2 lines of the clique file
    result = commands.getoutput('head -2 '+ clique)
    # Split by '\n', take index[1], then split by ' ', take index[2]
    RMSD = result.split('\n') # ['The number ... = 206', 'RMSD = 1.18']
    RMSD = RMSD[1].split()    # ['RMSD', '=', '1.18']
    RMSD = RMSD[2]            # '1.18'
    # Return the RMSD
    return RMSD
# End of runAlignment

### End of Functions ###

### Main ###

print '\nRunning runClick.py...'
# Usage
if(len(sys.argv) != 2):
    sys.stderr.write('Usage: '+ sys.argv[0] + ' <PDBList>\n\n')
    sys.exit(1)

# Read in the .pdb file names
pdbs = splitLines(sys.argv[1])

# Change directory to location of click.py script
os.chdir(click_dir)

# Initialize distance matrix with zeros
RMSD_matrix = []
for row in range( len(pdbs) ):
    RMSD_matrix.append([])
    for col in range( len(pdbs) ):
        RMSD_matrix[row].append('0.0')

for A in range( len(pdbs) ):
    for B in range( len(pdbs) ):
        if(B < A):
            # Fill in matrix[A][B] and matrix[B][A] with RMSD value
            RMSD_matrix[A][B] = runAlignment(pdbs[A][0], pdbs[B][0])
            RMSD_matrix[B][A] = RMSD_matrix[A][B]

# Return to location of pdb files to create output file
os.chdir(pdb_dir)

outfile = open('clickRMSD.out', 'w')
# Follow PHYLIP distance matrix format
outfile.write( str(len(pdbs)) )
# Send distance matrix numbers to output file
for row in range( len(RMSD_matrix) ):
    outfile.write( '\n' + pdbs[row][0][:-4] + '         ' )
    for col in range( len(RMSD_matrix[0]) ):
        outfile.write( ' ' + RMSD_matrix[row][col]  )
outfile.write( '\n' )
outfile.close()

print 'Distance matrix written to clickRMSD.out\n'

#### End of Main ###
