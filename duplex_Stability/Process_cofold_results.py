#!/usr/bin/env python
import argparse


def get_args():
    parser = argparse.ArgumentParser(
        description="Takes a csv and coverts it to a fasta file in the format needed for RNACoFold"
    )
    parser.add_argument(
        "-f",
        "--file",
        help="Name of input RNACoFold file",
        required=True,
    ),
    parser.add_argument("-o", "--output", help="name for output csv", required=True)
    return parser.parse_args()


args = get_args()

# openning output file
fh_out = open(args.output, "w")

with open(args.file) as fh:
    # Writing the column names to the output file
    fh_out.write(
        "Species,miRNA names,Duplex Sequences,Sequence 1, Sequence 2, Secondary Structure,Free Energy(kcal/mol),Partition Function,Frequency of mfe Structure in Ensemble,Delta G Binding(kcal/mol)\n"
    )
    # collect all the lines pertaining to one entry (5 lines long)
    counter = 0
    line_storage = []
    for line in fh:
        counter += 1
        line_storage.append(line.strip())
        # once I have all 5 lines
        if counter % 5 == 0:
            # complicated splitting to grab needed info (probably should've used Regex)
            species = line_storage[0].split(">")[1].split("-")[0]
            names = line_storage[0].split(">")[1]
            sequence = line_storage[1]
            seq1 = line_storage[1].split("&")[0]
            seq2 = line_storage[1].split("&")[1]
            secondary = line_storage[2].split(" ")[0]
            # to handle when the number is 3 digits instead of 4
            try:
                free_energy = line_storage[2].split(" ")[-1].split("(")[1].split(")")[0]
            except:
                free_energy = line_storage[2].split(" ")[-1].split(")")[0]
            try:
                part_funt = line_storage[3].split(" ")[-1].split("[")[1].split("]")[0]
            except:
                part_funt = line_storage[3].split(" ")[-1].split("]")[0]
            freq = line_storage[4].split(" ")[6].split(";")
            delta_g = line_storage[4].split(" ")[-1]
            # writing a new line the output file with all relevant info
            fh_out.write(
                species
                + ","
                + names
                + ","
                + sequence
                + ","
                + seq1
                + ","
                + seq2
                + ","
                + secondary
                + ","
                + free_energy
                + ","
                + part_funt
                + ","
                + freq
                + ","
                + delta_g
                + "\n"
            )
            # empyting list holding the entry's lines
            line_storage = []

fh_out.close
