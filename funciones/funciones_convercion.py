def convertir_a_enteros(valores:list)->tuple:
    # convertir una lista de strings a enteros. Los valores de la lista deben ser convertibles a enteros.
    for i in range(len(valores)):
        valores[i]=int(valores[i])
    return tuple(valores)

def convertir_propiedades_a_string(iterable_propiedades:list)->list:
    # convertir la elección de búsqueda en el menu de creacion (int) a su valor correspondiente en string.
    diccionario_propiedades={1:'nombre',2:'estado',3:'pais',4:'ubicacion',5:'tipo_cohete',6:'tipo_combustible',7:'peso',8:'altura',9:'empuje'}
    propiedades_string_list=[]
    for key in iterable_propiedades:
        propiedades_string_list.append(diccionario_propiedades[key])
    return propiedades_string_list

def convertir_planeta_a_string(planeta:str)->str:
    # devuelve el valor en string de el numero dado.
    diccionario_planetas={1:'luna',2:'marte',3:'pluton',4:'tierra',5:'jupiter',6:'saturno',7:'neptuno',8:'mercurio'}
    return diccionario_planetas[planeta]

def convertir_a_int(valor:str)->int:
    return int(valor)