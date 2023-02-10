class Cohete:
    
    def __init__(self,nombre:str,pais:str,empuje:int,peso:int,altura:int,tipo_combustible:str)->None:
        self.nombre=nombre
        self.pais=pais
        self.empuje=empuje
        self.peso=peso
        self.altura=altura
        self.tipo_combustible=tipo_combustible
        self.ubicacion='tierra'
        self.estado='listo para despegar'
        self.accesorio='vacio'

    def iniciar_mision(self,accesorio:object,destino:str)->None:
        # iniciar una mision con el cohete dado y el accesorio apto para el cohete.
        self.accesorio=accesorio
        self.estado=f'en misión hacia {destino}'
        self.ubicacion='espacio exterior'
        self.accesorio.ubicacion='espacio exterior'

    def finalizar_mision(self)->None:
        # finalizar la mision iniciada por el cohete y dejar el accesorio.
        self.accesorio.ubicacion=self.estado[16:]
        self.accesorio='vacio'
        self.ubicacion=self.estado[16:]
        self.estado='listo para despegar'

    def __iter__(self)->tuple:
        return (self.nombre,self.pais,self.empuje,self.peso,self.altura,self.tipo_combustible,self.ubicacion,self.estado)

class CoheteLanzadera(Cohete):
    
    tipo_cohete='lanzadera'
    def __init__(self,nombre,pais,empuje,peso,altura,tipo_combustible):
        super().__init__(nombre,pais,empuje,peso,altura,tipo_combustible)
        self.capacidad_carga=100
        
    def iniciar_mision(self,accesorio:object,destino:str)->None:
        # iniciar una mision con el cohete dado y el accesorio apto para el cohete.
        print(f'El cohete {self.nombre} inicia su misión, con carga {accesorio.nombre} que será dejada en {destino}')
        self.accesorio=accesorio
        self.estado=f'en misión hacia {destino}'
        self.ubicacion='espacio exterior'
        self.accesorio.ubicacion='espacio exterior'

    def finalizar_mision(self)->None:
        # finalizar la mision iniciada por el cohete y dejar el accesorio.
        self.accesorio.ubicacion=self.estado[16:]
        self.ubicacion=self.estado[16:]
        print(f'El cohete {self.nombre} finaliza su misión, la carga de {self.accesorio.nombre} será dejada en {self.ubicacion}')
        self.accesorio='vacio'
        self.estado='listo para despegar'

class CoheteRobótico(Cohete):
    tipo_cohete = 'robotico'
    def __init__(self,nombre,pais,empuje,peso,altura,tipo_combustible):
        super().__init__(nombre,pais,empuje,peso,altura,tipo_combustible)
        self.capacidad_cientifica=100

    def iniciar_mision(self,accesorio:object,destino:str)->None:
        # iniciar una mision con el cohete dado y el accesorio apto para el cohete.
        print(f'El cohete {self.nombre} inicia su misión, con herramienta {accesorio.nombre} que ayudará a estudiar {destino}')
        self.accesorio=accesorio
        self.ubicacion='espacio exterior'
        self.estado=f'en misión hacia {destino}'
        self.accesorio.ubicacion='espacio exterior'

    def finalizar_mision(self)->None:
        # finalizar la mision iniciada por el cohete y dejar el accesorio.
        self.accesorio.ubicacion=self.estado[16:]
        self.ubicacion=self.estado[16:]
        print(f'El cohete {self.nombre} finaliza su misión, la herramienta {self.accesorio.nombre} será dejada en {self.ubicacion}')
        self.accesorio='vacio'
        self.estado='listo para despegar'

class CoheteTripulado(Cohete):
    tipo_cohete = 'tripulado'
    def __init__(self,nombre,pais,empuje,peso,altura,tipo_combustible):
        super().__init__(nombre,pais,empuje,peso,altura,tipo_combustible)
        self.capacidad_tripulantes=100
    
    def iniciar_mision(self,accesorio:object,destino:str)->None:
        # iniciar una mision con el cohete dado y el accesorio apto para el cohete.
        print(f'El cohete {self.nombre} inicia su misión, con tripulacion {accesorio.nombre} que será dejada en {destino}')
        self.accesorio=accesorio
        self.estado=f'en misión hacia {destino}'
        self.ubicacion='espacio exterior'
        self.accesorio.ubicacion='espacio exterior'

    def finalizar_mision(self)->None:
        # finalizar la mision iniciada por el cohete y dejar el accesorio.
        self.accesorio.ubicacion=self.estado[16:]
        self.ubicacion=self.estado[16:]
        print(f'El cohete {self.nombre} finaliza su misión, la tripulacion {self.accesorio.nombre} será dejada en {self.ubicacion}')
        self.accesorio='vacio'
        self.estado='listo para despegar'