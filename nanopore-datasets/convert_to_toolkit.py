def convert_clusters_to_format(input_file, output_file):
    """
    Convert a clusters.txt file to the desired format.
    
    :param input_file: Path to the input clusters.txt file.
    :param output_file: Path to the output file.
    """
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        cluster_index = 0
        for line in infile:
            if line.startswith('='):
                outfile.write(f"CLUSTER {cluster_index}\n")
                cluster_index += 1
            else:
                outfile.write(line)

    print(f"Conversion complete. Output written to {output_file}")

# Define the path to the input and output files
input_file_path = 'Clusters.txt'
output_file_path = 'output.txt'

# Convert the clusters file
convert_clusters_to_format(input_file_path, output_file_path)
