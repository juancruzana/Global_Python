class Detector:
    def __init__(self, adn):
        self.adn = adn

    def detectar_mutantes(self):
        mensajes = []  # Almacena mensaje según forma de mutación
        if self.detector_horizontal():
            mensajes.append('Tienes una mutación horizontal.')
        if self.detector_vertical():
            mensajes.append('Tienes una mutación vertical.')
        if self.detector_diagonal():
            mensajes.append('Tienes una mutación diagonal.')    
        return mensajes != [], '\n'.join(mensajes) if mensajes else 'No hay mutaciones detectadas.'  
    
    def detector_vertical(self):
        posicion = [] # Donde se guarda la posición inicial y final de la mutación
        for col in range(6):
            contador = 1  # Cuenta de caracteres consecutivos
            for fila in range(1, 6): 
                # Compara el carácter actual con el anterior en la misma columna
                if self.adn[fila][col] == self.adn[fila - 1][col]:
                    contador += 1
                    # Si contador se incrementa se guardará las posición inicial y final de la mutación
                    if contador == 2: # Posición inicial
                        posicion.append([fila-1,col])
                    if contador == 4: # Posición final
                        posicion.append([fila,col])
                    # Si hay 4 consecutivos iguales, retorna True
                    if contador == 4:
                        return True, posicion
                else:
                    contador = 1  # Reinicia el contador si no son iguales
        # Si no encuentra secuencia de 4 consecutivos iguales en ninguna columna, retorna False
        return False
    
    def detector_horizontal(self):
        posicion = [] # Donde se guarda la posición inicial y final de la mutación
        for fila in range(6):
            contador = 1  # Cuenta de caracteres consecutivos
            for col in range(1, 6):
                if self.adn[fila][col] == self.adn[fila][col - 1]:  # Comparamos con el elemento anterior de la fila
                    contador += 1

                    if contador == 2:
                        posicion.append([fila,col - 1])
                    if contador == 4:
                        posicion.append([fila,col])

                    if contador == 4:  # Si hay 4 consecutivos iguales, retorna True
                        return True, posicion
                else:
                    contador = 1  # Reinicia el contador si no hay coincidencia
        # Si no encuentra secuencia de 4 consecutivos iguales en las filas, retorna False
        return False
    
    def detector_diagonal(self):
        # Dimensiones del adn
        filas = len(self.adn)
        columnas = len(self.adn[0])
        # Verificar diagonales de izquierda a derecha
        for i in range(filas - 3):
            for j in range(columnas - 3):
                if (self.adn[i][j] == self.adn[i+1][j+1] == self.adn[i+2][j+2] == self.adn[i+3][j+3]):
                    return True
        # Verificar diagonales de derecha a izquierda
        for i in range(filas - 3):
            for j in range(3, columnas):
                if (self.adn[i][j] == self.adn[i+1][j-1] == self.adn[i+2][j-2] == self.adn[i+3][j-3]):
                    return True
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
        if self.orientacion_de_la_mutacion == 'h': 
            self.adn[self.posicion_inicial] = (self.base_nitrogenada * 4) + (self.adn[self.posicion_inicial][4:]) # Agrega base nitrogenada en la posicion seleccionada
            return print(self.adn)
        if self.orientacion_de_la_mutacion == 'v':
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
            return [print(self.adn[x]) for x in range(len(self.adn))]
        else: # Mutar de derecha a izquierda
            for i in range(4):
                self.adn[fila] = self.adn[fila][:col] + self.base_nitrogenada + self.adn[fila][col+1:] # Agrega la mutación desde posición_inicial
                fila += 1
                col -= 1
            return [print(self.adn[x]) for x in range(len(self.adn))]


class Sanador(Detector): 
    def __init__(self, adn):
        super().__init__(adn)
    
    def sanar_mutantes(self): 
        pass