#!/usr/bin/env python
import argparse
import csv
from datetime import datetime 
import os

def get_args():
    parser = argparse.ArgumentParser(
        description="Takes a csv of ontologous genes and convert it to separate Fasta files for hairpin analysis"
    )
    parser.add_argument(
        "-f",
        "--file",
        help="csv with first coloumn as gene names",
        required=True,
    ),
    parser.add_argument(
        "-o",
        "--output",
        help="output directory",
        default = datetime.now(),
    )
    return parser.parse_args()

def convert_fasta(file,output):
    with open(file, encoding='utf-8-sig') as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=',')
        data = list(csv_reader)
        for i in data:
            ontologous_gene = (i['Group_name'] + '.fa')
            ontologous_gene_directory = i['Group_name']
            directory_exists = os.path.exists(os.path.join(output,ontologous_gene_directory))
            if directory_exists == False:
                os.mkdir(os.path.join(output,ontologous_gene_directory))
            file_exists = os.path.exists(os.path.join(output,ontologous_gene_directory,ontologous_gene))
            if file_exists:
                with open(os.path.join(output,ontologous_gene_directory,ontologous_gene), 'a') as fasta:
                    fasta.write('>' + i['Hairpin_name'] + '-hairpin' '\n')
                    fasta.write(i['Hairpin_Sequence'] + '\n')
                    fasta.write('>' + i['5pMature'] +  '\n')
                    fasta.write(i['5pSequence'] + '\n')
                    fasta.write('>' + i['3pMature'] + '\n')
                    fasta.write(i['3pSequence'] + '\n')            
            else:
                 with open(os.path.join(output,ontologous_gene_directory,ontologous_gene), 'w') as fasta:
                    fasta.write('>' + i['Hairpin_name'] + '-hairpin' '\n')
                    fasta.write(i['Hairpin_Sequence'] + '\n')
                    fasta.write('>' + i['5pMature'] +  '\n')
                    fasta.write(i['5pSequence'] + '\n')
                    fasta.write('>' + i['3pMature'] + '\n')
                    fasta.write(i['3pSequence'] + '\n') 

if __name__=='__main__':
    args = get_args()
    parent_dir = os.path.dirname(os.getcwd())
    path = os.path.join(parent_dir, "data",  str(args.output))
    file_exists = os.path.exists(path)
    if file_exists == False:
        os.mkdir(path)
    else:
        print('directory already exists but the program will continue anyway')
    convert_fasta(args.file,path)

