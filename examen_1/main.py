import pandas as pd
import sqlite3
from typing import Union, List
from pathlib import Path
import os

path = Path(os.getcwd())

database = "sqlite.db"
conn = sqlite3.connect(database)

def creates_tables()->None:
    """
    Esta función crea a las tablas de la base de datos,
    leyendo el archivo create_tables.sql
    """
    cur = conn.cursor()
    with open("create_tables.sql", encoding="utf-8") as file:
        cur.executescript(file.read())

def saves_values(file_path:str, conn)->Union[pd.DataFrame,str]:
    """Esta función guarda los valores en la base de datos,
    aunque ya pandas, crea la base de datos por default.
    Para mi es mejor crearla con sql para  seguir con las relaciones

    Args:
        file_path (str): path del directorio donde está el archivo
        conn : Conección de sqlite

    Returns:
        Union[pd.DataFrame,str]: dataframe de la tabla a guarda y el nombre de esté
    """

    file_name = file_path.name.split(".")[0]
    df = pd.read_csv(file_path)
    row = df.to_sql(file_name.capitalize(), conn, index=False, if_exists = "append")
    print(f"Save in {file_name}, total row {row}")
    return df, file_name

def creates_table_master(user:pd.DataFrame, trx:pd.DataFrame, alert:pd.DataFrame, conn):
    merge_trx_user = user.merge(trx,how="outer")
    merge_trx_user["is_claim"] = merge_trx_user.id_trx.isin(alert.id_trx)
    values_save = merge_trx_user[
        [
            "id_trx", 
            "first_name", 
            "last_name",
            "email",
            "gender",
            "Town",
            "is_claim"]
        ]
    values_save.to_sql("Master", conn, if_exists = "append")
    values_save.to_excel("Master.xlsx")
    print("The table Master are create and save")
    
        
def gets_csv(path: Path)->List[Path]:
    """
    Está función obtiene los archivos de la carpeta 
    data (Donde se encuentran todos los datos) los lista y están listo para guardarse

    Args:
        path (Path): Pathlib del directorio del proyecto

    Returns:
        List[Path]: Lista de todos los directorios, en este caso de los csv
    """
    path_csv = path/"data"
    csv_files = os.listdir(path_csv)
    absolute_csv_files = list(map(lambda x: path_csv/x, csv_files))
    return absolute_csv_files
    



# Solo se ejecuta desde la consola, llamando el archivo
if __name__ == "__main__":

    if not (path/database).exists():
        # las bases de datos se crean, si no está el archivo sqlite creado
        creates_tables()
    
    # Caso contrario, se sobre escribiran los datos en las tables
    path_csv = gets_csv(path)
    dict_df = {}
    # pasamos todos los archivos por la función save values
    for csv_file in path_csv:
        df, name_csv = saves_values(csv_file, conn)
        dict_df[name_csv] = df
    creates_table_master(dict_df["Users"], dict_df["Trx"], dict_df["Alerts"], conn)
    