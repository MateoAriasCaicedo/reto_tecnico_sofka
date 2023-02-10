class Accesorio:
    
    def __init__(self,nombre,uso,ubicacion,tipo_cohete_destinatario):
        self.nombre=nombre
        self.uso=uso
        self.ubicacion=ubicacion
        self.tipo_cohete_destinatario=tipo_cohete_destinatario
    
    def __iter__(self):
        return (self.nombre,self.uso,self.ubicacion,self.tipo_cohete_destinatario)