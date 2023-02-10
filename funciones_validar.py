from database_manipulation.manipular_db import consultar_db

def validar_opcion_menu(respuesta:str,valor_mayor:int)->bool:
    # validar que opcion de un menu sea entera y este en el rango del menu.
    try:
        int(respuesta)
        if int(respuesta)<1 or int(respuesta)>valor_mayor:
            return True
    except ValueError:
            return True
    if valor_mayor<=0:
        return True
    if int(respuesta)<=0:
        return True
    return False

def validar_enteros_positivos(valores:tuple,max=0)->bool:
    # validar que los numeros enteros dados sean convertibles a enteros y mayores que 0, con un argumento de valor maximo que no es requisito.
    if max==0:
        for i in range(len(valores)):
            try:
                int(valores[i])
                if int(valores[i])<=0:
                    return True
            except ValueError:
                return True
        return False
    else:
        for i in range(len(valores)):
            try:
                int(valores[i])
                if int(valores[i])<=0 or int((valores)[i])>max:
                    return True
            except ValueError:
                return True
        return False

def validar_nombre_unico(nombre:str)->bool:
    # validar que el nombre de cohete dado no exista en la base de datos.
    lista_cohete=consultar_db('select',f"SELECT * FROM cohetes WHERE nombre='{nombre}'")
    if not lista_cohete:
        return True
    return False