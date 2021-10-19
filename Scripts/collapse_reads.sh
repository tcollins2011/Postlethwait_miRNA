#!/usr/bin/bash
#SBATCH --account=bgmp
#SBATCH --partition=bgmp
#SBATCH --cpus-per-task=1
#SBATCH --mail-type=END,FAIL
#SBATCH --time=10:00:00

dir="/projects/bgmp/shared/2021_projects/Postlethwait/Provided_Project_Data/reads/Size_Selected/"

ls -1 ${dir}| while read line
do
    mkdir ${dir}${line}/Collapsed || rm -r ${dir}${line}/Collapsed
    mkdir ${dir}${line}/Collapsed
    ls -1 ${dir}${line} | while read file 
    do
        if [[${file} == *.fa]]
        then 
            echo "made it"
            #collapse_reads_md.pl ${file} COP > ${dir}${line}/Collapsed/collapsed_${file}
        else
            echo "${dir}${line} has no fa files"
        
        fi
    done
done