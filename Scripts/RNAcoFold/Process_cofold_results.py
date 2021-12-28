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

fh_out = open(args.output, "w")

with open(args.file) as fh:
    fh_out.write(
        "Species,miRNA names,Duplex Sequences,Free Energy(kcal/mol),Partition Function,Frequency of mfe Structure in Ensemble,Delta G Binding(kcal/mol)\n"
    )
    counter = 0
    line_storage = []
    for line in fh:
        counter += 1
        line_storage.append(line.strip())
        if counter % 5 == 0:
            species = line_storage[0].split(">")[1].split("-")[0]
            names = line_storage[0]
            sequence = line_storage[1]
            try:
                free_energy = line_storage[2].split(" ")[-1].split("(")[1].split(")")[0]
            except:
                free_energy = line_storage[2].split(" ")[-1].split(")")[0]
            try:
                part_funt = line_storage[3].split(" ")[-1].split("[")[1].split("]")[0]
            except:
                part_funt = line_storage[3].split(" ")[-1].split("]")[0]
            freq = line_storage[4].split(" ")[6]
            delta_g = line_storage[4].split(" ")[-1]
            fh_out.write(
                species
                + ","
                + names
                + ","
                + sequence
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
            line_storage = []

fh_out.close
