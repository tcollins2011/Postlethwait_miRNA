#!/usr/bin/bash
#SBATCH --account=bgmp
#SBATCH --partition=bgmp
#SBATCH --cpus-per-task=1
#SBATCH --mail-user='tcollin2@uoregon.edu'
#SBATCH --mail-type=END,FAIL
#SBATCH --time=10:00:00

OutputDirectory=$1
OutputFile=$2
[ -d ${OutputDirectory} ] || mkdir ${OutputDirectory}
echo -n"" > ${OutputDirectory}/$OutputFile
python miRDeep2_detangle.py -f '/projects/bgmp/shared/2021_projects/Postlethwait/Provided_Project_Data/mirdeep2_outputs/Bovichtus_diacanthus/result_05_11_2021_t_15_32_31.csv' -p'BDI' -o${OutputDirectory}/$OutputFile
python miRDeep2_detangle.py -f '/projects/bgmp/shared/2021_projects/Postlethwait/Provided_Project_Data/mirdeep2_outputs/Chaenocephalus_aceratus/result_08_11_2021_t_17_06_39.csv' -p'CAC' -o${OutputDirectory}/$OutputFile
python miRDeep2_detangle.py -f '/projects/bgmp/shared/2021_projects/Postlethwait/Provided_Project_Data/mirdeep2_outputs/Champsocephalus_gunnari/result_09_11_2021_t_16_00_36.csv' -p'CGU' -o${OutputDirectory}/$OutputFile
python miRDeep2_detangle.py -f '/projects/bgmp/shared/2021_projects/Postlethwait/Provided_Project_Data/mirdeep2_outputs/Cottoperca_gobio/result_08_11_2021_t_20_44_18.csv' -p'CGO' -o${OutputDirectory}/$OutputFile
python miRDeep2_detangle.py -f '/projects/bgmp/shared/2021_projects/Postlethwait/Provided_Project_Data/mirdeep2_outputs/Eleginops_maclovinus/result_08_11_2021_t_20_45_36.csv' -p'EMA' -o${OutputDirectory}/$OutputFile
python miRDeep2_detangle.py -f '/projects/bgmp/shared/2021_projects/Postlethwait/Provided_Project_Data/mirdeep2_outputs/Gobionotothen_gibberifrons/result_08_11_2021_t_20_46_14.csv' -p'GGI' -o${OutputDirectory}/$OutputFile
python miRDeep2_detangle.py -f '/projects/bgmp/shared/2021_projects/Postlethwait/Provided_Project_Data/mirdeep2_outputs/Notothenia_coriiceps/result_08_11_2021_t_20_46_54.csv' -p'NCO' -o${OutputDirectory}/$OutputFile

#  Create / check the output folder
#  Create file to write in the output folder
#  Call python function for each species 
