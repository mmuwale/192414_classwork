class Graph:
    def __init__(self, directed = False):
        self.directed = directed # boolean to indicate if the graph is directed or undirected
        self.adj_list = dict() # dictionary to hold adjacency list representation of the graph

    def __repr__(self): # dunder method for string representation
        str_graph = ""
        for key, value in self.adj_list.items(): 
            str_graph += f"{key} -> {value} " # format: node -> [list of adjacent nodes]
        return str_graph

    def bfs(self, start): # We use QUEUES(fifo) IN BFS,  AND STACK(lifo) FOR DFS, as helping data structures    
        visited = set() # set of visited nodes    
        queue = [start] # nodes to be processed, so have a starting node    
        order = [] # Our result in order, which is traversal order    
        while queue: 
            # while we still have elements to process, get the elements to process in fifo way        
            node = queue.pop(0) # first element added 
            print(f"Exploring room: {node}, Path so far: {path}")        
            if node == goal: # if we reached the goal, we can stop the search    
                print("\n🎯 Theseus found the Minotaur!")     
                return path        
            if node not in visited: # if node is not visited            
                visited.add(node) # first add it to the visited nodes            
                order.append(node) # append it to our resulting list            
                #Then get all the neighbours of this node, use our available function            
                neighbours = self.get_neighbours(node) # then iterate through them            
                for neighbour in neighbours:                
                    #means we have a weighted connection not just individual value                
                    if isinstance(neighbour, tuple):                    
                        neighbour = neighbour[0]  #just take the value and leave the weight,     
                        # Sometimes neighbors might come as (value, weight), so we only take the value                    
                        # if neighbour is not visited, append it to queue                
                        if neighbour not in visited:                    
                            queue.append(neighbour)    
                            return order
                        
    def dfs(self, start): # We use STACK(lifo) FOR DFS, as helping data structures    
        visited = set()  # set of visited nodes    
        stack = [start]  # nodes to be processed, so have a starting node    
        order = []  # Our result in order, which is traversal order    
        while stack: # while we still have elements to process,        
            # get the elements to process in fifo way       
            node = stack.pop()  # first element added        
            if node not in visited:  # if node is not visited            
                visited.add(node)  # first add it to the visited nodes            
                order.append(node)  # append it to our resulting list            
                # Then get all the neighbours of this node, use our available function            
                neighbours = self.get_neighbours(node)            
                # then iterate through them            
                for neighbour in sorted(neighbours, reverse=True): 
                    # means we have a weighted connection not just individual value                
                    if isinstance(neighbour, tuple):                    
                        neighbour = neighbour[0]  # just take the value and leave the weight      
                        # if neighbour is not visited, append it to queue                
                        if neighbour not in visited:                    
                            stack.append(neighbour)    
                            return order

    def add_node(self, node):
        if node not in self.adj_list: # check if the node already exists
            self.adj_list[node] = set() # initialize a tuple to store the adjacent node and the weight of the edge, to avoid repetition
        else:
            raise ValueError("Node Exists!!")

    def add_edge(self, source_node, destination_node, weighted = None):
        if source_node not in self.adj_list:
            self.add_node(source_node) # add source node if it does not exist
        if destination_node not in self.adj_list:
            self.add_node(destination_node) # add destination node if it does not exist
        if weighted is None:
            self.adj_list[source_node].add(destination_node) # add destination node to the adjacency list of source node if not weighted
            if self.directed:
                self.adj_list[destination_node].add(source_node) # add source node to the adjacency list of destination node if directed
        else:
            self.adj_list[source_node].add((destination_node, weighted))
            if self.directed:
                self.adj_list[destination_node].add((source_node, weighted))

    def obtain_neighbours(self, key_node):
        return self.adj_list.get(key_node, set())

    def adj_matrix(self):
        ...

if __name__ == "__main__":
    graph_obj = Graph()
    print(graph_obj)