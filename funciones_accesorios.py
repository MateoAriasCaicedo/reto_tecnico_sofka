from clases.clase_accesorio import Accesorio

def crear_accesorio(nombre,uso,ubicacion,tipo_cohete_destinatario):
    return Accesorio(nombre,uso,ubicacion,tipo_cohete_destinatario)

def crear_accesorio_desde_lista_de_propiedades(lista_propiedades):
    id,nombre,uso,ubicacion,tipo_cohete_destinatario=lista_propiedades
    return crear_accesorio(nombre,uso,ubicacion,tipo_cohete_destinatario)

def imprimir_accesorio_desde_lista_de_propiedades(lista_propiedades):
    id,nombre,uso,ubicacion,tipo_cohete_destinatario=lista_propiedades
    print(f'Este accesorio se llama: {nombre}')
    print(f'Su uso es: {uso}')
    print(f'Está ubicado en: {ubicacion}')
    print(f'Puede ser usado por: {tipo_cohete_destinatario}')

def imprimir_accesorio(accesorio):
    print(f'Este accesorio se llama: {accesorio.nombre}')
    print(f'Su uso es: {accesorio.uso}')
    print(f'Está ubicado en: {accesorio.ubicacion}')
    print(f'Puede ser usado por: {accesorio.tipo_cohete_destinatario}')