from paquetes.clases import *

no_mutacion = ["TGADCA", "GTTTCA", "CATCAT", "GAGATA", "ATTGCG", "CTGTTC"] # Sin mutación.

mutacion = Virus(no_mutacion,'*','d',[2,5],4)

mutacion.crear_mutante()
