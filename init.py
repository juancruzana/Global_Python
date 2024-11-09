import time 
from clases import * 
from funciones_main import *

 
def pulsar_enter_para_continur(): 
    input("Pulsa ENTER para ir al menu De Opciones\n") 
            
    
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
mostrar_matriz(adn_ingresado,id_ingresado)

time.sleep(0.8)
pulsar_enter_para_continur()

time.sleep(0.8)
mostrar_menu() 
opcion = ingresar_opcion_menu() 

if opcion == 1 :
    
    time.sleep(0.8)
    mostrar_matriz(adn_ingresado,id_ingresado)
    time.sleep(0.8)
    pulsar_enter_para_continur()
    
elif opcion == 2: 
    longitud_mutante = 4
    
    detector = Detector(adn_ingresado,longitud_mutante)
    se_detecto,mutaciones_totales = detector.detectar_mutante()
    
    if se_detecto:
        print(f"Se han detectado {mutaciones_totales} Mutaciones\n") 
        time.sleep(0.8)
        
        print("Desea ver los analisis")
        time.sleep(0.8)
        print("1)_ SI ")
        print("2)_ NO ")
        opcion_ver_mutaciones = Ingresar_opcion_1_or_2()
        if opcion_ver_mutaciones == 1 : 
            print(f""" 
        ----------------------Analisis De Mutacines ADN--------------------
        -- id ADN: {id_ingresado}
        -- Matriz : 6x6
        -- Mutaciones Totales : {mutaciones_totales}           
        """)
            time.sleep(0.8)
            detector.mostrar_total_mutaciones()
            print("\n")
        else: 
            pass
        
    else : 
        print("ADN Limpio\n")
    
    
elif opcion == 3 : 
    
    base_nitrogenada = ingresar_base_nitrogenada()
    mutante = Mutador(adn_ingresado,base_nitrogenada)
    
    print(" TIPOS DE INSERCIONES DE MUTANTES " )
    print("""
          1) _ RADIACIÓN
          2) _ VIRUS
          
          -Opciones(1/2)
        """)
    time.sleep(0.8)
    
    mutacio_elegida = Ingresar_opcion_1_or_2() 
    if mutacio_elegida == 1 :
        time.sleep(0.8)
        print(
    """ 
    --------------INGRESE LA ORIENTACIÓN DE LA MUTACIÓN------------- 
    
    - Al ser inyectado por radiaón las mutaciones puden ser: 
    
    - HORIZONTALES(h)
    - VERTICALES(v)
    
    ----------------------------------------------------------------
    """)
        time.sleep(0.8)
       
        orientacion = ingresar_orientacion_de_mutacion()
        if orientacion == "h": 
            comprobar_horizontal = True
        else: 
            comprobar_horizontal = False
        
        time.sleep(0.8)
        
        print("----------------INGRESE LA POSICIÓN INICIAL---------------------")
        print("- X(Fila)")
        print("- Y(Columna)")
        print("----------------------------------------------------------------")
        posicion = ingresar_posicion_inicial(comprobar_horizontal)
        print("\n")
        time.sleep(0.8)
        
        print("----INGRESE CANTIDAD DE BASES NITROGENTADAS A INYECTAR--------")
        cantidad_bases = ingresar_cantidad(posicion,comprobar_horizontal,base_nitrogenada)
        
        time.sleep(0.8)
        
        mutante_radiacion = Radiacion(adn_ingresado,base_nitrogenada)
        
        adn_mutado_radiacion= mutante_radiacion.crear_mutante(posicion,comprobar_horizontal,cantidad_bases)
        time.sleep(0.8)
        print(" ADN INYECTADO CON RADIACION ")
        time.sleep(0.8)
        mostrar_matriz(adn_mutado_radiacion,id_ingresado)
    

else: 
    
    pass



