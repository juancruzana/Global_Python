import random

class Detector:
    def __init__(self, adn):
        self.adn = adn

    def detectar_mutante(self):
        mensajes = []  # Almacena mensaje según forma de mutación
        if self.detector_horizontal():
            mensajes.append('Tienes una mutación horizontal.')
        if self.detector_vertical():
            mensajes.append('Tienes una mutación vertical.')
        if self.detector_diagonal():
            mensajes.append('Tienes una mutación diagonal.')    
        return mensajes != [], '\n'.join(mensajes) if mensajes else 'No hay mutaciones detectadas.'  
    
    def detector_vertical(self):
        secuencias = []  # Para almacenar todas las secuencias detectadas
        for col in range(len(self.adn[0])):  # Iterar por columnas
            posicion_inicial = None
            contador = 1  # Contador de coincidencias consecutivas

            for fila in range(1, len(self.adn)):  # Iterar por filas
                # Comparar el carácter actual con el anterior en la misma columna
                if self.adn[fila][col] == self.adn[fila - 1][col]:
                    contador += 1

                    if contador == 2:  # Registrar posición inicial en la segunda coincidencia
                        posicion_inicial = [fila - 1, col]

                    if contador == 4:  # Detectar secuencia de 4
                        posicion_final = [fila, col]
                        secuencias.append([posicion_inicial, posicion_final])
                else:
                    contador = 1  # Reiniciar el contador si no coinciden

        # Retornar si se encontraron secuencias y la lista de secuencias
        return bool(secuencias), secuencias
    
    def detector_horizontal(self):
        posicion = [] # Donde se guarda la posición inicial y final de la mutación
        for fila in range(6):
            contador = 1  # Cuenta de caracteres consecutivos
            for col in range(1, 6):
                if self.adn[fila][col] == self.adn[fila][col - 1]:  # Comparamos con el elemento anterior de la fila
                    contador += 1

                    # Si contador se incrementa se guardará las posición inicial y final de la mutación
                    if contador == 2:
                        posicion.append([fila,col - 1])
                    if contador == 4:
                        posicion.append([fila,col])
                        
                    # Si hay 4 consecutivos iguales, retorna True
                    if contador == 4:  # Si hay 4 consecutivos iguales, retorna True
                        return True, posicion
                else:
                    contador = 1  # Reinicia el contador si no hay coincidencia
        # Si no encuentra secuencia de 4 consecutivos iguales en las filas, retorna False
        return False
    
    def detector_diagonal(self):
        posicion = [] # Donde se guarda la posición inicial y final de la mutación

        # Dimensiones del adn
        filas = len(self.adn)
        columnas = len(self.adn[0])

        # Verificar diagonales de izquierda a derecha
        for i in range(filas - 3):
            for j in range(columnas - 3):
                if (self.adn[i][j] == self.adn[i+1][j+1] == self.adn[i+2][j+2] == self.adn[i+3][j+3]):
                    posicion.extend([[i,j],[i+3,j+3]])
                    return True, posicion
                
        # Verificar diagonales de derecha a izquierda
        for i in range(filas - 3):
            for j in range(3, columnas):
                if (self.adn[i][j] == self.adn[i+1][j-1] == self.adn[i+2][j-2] == self.adn[i+3][j-3]):
                    posicion.extend([[i,j],[i+3,j-3]])
                    return True, posicion
        return False

   
class Mutador(): 
    def __init__(self, adn, base_nitrogenada, posicion_inicial):
        self.adn = adn
        self.base_nitrogenada = base_nitrogenada.upper() # De que tipo de base nitrogenada será la mutación
        self.posicion_inicial = posicion_inicial # Posición de la mutación en el adn

    def crear_mutante(self): 
        pass


