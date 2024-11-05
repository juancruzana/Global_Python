from paquetes.clases import *

# *Matrices de prueba*.
h_mutacion = ["TTTTCA", "GATTCA", "CAACAT", "GAGCTA", "ATTGCG", "CTGTTC"] # Mutación horizontal.
v_mutacion = ["AGATCA", "GATTCA", "CAATAT", "GAGTTA", "ATTGCG", "CTGTTC"] # Mutación vertical.
d_mutacion = ["TGATCA", "GTTTCA", "CATCAT", "GAGTTA", "ATTGCG", "CTGTTC"] # Mutación diagonal.
sup_mutacion = ["TTTTCA", "TTTTCA", "TATCAT", "TAGTTA", "ATTGCG", "CTGTTC"] # Mutacion en posiciones horizontal, vertical y diagonal.
no_mutacion = ["TGADCA", "GTTTCA", "CATCAT", "GAGATA", "ATTGCG", "CTGTTC"] # Sin mutación.

# Objetos para detectar
horizontal = Detector(h_mutacion) 
vertical = Detector(v_mutacion) 
diagonal = Detector(d_mutacion) 
super_mutacion = Detector(sup_mutacion) 
adn_sano = Detector(no_mutacion) 

# Objetos para mutar
adn_para_mutar = Mutador(no_mutacion,'A','v',5,4) 

#Clase Viruz
mutacion = Radiacion(no_mutacion,'5','h',5,4)

mutacion.crear_mutante()