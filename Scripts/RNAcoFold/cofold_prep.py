#!/usr/bin/env python
import argparse


def get_args():
    parser = argparse.ArgumentParser(
        description="Takes a csv and coverts it to a fasta file in the format needed for RNACoFold"
    )
    parser.add_argument(
        "-f",
        "--file",
        help="csv file with duplex sequences on the same line",
        required=True,
    ),
    parser.add_argument("-o", "--output", help="name for output fasta", required=True)
    return parser.parse_args()


args = get_args()

fh_out = open(args.output, "w")

first = True
with open(args.file) as fh:
    for line in fh:
        if first == True:
            first = False
            continue
        line = line.strip()
        line_list = line.split(",")
        fh_out.write(">" + line_list[0] + "+" + line_list[2] + "\n")
        fh_out.write(line_list[1] + "$" + line_list[3] + "\n")

fh_out.close()
