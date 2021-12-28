# Script that looks thorugh all of our fa files and ensures that they are in DNA format and not RNA 

dir="/projects/bgmp/shared/2021_projects/Postlethwait/Provided_Project_Data/reads/"

ls -1 ${dir}| while read line
do
    ls -1 ${dir}${line}| while read file
    do  
        grep "U"  ${dir}${line}/${file}
    done
done;
