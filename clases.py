

import random
import time

class Detector(): 
    #Atributos: Matriz de ADN // longitud_secunecia_mutantes = cuantas veces tiene que estar repetida 
    #la base para que sea un mutante
    def __init__(self,lista_adn):
        self.lista_adn = lista_adn
    
    #Funcion que recibe letra de base nitrogenada y devuelve la palabra
    def convertir_letra_a_palabra(self,letra): 
        letra = letra.lower()
        if letra == "a":
            letra = "Adenina" 
        elif letra == "g": 
            letra = "Guanina"
        elif letra == "c": 
            letra = "Citocina"
        elif letra == "t": 
            letra = "Tinina"
        
        return letra

    #FUNCIONES PARA IMPRIMIR POR PANTALLA TIPO DE MUTACIÓN
    def mostrar_mutacion_horizontal(self,lista_horizontales):
        
        print("-------------MUTACIONES HORIZONTALES--------------")
        for posicion in lista_horizontales: 
            print(f"Fila {posicion[0]+1}: Mutacón de {self.convertir_letra_a_palabra(posicion[1])}")
            time.sleep(0.8)
        print("\n")
        
    def mostrar_mutacion_vertical(self,lista): 
        
        print("-------------MUTACIONES VERTICALES--------------")
        for poscicon in lista: 
            print(f"Columna {poscicon[0]+1}: Mutación de {self.convertir_letra_a_palabra(poscicon[1])}")
            time.sleep(0.8) 
            
        print("\n")

    def mostrar_mutacion_diagonal(self,lista,contador):
        
        print("------------MUTACIONES DIAGONALES--------------")
        print(f"Mutaciones : {contador}")
        print("Bases Causantes del mutante: ")
        for i in lista: 
            base = self.convertir_letra_a_palabra(i)
            print(f"-{base}")
            time.sleep(0.8)
        print("\n")
        
    #funcion que verifica si hay mutacion diagonal    
    def detectar_diagonal(self,adn): 
        
        contador = 0
        bases_repetidas = set()
        
        #Bucle que recorre la lista de forma descendente de izzquierda a derecha 
        # y = recorre los elementos de la lista(filas)
        for y in range(len(adn)-3):
            #x = recorre las filas 
            for x in range(len(adn[y])-3):
                if adn[y][x] == adn[y+1][x+1] == adn[y+2][x+2] == adn[y+3][x+3]: 
                    bases_repetidas.add(adn[y][x])
                    contador +=1
                    
        #Bucle que recorre de manera descendente de derecha a i
        # zquierda 
        for y in range(len(adn)-3):
            
            for x in range(3,len(adn[y])):
                if adn[y][x] == adn[y+1][x-1] == adn[y+2][x-2] == adn[y+3][x-3]: 
                        bases_repetidas.add(adn[y][x])
                        contador +=1

        return  bases_repetidas,contador 
        #devuelve cant de mutaciones y cuales son las bases nitrogenadas de las mismas.    

    #funcio para verificar si hay mutacion vertical.
    def detectar_vertical(self,adn,secuencia_mutante): 
        
        lista_bases_repetidas = [] 
        #recorre filas de la lista
        for y in range(0,6):
            contador = 1
            #recorre elementos de cada fila 
            for x in range(0,6):
                caracter_inicial = adn[x][y]
                if x != 5 : 
                    if caracter_inicial == adn[x+1][y]: 
                        contador+=1 
                    else: 
                        contador = 1
                        caracter_inicial = adn[x+1][y]
                    #si hay 4 coincidenicias se guarda la fila y la base en una lista 
                if contador  >= secuencia_mutante: 
                    if (y,caracter_inicial) not in lista_bases_repetidas: 
                        lista_bases_repetidas.append((y,caracter_inicial)) 
        
        return lista_bases_repetidas
                    
    #Funcion para verificar mutacion horizontal  
    def detectar_horizontal(self,adn,secuencia_mutante): 
        bases_repetidas_horizontal = []
        
        #bucle que recorre las filas con su indice
        for n_fila,fila in enumerate(adn): 
            contador = 1 
            for i,caracter in enumerate(fila): 
                if i != 5 : 
                    if caracter == fila[i+1]: 
                        contador+=1
                    else: 
                        contador = 1
                        #si hay 4 bases repetidas horizontalmente se guarda columna y base en una lista
                if contador >= secuencia_mutante :
                    if (n_fila,caracter) not in bases_repetidas_horizontal:  
                        bases_repetidas_horizontal.append((n_fila,caracter))
            
        return bases_repetidas_horizontal
    
    def detectar_mutante(self,lista_adn):
       
        self.longitud_secuncia_mutantes = 4
        self.contador_mutaciones_totales = 0 
        self.mutacion = True 
        self.mutante_diagonal,self.contador = self.detectar_diagonal(lista_adn) 
        self.mutante_vertical = self.detectar_vertical(lista_adn,self.longitud_secuncia_mutantes)
        self.mutante_horizontal = self.detectar_horizontal(lista_adn,self.longitud_secuncia_mutantes)
        
        if self.mutante_horizontal or self.mutante_vertical or self.mutante_diagonal: 
           
           self.contador_horizontales = len(self.mutante_horizontal)
           self.contador_verticales = len(self.mutante_vertical)
           self.contador_diagonal = len(self.mutante_diagonal)
           
           self.contador_total = self.contador_diagonal + self.contador_horizontales + self.contador_verticales
           
        else : self.mutacion = False
        
        return self.mutacion, self.contador_total
    
    def mostrar_total_mutaciones(self):
         
        if self.mutante_horizontal: 
                self.mostrar_mutacion_horizontal(self.mutante_horizontal)
        if self.mutante_vertical:
                self.mostrar_mutacion_vertical(self.mutante_vertical) 
        if self.mutante_diagonal:
                self.mostrar_mutacion_diagonal(self.mutante_diagonal,self.contador)
        
        
