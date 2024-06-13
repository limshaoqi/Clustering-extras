import argparse
import os

def convert_clusters(input_file):
    with open(input_file, 'r') as infile:
        lines = infile.readlines()
    
    output_lines = []
    current_cluster = None
    
    for line in lines:
        line = line.strip()
        if line.startswith("CLUSTER"):
            current_cluster = int(line.split()[1]) + 1  # Convert to 1-based indexing
        elif line:  # Ensure the line is not empty
            sequence = line.replace(" ", "")  # Remove any spaces in the sequence
            if current_cluster is not None:  # Ensure there is a valid current cluster
                output_lines.append(f"{current_cluster} {sequence}\n")
            else:
                print(f"Warning: Sequence found without a cluster: {line}")

    output_file = os.path.join(os.getcwd(), 'converted_output.txt')
    with open(output_file, 'w') as outfile:
        outfile.writelines(output_lines)
    
    print(f"Output written to {output_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Convert cluster format')
    parser.add_argument('-i', '--input', required=True, help='Path to the input file')
    args = parser.parse_args()
    
    convert_clusters(args.input)
