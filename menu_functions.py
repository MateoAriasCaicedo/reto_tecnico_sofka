from funciones_crear_cohete import crear_cohete
def imprimir_cohete(lista_propiedades):
    print(f'''Nombre de la nave: {lista_propiedades[1]}''')
    print(f'Pais proveniente de la nave: {lista_propiedades[2]}')
    print(f'Altura de la nave: {lista_propiedades[3]} metros')
    print(f'Empuje de la nave: {lista_propiedades[4]} toneladas')
    print(f'Peso de la nave: {lista_propiedades[5]} toneladas')
    print(f'Tipo de combustible que utiliza la nave: {lista_propiedades[6]}')
    print(f'Estado actual de la nave: {lista_propiedades[7]}')
    print(f'Ubicacion actual de la nave: planeta {lista_propiedades[8]}')
    print(f'Tipo de nave nave: nave {lista_propiedades[9]}')

def imprimir_cohete_inexistente():
    print('¡No se ha encontrado una nave con esa propiedad!')
    print('')
    print('Volverás a la pantalla de inicio')
    print('')

def añadir_comillas_a_string(string):
    string="'"+string+"'"
    return string

def quitar_comillas_a_propiedades(propiedades,valor_propiedades):
    if 'nombre' in propiedades:
        valor_propiedades[propiedades.index('nombre')]=valor_propiedades[propiedades.index('nombre')][1:-1]
    elif 'estado' in propiedades:
        valor_propiedades[propiedades.index('estado')]=valor_propiedades[propiedades.index('estado')][1:-1]
    elif 'ubicacion' in propiedades:
        valor_propiedades[propiedades.index('ubicacion')]=valor_propiedades[propiedades.index('ubicacion')][1:-1]
    elif 'tipo_cohete' in propiedades:
        valor_propiedades[propiedades.index('tipo_cohete')]=valor_propiedades[propiedades.index('tipo_cohete')][1:-1]
    elif 'tipo_combustible' in propiedades:
        valor_propiedades[propiedades.index('tipo_combustible')]=valor_propiedades[propiedades.index('tipo_combustible')][1:-1]
    return valor_propiedades

def hallar_propiedad_que_cumple_cohete(cohete,valores_propiedades,propiedades):
    valores_propiedades=quitar_comillas_a_propiedades(propiedades,valores_propiedades)
    propiedades_cumplidas=[]
    for x in range(len(propiedades)):
        if valores_propiedades[x] in cohete:
            propiedades_cumplidas.append(propiedades[x])
    return propiedades_cumplidas