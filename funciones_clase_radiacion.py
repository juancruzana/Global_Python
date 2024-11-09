
from funciones_clase_detector import *

#Funcion para que ele ususario ingrese una orientacion 
def ingresar_orientacion_de_mutacion(): 
    lista_orientaciones = ["h","v"]
    
    while True: 
        try: 
            orientacion = input("Orientación: ")
            if orientacion.lower() in lista_orientaciones: 
                break
            else: 
                    print("ERROR")
                    print("- Ingrese una Orientación Válida(H/V). \n ")
            
        except: 
            print("ERROR")
            print("- Valor incorrecto.\n  ")
          
    return orientacion

#funcion para que el usuario ingrese la base nitrogenada.    
def ingresar_base_nitrogenada():
    
    lista_bases = ["a","t","g","c","adenina","tinina","guanina","citocina"]
    
    while True: 
        try: 
            base_ingresada = input("Base: ")
            if base_ingresada.lower() in lista_bases: 
                break
            else: 
                print("""ERROR
                    - Ingrese una Base Nitrogenada Válida.\n """)
        except:  
                print("""ERROR
                    - Valor incorrecto.\n """)
    return base_ingresada            

#funcion que retorna la poscicion de y(columna), elegida por el usuario   
def conseguir_y(horizontal): 
    #mientras no se ingrese una posicion valida el bucle se repetira
    while True: 
        posicion_y = int(input("Posicion y: ")) 
        if posicion_y >= 1 and posicion_y <= 6: 
            if horizontal: 
                if posicion_y <= 2: 
                    break
                else: 
                    print("ERROR")
                    print("-Posicion inválida para crear mutante horizontal\n")
            else: 
                break
        else:
            print("ERROR")
            print("-Posicion Inválida.\n")
        
    return posicion_y

#funcion que retorna la poscicion de x(fila), elegida por el usuario
def conseguir_x(horizontal):
    
    while True: 
        try: 
            posicion_x = int(input("Posicion X: ")) 
            if posicion_x >= 1 and posicion_x <= 6: 
                if horizontal: 
                    break
                else: 
                    if posicion_x <= 2: 
                        break
                    else: 
                        print("ERROR")
                        print("-Posicion inválida para crear mutante Vertical\n")
            else: 
                print("ERROR")
                print("- Posicion Inválida.\n")
        except: 
            print("ERROR")
            print("-Valor Inválido")
    return posicion_x

#funcion que devuelve los dos valores conseguidos en las anteriores funciones(x,y)             
def ingresar_posicion_inicial(horizontal):
    while True: 
        try: 
            posicion_x = conseguir_x(horizontal)
            break
        except: 
            print("Error")
            print("- Ingrese valor válido. \n")
    
    while True: 
        try: 
            posicion_y = conseguir_y(horizontal)
            break
        except: 
            print("Error")
            print("- Ingrese valor válido")
    #devuelve una tupla         
    return (posicion_x,posicion_y)
            
#funcion para ingresar la cantidad de bases nitrgenadas que se van a inyectar.
#contiene manejo de  errores 
def ingresar_cantidad(posicion_inicial,es_horizontal,base): 
    
    if es_horizontal : 
        print(f"Puede ingresar como maximo una mutacion de {7-posicion_inicial[1]} de {convertir_letra_a_palabra(base)}")
    else: 
        print(f"Puede ingresar como maximo una mutacion de {7-posicion_inicial[0]} de {convertir_letra_a_palabra(base)}")
    
    while True: 
        try: 
            cantidad = int(input("Cantidad : "))
            if cantidad < 4 or cantidad > 6:
                print("ERROR") 
                print("-Valor invalido\n") 
            elif es_horizontal and cantidad + posicion_inicial[1] > 7 : 
                print("ERROR")
                print(f"Puede ingresar como maximo una mutacion de {7-posicion_inicial[1]} de {convertir_letra_a_palabra(base)}\n")
            
            elif not es_horizontal and cantidad + posicion_inicial[0] > 7:
                print("ERROR") 
                print(f"Puede ingresar como maximo una mutacion de {7-posicion_inicial[0]} de {convertir_letra_a_palabra(base)}\n")  
            else: 
                break
        except: 
            print("Ingrese un valor correcto(1/6)\n")
            
    return cantidad

#esta funcion es para crear y devolver la matriz de adn con su mutante horizontal inyectado        
def crear_mutacion_horizontal(adn,posicion_inicial,base,cantidad): 
    
    inicio = posicion_inicial[1] - 1
    fin = cantidad + inicio
    
    fila = list(adn[posicion_inicial[0]-1])
    fila[inicio:fin] = [base for i in range(0,cantidad)]
    fila = "".join(fila)
    adn[posicion_inicial[0]-1] = fila
            
    return adn

#esta funcion es para crear y devolver la matriz de adn con su mutante vertical inyectado       
def crear_mutacion_vertical(adn,posicion_inicial,base,cantidad): 
    fila_inicio = posicion_inicial[0]-1
    columna = posicion_inicial[1]-1
    
    for i in range(fila_inicio,cantidad+1): 
        fila_elegida = list(adn[i]) 
        fila_elegida[columna] = base
        fila_elegida = "".join(fila_elegida)
        adn[i] = fila_elegida
    return adn   
        
