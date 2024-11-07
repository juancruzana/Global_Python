
from funciones_clase_detector import *
import random

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
    
def ingresar_base_nitrogenada():
    
    lista_bases = ["a","t","g","c"]
    
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
    
def conseguir_y(horizontal): 
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

def conseguir_x(horizontal):
    
    while True: 
        posicion_x = int(input("Posicion X: ")) 
        if posicion_x >= 1 and posicion_x <= 6: 
            if not horizontal: 
                if posicion_x <= 2: 
                    break
                else: 
                    print("ERROR")
                    print("-Posicion inválida para crear mutante Vertical\n")
            else: 
                break
        else: 
            print("ERROR")
            print("- Posicion Inválida.\n")
        
    return posicion_x
             
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
            
    return (posicion_x,posicion_y)
            

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
        
def crear_mutacion_horizontal(posicion_inicial,adn,base,cantidad): 
    
    inicio = posicion_inicial[1] - 1
    fin = cantidad + inicio
    
    fila = list(adn[posicion_inicial[0]-1])
    fila[inicio:fin] = [base for i in range(0,cantidad)]
    fila = "".join(fila)
    adn[posicion_inicial[0]-1] = fila
            
    return adn

     
def crear_mutacion_vertical(posicion_inicial,adn,base,cantidad): 
    fila_inicio = posicion_inicial[0]-1
    columna = posicion_inicial[1]-1
    
    for i in range(fila_inicio,cantidad+1): 
        fila_elegida = list(adn[i]) 
        fila_elegida[columna] = base
        fila_elegida = "".join(fila_elegida)
        adn[i] = fila_elegida
    return adn   
        
adn_ingresado = ["aaaaaa","aaaaaa","aaaaaa","aaaaaa","aaaaaa","aaaaaa"]

orientacion = ingresar_orientacion_de_mutacion()
base = ingresar_base_nitrogenada()
if orientacion.lower() == "h": 
    es_horizontal = True
else :
    es_horizontal = False 

posicion=   ingresar_posicion_inicial(es_horizontal)

cantidad = ingresar_cantidad(posicion,es_horizontal,base)


if es_horizontal: 
    adn_mutado = crear_mutacion_horizontal(posicion,adn_ingresado,base,cantidad)
else: 
    adn_mutado = crear_mutacion_vertical(posicion,adn_ingresado,base,cantidad)
    
    
for i in adn_mutado: 
    print(i)