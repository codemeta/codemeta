import csv
import sys
import os

from sssom.parsers import parse_sssom_table
from sssom.writers import write_owl

header = ["subject_id","subject_label","predicate_id","object_id","object_label","match_type","subject_source","object_source","confidence"]

def convert_csv_to_tsv(input_metadata_file, input_file, output_file, ttl_file):
    
    input_metadata_f = open(input_metadata_file, mode='r', newline='', encoding='utf-8')
    reader_metadata = csv.reader(input_metadata_f)
    #Skip the first line
    next(reader_metadata)
    
    # Open the input CSV file for reading
    input_f = open(input_file, mode='r', newline='', encoding='utf-8')
    #reader = csv.reader(input_f)
    reader = csv.DictReader(input_f)


    
    # Open the output TSV file for writing
    output_f = open(output_file, mode='w', newline='', encoding='utf-8')

    for row in reader_metadata:
        # Join the row with tabs and comment it
        commented_row = '# ' + '\t'.join(row) + '\n'
        output_f.write(commented_row)
    #writer.writerows(commented_lines)
    writer = csv.writer(output_f, delimiter='\t')
    writer.writerow(header)
    
    #Write each row from CSV to TSV
    for row in reader:
        if (row["type_relation"]=="exact_match"):
            predicate_id = "skos:exactMatch"
        elif (row["type_relation"]=="part_of"):
            predicate_id = "skos:closeMatch"
        elif (row["type_relation"]=="more_specific_than"):
            predicate_id = "skos:narrower"
        elif (row["type_relation"]=="more_generic_than"):
            predicate_id = "skos:broader"
        row = ["codemeta:"+row["source_term"],row["source_term"],predicate_id,"target:"+row["target_term"],row["target_term"],"SSSOM:HumanCurated","schema","target",1]
        writer.writerow(row)
    
    # Close the files
    input_f.close()
    input_metadata_f.close()
    output_f.close()

    msdf = parse_sssom_table(output_tsv_file)
    
    with open(ttl_file,"w") as f:
        write_owl(msdf, f)

# Example usage
if len(sys.argv) != 3:
    print("Error: This script requires exactly two arguments.")
    print("Usage: python script.py <metadata_file.yml> <input_file.csv>")
    sys.exit(1)  # Exit with an error code
output_tsv_file = os.path.splitext(sys.argv[2])[0]+".sssom.tsv"
output_ttl_file = os.path.splitext(sys.argv[2])[0]+".sssom.ttl"
convert_csv_to_tsv(sys.argv[1], sys.argv[2], output_tsv_file, output_ttl_file)