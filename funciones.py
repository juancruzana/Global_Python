
#Funcion que muestra la lista de adn como una matriz en pantalla 
def mostrar_matriz(lista_adn): 
    
    #Matriz rellena con números para luego remplazar los valores
    vector_inicial = """[0|1|2|3|4|5]"""
   
    #ciclo de bucles que itera sobre toda la lista ADN para repmplazar el valor 
    #de vector inicial por la base nitrogenada iterada
    
    for fila in lista_adn: 
        
        fila_modificada = vector_inicial
       
        for contador,caracter in enumerate(fila): 
            fila_modificada = fila_modificada.replace(str(contador),caracter)
        print (fila_modificada)

    
    
    
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
        print("""
              - ERROR :
              - Se deben Ingresar 6 Bases Nitrogenadas por fila.
              """)
        return False
    
    if es_valido == False:
        lista_errores_ingresados = '-'.join(lista_errores_ingresados) 
        print(f"""
              - ERROR: ({lista_errores_ingresados}) 
              - bases nitrogenadas Permitidas: 
              - Adenina (A), Timina (T), Citosina (C) y Guanina (G).
              """)
        return False
    else: return True
    
     
def ingresar_secuencia_adn(): 
    
    lista_secuencia_adn = [] 
    
    for fila in range(0,6): 
        
        while True: 
            try: 
                
                contenido_fila = input(f" - Fila {fila+1}: ")     
                    
                if comprobar_contenido_fila(contenido_fila):
                        
                    lista_secuencia_adn.append(contenido_fila)
                        
                    break
                    
            except: 
                print(" - ERROR: ")
                print(" - Valores Permiridos(A,T,C,G)")
                print(" - Cada fila debe contener una secuencia de 6 bases Nitrogeneda")
    
    return lista_secuencia_adn
                
         