Sequence Versus Structure
=======

Kyle McNamara

kmcnamara@ucsd.edu

This is a collection of all the source code used to control the work flow
for all the prediction, alignment, and tree drawing software used in this
project.

Prediction and Alignment Prep
-----------------------------

* splitPDB.py
* pullSeqFromPDB.py
* runClustal.sh
* kmutils.py
* runPrediction.sh

Alignment
---------

These scripts all accept a list of filenames for the <b>.pdb</b> files of
structures to be analyzed. And, for output they generate a comma-separated
distance matrix to be passed along to the tree drawing program.

* runClick.py
* runDeepAlign.py
* runFatCat.py
* runMatt.py

Tree Calculation and Illustration
---------------------------------

* neighborjoin.sh
* drawunrooted.py
* drawunrootedcircular.py


Installed Programs, Libraries, and Dependencies
-----------------------------------------------

This is a list of all the installed software being used for this project.

* I-TASSER		(structure prediction)
* DeepAlign		(structure alignment)
* FATCAT		(structure alignment)
* Click			(structure alignment)
* Modeller		(for use by Click)
* Matt			(structure alignment)
* ClustalW		(sequence alignment)
* PHYLIP		(tree construction)
* Ete2			(tree drawing)
* BioPython		(pdb file handling)
* Numpy
* Scipy


<i>Updated 5/19/13</i>