class Mutador(): 

    def __init__(self,lista_adn,base_nitrogrnada):
        self.lista_adn = lista_adn
        self.base_nitrogenada = base_nitrogrnada 

    def crear_mutante(self): 
        pass

class Radiacion(Mutador):
    
    def __init__(self, lista_adn, base_nitrogrnada):
        super().__init__(lista_adn, base_nitrogrnada)
    
    def crear_mutacion_horizontal(self,lista_adn,posicion_x,posicion_y,base_n,cantidad): 
        posicion_final = (posicion_y + cantidad) + 1
        fila = lista_adn[posicion_x]
        fila_modificada = fila[:posicion_y] + base_n * cantidad + fila[posicion_final:]
        lista_adn[posicion_x] = fila_modificada
        return lista_adn
        
    def crear_mutacion_vertical(self,lista_adn,posicion_x,posicion_y,base_n,cantidad):
        
        for fila in range(posicion_x,cantidad+1):
            lista_fila = list(lista_adn[fila])
            lista_fila[posicion_y] = base_n
            lista_fila = ''.join(lista_fila)
            lista_adn[posicion_x]= lista_fila
        return lista_adn
            
    def crear_mutante(self,posicion_inicial,orientacion,cantidad):

        posicion_x = posicion_inicial[0]-1
        posicion_y = posicion_inicial[1]-1

        if orientacion: 
            self.adn_mutado = self.crear_mutacion_horizontal(self.lista_adn,posicion_x ,posicion_y,self.base_nitrogenada,cantidad)
        else: 
            self.adn_mutado = self.crear_mutacion_vertical(self.lista_adn,posicion_x,posicion_y,self.base_nitrogenada,cantidad)
            
        return self.adn_mutado
    
    
class Virus(Mutador):
    
    def __init__(self,lista_adn, base_nitrogrnada):
        super().__init__(lista_adn,base_nitrogrnada) 
    
    def crear_diagonal_derecha(self,base, lista_adn, posicion_inicial, cantidad):

        fila_inicial, columna_inicial = posicion_inicial
        fila_inicial -= 1
        columna_inicial -= 1

        for i in range(cantidad):
            lista_fila = list(lista_adn[fila_inicial + i])
            lista_fila[columna_inicial + i] = base
            lista_adn[fila_inicial + i] = ''.join(lista_fila)

        return lista_adn


    def crear_diagonal_izquierda(self,base,lista_adn,posicion_inicial,cantidad):

        fila_inicial, columna_inicial = posicion_inicial
        fila_inicial -= 1
        columna_inicial -= 1

        for i in range(cantidad):
            lista_fila = list(lista_adn[fila_inicial+i])
            lista_fila[columna_inicial-i] = base
            lista_adn[fila_inicial+i] = ''.join(lista_fila)
        return lista_adn
    
    
    def crear_mutante(self,orientacion,posicion_inicial,cantidad):
        
        if orientacion: 
            lista_mutada_diagonal = self.crear_diagonal_derecha(self.base_nitrogenada,self.lista_adn,posicion_inicial,cantidad)
        else: 
            lista_mutada_diagonal = self.crear_diagonal_izquierda(self.base_nitrogenada,self.lista_adn,posicion_inicial,cantidad)
        
        return lista_mutada_diagonal 
           

class Sanador(Detector): 
    
    def __init__(self, lista_adn):
        super().__init__(lista_adn)
    
 
    def sanar_mutante_completo(self): 
        
        lista_limpia = []
        bases_permitidas = "cgta"
        while True:     
            for i in range(0,6):     
                fila_aleatoria = ''.join(random.choices(bases_permitidas,k=6))
                lista_limpia.append(fila_aleatoria)
            if self.detectar_mutante(lista_limpia): 
                return lista_limpia
    
                
    def sanar_mutantes(self): 
        
        self.hay_mutacion,self.mutaciones_totales = self.detectar_mutante(self.lista_adn) 

        if self.hay_mutacion: 
            lista_sanador = self.sanar_mutante_completo()
        else: 
            return False

        return lista_sanador
        
    
