from paquetes.clases import *

no_mutacion = ["TGADCA", "GTTTCA", "CATCAT", "GAGATA", "ATTGCG", "CTGTTC"] # Sin mutación.

#Clase Viruz
mutacion = Virus(no_mutacion,'*','d',[2,2],4)

mutacion.crear_mutante()
