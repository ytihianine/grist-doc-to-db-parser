import sqlite3
import pandas as pd

from grist_doc_parser import (
    export_to_csv, process_tbl_info, process_col_info, process_dbml, generate_dbml_file
)

# Grist table names which contains our informations
GRIST_TBL_INFO = "_grist_Tables"
GRIST_COL_INFO = "_grist_Tables_column"

if __name__ == "__main__":
    # Set those values
    grist_doc_path = ""
    dbml_output_path = ""
    export = False
    csv_output_path = ""

    # Start
    db_conn = sqlite3.connect(grist_doc_path)

    # Process table information
    print("Processing table information")
    df_tbl = pd.read_sql(f"SELECT * FROM {GRIST_TBL_INFO}", con=db_conn)
    print("Nb lignes avant processing: ", len(df_tbl))
    df_tbl = process_tbl_info(df=df_tbl, lower_tbl_name=True)
    print("Nb lignes après processing: ", len(df_tbl))

    # Process columns information
    print("Processing columns information")
    df_cols = pd.read_sql(f"SELECT * FROM {GRIST_COL_INFO}", con=db_conn)
    print("Nb lignes avant processing: ", len(df_cols))
    df_cols = process_col_info(df=df_cols, lower_col_name=True)
    print("Nb lignes après processing: ", len(df_cols))

    # Prepare last df before formating
    print("Generating DBML file")
    df_dbml = process_dbml(df_tbl=df_tbl, df_col=df_cols)
    print(df_dbml.head())

    # (Optional) Export dataframe to csv format
    if export:
        export_to_csv(path=csv_output_path, df=df_dbml)

    # Export to dbml format
    generate_dbml_file(output_path=dbml_output_path, df=df_dbml)
