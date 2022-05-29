from queue import Queue #Importamos la libreria Queue
#Implementa colas multiproductor y multiconsumo

"""
Autor: Borja Vinicio
Para iniciar con la generación de los métodos de busqueda se uso librerias 
En python los metodos de busqueda se puede asociar con la teoria de Grafos.
Esta programa es un buen punto de partida si desea profundizar en la implementación de algoritmos relacionados con grafos.

"""

class Grafo:
    """
    Una clase que representa un Grafo

    ...
    Atributos
    ---------------------
    numero_de_nodos : int
        cantidad de nodos del grafo
    dirigido: boolean
        especifica si es dirigido o no
    m_nodes: int 
        almacena la secuencia de números 
    m_adjutando_lista: estructura de un  diccionario {}
        implementa una lista de adyacencia
    ---------------------

    Métodos
    -------
    agregando_borde(self, node1, node2, peso=1):
        Agrega un nuevo grafo
    imprimiendo_lista_adjuntada(self):
         Recorre el diccionario y muestra los datos tanto la llave como el valor 
    bfs_traversal(self, nodo_inicio):
        Imprimir recorrido BFS
    """
    def __init__(self, numero_de_nodos, dirigido=True):#Consstructor con sus parametros


        self.m_numero_de_nodos = numero_de_nodos#Inicializamos variable m_numero_de_nodos
        self.m_nodes = range(self.m_numero_de_nodos)#Inicializamos variable m_nodes 
        self.m_dirigido = dirigido#Inicializamos variable m_dirigido
		
        self.m_adjutando_lista = {node: set() for node in self.m_nodes}# creamos la estructura de un diccionario de datos   
	
    # Add edge to the Grafo
    def agregando_borde(self, node1, node2, peso=1):#agregamos los parametros en la función agregando_borde

        self.m_adjutando_lista[node1].add((node2, peso))#Agregamos nodo y peso

        if not self.m_dirigido:
            self.m_adjutando_lista[node2].add((node1, peso))#Nodo y peso agregado


    def imprimiendo_lista_adjuntada(self):

        for llave in self.m_adjutando_lista.keys():#Realizamos recorrido
            print("nodo", llave, ": ", self.m_adjutando_lista[llave])#Se imprmir el recorrido junto la llave y el valor


    def bfs_traversal(self, nodo_inicio):


        # Conjunto de nodos visitado para no ocasionar bucles
        #Creamos un objeto set
        visto = set()
        #El módulo para implementar colas
        queue = Queue()

        
        # Añadiendo nodo inicio a la cola
        queue.put(nodo_inicio)
        # Añadiendo nodo inicio a la cola
        visto.add(nodo_inicio)

            #Recorrido bucle while 
        while not queue.empty():
            #Desencolando un vértice
            current_node = queue.get()
            #Hacer cola e imprimirlo
            print(current_node, end = " ")


            for (next_node, peso) in self.m_adjutando_lista[current_node]: 
                """Obtenemos todos los vértices adyacentes"""
                    #no ha sido visto, entonces agregar
                if next_node not in visto:
                    #vértice desencolado
                    queue.put(next_node)
                    #Si no ha sido visto lo agregamos 
                    visto.add(next_node)


if __name__ == "__main__":
    #### Programa principal #####


    g = Grafo(5, dirigido=False)#Creamos una instancia de la clase Grafo con 5 nodos

    # Agregamos arista al grafo con peso por defecto en 1
    #primer arista 
    g.agregando_borde(0, 1)
    #segunda arista 
    g.agregando_borde(0, 2)
    #tercera arista 
    g.agregando_borde(1, 2)
    #cuarta arista 
    g.agregando_borde(1, 4)
    #Quinta arista 
    g.agregando_borde(2, 3)


    # Imprmiendo la lista adyadencia con el formato nodo n: {(node, peso)}
    g.imprimiendo_lista_adjuntada()

    print ("A continuación se muestra el recorrido primero en amplitud"
                    " (comenzando desde el vértice 0)")
    g.bfs_traversal(0)
    print()