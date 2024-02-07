import argparse
import json

from nestedjson2sql.src.json_processor import JsonProcessor
from nestedjson2sql.src.sql_processor import SqlProcessor


def main():
    parser = argparse.ArgumentParser(description="Convert JSON to SQL.")
    parser.add_argument('--file', nargs='+', type=str,
                        required=True, help="Path to JSON file(s).")
    parser.add_argument('--db', type=str, default="nestedjson.db",
                        help="Database connection string.")
    parser.add_argument('--root', type=str, default="log",
                        help="Main table name containing the non-nested elements")
    parser.add_argument('--pin_root', action='store_true', default=False,
                        help="Map all nested children to the root level.")

    args = parser.parse_args()

    json_processor = JsonProcessor(args.file, args.root, args.pin_root)
    json_tables = json_processor.process()

    sql_processor = SqlProcessor(f"sqlite:///{args.db}")
    sql_processor.write_to_db(json_tables)


if __name__ == "__main__":
    main()
