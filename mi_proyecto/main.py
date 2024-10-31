#Clase Detector
class Detector:
    def __init__(self, matriz):
        self.matriz = matriz

    def detectar_mutantes(self):
            mensajes = []  

            if self.detector_horizontal():
                mensajes.append('Tienes una mutación horizontal.')
            if self.detector_vertial():
                mensajes.append('Tienes una mutación vertical.')
            if self.detector_diagonal():
                mensajes.append('Tienes una mutación diagonal.')
            
            return '\n'.join(mensajes) if mensajes else 'No hay mutaciones detectadas.'
        

    def detector_vertial(self):
        for col in range(6):
            contador = 1  # Cuenta de caracteres consecutivos
            for fila in range(1, 6): 
                # Compara el carácter actual con el anterior en la misma columna
                if self.matriz[fila][col] == self.matriz[fila - 1][col]:
                    contador += 1
                    # Si hay 4 consecutivos iguales, retorna True
                    if contador == 4:
                        return True
                else:
                    contador = 1  # Reinicia el contador si no son iguales
        # Si no encuentra secuencia de 4 consecutivos iguales en ninguna columna, retorna False
        return False
    

    def detector_horizontal(self):
        for fila in self.matriz:
            contador = 1  # Cuenta de caracteres consecutivos
            for i in range(1, len(fila)):
                if fila[i] == fila[i - 1]:  # Comparamos con el elemento anterior de la fila
                    contador += 1
                    if contador == 4:  # Si hay 4 consecutivos iguales, retorna True
                        return True
                else:
                    contador = 1  # Reinicia el contador si no hay coincidencia
        # Si no encuentra secuencia de 4 consecutivos iguales en las filas, retorna False
        return False
    

    def detector_diagonal(self):
        matriz = self.matriz
        
        # Dimensiones de la matriz
        filas = len(matriz)
        columnas = len(matriz[0])
        
        # Verificar diagonales de izquierda a derecha
        for i in range(filas - 3):
            for j in range(columnas - 3):
                if (matriz[i][j] == matriz[i+1][j+1] == matriz[i+2][j+2] == matriz[i+3][j+3]):
                    return True
        
        # Verificar diagonales de derecha a izquierda
        for i in range(filas - 3):
            for j in range(3, columnas):
                if (matriz[i][j] == matriz[i+1][j-1] == matriz[i+2][j-2] == matriz[i+3][j-3]):
                    return True
        return False
    
h_matriz = ["TTTTCA", "GATTCA", "CAACAT", "GAGCTA", "ATTGCG", "CTGTTC"]
v_matriz = ["AGATCA", "GATTCA", "CAATAT", "GAGTTA", "ATTGCG", "CTGTTC"]
d_matriz = ["TGATCA", "GTTTCA", "CATCAT", "GAGTTA", "ATTGCG", "CTGTTC"]
matriz = ["TTTTCA", "TTTTCA", "TATCAT", "TAGTTA", "ATTGCG", "CTGTTC"]

horizontal = Detector(h_matriz)
vertical = Detector(v_matriz)
diagonal = Detector(d_matriz)
matriz = Detector(matriz)

resultado = diagonal.detectar_mutantes()
print(resultado)