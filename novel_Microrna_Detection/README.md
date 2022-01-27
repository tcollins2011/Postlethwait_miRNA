miRDeep2 Analysis 
=================================================


Table of contents
-----------------

* [Introduction](#introduction)
* [Installation](#installation)
* [Authors and history](#authors-and-history)
* [Acknowledgments](#acknowledgments)


Introduction
------------

This section of the project contains all of the code that was used to run miRDeep2 analysis. It is structured in to the three main steps that were done on the data: pre-processing, running miRDeep2, and post-processing. 

Installation
------------

If miRDeep2 isn't installed yet you can obtain the main package from miRDeep2 and the patched files from patch by clicking on 'Clone or download' and then on 'Download Zip'. Extract the zipped files and then open a command line window. If you have git installed you can obtain the packages also directly from the command line by typing

git clone https://github.com/rajewsky-lab/mirdeep2.git
and
git clone https://github.com/Drmirdeep/mirdeep2_patch.git

To install the main package enter the directory was exracted to and then type:

perl install.pl

This will start the installer and download and install all third party dependencies. 

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