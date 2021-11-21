#!/usr/bin/bash
#SBATCH --account=bgmp
#SBATCH --partition=bgmp
#SBATCH --cpus-per-task=1
#SBATCH --time=10:00:00

dir="/projects/bgmp/shared/2021_projects/Postlethwait/Provided_Project_Data/reads/Size_Selected/"

for directory in ${dir}*;
do 
    for file in ${directory}/*fa;
    
    do
        collapse_reads_md.pl ${file} COP > ${directory}/Collapsed/collapsed_$(basename $file)
    done
    
done