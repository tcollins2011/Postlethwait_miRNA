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

We installed ViennaRNA version 2.5.0 (the software suite containing RNACoFold) using bioconda:
***
conda install -c bioconda viennarna
***
You can only install it using the instructions on the ViennaRNA github:
https://github.com/ViennaRNA/ViennaRNA 

Usage
-----
**cofold_prep.py:**
Takes a csv with miRNA dimer sequences and their names. The script expects the dimer sequnces in the first and third column and the names of the miRNAs in the second and fourth column.

The output is a fasta file with the miRNA names as the headers with a "+" between them, and the two sequnces as the sequence line with a "&" between them (this & is required by the RNACoFold software)

**RNACoFold:**
RNACoFold -p --temp=<tempurature in celcius> < <input fasta> > <output file>

**Process_cofold_results.py**
Takes RNACofold output file (-f) and returns an output csv file (-o) with all relevant information in columns

**GC_content_check.py**
Takes Process_cofold_results.py output (-f) and reuturns an output csv file (-o) that contains all info from the input file with added columns from GC content, as well as the percentage of Gs and Cs that are paired or unpaired in the dimer according to the RNACoFold predicted pairing.


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