#!/usr/bin/env python
import argparse


def get_args():
    parser = argparse.ArgumentParser(description="***FIX**")
    parser.add_argument(
        "-f",
        "--file",
        help="***FIX***",
        required=True,
    ),
    # parser.add_argument("-o", "--output", help="***FIX***", required=True)
    return parser.parse_args()


args = get_args()

# openning output files
# fh_out = open(args.output, "w")
filename = args.file.split(".")[0]
fh_out = open(f"{filename}_w_gc.csv", "w")

# (I think) I only want to count paired GC's one to avoid double counting them
paired_list = ["G(", "C(", "G)", "C)"]
unpaired_list = ["G.", "C."]


# using this variable to skip the first line (since it's column titles)
first = True
# reading through input file
with open(args.file) as fh:
    for line in fh:
        # skipping the first line
        if first == True:
            line = line.strip()
            fh_out.write(
                line
                + ","
                + "GC Content (Percent of Sequence)"
                + ","
                + "Paired GC Content (Percent of Sequence)"
                + ","
                + "Unpaired GC Content (Percent of Sequence)"
                + ","
                + "Paired GCs (Percent of GC Content)"
                + ","
                + "Unpaired GCs (Percent of GC Content)"
                + "\n"
            )
            first = False
            continue
        line = line.strip()
        line_list = line.split(",")
        # grabbing sequence and secondary structure
        Sequences = line_list[1].upper()
        Sec_structure = line_list[2]
        # counting G's and C's
        G = Sequences.count("G")
        C = Sequences.count("C")
        Total_GC = ((G + C) / (len(Sequences) - 1)) * 100
        Paired_GC_count = 0
        Unpaired_GC_count = 0
        for i in range(len(Sequences)):
            if (Sequences[i] + Sec_structure[i]) in paired_list:
                Paired_GC_count += 1
            if (Sequences[i] + Sec_structure[i]) in unpaired_list:
                Unpaired_GC_count += 1
            continue
        Paired_GC = (Paired_GC_count / (len(Sequences) - 1)) * 100
        Unpaired_GC = (Unpaired_GC_count / (len(Sequences) - 1)) * 100
        Paired_GC_portion = Paired_GC_count / (G + C) * 100
        Unpaired_GC_portion = Unpaired_GC_count / (G + C) * 100
        fh_out.write(
            ",".join(line_list)
            + ","
            + str(Total_GC)
            + ","
            + str(Paired_GC)
            + ","
            + str(Unpaired_GC)
            + ","
            + str(Paired_GC_portion)
            + ","
            + str(Unpaired_GC_portion)
            + "\n"
        )

fh_out.close()
