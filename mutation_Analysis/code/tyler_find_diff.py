from __future__ import print_function

import argparse
import os
import subprocess
from collections import defaultdict

parser = argparse.ArgumentParser()
parser.add_argument("--fasta",
                    help="File with hairpin and mature sequences.", required=True)
parser.add_argument("--species",
                    help="Reference species.", required=True)

args = parser.parse_args()

def split(fasta):
    skip = 0
    out = fasta + "-hairpin.fas"
    with open(fasta) as inh, open(out, 'w') as outh:
        for line in inh:
            if line.startswith(">"):
                if line.strip().endswith("5p") or line.strip().endswith("3p"):
                    skip = 1
                else:
                    skip = 0
            if skip == 0:
                print(line.strip(), file=outh)
    return(out)

def read_mature(fasta):
    hairpin = defaultdict(dict)
    mature = defaultdict(dict)
    with open(fasta) as inh:
        for line in inh:
            if line.startswith(">"):
                sps=line.strip().split("-")[0][1:4]
                cache = line.strip()
                if line.strip().endswith("3p"):
                    mature[sps]["3p"] = ""
                elif line.strip().endswith("5p"):
                    mature[sps]["5p"] = ""
                else:
                    hairpin[sps] = ""
            else:
                align=line.strip()
                if cache.endswith("3p"):
                    mature[sps]["3p"] += line.strip()
                elif cache.endswith("5p"):
                    mature[sps]["5p"] += line.strip()
                else:
                    hairpin[sps]+=align
    matures = defaultdict(dict)
    for sps in hairpin:
        start3p = hairpin[sps].find(mature[sps]["3p"])
        start5p = hairpin[sps].find(mature[sps]["5p"])
        matures[sps]["3p"] = [start3p, start3p + len(mature[sps]["3p"])]
        matures[sps]["5p"] = [start5p, start5p + len(mature[sps]["5p"])]
    return(matures)

def run_mafft(fasta):
    out = structure = 0
    log = fasta + ".log"
    out = fasta + ".txt"
    cmd = ("mafft {fasta} > {out} 2>{log}").format(**locals())
    # subprocess.check_call(cmd.split(" "))
    p = subprocess.Popen(cmd, shell=True)
    p.wait()
    return {"out": out, "log": log}

def read_alignments(fasta):
    res = defaultdict()
    with open(fasta) as inh:
        for line in inh:
            if line.startswith(">"):
                sps=line.strip().split("-")[0][1:4]
                res[sps] = ""
            else:
                align=line.strip()
                res[sps]+=align
    return(res)

def fix(reference, matures):
    shift = reference[0:matures["5p"][0]].count("-")
    mature5p = [matures["5p"][0] + shift, matures["5p"][1] + shift]
    shift = reference[0:matures["3p"][0]].count("-")
    mature3p = [matures["3p"][0] + shift, matures["3p"][1] + shift]
    return(mature5p, mature3p)

def analyze(data, matures, species, outfile):
    backup_species = ['gac','cgo','bdi','emc','ggi','nco','cgu','cac']
    if species in data:
        species = species
    else:
        for i in backup_species: 
            if i in data:
                species = i     
                break
    if species not in data:
        raise ValueError("%s is not in the output" % species)
    reference = data[species]
    ref5p, ref3p = fix(reference, matures[species])
    data.pop(species, None)
    ouh = open(outfile, 'w')
    for i,nt in enumerate(reference):
        print("nt,%s,%s,NA,%s" % (species, i, nt), file=ouh)
    print("5p-pos,%s,%s,%s,NA" % (species, ref5p[0], ref5p[1]), file=ouh)
    print("3p-pos,%s,%s,%s,NA" % (species, ref3p[0], ref3p[1]), file=ouh)
    for sps in data:
        # detect changes along the precursor
        for i,nt in enumerate(reference):
            if nt != data[sps][i]:
                print("nt-change,%s,%s,NA,%s" % (sps, i, data[sps][i]), file=ouh)
        # detect changes in mature positions
        m5p, m3p = fix(data[sps], matures[sps])
        print("5p-pos,%s,%s,%s,NA" % (sps, m5p[0], m5p[1]), file=ouh)
        print("3p-pos,%s,%s,%s,NA" % (sps, m3p[0], m3p[1]), file=ouh)

        if m5p[0] != ref5p[0]:
            print("5p-start,%s,%s,NA,NA" % (sps, m5p[0]), file=ouh)
        if m5p[1] != ref5p[1]:
            print("5p-end,%s,%s,NA,NA" % (sps, m5p[1]), file=ouh)
        if m3p[0] != ref3p[0]:
            print("3p-start,%s,%s,NA,NA" % (sps, m3p[0]), file=ouh)
        if m3p[1] != ref3p[1]:
            print("3p-end,%s,%s,NA,NA" % (sps, m3p[1]), file=ouh)
    ouh.close()
matures_positions = read_mature(args.fasta)
hairpins = split(args.fasta)
outputs = run_mafft(hairpins)
alignment = read_alignments(outputs['out'])
out_summary =  args.fasta + ".summary.txt"
analyze(alignment, matures_positions, args.species, out_summary)
cmd = ("Rscript code/plot.r {out_summary} ").format(**locals())
p = subprocess.Popen(cmd, shell=True)
p.wait()