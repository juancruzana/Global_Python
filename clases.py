class Detector(): 

    def __init__(self,lista_adn):
        pass
    
    def detectar_mutante(self): 
        pass 

class Mutador(): 

    def __init__(self,base_nitrogrnada):
        self.base_nitrogenada = base_nitrogrnada 

    def crear_mutante(self): 
        pass
    

class Radiacion(Mutador):
    
    def __init__(self, base_nitrogrnada):
        super().__init__(base_nitrogrnada) 
    
    def crear_mutante(self,posicion_inicial,orientacion):
        pass
    
class Virus(Mutador):
    
    def __init__(self, base_nitrogrnada):
        super().__init__(base_nitrogrnada) 
    
    def crear_mutante(self,posicion_inicial):
        pass
    
class Sanador(Detector): 
    
    def __init__(self, lista_adn):
        super().__init__(lista_adn)
    
    def sanar_mutantes(self): 
        pass
     
    
    
