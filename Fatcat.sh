#!/bin/bash

# example:

#  bash runFatcat.sh -pdb1 4hhb.A -pdb2 4hhb.B -pdbFilePath /tmp/ -autoFetch -show3d 
#  bash runFatcat.sh -pdb1 4hhb.A -pdb2 4hhb.B -pdbFilePath /tmp/ -printXML 
#  bash runFatcat.sh -pdb1 4hhb.A -pdb2 4hhb.B -pdbFilePath /tmp/ -printFatCat 
#  bash runFatcat.sh -pdb1 4hhb.A -pdb2 4hhb.B -pdbFilePath /tmp/ -printFatCat -flexible 

# send the arguments to the java app
# allows to specify a different config file
args="$*"

JDIR="/home/kyle/BIMM185/jfatcat";
cpath="$JDIR/core.jar:$JDIR/structure.jar:$JDIR/structure-gui.jar:$JDIR/alignment.jar:$JDIR/JmolApplet.jar:$JDIR/javaws.jar:$JDIR/biojava3-core.jar:$JDIR/biojava3-alignment.jar"
java -Xmx500M -cp $cpath org.biojava.bio.structure.align.fatcat.FatCat $args
