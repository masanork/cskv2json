import json
import sys

def cskv_to_json(file_path):
    # Open the file and read lines
    with open(file_path, 'r') as file:
        lines = file.readlines()

    results = []

    for line in lines:
        # Split the line using comma as separator and strip spaces
        tokens = [token.strip() for token in line.split(',')]

        # Create a dictionary for each line
        record = {}
        for i in range(0, len(tokens), 2):  # Iterate two tokens at a time
            key, value = tokens[i], tokens[i + 1]
            # If the key already exists in the dictionary, append the value to its list
            if key in record:
                # If the existing value is not a list, make it a list
                if not isinstance(record[key], list):
                    record[key] = [record[key]]
                record[key].append(value)
            else:
                record[key] = value

        results.append(record)

    # Return the JSON representation of the results
    return json.dumps(results, indent=4)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: cskv2json.py <file_path>")
        sys.exit(1)

    file_path = sys.argv[1]
    print(cskv_to_json(file_path))
