from sqlalchemy import create_engine
import pandas as pd


class SqlProcessor:
    def __init__(self, connection_string):
        self.engine = create_engine(connection_string)

    def write_to_db(self, json_tables):
        dataframes = {table_name: pd.DataFrame(
            rows) for table_name, rows in json_tables.items()}

        for table_name, df in dataframes.items():
            df = df.astype(str)
            try:
                df.to_sql(table_name, self.engine,
                          if_exists='replace', index=False)
            except Exception as e:
                print(f"Error writing table {table_name}: {e}")
