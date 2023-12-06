
import pandas as pd
import sys
import os


def csv_to_json(csv_file_path, json_file_path):
    # Read the CSV file
    data = pd.read_csv(csv_file_path)

    # Remove columns with all empty values
    data = data.dropna(axis=1, how='all')

    # Remove rows with all empty values
    data = data.dropna(axis=0, how='all')

    # Replace remaining NaNs with an empty string
    data = data.fillna('')

    # Convert the DataFrame to standard JSON format (array of objects)
    data.to_json(json_file_path, orient='records')


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(
            "Usage: python csv-to-json.py <source_csv_path> [destination_json_path]")
        sys.exit(1)

    source_csv_path = sys.argv[1]

    if len(sys.argv) > 2:
        destination_json_path = sys.argv[2]
    else:
        # If destination is not provided, use the same directory as source, but with .json extension
        base_name = os.path.splitext(source_csv_path)[0]
        destination_json_path = base_name + '.json'

    csv_to_json(source_csv_path, destination_json_path)
