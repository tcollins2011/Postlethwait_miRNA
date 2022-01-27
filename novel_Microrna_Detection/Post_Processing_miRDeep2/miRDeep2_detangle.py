import argparse


def get_args():
    parser = argparse.ArgumentParser(
        description="Extract Micro RNAs with a score above 10"
    )
    parser.add_argument("-f", "--file", help="input file name", required=True)
    parser.add_argument("-p", "--prefix", help="prefix for fasta header", required=True)
    parser.add_argument("-o", "--output", help='output file name', required=True)
    return parser.parse_args()


args = get_args()

fh_out = open(f"{args.output}", "a")
active = False
with open(args.file) as fh:
    for line in fh:
        line = line.strip()
        if "novel miRNAs predicted by miRDeep2" in line:
            active = True
            continue
        elif "mature miRBase miRNAs detected by miRDeep2" in line:
            break
        elif active == True:
            try:
                line = line.split("\t")
                score = float(line[1])
                if score >= 10:
                    fasta_header = ">" + args.prefix + "_" + line[0]
                    fh_out.write(fasta_header + "\n")
                    fh_out.write(line[15] + "\n")

            except:
                continue

fh_out.close()