class Radiacion(Mutador):  
    def __init__(self, adn, base_nitrogenada, posicion_inicial, orientacion_de_la_mutacion):
        super().__init__(adn, base_nitrogenada, posicion_inicial) 
        self.orientacion_de_la_mutacion = orientacion_de_la_mutacion.lower() # Forma en la q se mutará v,(vertica), h(horizontal), d (diagonal)

    def crear_mutante(self): 
        if self.orientacion_de_la_mutacion == 'h': # Mutación horizontal 
            self.adn[self.posicion_inicial] = (self.base_nitrogenada * 4) + (self.adn[self.posicion_inicial][4:]) # Agrega base nitrogenada en la posicion seleccionada
            return print(self.adn)
        
        if self.orientacion_de_la_mutacion == 'v': # Mutación vertical
            for x in range(4):
                self.adn[x] = self.adn[x][:self.posicion_inicial] + self.base_nitrogenada + self.adn[x][self.posicion_inicial+1:] # Replaza fila por fila en la columna seleccionada
            return print(self.adn)


class Virus(Mutador):
    def __init__(self, adn, base_nitrogenada, posicion_inicial):
        super().__init__(adn, base_nitrogenada, posicion_inicial)
    
    def crear_mutante(self):
        fila = self.posicion_inicial[0]
        col = self.posicion_inicial[1]
        if self.posicion_inicial[1] < 3: # Mutar de izquierda a derecha
            for i in range(4):
                self.adn[fila] = self.adn[fila][:col] + self.base_nitrogenada + self.adn[fila][col+1:] # Agrega la mutación desde posición_inicial
                fila += 1
                col += 1
            return [print(self.adn[x]) for x in range(len(self.adn))] # Imprime por pantalla adn mutado
        else: # Mutar de derecha a izquierda
            for i in range(4):
                self.adn[fila] = self.adn[fila][:col] + self.base_nitrogenada + self.adn[fila][col+1:] # Agrega la mutación desde posición_inicial
                fila += 1
                col -= 1
            return [print(self.adn[x]) for x in range(len(self.adn))] # Imprime por pantalla adn mutado


class Sanador: 
    def __init__(self, adn):
        self.adn = adn
        self.detector = Detector(adn)  # Creamos una instancia de Detector
        self.bases_nitrogenadas = ['T', 'A', 'G', 'C'] # Bases nitrogenadas posibles
    
    def sanar_mutantes(self): 
        objeto = self.detector  # Usamos la instancia para llamar a detectar_mutante
        
        if objeto.detector_horizontal():
            print('TODAVIA NO FUNCIONA')
            pass

        if objeto.detector_vertical():
            self.adn = [list(row) for row in self.adn]  # Convertir cada fila a una lista para permitir modificaciones
            _, secuencias = objeto.detector_vertical()  # Detectar secuencias
            for inicio, fin in secuencias:
                # Reemplazar en la matriz de ADN desde la posición inicial a la final
                for fila in range(inicio[0], fin[0] + 1):
                    self.adn[fila][inicio[1]] = random.choice(self.bases_nitrogenadas)
            return [''.join(fila) for fila in self.adn]

        if objeto.detector_diagonal(): 
            fila = objeto.detector_diagonal()[1][0][0]
            col = objeto.detector_diagonal()[1][0][1]

            if col < 3:
                # Sanar de izquierda a derecha
                for i in range(4): 
                    self.adn[fila] = self.adn[fila][:col] + random.choice(self.bases_nitrogenadas) + self.adn[fila][col+1:] # Agrega la mutación desde posición_inicial
                    # self.adn[fila] = self.adn[fila][:col] + '5' + self.adn[fila][col+1:] # Agrega la mutación desde posición_inicial
                    fila += 1
                    col += 1
            else:
                # Sanar de derecha a izquierda
                for i in range(4): 
                    # self.adn[fila] = self.adn[fila][:col] + '5' + self.adn[fila][col+1:] # Agrega la mutación desde posición_inicial
                    self.adn[fila] = self.adn[fila][:col] + random.choice(self.bases_nitrogenadas) + self.adn[fila][col+1:] # Agrega la mutación desde posición_inicial
                    fila += 1
                    col -= 1
            [print(self.adn[x]) for x in range(len(self.adn))]
            
        
        
   