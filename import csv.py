import csv
import json
import math

def extract_columns_to_json(input_file, output_file):
    """
    Extracts the second and third columns from a TSV file and writes them to a JSON file as a dictionary.

    Parameters:
    input_file (str): The path to the input TSV file.
    output_file (str): The path to the output JSON file where the extracted columns will be saved.
    """
    data = {}
    
    with open(input_file, mode='r', newline='', encoding='utf-8') as infile:
        reader = csv.reader(infile, delimiter='\t')
        
        for index, row in enumerate(reader):
            # Ensure the row has enough columns
            if len(row) >= 3:
                # Extract the second and third columns (index 1 and 2)
                try:
                    data[row[1]] = int(row[2])
                except ValueError:
                    print("Error extracting: "+index)
    sorted_data = dict(sorted(data.items()))
    
    # Write the dictionary to a JSON file
    with open(output_file, mode='w', encoding='utf-8') as outfile:
        json.dump(sorted_data, outfile, ensure_ascii=False, indent=4)

# Example usage
input_file_path = 'syn2015_lemma_utf8.tsv'
output_file_path = 'output.json'
extract_columns_to_json(input_file_path, output_file_path)
