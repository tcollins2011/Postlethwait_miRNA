#!/usr/bin/env python

import argparse
#Using Argeparse to get the input file
def get_args():
    parser = argparse.ArgumentParser(
        description="Size Selects reads from a fasta file")
    parser.add_argument("-f", "--file", help="filename", required=True)
    parser.add_argument("--min", help="minimum read length (inclusive)", required=True)
    parser.add_argument("--max", help="maximum read length (inclusive)", required=True)
    return parser.parse_args()

args = get_args()

#setting up variable to name files and directories correctly based on input
if "/" in args.file:
    filename = args.file.split("/")[-1]
    path = "/".join(args.file.split("/")[0:-2]) + "/Size_Select_" + args.file.split("/")[-2]
else:
    filename = args.file
    path = ""

#writing to a file with "size_select_" added to the front
out_fh = open(f"{path}/size_select_{filename}", "w")

#looping through the file
with open(args.file) as fh:
    for line in fh:
        line = line.strip()
        #saving header lines
        if line.startswith(">"):
            header = line
            continue
        #if sequence is between the min and max (inclusive) then header and sequence line are written to output
        elif len(line) >= int(args.min) and len(line) <= int(args.max):
            out_fh.write(header + "\n")
            out_fh.write(line + "\n")

out_fh.close()
            