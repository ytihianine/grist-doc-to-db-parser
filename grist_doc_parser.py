from enum import Enum

import pandas as pd


class GristType(Enum):
    TEXT = "Text"
    BLOB = "Blob"
    ANY = "Any"
    BOOL = "Bool"
    INT = "Int"
    NUMERIC = "Numeric"
    DATE = "Date"
    DATETIME = "DateTime"
    CHOICE = "Choice"
    CHOICELIST = "ChoiceList"
    REFERENCE = "Ref"
    REFERENCELIST = "RefList"
    ATTACHMENTS = "Attachments"


class DBMLType(Enum):
    UNDEFINED = "grist_any"
    TEXT = "text"
    TEXTLIST = "text[]"
    DATE = "date"
    DATETIME = "datetime"
    BINARY = "binary"
    INTEGER = "int"
    INTEGERLIST = "int[]"
    NUMERIC = "numeric"
    BOOL = "boolean"
    FILE = "file"


TYPE_CONVERT = {
    GristType.TEXT.value: DBMLType.TEXT.value,
    GristType.BLOB.value: DBMLType.BINARY.value,
    GristType.ANY.value: DBMLType.UNDEFINED.value,
    GristType.BOOL.value: DBMLType.BOOL.value,
    GristType.INT.value: DBMLType.INTEGER.value,
    GristType.NUMERIC.value: DBMLType.NUMERIC.value,
    GristType.DATE.value: DBMLType.DATE.value,
    GristType.DATETIME.value: DBMLType.DATETIME.value,
    GristType.CHOICE.value: DBMLType.TEXT.value,
    GristType.CHOICELIST.value: DBMLType.TEXTLIST.value,
    GristType.REFERENCE.value: DBMLType.INTEGER.value,
    GristType.REFERENCELIST.value: DBMLType.INTEGERLIST.value,
    GristType.ATTACHMENTS.value: DBMLType.FILE.value,
}


# Not necessary to have the full column name
GRIST_ADDITIONAL_TBL = ["summary"]
GRIST_INTERNAL_COLUMS = ["manual", "grist", "summary", "count", "group", "GristDocTour"]


def remove_grist_tbl(df: pd.DataFrame, column: str) -> pd.DataFrame:
    df_filtered = df.loc[df[column].str.contains(pat="|".join(GRIST_ADDITIONAL_TBL), na=False)]
    df = df.drop(index=df_filtered.index)
    return df


def remove_grist_col(df: pd.DataFrame, column: str) -> pd.DataFrame:
    df_filtered = df.loc[df[column].str.contains(pat="|".join(GRIST_INTERNAL_COLUMS), na=False)]
    df = df.drop(index=df_filtered.index)
    return df


def process_type_col(df: pd.DataFrame) -> pd.DataFrame:
    # Séparer les types et le nom des tables références
    df["type_processed"] = df.loc[:, "type"].str.split(":")
    df["type_grist"] = df.loc[:, "type_processed"].str.get(0)
    df["type_grist_tbl_name"] = df.loc[:, "type_processed"].str.get(1)
    return df


def convert_grist_type(df: pd.DataFrame, column: str = "type_grist") -> pd.DataFrame:
    df["type_dbml"] = df.loc[:, column].map(TYPE_CONVERT)
    return df


def process_tbl_info(df: pd.DataFrame) -> pd.DataFrame:
    cols_to_keep = ["id", "tableId"]
    df = df.loc[:, cols_to_keep].copy()
    df = remove_grist_tbl(df=df, column="tableId")
    return df


def process_col_info(df: pd.DataFrame) -> pd.DataFrame:
    cols_to_keep = ["id", "parentId", "colId", "type", "description"]
    df = df.loc[:, cols_to_keep].copy()
    df = remove_grist_col(df=df, column="colId")
    df = process_type_col(df=df)
    df = convert_grist_type(df=df)
    return df


def process_dbml(df_tbl: pd.DataFrame, df_col: pd.DataFrame) -> pd.DataFrame:
    df = pd.merge(
        left=df_tbl,
        right=df_col,
        left_on="id",
        right_on="parentId"
    )
    df = df.drop(columns=["id_x", "id_y"])
    df = df.sort_values(by="parentId")

    return df


def generate_dbml_file(output_path: str, df: pd.DataFrame) -> None:
    tbl_names = df.loc[:, "tableId"].unique()
    dbml = {}
    for tbl in tbl_names:
        dbml[tbl] = []
        dbml[tbl].append(f"Table {tbl}")
        dbml[tbl].append("\n{\n\tid integer [primary key]")

    for row in df.itertuples():
        if row.type_grist in [GristType.REFERENCE.value, GristType.REFERENCELIST.value]: # type: ignore
            dbml[row.tableId].append(f"\n\t{row.colId} {row.type_dbml} [ref: > {row.type_grist_tbl_name}.id]")  # type: ignore
        else:
            dbml[row.tableId].append(f"\n\t{row.colId} {row.type_dbml}")  # type: ignore

    with open(file=output_path, mode="w") as dbml_file:
        for key, values in dbml.items():
            dbml_file.write("".join(values))
            dbml_file.write("\n}\n\n")


def export_to_csv(path: str, df: pd.DataFrame, sep: str = ";") -> None:
    df.to_csv(path_or_buf=path, sep=sep)
