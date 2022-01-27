#!/usr/bin/bash
#SBATCH --account=bgmp
#SBATCH --partition=bgmp
#SBATCH --cpus-per-task=1
#SBATCH --mail-user='tcollin2@uoregon.edu'
#SBATCH --mail-type=END,FAIL
#SBATCH --time=10:00:00

# Call The tyler_find_diff.py code on each directory in output land

targetdirectory=$1
ReferenceSpecies=$2

conda activate fixed_icefish
for dir in ${targetdirectory}*
do  
    for file in $dir/*
    do
        if [[ -f $file ]]
        then
            python code/find_diff.py --fasta $file --species $ReferenceSpecies
        fi
    done
done

