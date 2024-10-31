from paquetes.detector import Detector

h_matriz = ["TTTTCA", "GATTCA", "CAACAT", "GAGCTA", "ATTGCG", "CTGTTC"]
v_matriz = ["AGATCA", "GATTCA", "CAATAT", "GAGTTA", "ATTGCG", "CTGTTC"]
d_matriz = ["TGATCA", "GTTTCA", "CATCAT", "GAGTTA", "ATTGCG", "CTGTTC"]
matriz = ["TTTTCA", "TTTTCA", "TATCAT", "TAGTTA", "ATTGCG", "CTGTTC"]

horizontal = Detector(h_matriz)
vertical = Detector(v_matriz)
diagonal = Detector(d_matriz)

matriz = Detector(matriz)

resultado = matriz.detectar_mutantes()
print(resultado)