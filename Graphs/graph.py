class Graph():

    def __init__(self, vertices):
        self.vertices = vertices
        self.graphDict = dict()

    def vertexCount(self):
        '''Returns number of vertices'''
        return len(self.graphDict)

    def edges(self):
        self.edgeList = []
        for i in self.graphDict:
            for j in self.graphDict.values():
                self.edgeList.append((i,j))
        return self.edgeList

    def isEdge(self,source,destination):
        try:
            if destination in  self.graphDict[source]:
                return True
        except KeyError:
            return False
    def edgeCount(self):
        sum = 0
        for i in self.graphDict.keys():
            sum += len(self.graphDict[i])
        return sum
    def vertices(self):
        return self.graphDict.keys()

    def addVertex(self,vertex):
        """Adding vertex to graph"""
        if vertex not in self.graphDict:
            graphDict[source] = []
        else:
            print("Vertex is already present")
    def removeVertex(self,vertex):
        for i in self.graphDict.keys():
            for j in self.graphDict[i]:
                if j == vertex:
                    self.graphDict[i].remove(vertex)
        del self.graphDict[vertex]
    def removeEdge(self,source,destination):
        try:
            self.graphDict[source].remove[destination]
        except ValueError:
            print("Element is not in the list")
    def addEdge(self,source,destination):
        """Adding Edges to the graph"""
        if source not in self.graphDict:
            graphDict[source] = [destination]
        else:
            graphDict[source].append(destination)
    def degree(self,vertex):

n = int(input("Enter number of vertices: "))
