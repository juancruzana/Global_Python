from funciones_clase_detector import * 
from funciones_clase_radiacion import * 

class Detector(): 
    #Atributos: Matriz de ADN // longitud_secunecia_mutantes = cuantas veces tiene que estar repetida 
    #la base para que sea un mutante
    def __init__(self,lista_adn,longitud_secuncia_mutantes):
        self.lista_adn = lista_adn
        self.longitud_secuncia_mutantes = longitud_secuncia_mutantes
    
    def detectar_mutante(self):
       
        self.contador_mutaciones_totales = 0 
        self.mutacion = True 
        self.mutante_diagonal,self.contador = verificar_diagonal(self.lista_adn) 
        self.mutante_vertical = verificar_vertical(self.lista_adn,self.longitud_secuncia_mutantes)
        self.mutante_horizontal = verificar_horizontal(self.lista_adn,self.longitud_secuncia_mutantes)
        
        if self.mutante_horizontal or self.mutante_vertical or self.mutante_diagonal: 
           
           self.contador_horizontales = len(self.mutante_horizontal)
           self.contador_verticales = len(self.mutante_vertical)
           self.contador_diagonal = len(self.mutante_diagonal)
           
           self.contador_total = self.contador_diagonal + self.contador_horizontales + self.contador_verticales
           
        else : self.mutacion = False
        
        return self.mutacion, self.contador_total
    
    def mostrar_total_mutaciones(self):
         
        if self.mutante_horizontal: 
                mostrar_mutacion_horizontal(self.mutante_horizontal)
        if self.mutante_vertical:
                mostrar_mutacion_vertical(self.mutante_vertical) 
        if self.mutante_diagonal:
                mostrar_mutacion_diagonal(self.mutante_diagonal,self.contador)
        
        
class Mutador(): 

    def __init__(self,lista_adn,base_nitrogrnada):
        self.lista_adn = lista_adn
        self.base_nitrogenada = base_nitrogrnada 

    def crear_mutante(self): 
        pass

class Radiacion(Mutador):
    
    def __init__(self, lista_adn, base_nitrogrnada):
        super().__init__(lista_adn, base_nitrogrnada)
    
    def crear_mutante(self,posicion_inicial,orientacion,cantidad):

        if orientacion: 
            self.adn_mutado = crear_mutacion_horizontal(self.lista_adn,posicion_inicial,self.base_nitrogenada,cantidad)
        else: 
            self.adn_mutado = crear_mutacion_vertical(self.lista_adn,posicion_inicial,self.base_nitrogenada,cantidad)
            
        return self.adn_mutado
    
    
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
     
    
    
