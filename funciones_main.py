
#Funcion que muestra la lista de adn como una matriz en pantalla 
def mostrar_matriz(lista_adn,id): 
    
    print("- ADN : Matriz 6x6")
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

    
def ingresar_id(): 
  print("- Ingrese Id de ADN")
  while True: 
    try: 
      id = int(input("ID: "))
      return id
    except: 
      print("Id invávlido \n")

    
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
            print("Secuencia ADN: ") 
            for i in lista_secuencia_adn: 
                print(f"   {i}")
        
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
                

