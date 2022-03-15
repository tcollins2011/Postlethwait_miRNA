'''
This script extracts a the sequences from a fasta file given the coordinates of the miRNAs

Usage: python3 seqExtract.py
Line 47 and 55 needs to be edited to the name of the input files. 
Line 47 for the input excel sheet containing the coordinates
Line 55 for the input fasta file
'''

import pandas as pd
import math

def oneline_fasta(file):	
	header = ''
	sequence = ''

	with open(file) as fh:	
		header = ''
		sequence = ''

		# Append first header
		line = fh.readline()
		header = line[1:].rstrip()

		for line in fh:
			if line.startswith ('>'):
				yield header,sequence
				header = line[1:].rstrip()
				sequence = ''
			else :
				sequence += ''.join(line.rstrip().split()).upper()
					
	yield header,sequence

def ReverseComplement(seq):
    for base in seq:
        if base not in 'ATCGatcg':
            print("Error: NOT a DNA sequence")
            return None
    seq1 = 'ATCGTAGCatcgtagc'
    seq_dict = { seq1[i]:seq1[i+4] for i in range(16) if i < 4 or 8<=i<12 }
    return "".join([seq_dict[base] for base in reversed(seq)])



# Start-------------------
def main():
	bdia = pd.read_excel('Emac_NovelHairpinPositions_211210.xlsx', index_col=None)
	hairpin_names = bdia['Hairpin_name'].tolist()
	hairpin_position_annot = bdia['Hairpin_position_annotation'].tolist()
	hairpin_position_m2m = bdia['Hairpin_position_m2m'].tolist()
	strand = bdia['Strand'].tolist()

	index_dict = dict()

	for header, sequence in oneline_fasta('Emaclovinus_scaffolds_v1.fa'):
		head = header.split(" ")
		index_dict[head[0]] = sequence

	#pprint.pprint(index_dict.keys())

	out_combine = 'Emac_Hairpin_m2m_Sequence.fa'
	m2m = open('{}'.format(out_combine),'w')

	annot_combine = 'Emac_Hairpin_Annotation_Sequence.fa'
	annotation = open('{}'.format(annot_combine),'w')

	for count in range(0, len(hairpin_names), 1):
		sequence_positions = ''
		annotation.write('>' + hairpin_names[count] + '\n')
		split_1 = hairpin_position_annot[count].split(':')
		index = split_1[0]
		positions = split_1[1]
		positions_split = positions.split('-')
		position_1 = positions_split[0] 
		position_2 = positions_split[1]

		sequence = index_dict[index]

		if strand[count] == '+':
			sequence_positions = sequence[int(position_1)-1:int(position_2)]
		else:
			sequence_positions = sequence[int(position_2)-1:int(position_1)]
			sequence_positions = ReverseComplement(sequence_positions)
		annotation.write(sequence_positions + '\n')

		# ---------------------------------------------

		# When hairpin position equals NA
		if pd.isna(hairpin_position_m2m[count]):
			continue

		sequence_positions = ''
		m2m.write('>' + hairpin_names[count] + '\n')
		split_1 = hairpin_position_m2m[count].split(':')
		index = split_1[0]
		positions = split_1[1]
		positions_split = positions.split('-')
		position_1 = positions_split[0] 
		position_2 = positions_split[1]
		sequence = index_dict[index]

		if strand[count] == '+':
			sequence_positions = sequence[int(position_1)-1:int(position_2)]
		else:
			sequence_positions = sequence[int(position_2)-1:int(position_1)]
			sequence_positions = ReverseComplement(sequence_positions)
		m2m.write(sequence_positions + '\n')
	
if __name__ == "__main__":
    main()
