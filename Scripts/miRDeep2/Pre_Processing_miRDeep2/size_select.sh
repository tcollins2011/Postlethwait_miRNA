#!/usr/bin/bash
#SBATCH --account=bgmp
#SBATCH --partition=bgmp
#SBATCH --cpus-per-task=1
#SBATCH --mail-user='llewis3@uoregon.edu'
#SBATCH --mail-type=END,FAIL
#SBATCH --time=10:00:00
dir="/projects/bgmp/shared/2021_projects/Postlethwait/Provided_Project_Data/reads/"

ls -1 ${dir}| while read line
do
    # mkdir ${dir}/Size_Select_${line}
    ls -1 ${dir}${line}| while read file
    do
        python size_select.py -f ${dir}${line}/${file} --min 17 --max 25
    done
done