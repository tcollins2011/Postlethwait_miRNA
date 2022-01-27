Vienna RNAfold 
=================================================


Table of Contents
-----------------


* [Introduction](#introduction)
* [Installation](#installation)
* [Usage](#usage)
* [Authors and history](#authors-and-history)
* [Acknowledgments](#acknowledgments)


Introduction
------------
This section of the project contains all of the code that was used to run Vienna RNAfold (Version 2.5.0).

Installation
------------
If Vienna RNAfold is not installed yet, download the software from https://anaconda.org/bioconda/viennarna

Talapas Installation
------------
1) Create a new conda environment that includes your Vienna RNAfold installation
2) Activate your newly created environment

Usage
-----
RNAfold -p -d2 --noLP -T <temperature in Celsius> < <input_sequence.txt> > <output.txt>

Authors and history
---------------------------

* Logan Lewis - Algorithm Design
* Began Nguy - Algorithm Design
* Tyler Collins - Algorithm Design
* Thomas Desvignes - Conceptual Design Leader
* John H. Postlethwait - Project Advisor

Acknowledgments
---------------

We’d like to thank Dr. Thomas Desvignes and Dr. John Postlethwait for their guidance on the project, as well as the wonderful BGMP staff: Jason Sydes, Pete Batzel, Dr. Leslie Coonrod, and Dr. Stacey Wagner.
Sequencing performed at the University of Oregon Genomics Characterization Core Facility (GC3F). This work benefited from access to the University of Oregon supercomputer, Talapas.