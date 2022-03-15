import argparse
import os
import csv
import pprint
from datetime import datetime 

#  global variables
f = []
target_files = []

# Get command Line Arguments
def get_args():
    parser = argparse.ArgumentParser(
        description = 'Takes find_diff output and recombines it to a csv file'
    )
    parser.add_argument(
        "-f",
        help="Output from find_diff.", 
        required=True,
        ),
    parser.add_argument(
        "-o",
        "--output",
        help="output file name",
        default = datetime.now(),
    ),
    return parser.parse_args()

# Function that looks through target directroy and gets all of the txt files that we need to loop though 
def find_summary_files(directory):
    for item in os.listdir(directory):
        if not item.endswith('.csv'):
            f.append( os.path.join(directory,item))
    for entry in f:
        path = os.listdir(entry)
        for file in path:
            if file.endswith('.summary.txt'):
                target_files.append(os.path.join(entry,file))
    return

# Determines which region a change happened 
def determine_region(p5,p3,position):
    if position < min(p5):
        return 'head'
    elif position in p5:
        if position > min(p5) + 1 and position < min(p5) + 9:
            return '5p-seed'
        else:
            return '5p'
    elif position > max(p5) and position < min(p3): 
        return 'loop'
    elif position in p3:
        if position > min(p3) + 1 and position < min(p3) + 9:
            return '3p-seed'
        else:
            return '3p'
    else:
        return 'tail'
    
# Messy function where the error most likely is
def get_data(file,dictionary):
    with open(file, 'r', encoding='utf-8') as f:
        gene = os.path.basename(file).split('.')[0]
        total_counter_set = set()
        nt_changes = {}
        reference_positions = {}
        for line in f:
            x = line.strip().split(',')
            species = x[1]
            if species not in dictionary.keys():
                dictionary[species]={'changes':{},'total_count':0}
            if species not in nt_changes.keys():
                nt_changes[species]=[]
            if species not in reference_positions.keys():
                reference_positions[species]=[]
           
            total_counter_set.add(species)

            if x[0] == 'nt-change':
                nt_changes[species].append((x[2],x[4]))
            
            elif x[0] == '3p-pos' or x[0] == '5p-pos':
                reference_positions[species].append((x[0],x[2],x[3]))
    
        
    for key, value in nt_changes.items():
 
        p5_low = int(reference_positions[key][0][1])
        p5_high = int(reference_positions[key][0][2])
        p3_low = int(reference_positions[key][1][1])
        p3_high = int(reference_positions[key][1][2])
        p5 = range(p5_low,p5_high)
        p3 = range(p3_low,p3_high)
        species = key
        for item in value:
            position,nucleotide = item
        
            region = determine_region(p5,p3,int(position))
            tuple_key = (position,region,nucleotide)
            dictionary[species]['changes'][tuple_key] = gene
            
    
    for species in total_counter_set:
        dictionary[species]['total_count'] += 1
            
    return dictionary


# Main function 
if __name__=='__main__':
    args = get_args()
    find_summary_files(args.f)
    temp = {}


    # dictionary format temp = {species:{ 'total_count': 0 , changes:[(change,location,region)]}}
    for file in target_files:
        temp = get_data(file,temp)


    # Create CSV output
    with open (args.output +'.csv', 'w') as f:
        csv_writer = csv.writer(f, delimiter=',')
        headers = ['Species','Location','Feature','Nucleotide_Change','Gene_ID','Total']
        csv_writer.writerow(headers)

        for key in temp:
            # construct list [speices, location, feature, nucleotide, gene_Id, total]
            species = key
            for item in temp[key]['changes']:
                position = item[0]
                region = item[1]
                nucleotide = item[2]
                gene_id = temp[key]['changes'][item]
                total_count = temp[key]['total_count']
                line = [species, position, region, nucleotide, gene_id, total_count]
                csv_writer.writerow(line)
                
            
    