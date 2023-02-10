from database_manipulation.manipular_db import consultar_db
from database_manipulation.crud_cohetes import get_id_cohete

def crear_capacidad_en_db(capacidad:int,id_cohete:int,tipo_cohete:str)->None:
    if tipo_cohete=='lanzadera':
        sql_query=f"INSERT INTO capacidades_cargas VALUES({id_cohete},{capacidad})"
    elif tipo_cohete=='robotico':
        sql_query=f"INSERT INTO capacidades_cientificas VALUES({id_cohete},{capacidad})"
    elif tipo_cohete=='tripulado':
        sql_query=f"INSERT INTO capacidades_tripulantes VALUES({id_cohete},{capacidad})"
    consultar_db('insert',sql_query)

def actualizar_capacidad_en_db(capacidad:int,cohete:object,tipo_cohete:str)->None:
    id_cohete=get_id_cohete(cohete)
    sql_query=''
    if tipo_cohete=='lanzadera':
        sql_query=f"UPDATE capacidades_cargas SET capacidad_carga={capacidad} WHERE cohete_id={id_cohete}"
    elif tipo_cohete=='robotico':
        sql_query=f"UPDATE capacidades_cientificas SET capacidad_cientifica={capacidad} WHERE cohete_id={id_cohete}"
    elif tipo_cohete=='tripulado':
        sql_query=f"UPDATE capacidades_tripulantes SET capacidad_tripulantes={capacidad} WHERE cohete_id={id_cohete}"
    consultar_db('update',sql_query)