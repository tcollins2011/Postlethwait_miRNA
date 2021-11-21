#!/usr/bin/bash
#SBATCH --account=bgmp
#SBATCH --partition=bgmp
#SBATCH --cpus-per-task=1
#SBATCH --mail-user='tcollin2@uoregon.edu'
#SBATCH --mail-type=END,FAIL
#SBATCH --time=10:00:00


function generic_miRDeep2() {

    # $1 = index file
    # $2 = genome indexes
    # $3 = .arf files
    # $4 = mature Mirbase candidates by species
    # $5 = all mature miRbase candidates 
    # $6 = hairpin Mirbase candidates by species
    # -t species for UCSC genome browser
    # Should probably specify an output directory

    miRDeep2.pl $1 $2 $3 $4 $5 $6
}


# Can call the function down here and pass in the values that we want
# Could make an array with all of the files and pass those in


