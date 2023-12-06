# Convert CSV to JSON

## Project Overview

This project provides a Python script (`csv-to-json.py`) that converts CSV files to JSON format. It is particularly useful for processing large datasets and handling missing values by leaving corresponding JSON values blank.

## CSV File Requirements

- The script assumes the first row of the CSV file contains column headers, which are used as keys in the JSON objects.
- Each subsequent row in the CSV file is converted into a JSON object.
- The script removes any columns and rows that are completely empty.
- It is designed to work with standard CSV files that have a clear header row and consistent columns.

Example JSON output:

```
[
  {"Rank":1.0, "Authors":"Jon Doe", ... },
  {"Rank":2.0, "Authors":"Jane Doe", ... },
  {"Rank":3.0, "Authors":"George Orwell", ... },
  {"Rank":4.0, "Authors":"Julia Donaldson", ... }
]
```

## Requirements

- Python 3.x
- Pandas library

## Installation

### Clone the Repository

First, clone the repository to your local machine:

```
git clone https://github.com/your-username/convert-csv-to-json.git
```

### Installing Python

Ensure you have Python 3 installed. If not, download and install it from the [Python official website](https://www.python.org/downloads/).

### Setting Up a Virtual Environment (Optional)

It's recommended to create a virtual environment for your Python projects. Here's how you can do it:

#### For macOS/Linux:

```
python3 -m venv myenv
source myenv/bin/activate
```

#### For Windows:

```
python -m venv myenv
myenv\Scripts\activate
```

### Installing Dependencies

With your virtual environment activated, install the required packages using:

```
pip install -r requirements.txt
```

## How to Run the Project

Run the script with the following command:

```
python csv-to-json.py <source_csv_path> [destination_json_path]
```

- `<source_csv_path>`: The path to the source CSV file.
- `[destination_json_path]`: Optional. The path where the JSON file will be saved. If not specified, the JSON file will be saved in the same directory as the source file, with the same base name.

### Example Usage

1. Specifying both source and destination:

   ```
   python csv-to-json.py path/to/source.csv path/to/destination.json
   ```

2. Specifying only the source (the JSON file will be saved in the same location as the CSV file):
   ```
   python csv-to-json.py path/to/source.csv
   ```

## License

This project is open-sourced under the [MIT license](https://opensource.org/licenses/MIT).
