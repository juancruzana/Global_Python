
#Funcion que muestra la lista de adn como una matriz en pantalla 
def mostrar_matriz(lista_adn): 
    
    #Matriz rellena con números para luego remplazar los valores
    vector_inicial = """[0|1|2|3|4|5]"""
   
    #ciclo de bucles que itera sobre toda la lista ADN para repmplazar el valor 
    #de vector inicial por la base nitrogenada iterada
    
    for fila in lista_adn: 
        
        fila_modificada = vector_inicial
       
        for contador,caracter in enumerate(fila): 
            fila_modificada = fila_modificada.replace(str(contador),caracter)
        print (fila_modificada)


matriz = ["ATTCGG","GGGACT","CTTTII","CTTTII","CTTTII","CTTTII"]
mostrar_matriz(matriz)