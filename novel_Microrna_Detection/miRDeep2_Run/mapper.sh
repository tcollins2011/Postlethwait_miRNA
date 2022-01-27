#!/usr/bin/bash
#SBATCH --account=bgmp
#SBATCH --partition=bgmp
#SBATCH --cpus-per-task=1
#SBATCH --mail-user='tcollin2@uoregon.edu'
#SBATCH --mail-type=END,FAIL
#SBATCH --time=10:00:00

# Pass in Config File Location
# Pass in Genome FIle Location and Prefix
# Pass in Output Directory Pathway

ConfigFile=$1
Genome=$2
OutputDirectory=$3

[ -d ${OutputDirectory} ] || mkdir ${OutputDirectory}
mapper.pl ${ConfigFile} -d -c -j -i -l 17 -p ${Genome} -t ${OutputDirectory}/read_col_vs_genome.arf -s ${OutputDirectory}/reads.fa

# /projects/bgmp/shared/2021_projects/Postlethwait/Provided_Project_Data/reads/Size_Selected/Size_Select_Champsocephalus_gunnari/Collapsed/config.txt
# /projects/bgmp/shared/2021_projects/Postlethwait/Provided_Project_Data/genome_assemblies/index_genomes/Champsocephalus_gunnari/index_champ.fa
# /projects/bgmp/shared/2021_projects/Postlethwait/Provided_Project_Data/Mappings/Champsocephalus_gunnari