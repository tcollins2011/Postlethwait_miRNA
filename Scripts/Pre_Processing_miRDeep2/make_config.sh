#!/usr/bin/bash
#SBATCH --account=bgmp
#SBATCH --partition=bgmp
#SBATCH --cpus-per-task=1
#SBATCH --time=10:00:00

dir="/projects/bgmp/shared/2021_projects/Postlethwait/Provided_Project_Data/reads/Size_Selected/"
Identifer=$1
for directory in ${dir}*;
do 
    target=${directory}/Collapsed
    rm ${target}/config.txt
    COUNTER=0
    for file in ${target}/*.fa;
    
    do
        if [ "$COUNTER" -gt 9 ]; then
            echo ${file} ${Identifer:0:1}${COUNTER} >> ${directory}/Collapsed/config.txt
        else
            echo ${file} ${Identifer}${COUNTER} >> ${directory}/Collapsed/config.txt
        fi
        let COUNTER++

        
    done
    
done