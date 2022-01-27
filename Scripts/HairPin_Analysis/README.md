# mirna-evolution-analysis

some basic script to make multi-alignment and parse the changes

## Installation

Having conda and the channels properly configures as in :https://bioconda.github.io/user/install.html#set-up-channels

```
conda install mafft
conda install r-tidyverse
conda install r-ggthemes
conda install r-ggplot2
```

## Method

The important tool here is: https://mafft.cbrc.jp/alignment/software/, it has been used for this goal in the past, so maybe it is a good option.

## Usage

From this folder, run:

```
 python code/find_diff.py --fasta input/let-7h-2_example_190820.fas  --species gac
```

The output files are:

* input.summary.txt: reference nts and mirna positions, and then all the changes in the other species.
  * `nt,ref,NA,1`: this kind of lines indicates the nt of the reference species at that position
  * `5p-pos,sps,10,32`: this kind of lines indicates the position start and end of the mature mirna in a given species
  * `nt-change,sps1,104,NA,a`: this kind of lines indicate a nt-change in a species in a given position and to a given nt
* input.summary.txt.pdf: plot of the nts in the reference species, the changes in others, and the location of the mirnas in all.
