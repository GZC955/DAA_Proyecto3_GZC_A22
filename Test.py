from Random_Graphs import *
import random

def run():

    '''
    g = Graph(False,False,"Test_DAA_Rene")
    g.addEdge('0 -> 1', '0', '1', 2)
    g.addEdge('1 -> 0', '1', '0', 2)
    g.addEdge('0 -> 5', '0', '5', 3)
    g.addEdge('5 -> 0', '5', '0', 3)
    g.addEdge('1 -> 2', '1', '2', 2)
    g.addEdge('2 -> 1', '2', '1', 2)
    g.addEdge('1 -> 3', '1', '3', 1)
    g.addEdge('3 -> 1', '3', '1', 1)
    g.addEdge('1 -> 4', '1', '4', 4)
    g.addEdge('4 -> 1', '4', '1', 4)
    g.addEdge('2 -> 3', '2', '3', 1)
    g.addEdge('3 -> 2', '3', '2', 1)
    g.addEdge('2 -> 6', '2', '6', 2)
    g.addEdge('6 -> 2', '6', '2', 2)
    g.addEdge('6 -> 5', '6', '5', 2)
    g.addEdge('5 -> 6', '5', '6', 2)
    g.addEdge('6 -> 3', '6', '3', 1)
    g.addEdge('3 -> 6', '3', '6', 1)
    g.addEdge('6 -> 4', '6', '4', 4)
    g.addEdge('4 -> 6', '4', '6', 4)
    g.addEdge('4 -> 3', '4', '3', 3)
    g.addEdge('3 -> 4', '3', '4', 3)
    '''

    
    
    #g = randomBarabasi(30,3,False,False,"Test_Barabasi")
    #g.addRandomWeights(5,100)
    


    
    #Grafo Profe rollando
    g = Graph(False,False,"Test_DAA")
    g.addEdge("0 -> 1","0","1",9)
    g.addEdge("0 -> 5","0","5",14)
    g.addEdge("0 -> 6","0","6",15)
    g.addEdge("1 -> 2","1","2",24)
    g.addEdge("5 -> 2","5","2",18)
    g.addEdge("5 -> 6","5","6",5)
    g.addEdge("5 -> 4","5","4",30)
    g.addEdge("6 -> 4","6","4",20)
    g.addEdge("6 -> 7","6","7",44)
    g.addEdge("4 -> 3","4","3",11)
    g.addEdge("4 -> 7","4","7",16)
    g.addEdge("2 -> 4","2","4",2)
    g.addEdge("2 -> 7","2","7",19)
    g.addEdge("3 -> 2","3","2",6)
    g.addEdge("3 -> 7","3","7",6)
    

    #g.toGVWeights()
    print("---------- GRAFO ORIGINAL ----------")
    g.printEdges()
    g.toGVWeights()
    print("")

    print("---------- GRAFO DIJKSTRA ----------")
    gd = g.Dijkstra(0)
    gd.printEdges()
    #gd.toGVWeights()
    #print("Cantidad de Aristas")
    #print(len(g.edges))

    


    '''
    # recuerdo metodos de listas
    print("------ Lista -----")
    l = ['a','b','c']
    print(l)
    print("l[0]: " + str(l[0]))
    print("------ Lista Recorrida -----")
    l.insert(0,'x')
    print(l)
    print("l[0]: " + str(l[0]))
    print("------ Lista Recuperada -----")
    l.pop(0)
    print(l)
    print("l[0]: " + str(l[0]))
    '''


    '''
    # Obtengo Lista de Aristas como objeto
    e = list(g.edges.values())
    print(e[1])
    # Le asigno un peso a la arista
    te = e[1]
    te.weight = 100
    print(te.weight)
    print(e[5].weight)     
    '''
    

if __name__ == '__main__':
    run()
