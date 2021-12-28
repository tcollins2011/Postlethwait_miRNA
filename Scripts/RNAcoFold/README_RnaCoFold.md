cofold_prep.py takes a csv with miRNA dimer sequences and their names. The script expects the dimer sequnces in the first and third column and the names of the miRNAs in the second and fourth column.
The output is a fasta file with the miRNA names as the headers with a "+" between them, and the two sequnces as the sequence line with a "$" between them (this $ is required by the RNACoFold software)

RNACoFold Dimer Analysis
=================================================


Table of contents
-----------------

* [Introduction](#introduction)
* [Installation](#installation)
* [Usage](#usage)
* [Authors and history](#authors-and-history)
* [Acknowledgments](#acknowledgments)


Introduction
------------

This section of the project contains all of the code that was used to run RNACoFold, which returns information regarding the sability of RNA dimers. For our purposes, we used the program to investigate miRNA dimers.

Installation
------------

If miRDeep2 isn't installed yet you can obtain the main package from miRDeep2 and the patched files from patch by clicking on 'Clone or download' and then on 'Download Zip'. Extract the zipped files and then open a command line window. If you have git installed you can obtain the packages also directly from the command line by typing

git clone https://github.com/rajewsky-lab/mirdeep2.git
and
git clone https://github.com/Drmirdeep/mirdeep2_patch.git

To install the main package enter the directory was exracted to and then type:

perl install.pl

This will start the installer and download and install all third party dependencies. 

Usage
-----


Authors and history
---------------------------

* Logan Lewis - Algorithm Design
* Began Nguy - Algorithm Design
* Tyler Collins - Algorithm Design
* Thomas Desvignes - Conceptual Design Leader
* John H. Postlethwait - Project Advisor

Acknowledgments
---------------

We wish to extend a heartfelt thanks to all faculty of BGMP for their assitance. 