import os

def convert_to_desired_format(encoded_file, underlying_file):
    output_file = 'GradHC_format.txt'
    
    with open(encoded_file, 'r') as ef:
        original_strands = ef.readlines()
    
    with open(underlying_file, 'r') as uf:
        lines = uf.readlines()
    
    with open(output_file, 'w') as of:
        cluster_data = {}
        current_cluster = None
        
        for line in lines:
            if line.startswith("CLUSTER"):
                current_cluster = line.strip()
                cluster_data[current_cluster] = set()  # Use a set to avoid duplicates
            elif line.strip():
                cluster_data[current_cluster].add(line.strip())  # Add to the set
        
        for i, original_strand in enumerate(original_strands):
            original_strand = original_strand.strip()
            cluster_key = f"CLUSTER {i}"
            of.write(original_strand + '\n')
            of.write('*****************************\n')
            if cluster_key in cluster_data:
                for erroneous_copy in cluster_data[cluster_key]:
                    of.write(erroneous_copy + '\n')
            of.write('\n\n')

    print(f"Output written to {output_file}")

# Define paths to the input files
encoded_file_path = '/home/shaoqi/DNAStorageToolkit/data/output/cat_naive/EncodedStrands.txt'
underlying_file_path = '/home/shaoqi/DNAStorageToolkit/3-clustering/input/UnderlyingClusters.txt'

# Convert the files
convert_to_desired_format(encoded_file_path, underlying_file_path)
