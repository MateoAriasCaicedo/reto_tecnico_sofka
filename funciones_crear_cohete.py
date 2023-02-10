from clases.clases_cohete import Cohete,CoheteLanzadera,CoheteRobótico,CoheteTripulado

def crear_cohete(nombre,pais,empuje,peso,altura,tipo_combustible,tipo_cohete):
    if tipo_cohete=='lanzadera':
        tipo_cohete='CoheteLanzadera'
    elif tipo_cohete=='robotico':
        tipo_cohete='CoheteRobótico'
    else:
        tipo_cohete='CoheteTripulado'
    return eval(tipo_cohete)(nombre,pais,empuje,peso,altura,tipo_combustible)

def recrear_cohete(nombre,pais,empuje,peso,ubicacion,estado,altura,tipo_combustible,tipo_cohete):
    if tipo_cohete=='lanzadera':
        tipo_cohete='CoheteLanzadera'
    elif tipo_cohete=='robotico':
        tipo_cohete='CoheteRobótico'
    else:
        tipo_cohete='CoheteTripulado'
    cohete=eval(tipo_cohete)(nombre,pais,empuje,peso,altura,tipo_combustible)
    cohete.ubicacion=ubicacion
    cohete.estado=estado
    return cohete

def crear_cohete_desde_lista_propiedades(lista_propiedades):
    id,nombre,pais,altura,empuje,peso,tipo_combustible,estado,ubicacion,tipo_cohete,id_accesorio=lista_propiedades
    return recrear_cohete(nombre,pais,empuje,peso,ubicacion,estado,altura,tipo_combustible,tipo_cohete)