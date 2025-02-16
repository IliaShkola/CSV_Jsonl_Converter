import csv
import json

# Define the input and output file paths
input_csv_file = "modeleducation_small_read.csv"
output_jsonl_file = "fine_tune_data_small_read.jsonl"

# System message to include in every entry
system_message = {
    "role": "system",
    "content": (
        "You are a professional Revit Python coder specializing in Dynamo Python nodes. When receiving a user request for "
        "implementing an action or functionality in Revit using Dynamo Python, you will provide only the Python code as your response. "
        "The provided code must:\n\n"
        "- Include all necessary dependencies, libraries, and imports specific to Revit and Dynamo.\n"
        "- Be compatible with the Revit API and Dynamo's Python scripting environment.\n"
        "- Include comments to explain key steps in the code for clarity and usability.\n"
        "- Be optimized for performance and reliability within the Revit environment.\n"
        "- Assume the script will run in a Python node within Dynamo and ensure compatibility with Dynamo's data structure "
        "(e.g., handling lists or nested lists).\n"
        "- Avoid including any unnecessary explanations or contextual information outside the code. Provide clean, ready-to-use code tailored to the request."
    )
}

# Open the CSV file and JSONL file
with open(input_csv_file, mode='r', encoding='utf-8') as csv_file, open(output_jsonl_file, mode='w', encoding='utf-8') as jsonl_file:
    # Create a CSV reader
    csv_reader = csv.DictReader(csv_file)
    
    # Process each row in the CSV file
    for row in csv_reader:
        # Construct the JSONL structure
        jsonl_entry = {
            "messages": [
                system_message,
                {"role": "user", "content": row["Prompt"]},
                {"role": "assistant", "content": row["Answer"]}
            ]
        }
        # Write the JSONL entry to the output file
        jsonl_file.write(json.dumps(jsonl_entry) + '\n')

print(f"Converted {input_csv_file} to {output_jsonl_file} with the specified structure successfully!")
