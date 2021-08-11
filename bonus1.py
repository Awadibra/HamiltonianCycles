import sys

class Graph():
    def __init__(self, vertices, edges):
        self.vertices = vertices
        self.edges = edges
    
    #check if edge [v,u] exists in the graph's list of edges
    def connected(self, v, u):
        if [v,u] in self.edges:
            return True
        return False
    
    #check if vertex u is in the given path
    def visited(self, u, path):
        if u in path:
            return True
        return False
    
    #check whether the vetex u is safe to be added to the hamiltonian cycle(or path) accumulated so far
    #by making sure that 1: it is connected to the vertex previous to it in the path
    #and 2: it has not been visited yet in the path.
    def safeForPath(self, u, path, index):
        #last vertex needs to be connected to the fist vertex
        if(index == self.vertices-1):
            if(self.connected(path[index-1], u) and self.connected(u, path[0]) and not self.visited(u, path)):
                return True
        elif(self.connected(path[index-1], u) and not self.visited(u, path)):
            return True
        return False

    #a recursive helper function that utilizes backtracking in order to solve the hamiltonian cycle problem.
    #at first i attempted to write this function without using an index to indicate the current position in the path
    #and instead append the next possible index to the end of the path, which led to a lot of problems.
    #however, as required by the assignment, i state that i drew inspiration from the following source:
    #https://www.geeksforgeeks.org/hamiltonian-cycle-backtracking-6/
    #which i found by googling "hamiltonian cycle backtracking", and surprisingly aligned very well with my own thought process.
    def recHamCycle(self, path, index):
        #stop condition: if we found a viable path
        if(path[-1] != None):
            return True
        #to save some steps, we can skip 1 since it is already included in the path.
        #for each vertex, check whether it is possible to add it to the path, if so, add it.
        for u in range(2, self.vertices+1):
            if self.safeForPath(u, path, index):
                path[index] = u
                #attemp to find the rest of the hamiltonian cycle.
                if self.recHamCycle(path, index+1):
                    return True
                #otherwise, revert the last added vertex in the path to None.
                path[index] = None
        return False

    #returns a hamiltonian cycle path ending with 0 (if it exists, otherwise just 0).
    def findHamCycle(self):
        #start the path with vertix 1, even though it does not matter which vertix it stats with.
        path = [None] * self.vertices
        path[0] = 1
        #call the recursive helper function to solve the hamCycle.
        if self.recHamCycle(path,1) == False:
            return [0]
        else:
            path.append(0)
            return path

#for each given instance of a graph fed into the ham cycle solver
#parse it, create a graph, and attempt to find a hamiltonian cycle.
#since sys.argv[0] is the program name ("bonus1"), simply skip it.
if __name__ == '__main__':
    for arg in sys.argv[1:]:
        f = open(arg,"r")
        #prepare the <instance>.hamsol filename, which will be located inside the results folder
        resName = arg.split("\\")
        resName = resName[-1]
        resName = "results//" + resName.split(".ham")[0] + ".hamsol"
        lines = f.readlines()
        vertices = None
        edges = None
        for line in lines:
            line = line.split()
            #skip comments
            if line[0] == 'c':
                continue

            #parse the number of vertices and edges.
            #although in my approach the number of edges is not needed(possibly thanks to python).
            elif line[0] == 'p':
                vertices = int(line[2])
                edges = []

            #parse each edge and add to the list of accumulated edges.
            #since this is an undirected graph, for vetices u, v, if edge [u,v] exists
            #also add edge [v,u].
            #althought this approach technically makes it a directed graph, it also makes the above code more readable and easie to manage
            elif line[0] == 'e':
                edges.append([int(line[1]),int(line[2])])
                edges.append([int(line[2]),int(line[1])])
        
        #create the graph
        graph = Graph(vertices, edges)
        #attempt to find a hamiltonian cycle
        path = graph.findHamCycle()
        #output the result
        output = open(resName, "w+")
        output.write(" ".join(map(str,path)))

        
