from database_manipulation.manipular_db import consultar_db

def actualizar_ubicacion_accesorio_en_db(accesorio:object)->None:
    # actualizar ubicacion del accesorio en la base de datos
    nombre,uso,ubicacion,tipo_cohete_destinatario=accesorio.__iter__()
    sql_query=f"UPDATE accesorios SET ubicacion='{ubicacion}' WHERE nombre='{nombre}'"
    consultar_db('update',sql_query)

def obtener_id_accesorio_unido_a_cohete(cohete):
    # obtener el id de un accesorio unido desde su nombre en el objeto dado. El objeto debe tener accesorio.
    return (consultar_db('select',f"SELECT * FROM cohetes WHERE nombre='{cohete.nombre}'"))[0][10]

def obtener_accesorio_desde_cohete(cohete):
    # obtener un accesorio desde un cohete con accesorio como propiedad.
    id_en_tabla_cohete=obtener_id_accesorio_unido_a_cohete(cohete)
    sql_query=f"SELECT * FROM accesorios WHERE id_accesorio={id_en_tabla_cohete}"
    return consultar_db('select',sql_query)[0]