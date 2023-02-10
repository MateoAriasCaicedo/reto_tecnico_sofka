from funciones_crear_cohete import crear_cohete,crear_cohete_desde_lista_propiedades
from funciones_accesorios import crear_accesorio_desde_lista_de_propiedades,imprimir_accesorio_desde_lista_de_propiedades

from database_manipulation.crud_cohetes import actualizar_cohete_en_db,actualizar_propiedad_en_db,eliminar_cohete_en_db,guardar_cohete_en_db,get_id_cohete
from database_manipulation.capacidades_crud import actualizar_capacidad_en_db,crear_capacidad_en_db
from database_manipulation.manipular_db import construir_consulta_select,consultar_db
from database_manipulation.crud_accesorios import actualizar_ubicacion_accesorio_en_db,obtener_accesorio_desde_cohete

from menu_functions import imprimir_cohete,imprimir_cohete_inexistente,añadir_comillas_a_string,hallar_propiedad_que_cumple_cohete

from funciones_validar import validar_opcion_menu,validar_nombre_unico,validar_enteros_positivos
from funciones.funciones_convercion import convertir_a_enteros,convertir_propiedades_a_string,convertir_planeta_a_string,convertir_a_int

def correr_programa():
    
    while True:
        
        # menu de inicio.
        print('')
        print('')
        print('')
        print('')
        print('*-------------------------------------*')
        print('Hola! Bienvenido a la estación espacial.')
        print('*-------------------------------------*')
        print('¿Qué deseas hacer?')
        print('')
        print('1-Crear cohete.')
        print('2-Buscar cohete.')
        print('3-Finalizar programa.')

        # validacion de respuesta introducida
        respuesta=input()
        while validar_opcion_menu(respuesta,3):
            print('')
            print('¡Haz introducido un valor incorrecto!')
            print('Introduce un valor correcto, por favor')
            respuesta=input()
        print('')
        respuesta=int(respuesta)
        
        if respuesta==1:
            
            # Menu de creación de cohete.
            print('*------------------*')
            print('¡Creemos un cohete!')
            print('*------------------*')
            nombre=input('¿Qué nombre desea para su cohete?')
            pais=input('¿Qué pais construyó su cohete?')
            empuje=input('¿Qué empuje tiene su cohete?')
            peso=input('¿Qué peso tiene su cohete?')
            altura=input('¿Qué altura tiene su cohete?')
            tipo_combustible=input('¿Qué tipo_combustible utiliza su cohete?')

            # validar que los valores introducidos sean correctos
            while not validar_nombre_unico(nombre):
                print('')
                print('¡Haz introducido un nombre ya existente!')
                print('Introduce un valor correcto, por favor')
                nombre=input('¿Qué nombre tiene su cohete?')

            while validar_enteros_positivos((empuje,peso,altura)):
                print('')
                print('¡Haz introducido un valor entero incorrecto!')
                print('Introduce un valor correcto, por favor')
                empuje=input('¿Qué empuje tiene su cohete?')
                peso=input('¿Qué peso tiene su cohete?')
                altura=input('¿Qué altura tiene su cohete?')
            empuje,peso,altura=convertir_a_enteros([empuje,peso,altura])

            # menu tipo cohete
            print('')
            print('*------------------------------*')
            print('¿Qué tipo de cohete desea crear?')
            print('*------------------------------*')
            print('1-lanzadera')
            print('2-robotico')
            print('3-tripulado')

            tipo_cohete=input()
            while validar_opcion_menu(tipo_cohete,3):
                print('')
                print('¡Haz introducido un valor incorrecto!')
                print('Introduce un valor correcto, por favor')
                tipo_cohete=input()
            print('')
            tipo_cohete=int(tipo_cohete)

            match tipo_cohete:
                case 1:
                    tipo_cohete='lanzadera'
                case 2:
                    tipo_cohete='robotico'
                case 3:
                    tipo_cohete='tripulado'
            
            # se instancia un cohete, dependiendo del tipo que sea este.
            cohete = crear_cohete(nombre,pais,empuje,peso,altura,tipo_combustible,tipo_cohete)
            print('*------------------------------------------------------*')
            print('Los datos han sido recibidos, ¡El cohete ha sido creado! ')
            print('*------------------------------------------------------*')
            print('¿Desea guardarlo en la base de datos?')
            print('1-Si')
            print('2-No')
            print('')

            # validar respuesta de menu
            respuesta=input()
            while validar_opcion_menu((respuesta),2):
                print('')
                print('¡Haz introducido un valor incorrecto!')
                print('Introduce un valor correcto, por favor')
                respuesta=input()
            respuesta=int(respuesta)
            print('')

            if respuesta==1:
                # se envian los atributos del cohete a la base de datos cohetes en sqlite.
                guardar_cohete_en_db(cohete)
                crear_capacidad_en_db(100,get_id_cohete(cohete),cohete.tipo_cohete)
                print('¡El cohete ha sido guardado en la base de datos!')
                print('Volverás al menu de inicio.')
                print('')
            else:
                print('El cohete no ha sido guardado en la base de datos.')
                print('Volverás al menu de inicio.')
                print('')

        elif respuesta==2:
            
            # menu de busqueda de cohete, donde se ofrecen los diferentes tipos de búsqueda.
            print('*------------------*')
            print('¡Busquemos un cohete!')
            print('*------------------*')
            print('¿Cómo desea buscar el cohete?')
            print('')
            print('1-Búsqueda simple.')
            print('2-Búsqueda perzonalizada.')

            # validar opciones del menu
            respuesta=input()
            while validar_opcion_menu(respuesta,2):
                print('')
                print('¡Haz introducido un valor incorrecto!')
                print('Introduce un valor correcto, por favor')
                respuesta=input()
            respuesta=int(respuesta)
            print('')

            cohete_encontrado=None
            
            if respuesta==1:
                
                # Menu donde se ofrece al usuario los diferentes tipos de búsqueda simple.
                print('*--------------------------------------------------------*')
                print('¿Por medio de qué propiedad  desea desea buscar el cohete?')
                print('*--------------------------------------------------------*')
                print('1-Por nombre')
                print('2-Por estado')
                print('3-Por pais')
                print('4-Por ubicación')
                print('5-Por tipo de cohete')
                print('6-Por tipo combustible')
                print('7-Por peso')
                print('8-Por altura ')
                print('9-Por empuje')

                propiedad_buscada=input()
                while validar_opcion_menu(propiedad_buscada,9):
                    print('')
                    print('¡Haz introducido un valor incorrecto!')
                    print('Introduce un valor correcto, por favor')
                    propiedad_buscada=input()
                propiedad_buscada=int(propiedad_buscada)
                print('')
                print(propiedad_buscada)
                propiedad_buscada=convertir_propiedades_a_string([propiedad_buscada])[0]
                print('')
                valor_propiedad_buscada=input(f'{propiedad_buscada} del cohete que desea encontrar:')
                print('')

                # se realiza una consulta a la base de datos que retornará los cohetes que coinciden con esa propiedad.
                if propiedad_buscada=='nombre':
                    # busqueda personalizada para la propiedad nombre, pues con esta propiedad es única.
                    consulta_sql=f"SELECT * FROM cohetes WHERE nombre='{valor_propiedad_buscada}'"
                    lista_propiedades_cohete=(consultar_db('select',consulta_sql))

                    if not lista_propiedades_cohete:
                        # en caso de no se hallado ningún cohete.
                        imprimir_cohete_inexistente()
                        print('')
                        print('Volverás al menu de inicio.')
                        print('')

                    else:
                        # se imprime el cohete encontrado en la consola
                        print('¡Ha sido encontrado un cohete con ese nombre!')
                        print('')
                        imprimir_cohete(lista_propiedades_cohete[0])
                        # se instancia un cohete para hacer uso de este en el programa. En este caso es el primer elemento de la lista_propiedades_cohete, pues sólo existe un cohete con determinado nombre.
                        cohete_encontrado=crear_cohete_desde_lista_propiedades(lista_propiedades_cohete[0])
                        print('')

                else:
                    # busqueda general para cualquier propiedad, pues son propiedades que cualquier cohete puede tener.
                    consulta_sql=f"SELECT * FROM cohetes WHERE {(propiedad_buscada)}='{valor_propiedad_buscada}'"
                    lista_propiedades_cohetes=consultar_db('select',consulta_sql)

                    if not lista_propiedades_cohetes:
                        # en caso de no se hallado ningún cohete, se notifica al usuario la inexistencia de un cohete con tal propiedad.
                        imprimir_cohete_inexistente()
                        print('')
                        print('Volverás al menu de inicio.')
                        print('')

                    else:
                        # se imprime la cantidad de cohetes que tienen esa propiedad y, uno por uno, se muestran en consola.
                        print(f'Se han encontrado {len(lista_propiedades_cohetes)} cohetes con esa propiedad')
                        print('')
                        # iteración por la lista donde están los cohetes, para imprimirlos.
                        nombres_cohetes=[]
                        for cohete in lista_propiedades_cohetes:
                            imprimir_cohete(cohete)
                            nombres_cohetes.append(cohete[1])
                            print('')

                        # se instancia un cohete para hacer uso de este en el programa. Se elige uno de los cohetes que resultaron de la consulta sql.
                        print('¿Cuál cohete deseas seleccionar?')
                        for i in range(len(nombres_cohetes)):
                            print(f'{i+1}-{nombres_cohetes[i]}')
                        print('')

                        respuesta=input()
                        while validar_opcion_menu(respuesta,len(nombres_cohetes)):
                            print('')
                            print('¡Haz introducido un valor incorrecto!')
                            print('Introduce un valor correcto, por favor')
                            respuesta=input()
                        respuesta=int(respuesta)-1

                        cohete_encontrado=crear_cohete_desde_lista_propiedades(lista_propiedades_cohetes[respuesta])
                        print('')

            elif respuesta==2:
            
                # menu donde se ofrece al usuario las propiedades que desea incluir en su consulta.
                print('*-----------------------------------------------------------------------------*')
                print('Qué propiedades desea incluir en la busqueda?(Digitelas separadas por una coma)')
                print('*-----------------------------------------------------------------------------*')
                print('')
                print('1-Incluir nombre')
                print('2-Incluir estado')
                print('3-Incluir pais')
                print('4-Incluir ubicacion')
                print('5-Incluir tipo de cohete')
                print('6-Incluir tipo combustible')
                print('7-Incluir peso')
                print('8-Incluir altura')
                print('9-Incluir empuje')

                # validar y convertir los input de las propiedades
                propiedades=input()
                while validar_enteros_positivos((propiedades.split(',')),9):
                    print('')
                    print('¡Haz introducido un valor incorrecto!')
                    print('Introduce un valor correcto, por favor')
                    propiedades=input()
                print('')
                propiedades=list(propiedades.split(','))
                propiedades=list(map(convertir_a_int,propiedades))
                propiedades=convertir_propiedades_a_string(propiedades)

                # recibir los input para los valores dados por medio de un bucle for.
                valores_propiedades=[]
                for propiedad in propiedades:
                    valor=(input(f'{propiedad} de la nave que deseas buscar:'))
                    # como en la consulta el valor de la propiedad debe ir entrecomillada cuando se trata de un string, a los valores que corresponden a strings se les aplica el método añadir_comillas_a_string().
                    if propiedad=='nombre' or propiedad=='pais' or propiedad=='estado' or propiedad=='ubicacion' or propiedad=='tipo_cohete' or propiedad=='tipo_combustible':
                        valores_propiedades.append(añadir_comillas_a_string(valor))
                    else:
                        while validar_opcion_menu(valor,float('inf')):
                            print('')
                            print('Haz introducido un valor entero incorrecto.')
                            valor=(input(f'{propiedad} de la nave que deseas buscar:'))
                            print('')
                        valores_propiedades.append(int(valor))
                print('')

                # menu donde se ofrecen los dos tipos de búsqueda personalizada.
                print('¿Desea que se cumplan todas las condiciones o prefiere realizar una busqueda flexible?')
                print('1-Todas las condiciones')
                print('2-Búsqueda flexible')
                tipo_busqueda=int(input())
                print('')

                if tipo_busqueda==1:
                
                    # esta búsqueda ofrece una consulta sql con la condición unida por AND, significando que todas las condiciones dadas deben cumplirse para retornar un cohete.
                    print('*-------------------------------------------------------------*')
                    print('Se buscará un cohete que cumpla con todas las condiciones dadas')
                    print('*-------------------------------------------------------------*')
                    print('')

                    sql_query=construir_consulta_select(propiedades,valores_propiedades,'AND')
                    lista_propiedades_cohetes=consultar_db('select',sql_query)

                    if not lista_propiedades_cohetes:
                        # en caso de no se hallado ningún cohete, se notifica al usuario la inexistencia de un cohete con tales propiedades.
                        imprimir_cohete_inexistente()
                        print('')
                        print('Volverás al menu de inicio.')
                        print('')

                    else:
                        # se imprime la cantidad de cohetes que tienen esa propiedad y, uno por uno, se muestran en consola.
                        print(f'Se han encontrado {len(lista_propiedades_cohetes)} cohetes que cumplen esas condiciones')
                        print('')
                        # iteración por la lista donde están los cohetes, para imprimirlos.
                        nombres_cohetes=[]
                        for cohete in lista_propiedades_cohetes:
                            imprimir_cohete(cohete)
                            nombres_cohetes.append(cohete[1])
                            print('')

                        # se instancia un cohete para hacer uso de este en el programa. Se elige uno de los cohetes que resultaron de la consulta sql.
                        print('¿Cuál cohete deseas seleccionar?')
                        for i in range(len(nombres_cohetes)):
                            print(f'{i+1}-{nombres_cohetes[i]}')
                        print('')
                        respuesta=input()
                        while validar_opcion_menu(respuesta,len(nombres_cohetes)):
                            print('')
                            print('¡Haz introducido un valor incorrecto!')
                            print('Introduce un valor correcto, por favor')
                            respuesta=input()
                        respuesta=int(respuesta)-1
                        
                        cohete_encontrado=crear_cohete_desde_lista_propiedades(lista_propiedades_cohetes[respuesta])
                        print('')

                if tipo_busqueda==2:

                    # esta búsqueda ofrece una consulta sql con la condición unida por OR, significando que al menos una de las condiciones dadas deben cumplirse para retornar un cohete.
                    print('*------------------------------------------------------------------*')
                    print('Se buscará un cohete que cumpla con alguna de las condiciones dadas')
                    print('*------------------------------------------------------------------*')
                    print('')

                    sql_query=construir_consulta_select(propiedades,valores_propiedades,'OR')
                    lista_propiedades_cohetes=consultar_db('select',sql_query)

                    if not lista_propiedades_cohetes:
                        # en caso de no se hallado ningún cohete, se notifica al usuario la inexistencia de un cohete con tales propiedades.
                        imprimir_cohete_inexistente()
                        print('')

                    else:
                        # se imprime la cantidad de cohetes que tienen esa propiedad y, uno por uno, se muestran en consola.
                        print(f'Se han encontrado {len(lista_propiedades_cohetes)} cohetes que cumplen con algunas de las condiciones')
                        print('')

                        nombres_cohetes=[]
                        for cohete in lista_propiedades_cohetes:
                            imprimir_cohete(cohete)
                            propiedades_que_cumple=hallar_propiedad_que_cumple_cohete(cohete[1:],valores_propiedades,propiedades)
                            print(f'Este cohete cumple la propiedad:')
                            for propiedad_cumplida in propiedades_que_cumple:
                                print(propiedad_cumplida)
                            nombres_cohetes.append(cohete[1])
                            print('')

                        # se instancia un cohete para hacer uso de este en el programa. Se elige uno de los cohetes que resultaron de la consulta sql.
                        print('¿Cuál cohete deseas seleccionar?')
                        for i in range(len(nombres_cohetes)):
                            print(f'{i+1}-{nombres_cohetes[i]}')
                        print('')

                        # validar el input del valor que se desea seleccionar
                        respuesta=input()
                        while validar_opcion_menu(respuesta,len(nombres_cohetes)):
                            print('')
                            print('¡Haz introducido un valor incorrecto!')
                            print('Introduce un valor correcto, por favor')
                            respuesta=input()
                        respuesta=int(respuesta)-1

                        cohete_encontrado=crear_cohete_desde_lista_propiedades(lista_propiedades_cohetes[respuesta])
                        print('')

            # menu de opciones para cambiar propiedades del cohete
            if cohete_encontrado!=None:
                print('*-------------------------------*')
                print('¿Qué desea hacer con este cohete?')
                print('*-------------------------------*')
                print('1-Destruirlo')
                print('2-Administrar misiones')
                print('3-Cambiar sus propiedades')

                # validacion de respuesta en el menu
                respuesta=input()
                while validar_opcion_menu(respuesta,3):
                    print('')
                    print('¡Haz introducido un valor incorrecto!')
                    print('Introduce un valor correcto, por favor')
                    respuesta=input()
                respuesta=int(respuesta)
                print('')

                if respuesta==1:
                    
                    # menu de eliminacion de cohete
                    print('*------------------------*')
                    print('¡El cohete será destruido!')
                    print('*------------------------*')
                    print('¿Estás seguro de eliminarlo?')
                    print('1-Sí')
                    print('2-No')

                    respuesta=input()
                    while validar_opcion_menu(respuesta,2):
                        print('')
                        print('¡Haz introducido un valor incorrecto!')
                        print('Introduce un valor correcto, por favor')
                        respuesta=input()
                    respuesta=int(respuesta)
                    print('')

                    match respuesta:
                        case 1:
                            # eliminacion del cohete en la base de datos por medio de la funcion eliminar_cohete_en_db().
                            eliminar_cohete_en_db(cohete_encontrado)
                            print('¡El cohete ha sido eliminado!')
                            print('')
                        case 2:
                            print('¡El cohete no ha sido eliminado!')
                            print('')
                    print('Volverás al menú de inicio.')
                    print('')

                elif respuesta==2:
                    
                    # menu de opciones para cambiar propiedades de ubicacion y estado.
                    print('¡Este es el panel de administración del cohete!')
                    print(f'El cohete está ubicado actualmente en {cohete_encontrado.ubicacion}')
                    print(f'El cohete está {cohete_encontrado.estado}')
                    print('*-------------------------*')
                    print('¿Qué acción desea realizar?')
                    print('*-------------------------*')

                    # si el cohete esta en estado 'listo para despegar', se dara la opción de iniciar mision. Si por el contrario esta en misión, se dara la opcion de finalizar mision.
                    if cohete_encontrado.estado=='listo para despegar':
                        print('1-Emprender misión')
                        print('2-Volver al menu de inicio.')

                        # validar la respuesta de este menu
                        respuesta=input()
                        while validar_opcion_menu(respuesta,2):
                            print('')
                            print('¡Haz introducido un valor incorrecto!')
                            print('Introduce un valor correcto, por favor')
                            respuesta=input()
                        respuesta=int(respuesta)
                        print('')
                        
                        if respuesta==1:
                            
                            # seleccion de accesorios que son aptos para ser usados por el tipo de cohete y estan en la misma ubicacion del mismo.
                            sql_query_accesorios=f"SELECT * FROM accesorios WHERE tipo_cohete_destinatario='{cohete_encontrado.tipo_cohete}' AND ubicacion='{cohete_encontrado.ubicacion}'"
                            accesorios_lista_propiedades=consultar_db('select',sql_query_accesorios)

                            if not accesorios_lista_propiedades:
                                print('No se ha encontrado ningun accesorio disponible para emprender una mision.')
                                print('Volviendo al menu de inicio')

                            else:
                                print('Los accesorio disponibles para su cohete son')
                                nombres_accesorios=[]
                                for accesorio in accesorios_lista_propiedades:
                                    print('')
                                    imprimir_accesorio_desde_lista_de_propiedades(accesorio)
                                    nombres_accesorios.append(accesorio[1])
                                    print('')
                                
                                print('¿Cuál accesorio desea elegir?')
                                for index in range(len(nombres_accesorios)):
                                    print(f'{index+1}-{nombres_accesorios[index]}')
                                respuesta=input()
                                while validar_opcion_menu(respuesta,len(nombres_accesorios)):
                                    print('')
                                    print('¡Haz introducido un valor incorrecto!')
                                    print('Introduce un valor correcto, por favor')
                                    respuesta=input()
                                respuesta=int(respuesta)-1
                                print('')

                                accesorio_elegido=crear_accesorio_desde_lista_de_propiedades(accesorios_lista_propiedades[respuesta])

                                print('¿Cuál es el destino de la nave?')
                                print('1-Luna')
                                print('2-Marte')
                                print('3-Plutón')
                                print('4-Tierra')
                                print('5-Júpiter')
                                print('6-Saturno')
                                print('7-Neptuno')
                                print('8-Mercurio')
                                print('9-Otro')

                                respuesta=input()
                                while validar_opcion_menu(respuesta,9):
                                    print('')
                                    print('¡Haz introducido un valor incorrecto!')
                                    print('Introduce un valor correcto, por favor')
                                    respuesta=input()
                                respuesta=int(respuesta)
                                print('')
                                destino_nave=''

                                if respuesta==9:
                                    print('Digite el nombre del destino de la nave:')
                                    destino_nave=input()
                                else:
                                    # convertir a string los valores int dados en el input
                                    destino_nave=convertir_planeta_a_string(respuesta)
                                    
                                # iniciar mision con el metodo de la clase cohete
                                cohete_encontrado.iniciar_mision(accesorio_elegido,destino_nave)
                                actualizar_cohete_en_db(cohete_encontrado)
                                print(cohete_encontrado.estado)
                                actualizar_ubicacion_accesorio_en_db(cohete_encontrado.accesorio)
                                print('')
                                print('Volverás al menú de inicio.')
                                print('')

                    else:
                        print('1-Finalizar misión.')
                        print('2-Volver al menú de inicio.')

                        respuesta=input()
                        while validar_opcion_menu(respuesta,2):
                            print('')
                            print('¡Haz introducido un valor incorrecto!')
                            print('Introduce un valor correcto, por favor')
                            respuesta=input()
                        respuesta=int(respuesta)
                        print('')

                        if respuesta==1:

                            # finalizar mision en el objeto cohete_encontrado y guardar los cambios en la db
                            lista_propiedades_accesorio=obtener_accesorio_desde_cohete(cohete_encontrado)
                            cohete_encontrado.accesorio=crear_accesorio_desde_lista_de_propiedades(lista_propiedades_accesorio)
                            print(f'El cohete está finalizando su misión con destino a {cohete_encontrado.estado[16:]}')
                            cohete_encontrado.accesorio.ubicacion=f'{cohete_encontrado.estado[16:]}'
                            actualizar_ubicacion_accesorio_en_db(cohete_encontrado.accesorio)
                            cohete_encontrado.finalizar_mision()
                            actualizar_cohete_en_db(cohete_encontrado)
                            print(f'La misión ha finalizado, el cohete ahora está en {cohete_encontrado.ubicacion}')
                            print('')
                            print('Volverás al menu de incio')

                elif respuesta==3:
                    print('Cambiar propiedades del cohete')
                    print('¿Qué propiedad deseas cambiar?')
                    print('1-Nombre')
                    print('2-Estado')
                    print('3-Pais')
                    print('4-Ubicacion')
                    print('5-Tipo de cohete')
                    print('6-Tipo combustible')
                    print('7-Peso')
                    print('8-Altura')
                    print('9-Empuje')
                    tipo_cohete_encontrado=cohete_encontrado.tipo_cohete
                    tipo_capacidad_encontrada=''
                    match tipo_cohete_encontrado:
                        case 'lazadera':
                            tipo_capacidad_encontrada='capacidad_carga'
                        case 'robotico':
                            tipo_capacidad_encontrada='capacidad_cientifica'
                        case 'tripulada':
                            tipo_capacidad_encontrada='capacidad_tripulacion'

                    match tipo_cohete_encontrado:
                        case 'lanzadera':
                            print(f'10-Capacidad carga')
                        case 'robotico':
                            print(f'10-Capacidad científica')
                        case 'tripulado':
                            print(f'10-Capacidad tripulantes')

                    respuesta=input()
                    while validar_opcion_menu(respuesta,10):
                        print('')
                        print('¡Haz introducido un valor incorrecto!')
                        print('Introduce un valor correcto, por favor')
                        respuesta=input()
                    respuesta=int(respuesta)
                    print('')

                    match respuesta:
                        case 1:
                            nombre=input('Nuevo nombre de la nave')
                            while not validar_nombre_unico(nombre):
                                print('')
                                print('El nombre ya está siendo usado por otro cohete')
                                nombre=input('Nuevo nombre de la nave')
                            actualizar_propiedad_en_db(cohete_encontrado,'nombre',nombre)                            
                        case 2:
                            estado=input('Nuevo estado de la nave')
                            actualizar_propiedad_en_db(cohete_encontrado,'estado',estado)
                        case 3:
                            pais=input('Nuevo pais de la nave')
                            actualizar_propiedad_en_db(cohete_encontrado,'pais',pais)
                        case 4:
                            ubicacion=input('Nueva ubicacion de la nave')
                            actualizar_propiedad_en_db(cohete_encontrado,'ubicacion',ubicacion)
                        case 5:
                            tipo_cohete=input('Nuevo tipo de cohete de la nave')
                            actualizar_propiedad_en_db(cohete_encontrado,'tipo_cohete',tipo_cohete)
                        case 6:
                            tipo_combustible=input('Nuevo tipo de combustible de la nave')
                            actualizar_propiedad_en_db(cohete_encontrado,'tipo_combustible',tipo_combustible)
                        case 7:
                            peso=input('Nuevo peso de la nave')
                            actualizar_propiedad_en_db(cohete_encontrado,'peso',peso)
                        case 8:
                            altura=input('Nueva altura de la nave')
                            actualizar_propiedad_en_db(cohete_encontrado,'altura',altura)
                        case 9:
                            empuje=input('Nuevo empuje de la nave')
                            actualizar_propiedad_en_db(cohete_encontrado,'empuje',empuje)
                        case 10:
                            capacidad=input('Nueva capacidad de la nave:')
                            while validar_opcion_menu(capacidad,float('inf')):
                                print('')
                                print('Has dado un valor incorrecto, digite el valor de nuevo.')
                                print('')
                                capacidad=input('Nueva capacidad de la nave:')
                            capacidad=int(capacidad)
                            actualizar_capacidad_en_db(capacidad,cohete_encontrado,tipo_cohete_encontrado)

                    print('')
                    print('Se ha cambiado el valor de la propiedad del cohete.')
                    print('Volviendo al menu de inicio')
                    print('')

        elif respuesta==3:
            print('¡Hasta pronto! Muchas gracias por usar este programa.')
            break

correr_programa()