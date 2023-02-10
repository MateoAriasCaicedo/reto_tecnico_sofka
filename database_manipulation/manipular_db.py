import sqlite3
from funciones_crear_cohete import crear_cohete

def consultar_db(operacion:str,sql_query:str)->None:
    
    # conectar con la base de datos y realizar determinada consulta sql.
    if operacion=='select':
        conexion=sqlite3.connect('cohetes')
        cursor=conexion.cursor()
        cursor.execute(sql_query)
        row=(cursor.fetchall())
        conexion.close()
        return row
    elif operacion=='insert':
        conexion=sqlite3.connect('cohetes')
        cursor=conexion.cursor()
        cursor.execute(sql_query)
        conexion.commit()
        conexion.close()  
    elif operacion=='update' or operacion=='delete':
        conexion=sqlite3.connect('cohetes')
        cursor=conexion.cursor()
        cursor.execute(sql_query)
        conexion.commit()
        conexion.close()

def construir_consulta_select(lista_propiedades,valores_propiedades,tipo_condicion):
    sql_query=f"SELECT * FROM cohetes WHERE "
    for index in range(len(lista_propiedades)):
        sql_query+=f"{lista_propiedades[index]}={valores_propiedades[index]} "
        if (index+1)==len(lista_propiedades):
            sql_query+=';'
        else:
            sql_query+=f' {tipo_condicion} '
    return sql_query