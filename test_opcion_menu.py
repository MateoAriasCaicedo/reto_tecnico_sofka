from funciones_validar import validar_opcion_menu
from pytest import mark

@mark.parametrize(
    "respuesta,numero_maximo,boolean_esperado",
    [
    ('1',10,True),
    ('-1',10,True),
    ('10',-1,True),
    ('0',-1,True)
    ('s',-1,True)
    ('1',2,False)
    ]
)
def test_validar_opcion_menu(respuesta,numero_maximo,boolean_esperado):
    assert validar_opcion_menu(respuesta,numero_maximo)==boolean_esperado