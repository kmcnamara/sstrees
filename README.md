Sequence Versus Structure
=======

<b>Kyle McNamara</b>

<b>kmcnamara@ucsd.edu</b>

This is a collection of all the source code used to control the work flow
for all the prediction, alignment, and tree drawing software used in this
project.

Master scripts
--------------
* masterHandle.py
* handleSeqTree.py

Alignment Prep
-----------------------------

* splitPDB.py
* runsplitPDB.py
* pullSeqFromPDB.py
* runClustal.sh
* kmutils.py
* makeChainFile.py
* getStuctures.py

Alignment
---------

These scripts all accept a list of filenames for the <b>.pdb</b> files of
structures to be analyzed. And, for output they generate a comma-separated
distance matrix to be passed along to the tree drawing program.

* runClick.py
* runDeepAlign.py
* runFatCat.py
	- Fatcat.sh
* runMatt.py
* runTMAlign.py

Tree Calculation and Illustration
---------------------------------

* neighborjoin.sh
* printunrooted.py

Webpage
-------

* index.html
* analysis.html
* input.php
* result.php
* about.html
* contact.html
* override.css


Installed Programs, Libraries, and Dependencies
-----------------------------------------------

This is a list of all the installed software being used for this project.

* DeepAlign		(structure alignment)
* FATCAT		(structure alignment)
* Click			(structure alignment)
* Modeller		(for use by Click)
* Matt			(structure alignment)
* TMalign		(structure alignment)
* ClustalW		(sequence alignment)
* PHYLIP		(tree construction)
* Mechanize             (Python - tree printing)
* Bootstrap             (webpage)



<i>Updated 5/27/13</i>
