# nestedjson2sql

`nestedjson2sql` is a Python tool for converting JSON data into SQL tables. It dynamically detects column names for each table, handles nested JSON elements, and ensures no duplicates are inserted. This tool is particularly useful for dealing with JSON data that needs to be stored and queried in a relational database format.

## Installation

To install `nestedjson2sql`, run the following command:

```bash
pip install nestedjson2sql
```

## Usage

### Basic Usage

To convert a JSON file to SQL, run:

```bash
json2sql --file path/to/yourfile.json --db yourdatabase.db
```

This will process the JSON file and create corresponding tables in the specified SQLite database.

### Handling Multiple Files

`nestedjson2sql` can also process multiple JSON files at once:

```bash
json2sql --file file1.json file2.json file3.json --db yourdatabase.db
```

This will combine and process the JSON data from all specified files and store it in the SQLite database.

`nestedjson2sql` offers an additional command line argument --root to specify the name of the main table that will contain the non-nested elements of your JSON data.

#### Usage of --root:

You can specify the main table name using the --root parameter. If not specified, it defaults to `log`.

Example command:

```
json2sql --file path/to/yourfile.json --db yourdatabase.db --root main_table
```
In this example, the non-nested elements of the JSON file will be stored in a table named main_table in the specified SQLite database.

### File Types

The tool can handle two types of JSON files:

1. **Regular JSON File**: A file containing a single JSON object.
2. **Multi-line JSON File**: A file where each line is a valid JSON object.

### Examples

1. **Single JSON File**:

    If `data.json` contains a single JSON object, simply run:

    ```bash
    json2sql --file data.json --db database.db
    ```

2. **Multi-line JSON File**:

    `nestedjson2sql` will detect the multi-line json format. Simply run:

    ```bash
    json2sql --file multi_line_json.txt --db database.db
    ```

3. **Multiple Files**:

    To process multiple files, for example, `data1.json`, `multi_line_json.txt`, and `data3.json`, use:

    ```bash
    json2sql --file data1.json multi_line_json.txt data3.json --db database.db
    ```

4. **Map all nested elements to root level:**
    Add the `--pin_root` flag :
    ```bash
    json2sql --file data1.json multi_line_json.txt data3.json --db database.db --pin_root
    ```

## Contributions

Contributions to `nestedjson2sql` are welcome! Please feel free to submit pull requests or open issues to improve the tool or suggest new features.
