import time 
from clases import * 
from funciones_main import *


mostrar_pantalla_principal()
time.sleep(0.8)
input("Presione enter para ingresar ADN\n")
time.sleep(0.8)
mostrar_Instrucciones()


adn_ingresado = ingresar_secuencia_adn()

print("\n....ADN Ingresado....\n")
time.sleep(0.8)
id_ingresado = ingresar_id()

time.sleep(0.8)
mostrar_matriz(adn_ingresado, id_ingresado)

time.sleep(0.8)
pulsar_enter_para_continur()

while True:
    time.sleep(0.8)
    mostrar_menu()
    opcion = ingresar_opcion_menu()
    

    if opcion == 1:
        time.sleep(0.8)
        mostrar_matriz(adn_ingresado, id_ingresado)
        time.sleep(0.8)
        pulsar_enter_para_continur()

    elif opcion == 2:

        detector = Detector(adn_ingresado)
        se_detecto, mutaciones_totales = detector.detectar_mutante(adn_ingresado)

        if se_detecto:
            print(f"Se han detectado {mutaciones_totales} Mutaciones\n")
            time.sleep(0.8)

            print("Desea ver los análisis")
            time.sleep(0.8)
            
            print("1)_ SI ")
            print("2)_ NO ")
            
            opcion_ver_mutaciones = Ingresar_opcion_1_or_2()
            
            if opcion_ver_mutaciones == 1:
                print( 
f"""----------------------Análisis De Mutaciones ADN--------------------
-- id ADN: {id_ingresado}
-- Matriz : 6x6
-- Mutaciones Totales : {mutaciones_totales}           
""")
                time.sleep(0.8)
                detector.mostrar_total_mutaciones()
                print("\n")
        else:
            print("ADN Limpio\n")

    elif opcion == 3:
     
        base_nitrogenada = ingresar_base_nitrogenada()
        mutante = Mutador(adn_ingresado, base_nitrogenada)

        print(
"""
 TIPOS DE INYERCIONES DE MUTANTES 

1) _ RADIACIÓN
2) _ VIRUS

-Opciones(1/2)
""")
        time.sleep(0.8)

        mutacion_elegida = Ingresar_opcion_1_or_2()
        if mutacion_elegida == 1:
            time.sleep(0.8)
            print(
""" 
--------------INGRESE LA ORIENTACIÓN DE LA MUTACIÓN------------- 

- Al ser inyectado por radiación, las mutaciones pueden ser: 

- HORIZONTALES(h)
- VERTICALES(v)

-----------------------------------------------------------------'
""")
            time.sleep(0.8)

            orientacion = ingresar_orientacion_de_mutacion()
            comprobar_horizontal = orientacion == "h"

            time.sleep(0.8)

            print("----------------INGRESE LA POSICIÓN INICIAL---------------------")
            print("- X(Fila)")
            print("- Y(Columna)")
            print("----------------------------------------------------------------")
            posicion = ingresar_posicion_inicial(comprobar_horizontal)
            print("\n")
            time.sleep(0.8)

            print("----INGRESE CANTIDAD DE BASES NITROGENADAS A INYECTAR--------")
            cantidad_bases = ingresar_cantidad(posicion, comprobar_horizontal, base_nitrogenada)

            time.sleep(0.8)

            mutante_radiacion = Radiacion(adn_ingresado, base_nitrogenada)
            
            adn_mutado_radiacion = mutante_radiacion.crear_mutante(posicion, comprobar_horizontal, cantidad_bases)
            time.sleep(0.8)
            print("----- ADN INYECTADO CON RADIACIÓN -----\n")
            time.sleep(0.8)
            mostrar_matriz(adn_mutado_radiacion, id_ingresado)

        else:
            
            mutante_virus = Virus(adn_ingresado,base_nitrogenada)
            
            print(""" 
                --------------- Inyectar MUTANTE con VIRUS --------------------------------------- 
                
                -- El adn al ser inyectado con un virus.
                -- Se crea una Mutacion diagonal.
                -- La base inicial de la mutacion se va inyerctar en una posición Inicial. 
                
                -- Y va a seguir el orden Diagonal de una forma descendente hacia la : 
                - DERECHA o IZQUIERDA 
                
                DEBE INGRESAR : 
                . La horientación de la mutación (Si va a desceder hacia: DERECHA / IZQUIERDA )  
                . La posición Incial. 
                . Cantidad de bases Nitrogenadas a inyectar(Que magnitud va a tener el MUTANTE).
                
                ------------------------------------------------------------------------------------ """)
            print(" Ingrese La horientación(d/i) ")
            orientacion = ingresar_orientacion_virus()
            print("\n")
            
            if orientacion.lower() == "d":
                es_derecha = True 
            else : 
                es_derecha = False 
            
            print("Ingrese Posición Inicial")
            print("- x : FILA ")
            print("- Y : COLUMNA \n")
            
            posicion_inicial = ingresar_posicion_inicial_virus(es_derecha)
            
            print("\n")
        
            cantidad_bases = ingresar_cantidad_virus(posicion_inicial,es_derecha)
         
            adn_mutacion_diagonal = mutante_virus.crear_mutante(es_derecha,posicion_inicial,cantidad_bases)
        
            mostrar_matriz(adn_mutacion_diagonal,id_ingresado)
    elif opcion == 4: 
            print("--------------- SANAR MUTANTE -------------------")
            sanador = Sanador(adn_ingresado)
            matriz_sanada = sanador.sanar_mutantes()
            if matriz_sanada: 
                mostrar_matriz(matriz_sanada,id_ingresado)
            else: 
                print("ADN sin mutaciones...")
    else:
        
        break
    # Salir del bucle si la opción no corresponde a las anteriores


