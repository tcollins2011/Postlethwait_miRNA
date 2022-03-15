'''
This script extract the major measurements from Vienna RNA fold raw output. The extracted measurements is generated on to an excel sheet.
Line to change for input is 77 and 101

Usage: python3 rna_fold_extract.py
'''

import pandas as pd
import re

def parse_rnafold(read_rnafold):
	header = str()
	sequence = str()
	optimal_secondary_structure = str()
	optimal_secondary_mfe = str()
	free_energy_thermo_ensemb = str()
	frequency_MFE_structure_ensemb = str()
	ensemb_diversity = str()
	centroid_secondary_structure = str()
	centroid_secondary_mfe = str()

	count = 0

	for line in read_rnafold:
		line = line.strip("\n")
		if count % 6 == 0:
			header = line[1:]
			count += 1
		elif count % 6 == 1:
			sequence = line
			count += 1
		elif count % 6 == 2:
			structure_split = line.split(" ")
			optimal_secondary_structure  = structure_split[0]
			if len(structure_split) > 2:
				optimal_secondary_mfe = structure_split[2].replace(")","")
			else:
				optimal_secondary_mfe = structure_split[1].replace("(","").replace(")","")
			count += 1
		elif count % 6 == 3:
			structure_split = line.split(" ")
			if len(structure_split) > 2:
				free_energy_thermo_ensemb = structure_split[2].replace("]","")
			else:
				free_energy_thermo_ensemb = structure_split[1].replace("[","").replace("]","")
			count += 1
		elif count % 6 == 4:
			structure_split = line.split(" ")
			centroid_secondary_structure  = structure_split[0]
			if len(structure_split) > 3:
				centroid_secondary_mfe = structure_split[2]
			else:
				centroid_secondary_mfe = structure_split[1].replace("{","")
			count += 1
		elif count % 6 == 5:
			ensembl_freq = re.search('ensemble ([0-9\.]+);', line)
			frequency_MFE_structure_ensemb = float(ensembl_freq[1]) * 100
			frequency_MFE_structure_ensemb = str(frequency_MFE_structure_ensemb)

			re_ensemb = re.search('ensemble diversity ([0-9\.]+)', line)
			ensemb_diversity = re_ensemb[1]
			count = 0
			yield(header, sequence, optimal_secondary_structure,
				optimal_secondary_mfe, free_energy_thermo_ensemb, frequency_MFE_structure_ensemb, 
				ensemb_diversity, centroid_secondary_structure, centroid_secondary_mfe)

def main():
	header_list = list()
	sequence_list = list()
	optimal_secondary_structure_list = list()
	optimal_secondary_mfe_list = list()
	free_energy_thermo_ensemb_list = list()
	frequency_MFE_structure_ensemb_list = list()
	ensemb_diversity_list = list()
	centroid_secondary_structure_list = list()
	centroid_secondary_mfe_list = list()

	read_rnafold = open("annotation_noto_miRNA.out", "r")

	for header, sequence, optimal_secondary_structure, optimal_secondary_mfe, free_energy_thermo_ensemb, frequency_MFE_structure_ensemb, ensemb_diversity, centroid_secondary_structure, centroid_secondary_mfe in parse_rnafold(read_rnafold):
		header_list.append(header)
		sequence_list.append(sequence)
		optimal_secondary_structure_list.append(optimal_secondary_structure)
		optimal_secondary_mfe_list.append(optimal_secondary_mfe)
		free_energy_thermo_ensemb_list.append(free_energy_thermo_ensemb)
		frequency_MFE_structure_ensemb_list.append(frequency_MFE_structure_ensemb)
		ensemb_diversity_list.append(ensemb_diversity)
		centroid_secondary_structure_list.append(centroid_secondary_structure)
		centroid_secondary_mfe_list.append(centroid_secondary_mfe)

	ice_fish_dict = {"miRNA": header_list, "Sequence": sequence_list,
					"Optimal Secondary Structure": optimal_secondary_structure_list,
					"Minimum Free Energy of Optimal Secondary Structure (kcal/mol)": optimal_secondary_mfe_list,
					"Free Energy of the Thermodynamic Ensemble (kcal/mol)": free_energy_thermo_ensemb_list,
					"Frequency of the MFE Structure (%)": frequency_MFE_structure_ensemb_list,
					"Ensemble Diversity": ensemb_diversity_list,
					"Centroid Secondary Structure": centroid_secondary_structure_list,
					"Minimum Free Energy of Centroid Secondary Structure (kcal/mol)": centroid_secondary_mfe_list
	}
	
	ice_fish_pd_frame = pd.DataFrame.from_dict(ice_fish_dict)
	ice_fish_pd_frame.to_csv("annotation_noto_miRNA.csv", index=False)

if __name__ == "__main__":
    main()
