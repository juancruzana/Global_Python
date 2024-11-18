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

#Funciones para ingresar datos, CLASE MUTADOR/ VIRUS}

def ingresar_cantidad_virus(posicion,diagonal_derecha):

    posicion_x,posicion_y = posicion

    posicion_x -=1
    posicion_y -=1

    if diagonal_derecha :

        limite_x =  6 - posicion_x
        limite_y = 6 - posicion_y
    else:
        limite_x = 6 - posicion_x
        limite_y = posicion_y + 1

    if diagonal_derecha:
        while True:

            try:
                cantidad = int(input("Cantidad: "))

                if cantidad > limite_x  or cantidad > limite_y :
                    print(f"Ingrese cantidad válida, puede ingresar { 6- posicion_x } bases nitrogenadas\n")
                else :
                    break
            except ValueError:
                print("ERROR")
                print("- Ingrese un valor válido.\n")
    else:

        while True:

            try:
                cantidad = int(input("Cantidad: "))

                if cantidad >  limite_x   or cantidad > limite_y :
                    print(f"Ingrese cantidad válida, puede ingresar { posicion_y + 1}")
                else :
                    break
            except ValueError:
                print("ERROR")
                print("- Ingrese un valor válido.")


    return cantidad

def ingresar_posicion_inicial_virus(es_derecha):
    
    while True:
        try:
            posicion_x = int(input("Posición x: "))
            if posicion_x > 3 :
                print("ERROR")
                print("- Posición X Inválida, para crear mutante.\n ")
            else:
                break
        except ValueError:
                print("ERROR")
                print("- Valor Inválido.\n ")

    while True:
        try:
            posicion_y = int(input("Posición y: "))
            if es_derecha and (posicion_y < 1 or posicion_y > 3) :
                print("ERROR")
                print("- Posición Y Inválida, para crear mutante Diagonal//descendente//Derecha..\n ")
            elif not es_derecha and (posicion_y < 4 or posicion_y > 6) :
                print("ERROR")
                print("- Posición Inválida, para crear mutante Diagonal//descendente//Izquierda.\n ")
            else :
                break
        except ValueError :
                print("ERROR")
                print("- Valor Inválido.\n ")

    return (posicion_x,posicion_y)


def ingresar_orientacion_virus(): 
  while True: 
      try: 
        orientacion = input("Horientación: ")
        if orientacion.lower() == "d" or orientacion.lower() == "i": 
          break
        else: 
          print("ERROR")
          print(" -- Ingrese una Orientacion valida para la mutación ")
          print(" -- DERECHA : 'D' ")
          print(" -- IZQUERDA : 'I' \n")
      except ValueError: 
        print("ERROR ")
        print("-- Ingrese una orioentación válida ")
        print(" -- DERECHA : 'D' ")
        print(" -- IZQUERDA : 'I' \n")
  return orientacion


#----------------------------------------------------------------
#CLASE MUTADOR/ RADIACION
#----------------------------------------------------------------

def conseguir_y(horizontal): 
    #mientras no se ingrese una posicion valida el bucle se repetira
    print(f"Rango válido para y: 1-3" ) if horizontal else print("Rango válido Para y: 1-6 ")
    while True: 
        posicion_y = int(input("Posicion y: ")) 
        if posicion_y >= 1 and posicion_y <= 6: 
            if horizontal: 
                if posicion_y <= 3: 
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
    
    print(f"Rango válido para x: 1-6" ) if horizontal else print("Rango válido Para y: 1-3 ")

    while True: 
        try: 
            posicion_x = int(input("Posicion X: ")) 
            if posicion_x >= 1 and posicion_x <= 6: 
                if horizontal: 
                    break
                else: 
                    if posicion_x <= 3: 
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
    
    posicion_x = posicion_inicial[0]
    posicion_y = posicion_inicial[1]
    
    posicion_x -= 1 
    posicion_y -= 1 
    
    if es_horizontal : 
        print(f"Puede ingresar como maximo una mutacion de {6-posicion_y} de {convertir_letra_a_palabra(base)}")
    else: 
        print(f"Puede ingresar como maximo una mutacion de {6-posicion_x} de {convertir_letra_a_palabra(base)}")
    
    while True: 
        try: 
            cantidad = int(input("Cantidad : "))
            if  cantidad < 4 or cantidad > 6:
                
                print("ERROR") 
                print("-Valor invalido\n")
                 
            elif es_horizontal and cantidad + posicion_y > 6 : 
                print("ERROR")
                print(f"Puede ingresar como maximo una mutacion de {6-posicion_y} de {convertir_letra_a_palabra(base)}\n")
            
            elif not es_horizontal and cantidad + posicion_x > 6:
                print("ERROR") 
                print(f"Puede ingresar como maximo una mutacion de {6-posicion_x} de {convertir_letra_a_palabra(base)}\n")  
            else: 
                break
        except: 
            print("Ingrese un valor correcto(1/6)\n")
            
    return cantidad


#CLASE MUTADOR 
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

#funcion que retorna la poscicion de y(columna), elegida por el usuario   
 
    
    if es_horizontal : 
        print(f"Puede ingresar como maximo una mutacion  {7-posicion_inicial[1]} de {convertir_letra_a_palabra(base)}")
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

 
    fila_inicio = posicion_inicial[0]-1
    columna = posicion_inicial[1]-1
    
    for i in range(fila_inicio,cantidad+1): 
        fila_elegida = list(adn[i]) 
        fila_elegida[columna] = base
        fila_elegida = "".join(fila_elegida)
        adn[i] = fila_elegida
    return adn



