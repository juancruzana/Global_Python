from clases import * 

def comprobar_contenido_fila(fila_ingresada): 
    lista_bases_nitrogenadas = ["a","t","c","g"]
    lista_errores_ingresados = [] 
    es_valido = True
    
    if len(fila_ingresada) == 6: 
        
        for base_nitrogenada in fila_ingresada:
            
            if base_nitrogenada not in lista_bases_nitrogenadas:
                
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
    
    for fila in range(0,5): 
        
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
                
         


print("""
  -----------------Analisis De ADN--------------------------
      
  1)_ Ingresar bases nitrogenadas del ADN:
      
  - La secuencia de ADN sera representada en una matriz 6x6.
  - El ADN de una célula cuenta con cuatro bases nitrogenadas: 
  - Adenina (A), Timina (T), Citosina (C) y Guanina (G).
  - Cada fila debe contener 6 Bases Nitrogenadas.
  - Se debe ingresar cada base nitrogenada fila por fila.
      
  - Ejemplo: 
     -Una fila se veria representada asi: ATCG.
  ----------------------------------------------------------
  Ingrese la secuencia de ADN
""")
      
adn_ingresado = ingresar_secuencia_adn()

for fila in adn_ingresado: 
    print(fila)