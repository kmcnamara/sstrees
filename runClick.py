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

click = '~/BIMM185/Click/click.py'
click_dir = '~/BIMM185/Click/'
pdb_dir = '~/BIMM185/pdbs/'

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
    align = click +' '+ pdb_dir + pdb1 +' '+ pdb_dir + pdb2
    commands.getoutput(align)
    # Output clique file looks like "XXXX-YYYY.pdb.1.clique"
    clique = pdb1[:-4] +'-'+ pdb2 +'.1.clique'
    # Output the first 2 lines of the clique file
    result = commands.getoutput('head -2 '+ clique)
    # Split by '\n', take index[1], then split by ' ', take index[2]
    RMSD = result.split('\n') # ['The number ... = 206', 'RMSD = 1.18']
    RMSD = RMSD[1].split()    # ['RMSD', '=', '1.18']
    RMSD = RMSD[2]            # '1.18'
    # Cast string to float
    return float(RMSD)
# End of runAlignment

### End of Functions ###

### Main ###

# Usage
if(len(sys.argv) != 2):
    print 'Usage: '+ argv[0] + ' <PDBList>'
    sys.exit()

os.system('cd '+ click_dir)

pdbs = splitLines(sys.argv[1])
RMSD_matrix = [[]]
for pdbA in len(pdbs):
    for pdbB in len(pdbs):
        if(pdbB < pdbA):
            RMSD_matrix[pdbA].append(runAlignment(pdbs[pdbA][0],
                                                  pdbs[pdbB][0]))
        else:
            RMSD_matrix[pdbA].append(float(0))
output = ''
for row in len(RMSD_matrix):
    for col in len(RMSD_matrix[0]):
        output += (RMSD_matrix[row][col] + ',')
    output += '\n'

outfile = open('clickRMSD.out', 'w')


os.system('cd '+ pdb_dir)

#### End of Main ###
