''' *****************************************************************************
 *  Name:      Arbaaz Khan
 *  Language:  python3 
 *
 *  Description:  Implementation of graph with adjacency matrix representation.
 *
 *  Written:       22/1/2018
 *  Last updated:  22/1/2018
 *  
 *  TIME COMPLEXITIES:
 *  -----------------------------------------------------------------
 *  |   Operations  |   WorstCase   |  AverageCase  |    BestCase   |
 *  -----------------------------------------------------------------
 *  |   insertion   |    bigO(-)    |  bigO(-)  |    bigO(-)    |
 *  -----------------------------------------------------------------
 *  |   deletion    |    bigO(-)    |    bigO(-)    |    bigO(-)    |
 *  -----------------------------------------------------------------
 *  |   traversal   |    bigO(-)    |    bigO(-)    |    bigO(-)    |
 *  -----------------------------------------------------------------
 *  |   searching   |    bigO(-)    |  bigO(-)  |    bigO(-)    |
 *  -----------------------------------------------------------------
 *
 *  % python graph_matrix_representation.py
 *
***************************************************************************** '''

class Graph(object):
    def __init__(self, verticesNum, directed = False, weighted = False):
        self.vertices = [] #Stores the vertices
        self.verticesNum = verticesNum #Number of vertices
        self.adjMatrix = [[-1 for i in range(verticesNum)] for j in range(verticesNum)] #vertices X vertices matrix, -1 value means no edge
        self.directed = directed
        self.weighted = weighted

    def addVertex(self, id): #Stores the vertices
        self.vertices.append(id)

    def getIndex(self, vertex): #Returns the index of the vertex
        return self.vertices.index(vertex)
    
    def addEdge(self, src, dst, weight = 0):
        if self.directed: #If directed then add the edge in the specified direction
            self.adjMatrix[self.getIndex(src)][self.getIndex(dst)] = weight
        else:#If undirected then edge should be in both direction so we need to make both the vertices as each other's neighbour
            self.adjMatrix[self.getIndex(src)][self.getIndex(dst)] = weight
            self.adjMatrix[self.getIndex(dst)][self.getIndex(src)] = weight

    def getVertices(self):
        return self.vertices

    def removeEdge(self,src,dst):
        if self.adjMatrix[self.getIndex(src)][self.getIndex(dst)] != -1 or self.adjMatrix[self.getIndex(dst)][self.getIndex(src)] == -1:
            if self.directed: # if directed then remove the edge specified else remove both src->dst and dst->src
                self.adjMatrix[self.getIndex(src)][self.getIndex(dst)] = -1
            else:
                self.adjMatrix[self.getIndex(src)][self.getIndex(dst)] = -1
                self.adjMatrix[self.getIndex(dst)][self.getIndex(src)] = -1

    def show(self):
        print("Adjacency Matrix:")
        print('  \t',end=" ")
        for v in self.vertices:
            print(v,end="\t")
        print()
        for i in range(len(self.vertices)):
            print(self.vertices[i],end="\t")
            for j in range(len(self.vertices)):
                print(self.adjMatrix[i][j],end="\t")
            print()

if __name__ == "__main__":
    g = Graph(6,False,True)
    g.addVertex('a')
    g.addVertex('b')
    g.addVertex('c')
    g.addVertex('d')
    g.addVertex('e')
    g.addVertex('f')
    g.addEdge('a','c',5)
    g.addEdge('b','c',2)
    g.addEdge('b','e',8)
    g.addEdge('c','d',4)
    g.addEdge('c','e',3)
    print("Vertices: "+str(g.getVertices()))
    g.show()
    g.removeEdge('b','e')
    print("After removing the edge:")
    g.show()


'''
a               b
  .           . .
5   .     2 .   .
      .   .     .
        c       . 8
      .   .     .
 4  .    3  .   .
  .           . .
d               e

        f

Adjacency Matrix:
         a      b       c       d       e       f
a       -1      -1      5       -1      -1      -1
b       -1      -1      2       -1      8       -1
c       5       2       -1      4       3       -1
d       -1      -1      4       -1      -1      -1
e       -1      8       3       -1      -1      -1
f       -1      -1      -1      -1      -1      -1

After removing the edge:
Adjacency Matrix:
         a      b       c       d       e       f
a       -1      -1      5       -1      -1      -1
b       -1      -1      2       -1      -1      -1
c       5       2       -1      4       3       -1
d       -1      -1      4       -1      -1      -1
e       -1      -1      3       -1      -1      -1
f       -1      -1      -1      -1      -1      -1

'''


