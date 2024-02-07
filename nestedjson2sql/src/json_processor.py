from json_relational import JsonRelational
import json
import pandas as pd


def flatten_json_to_string(json_obj):
    return json.dumps(json_obj)


class JsonProcessor:
    def __init__(self, file_paths, root_name, pin_root):
        self.file_paths = file_paths
        self.jr = JsonRelational(root_name=root_name, pin_root=pin_root)

    def process(self):
        combined_lines = []
        for file_path in self.file_paths:
            with open(file_path, 'r') as file:
                try:
                    json_obj = json.load(file)
                    combined_lines.append(flatten_json_to_string(json_obj))
                except json.JSONDecodeError:
                    file.seek(0)  # Reset file pointer to the beginning
                    combined_lines.extend(file.readlines())

        return self.jr.flatten_lines('\n'.join(combined_lines))

    def write_to_db(self, engine, dataframes):
        for table_name, df in dataframes.items():
            df = df.astype(str)
            try:
                df.to_sql(table_name, engine, if_exists='replace', index=False)
            except Exception as e:
                print(f"Error writing table {table_name}: {e}")
