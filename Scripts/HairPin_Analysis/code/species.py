#!/usr/bin/env python
import argparse
import os
import csv
from datetime import datetime 

def get_args():
    parser = argparse.ArgumentParser(
        description="Takes a csv of ontologous genes and remove all genes that don't have the selected reference species"
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
    ),
    parser.add_argument(
        "-s",
        "--species",
        help="selected reference species",
        required=True,
    ),
    return parser.parse_args()

def clean_csv(file,species,output):
    all_genes = {}
    target = []
    with open(file, encoding='utf-8-sig') as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=',')
        data = list(csv_reader)
        for i in data:
            if i['Group_name'] not in all_genes.keys():
                all_genes[i['Group_name']] = []
            all_genes[i['Group_name']].append(i)
    for key,value in all_genes.items():
        reference_species_present = False 
        for entry in value:
           if (entry['Species']) == species:
               reference_species_present = True
        if reference_species_present:
            target.append(value)
    output_csv_location = os.path.join(output,species)
    with open(output_csv_location + '.csv','w', newline='') as csv_file:
        fieldnames = ['Group_name','Species','Hairpin_name','Hairpin_Sequence','5pMature','5pSequence','3pMature','3pSequence']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        writer.writeheader()
        for i in target:
            for j in i:
                writer.writerow(j)


if __name__=='__main__':
    args = get_args()
    parent_dir = os.path.dirname(os.getcwd())
    path = os.path.join(parent_dir, "data",  str(args.output))
    file_exists = os.path.exists(path)
    if file_exists == False:
        os.mkdir(path)
    else:
        print('directory already exists but the program will continue anyway')
    clean_csv(args.file,args.species,path)

