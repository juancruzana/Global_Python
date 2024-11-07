
#Funcion que recibe letra de base nitrogenada y devuelve la palabra
def convertir_letra_a_palabra(letra): 
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
def mostrar_mutacion_horizontal(lista_horizontales):    

    
    for posicion in lista_horizontales: 
        print(f"Fila {posicion[0]+1}: Mutacón Horaizontal de {convertir_letra_a_palabra(posicion[1])}")

def mostrar_mutacion_vertical(lista): 
    for poscicon in lista: 
        print(f"Columna {poscicon[0]+1}: Mutación Vertical de {convertir_letra_a_palabra(poscicon[1])}") 

def mostrar_mutacion_diagonal(lista,contador):
    
    print(f"Mutaciones Diagonales : {contador}")
    print("Bases Causantes del mutante: ")
    for i in lista: 
        base = convertir_letra_a_palabra(i)
        print(f"-{base}")
     

#funcion que verifica si hay mutacion diagonal    
def verificar_diagonal(adn): 
    
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
                
    #Bucle que recorre de manera descendente de derecha a izquierda 
    for y in range(len(adn)-3):
        
        for x in range(3,len(adn[y])):
            if adn[y][x] == adn[y+1][x-1] == adn[y+2][x-2] == adn[y+3][x-3]: 
                    bases_repetidas.add(adn[y][x])
                    contador +=1

    return  bases_repetidas,contador 
    #devuelve cant de mutaciones y cuales son las bases nitrogenadas de las mismas.    

#funcio para verificar si hay mutacion vertical.
def verificar_vertical(adn,secuencia_mutante): 
    
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
def verificar_horizontal(adn,secuencia_mutante): 
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


    
