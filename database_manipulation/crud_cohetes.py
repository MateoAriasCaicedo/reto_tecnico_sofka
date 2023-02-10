from database_manipulation.manipular_db import consultar_db

def guardar_cohete_en_db(cohete:object)->None:
    # guardar el cohete dado en la base de datos cohetes.
    nombre,pais,empuje,peso,altura,tipo_combustible,ubicacion,estado=cohete.__iter__()
    tipo_cohete = cohete.tipo_cohete
    sql_query=f"INSERT INTO cohetes (nombre,pais,empuje,peso,altura,tipo_combustible,ubicacion,estado,tipo_cohete) VALUES('{nombre}','{pais}',{empuje},{peso},{altura},'{tipo_combustible}','{ubicacion}','{estado}','{tipo_cohete}')"
    consultar_db('insert',sql_query)

def actualizar_cohete_en_db(cohete:object)->None:

    # actualizar propiedades de un cohete ya existente en la base de datos    
    nombre,pais,empuje,peso,altura,tipo_combustible,ubicacion,estado=cohete.__iter__()
    tipo_cohete = cohete.tipo_cohete
    sql_query=''
    
    if cohete.accesorio!='vacio':
        id_accesorio=consultar_db('select',f"SELECT * FROM accesorios WHERE nombre='{cohete.accesorio.nombre}'")[0][0]
        sql_query=sql_query=f"UPDATE cohetes SET nombre='{nombre}',pais='{pais}',altura={altura},empuje={empuje},peso={peso},tipo_combustible='{tipo_combustible}',estado='{estado}',ubicacion='{ubicacion}',tipo_cohete='{tipo_cohete}', accesorio_unido={id_accesorio} WHERE nombre='{nombre}'"

    else:
        sql_query=f"UPDATE cohetes SET nombre='{nombre}',pais='{pais}',altura={altura},empuje={empuje},peso={peso},tipo_combustible='{tipo_combustible}',estado='{estado}',ubicacion='{ubicacion}',tipo_cohete='{tipo_cohete}',accesorio_unido=NULL WHERE nombre='{nombre}'"

    consultar_db('update',sql_query)

def actualizar_propiedad_en_db(cohete:object,propiedad:str,valor_propiedad:str)->None:
    # actualizar una propiedad del cohete ya existente en la base de datos.
    sql_query=f"UPDATE cohetes SET {propiedad}='{valor_propiedad}' WHERE nombre='{cohete.nombre}'"
    consultar_db('update',sql_query)

def eliminar_cohete_en_db(cohete:object)->None:
    # eliminar cohete ya existente en la base de datos
    nombre=cohete.nombre
    sql_query=f"DELETE FROM cohetes WHERE nombre='{nombre}'"
    consultar_db('delete',sql_query)

def get_id_cohete(cohete):
    return consultar_db('select',f"SELECT * FROM cohetes WHERE nombre='{cohete.nombre}'")[0][0]