#CLASE DETECTOR 

def Ingresar_opcion_1_or_2(): 

    
    while True: 
        
        try : 
            opcion = int(input("Opcion : "))
            if opcion == 1 or opcion == 2:  
                break
            else: 
                print("Ingrese una Opción correcta(1/2). \n")
        except: 
            print("Valor Invalido.")
            print("Porfavor Ingrese una opción correcta.(1/2)\n")
            
    return opcion      


def ingresar_opcion_menu(): 
  while True: 
    try: 
      opcion = int(input("Opcion: "))
      if opcion < 1 or opcion > 4: 
        print("Ingrese numero en el rango válido (1/4)")
      else : 
        return opcion
    except: 
      print("ERROR")
      print("- Debe ingresar un número dentro del rango válido. ")


#Funcion que muestra la lista de adn como una matriz en pantalla 
def mostrar_matriz(lista_adn,id): 
    
    print("- ADN : Matriz 6x6 ")
    print(f"- ID : {id} ") 
    
    #Matriz rellena con números para luego remplazar los valores
    vector_inicial = """[0|1|2|3|4|5]"""
   
    #ciclo de bucles que itera sobre toda la lista ADN para repmplazar el valor 
    #de vector inicial por la base nitrogenada iterada
    
    for fila in lista_adn: 
        
        fila_modificada = vector_inicial
       
        for contador,caracter in enumerate(fila): 
            fila_modificada = fila_modificada.replace(str(contador),caracter.capitalize())
        print (f"  {fila_modificada}  ")
    print("\n")



#FuNCIONES PROPIAS MENU PRINCIPAL 

#Funcion para mostrar matriz     
def ingresar_id(): 
  print("- Ingrese Id de ADN")
  while True: 
    try: 
      id = int(input("ID: "))
      return id
    except: 
      print("Id invávlido \n")

#comprueba, la filaa que sele va pasando     
def comprobar_contenido_fila(fila_ingresada): 
    
    lista_bases_nitrogenadas = ["a","t","c","g"]
    lista_errores_ingresados = [] 
    es_valido = True
    
    if len(fila_ingresada) == 6: 
        
        for base_nitrogenada in fila_ingresada:
            
            if base_nitrogenada.lower() not in lista_bases_nitrogenadas:
                
                es_valido = False
                lista_errores_ingresados.append(base_nitrogenada)
    
    else: 
        print("- ERROR :")
        print("- Se deben Ingresar 6 Bases Nitrogenadas por fila.\n")
        return False
    
    if es_valido == False:
        lista_errores_ingresados = '-'.join(lista_errores_ingresados) 
        print(f"- ERROR: ({lista_errores_ingresados}") 
        print("- bases nitrogenadas Permitidas: ")
        print("- Adenina (A), Timina (T), Citosina (C) y Guanina (G).\n")
        return False
    else: return True
    
     
def ingresar_secuencia_adn(): 
    
    lista_secuencia_adn = [] 
    print("-Valores Permitidos(A,T,C,G)\n")
    for fila in range(0,6):
        
        if lista_secuencia_adn:
            print("\n-----------------")
            print("Secuencia ADN: ") 
            for i in lista_secuencia_adn: 
                print(f"   {i}")
            print("-----------------\n")
          
        
        while True: 
            try: 
                
                contenido_fila = input(f" - Fila {fila+1}: \n")     
                    
                if comprobar_contenido_fila(contenido_fila):
                        
                    lista_secuencia_adn.append(contenido_fila)    
                    break
                    
            except: 
                print("-ERROR: ")
                print("-Valores Permiridos(A,T,C,G)")
                print("-Cada fila debe contener una secuencia de 6 bases Nitrogeneda\n")
                
    return lista_secuencia_adn


def mostrar_menu():
  print(""" 
        ---------------- MANIPULADOR DE ADN --------------------

          opciones : 
          ----------------------------
            1 ) _ Ver Matriz De ADN : 
            2 ) _ Detectar Mutación.
            3 ) _ Crear Mutación.
            4 ) _ Sanar ADN. 
      
        --------------------------------------------------------
        """)  

  
def mostrar_pantalla_principal():      
  print("""
      -----------------ANÁLISIS DE ADN-------------------------
      
      -- Manipulador de ADN. ---
      --------------------------
      1)_ Ingresar ADN.
      2) _ Ingresar ID de ADN. 
      
      ---OPCIONES----------------------------------------------
      Detectar Mutante
        .Detectar Base Nitrogenada mutadora.
        .Detectar orientación de mutante.
      -------------------------------------------
      Crear mutante: 
        .Radiación
        .Virus
      ------------------------------------------- 
      Sanar Mutante.
      ---------------------------------------------------------
      """)

def mostrar_Instrucciones(): 
  print("""\n
  -----------------COMO INGRESAR EL ADN-----------------------
      
  1)_ Ingresar bases nitrogenadas del ADN:
      
  - La secuencia de ADN sera representada en una matriz 6x6.
  - El ADN de una célula cuenta con cuatro bases nitrogenadas: 
  - Adenina (A), Timina (T), Citosina (C) y Guanina (G).
  - Cada fila debe contener 6 Bases Nitrogenadas.
  - Se debe ingresar cada base nitrogenada fila por fila.
      
  _ Ejemplo: 
     -Una fila se veria representada asi: ATCG.
  ------------------------------------------------------------
  Ingrese la secuencia de ADN

""")
                

 
def pulsar_enter_para_continur(): 
    input("Pulsa ENTER para ir al menu De Opciones\n") 