#!/usr/bin/python

# kmutils.py
# Home for functions used commonly in other files in the SVS project

### File Parsing

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

### Number crunching

# scaleRMSD
# input: RMSD[[]], int maxval
# return: scaled[[]]
# Scale RMSD values to a [0,1] scale
def scaleRMSD(RMSD, maxval):
  scaled = []
  for row in range(len(RMSD)):
    scaled.append([])
    for col in range(len(RMSD[row])):
      if( row == col):
        # Skip over diagonal zeros
        scaled[row].append('0.0')
      else:
        scaled[row].append( str( float(RMSD[row][col]) / maxval ) )
  return scaled
# End of scaleRMSD

# scaleFakeTM
# input: Scores[[]], int maxval
# return: scaled[[]]
# Scale Scores to a [0,1] scale, then do (1 - value) for each score
def scaleFakeTM(Scores, maxval):
  scaled = []
  for row in range(len(Scores)):
    scaled.append([])
    for col in range(len(Scores[row])):
      if( row == col):
        # Skip over diagonal zeros
        scaled[row].append('0.0')
      else:
        score = 1.00 - ( float(Scores[row][col]) / maxval )
        scaled[row].append( str(score) )
  return scaled

### PDB to fasta

# threeToOneLetterAA
# Dictionary for converting three letter amino acid abbreviations to their
# respective single letter representations
threeToOneLetterAA = { 'ALA':'A', 'CYS':'C', 'ASP':'D', 'GLU':'E', 'PHE':'F',\
                       'GLY':'G', 'HIS':'H', 'ILE':'I', 'LYS':'K', 'LEU':'L',\
                       'MET':'M', 'ASN':'N', 'PRO':'P', 'GLN':'Q', 'ARG':'R',\
                       'SER':'S', 'THR':'T', 'VAL':'V', 'TRP':'W', 'TYR':'Y',\
                       'SEC':'U' }

# End of kmutils.py
