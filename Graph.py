from asyncio.windows_events import NULL
from Node import *
from Edge import *

class Graph:

    def __init__(self,directed,autocycles,graph_name):
        '''
        directed: True or False about the graph's direction
        autocycles: True or False about the autocycles on the graph existence
        graph_name: Created Graph's name
        '''
        self.name = graph_name
        self.nodes = {}
        self.edges = {}
        self.directed = False
        self.autocycles = False
        self.visited = False
    
    def addNode (self,name):
        '''
        Adding a new node to the node's graph dictionary
        name: New node name
        '''
        node = self.nodes.get(name)

        if node is None: # Check if the node already exists
            node = Node(name)
            self.nodes[name] = node # Add a new node

        return node

    def addEdge(self,name,node0,node1,weight):
        '''
        Adding a new edge to the edge's graph dictionary
        name: Edge name
        node0: source node
        node1: target node
        weight: Edge weight value if it is necessary
        '''
        ed = self.edges.get(name)
        
        if ed is None: # Check if the edge already exists
            n0 = self.addNode(node0)
            n1 = self.addNode(node1)
            ed = Edge(name,n0,n1,weight) # Creaating the edge object
            self.edges[name] = ed # Adding values to the edge dictionary

            n0.neighbors.append(n1) # Adding to each node their respective neigbors and edges list
            n1.neighbors.append(n0)

            n0.edges.append(ed)
            n1.edges.append(ed)

        return ed

    def getNode(self,name):
        '''
        Getting the Node as an object not just the name
        name: Node's name
        '''
        return self.nodes.get(name)

    def getDegree(self,node):
        '''
        Evaluate the quantity of neighbors on an specific node in the graph
        node: Node of interest name
        '''
        n = self.getNode(node)
        if n is None:
            return 0
        
        return len(n.neighbors)

    def getRandEdge(self):
        '''
        Get a random edge on the graph
        '''
        return random.choice(list(self.edges.values()))

    def printNodes(self):
        '''
        Printing the Graph nodes in console to verify functionality
        '''
        n = self.nodes.items()
        print(n)

    def printEdges(self):
        '''
        Printing the Graph edges in console to verify functionality
        '''
        e = self.edges.items()
        print(e)
    
    def toGVFormat(self):
        '''
        Create the GV file to show results on Gephi
        '''
        val = 'digraph '+ str(self.name) + ' {\n'
        for i in self.nodes.values():
            val += str(i.id) + ';'
        for e in self.edges.values():
            n0 = e.n0.id
            n1 = e.n1.id
            val += n0 + ' -> ' + n1 + ';\n'
        val += '}\n'
        with open ("./Graphs_Data/" + self.name +".gv","w") as gv:
          gv.write(val) 

    def BFS(self,s):
        '''
        Create the BFS tree graph starting at the node s
        s: Tree root node
        '''

        Tree_BFS = Graph(False,False,self.name + "_BFST") # Create the tree graph
        self.resetNodes() # Mark all nodes of the graph as unvisited
        
        L = {0:[s]} # Create the layers dictionary
        Tree_BFS.addNode(str(s)) # Adds the origin node chosen by the user to the tree
        k = 0 # Start the layer counter
        node = self.getNode(str(s)) # Take the node as an object
        node.visited = True # Mark it as visited

        while len(L[k]) != 0: # Check if the layer is empty
            L[k + 1] = [] # Create the next layer empty
            for i in range(len(L[k])): # Loop to evaluate each node in the layer 
                node = self.getNode(str(L[k][i]))  
                e = node.edges # Get neighbours from the edges
                for j in range(len(e)): # Loop to add the unvisited neigbors to the next layer
                    if e[j].n1.visited == False: 
                        e[j].n1.visited = True 
                        Tree_BFS.addNode(e[j].n1.id) 
                        Tree_BFS.addEdge(str(L[k][i])+" -> "+str(e[j].n1.id),str(L[k][i]),str(e[j].n1.id),NULL)
                        L[k + 1].append(e[j].n1.id)  # Add de node.id to the next layer

            k = k+1 # The layer counter pass to the next level

        print(L) 
        return Tree_BFS
    
    def resetNodes(self):
        '''
        Marks all the graph nodes as unvisited to start searchings
        '''
        n = len(self.nodes.items()) # Get the nodes quantity
        for i in range(n):
            node = self.getNode(str(i))  # Get nodes one by one
            node.visited = False  # Make the node as unvisited
    
    def DFS_R(self,s):
        '''
        Create the DFS tree graph starting at the node s by using the recursive algorithm
        s: Tree root node
        '''
        Tree_DFSR = Graph(False,False,self.name + "_DFSRT") # Create the tree graph
        self.resetNodes() # Mark all nodes of the graph as unvisited
        
        def DFRI(s2): # Define the internal function to be able to apply recursion
            node = self.getNode(str(s2)) # Take the root as an object
            node.visited = True # Mark it as visited
            Tree_DFSR.addNode(str(s2)) # Adds the root node to the tree
            e = node.edges # Get the root edges
            for i in range(len(e)): # For each edge evaluate if the neighbour is already visited
                if e[i].n1.visited == False: # If neighbour is not visited, add it to the tree and apply it the aboove steps
                    Tree_DFSR.addEdge(str(s2) + " -> " +str(e[i].n1.id),str(s2),str(e[i].n1.id),NULL)
                    DFRI(e[i].n1.id) # Apply the algorithm to the unvisited neighbour
                     

        DFRI(s) # Apply the recursive algorith startin with the node s chosen by the user    

        return Tree_DFSR
         
    def DFS_I(self,s):
        '''
        Create the DFS tree graph starting at the node s by using the iterative algorithm
        s: Tree root node
        '''
        Tree_DFSR = Graph(False,False,self.name + "_DFSIT") # Create the tree graph
        self.resetNodes() # Mark all nodes of the graph as unvisited
        S = [] # Create an empty stack to save the visited nodes
        S.append(self.getNode(str(s)).id) # Add the root node to the stack
        while len(S) != 0: # Executes the loop until there are no more connected nodes without visiting
            head = S.pop() # Take out the stack top
            node = self.getNode(str(head)) # Get the stack top as an object
            node.visited = True # Mark it as visited
            Tree_DFSR.addNode(node.id) # Add the stack top to the tree
            e = node.edges
            neis = list(map(lambda x : x.id ,node.neighbors)) # Get the stack top neighbors list 

            for i in range(len(e)): # Add the nodes to the stack if they were not in and have not been visited before. 
                if e[i].n1.id not in S and e[i].n1.visited == False:
                    S.append(e[i].n1.id)
                    Tree_DFSR.addEdge(node.id + " -> " + e[i].n1.id, node.id, e[i].n1.id,NULL)

        return Tree_DFSR

    def addRandomWeights(self,lower_limit,upper_limit):
        '''
        Given a graph it adds random weights on every edge
        lower_limit: The lowest value on the edges
        upper_limit: The highest value on the edges
        '''
        e = list(self.edges.values())
        for i in range(len(e)):
            w = random.randrange(lower_limit,upper_limit)
            e[i].weight = w

    def toGVWeights(self):
        '''
        Create the GV file to show results on Gephi with weights onj the edges
        '''

        val = 'digraph '+ str(self.name) + ' {\n'
        for i in self.nodes.values():
            val += str(i.id) + ';'
        for e in self.edges.values():
            n0 = e.n0.id
            n1 = e.n1.id
            val += n0 + ' -> ' + n1 + ' [label = ' + str(e.weight) + ']' + ';\n'
        val += '}\n'
        with open ("./Graphs_Data/" + self.name +".gv","w") as gv:
          gv.write(val) 

    def Dijkstra(self,s):
        '''
        Given a Graph and a source node, this method create the dijkstra tree with minimal distance to each node

        s: source node
        
        '''

        Dijk_Tree = Graph(False,False,self.name + "_DijkTree") # Creating the graph
        self.resetNodes() # Mark all nodes as unvisited
        q = list(self.nodes.keys()) # Starting the Priority queue
        wd = {str(i):int(99999999) for i in range(len(self.nodes))} # Dictionary that helps store the accumulated weight of each node
        wd[str(s)] = 0 # The source node have a weight equal to zero
        pe = {} # Empty Dictionary that store's the last edge that reach the accumulated weight of each node 
        self.getNode(str(s)).visited = True # Marking the node as visited (set S learned in class)
        q.remove(str(s)) # Remove the source node from the queue temporarily, to add it first 
        q.insert(0,str(s)) 
        Dijk_Tree.addNode(s) #Adding the source node to the Dijkstra Tree
        j = 1
        
        def min_list_value(interest_list):
            '''
            Method to get the minimal valu on a list

            interest_list: List from which the minimum value is obtained
            '''

            if len(interest_list) != 0:
                min = interest_list[0]
                for x in interest_list:
                    if x < min:
                        min = x
            
            if len(interest_list) == 0:
                min = 1
                

            return min

        def ordkeys(key_value, key_list , dicc):
            '''
            Method to place the value of a list according to the weight stored in a dictionary 

            key_value: Value of interest
            key_list: List on wich we order the key value
            dicc: Dictionary that stores the list values weights

            '''

            key_list.remove(key_value) # Remove the value from the list to avoid compare it with itself
            pointer = len(key_list) - 1 # Pointer to evaluate all the posible positions inside the list
            pos = [] # List to store the posible positions whre the value can be placed

            while pointer != -1: # Cycle to evaluate echa position in the list 

                dk = key_list[pointer] # Value stored  with the key in the list on the pointer position
                dis = dicc[dk] >= dicc[key_value] # Condition to evaluate

                if dis == True: # If the condition is true, saves the position as a possible candidate
                    pos.append(pointer)
            
                elif dis == False: # If the condition is false and the pointer is on the last position we add the value at the end
                            
                    if pos == (len(key_list) - 1):
                        pos.append(pointer)
                        break
                        
                pointer = pointer - 1
            
            key_list.insert(min_list_value(pos),key_value) # Insert the value in the lowest position among the candidate positions

        while len(q) != 0: # Cycle untill the priority queue is empty

            t = self.getNode(q[0])
            t.visited = True # Adding the firt node on the queue to S  
            npop = q.pop(0) # Take out the node with the lowest weight on the priority queue 

            if j != 1: # Add an Edge to the three if there a previous edge, that means the node es raeachable and is already evaluated
                try:
                    Dijk_Tree.addEdge(pe[npop].n0.id + " -> " + npop + " (" + str(wd[npop]) + ")", pe[npop].n0.id, npop, pe[npop].weight)
                except KeyError:
                    pass

            e = t.edges # Getting all the edges to update values

            for i in range(len(e)):
                if e[i].n1.visited == False: # If target node is not already on the tree
                    j = j+1
                    if int(wd[e[i].n1.id]) > int(wd[e[i].n0.id]) + e[i].weight: # And the acumulated weight is bigger than the new value  
                        wd[e[i].n1.id] = wd[e[i].n0.id] + e[i].weight 
                        pe[e[i].n1.id] = e[i] # Once the acumulated weight is updated, store the last edge to get that value
                        ordkeys(e[i].n1.id,q,wd) # Ordering the update node among the priority queue

        
        val = 'digraph '+ str(Dijk_Tree.name) + ' {\n'
        for i in Dijk_Tree.nodes.values():
            val += str(i.id) + '(' + str(wd[str(i.id)]) + ') ' + ';'
        for e in Dijk_Tree.edges.values():
            n0 = e.n0.id + '(' + str(wd[str(e.n0.id)]) + ')'
            n1 = e.n1.id + '(' + str(wd[str(e.n1.id)]) + ')'
            val += n0 + ' -> ' + n1 + ' [label = ' + str(e.weight) + ']' + ';\n'
        val += '}\n'
        with open ("./Graphs_Data/" + Dijk_Tree.name +".gv","w") as gv:
          gv.write(val)                                

        
        print("Minimal distances to each node is: ")
        print(wd)

        return Dijk_Tree






        
        

