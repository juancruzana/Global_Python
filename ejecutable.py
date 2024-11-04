from paquetes.clases import Detector

# *Matrices de prueba*
h_mutacion = ["TTTTCA", "GATTCA", "CAACAT", "GAGCTA", "ATTGCG", "CTGTTC"] # Mutación horizontal
v_mutacion = ["AGATCA", "GATTCA", "CAATAT", "GAGTTA", "ATTGCG", "CTGTTC"] # Mutación vertical
d_mutacion = ["TGATCA", "GTTTCA", "CATCAT", "GAGTTA", "ATTGCG", "CTGTTC"] # Mutación diagonal
sup_mutacion = ["TTTTCA", "TTTTCA", "TATCAT", "TAGTTA", "ATTGCG", "CTGTTC"] # Mutacion en posiciones horizontal, vertical y diagonal
no_mutacion = ["TGADCA", "GTTTCA", "CATCAT", "GAGATA", "ATTGCG", "CTGTTC"] # Mutación diagonal

# Objetos
horizontal = Detector(h_mutacion) 
vertical = Detector(v_mutacion) 
diagonal = Detector(d_mutacion) 
sup_mutacion = Detector(sup_mutacion) 
mutacion_nula = Detector(no_mutacion) 

resultado = sup_mutacion.detectar_mutantes()
print(resultado)