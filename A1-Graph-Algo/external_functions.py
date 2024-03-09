from graph import Graph
import random

def readGraph(filename):
    '''
    the information about a graph is read from a given textfile and the graph is created
    '''
    try:
        with open(filename, "r") as file:
            lines = file.readlines()
            lines[0] = lines[0].strip("\n")
            graphVerticesAndEdges = lines[0].split(" ")
            numberOfVertices = int(graphVerticesAndEdges[0])
            numberOfEdges = int(graphVerticesAndEdges[1])
            graph = Graph(numberOfVertices, numberOfEdges)
            lines = lines[1:]
            for line in lines:
                line = line.strip("\n")
                edge = line.split(" ")
                vertex1 = int(edge[0])
                vertex2 = int(edge[1])
                cost = int(edge[2])
                graph.addEdge(vertex1, vertex2, cost)
    except:
        raise ValueError("File not found")
    return graph

def writeGraph(graph, filename):
    '''
    writes the info of a graph to a given file
    '''
    with open(filename, "w+") as file:
        numberOfVertices = graph.NumberOfVertices
        numberOfEdges = graph.NumberOfEdges
        file.write(str(numberOfVertices) + " " + str(numberOfEdges) + "\n")
        for vertex1 in graph.VerticesOutboundEdges:
            for vertex2 in graph.VerticesOutboundEdges[vertex1]:
                file.write(str(vertex1) + " " + str(vertex2) + " " + str(graph.Costs[(vertex1, vertex2)]) + "\n")

def writeGraphConsole(graph):
    '''
    writes the info of a graph to the console
    '''
    numberOfVertices = graph.NumberOfVertices
    numberOfEdges = graph.NumberOfEdges
    print(str(numberOfVertices) + " " + str(numberOfEdges) + "\n")
    for vertex1 in graph.VerticesOutboundEdges:
        if graph.VerticesOutboundEdges[vertex1] == []:
            print(str(vertex1) + " has no outbound edges\n")
        for vertex2 in graph.VerticesOutboundEdges[vertex1]:
            print(str(vertex1) + " " + str(vertex2) + " " + str(graph.Costs[(vertex1, vertex2)]) + "\n")


def randomGraph(numberOfVertices, numberOfEdges):
    '''
    generates a random graph with a given number of vertices and a given number of edges
    '''
    graph = Graph(numberOfVertices, numberOfEdges)
    for vertex in range(numberOfVertices):
        graph.addVertex(vertex)
    numberOfAddedEdges = 1
    while numberOfAddedEdges <= numberOfEdges:
        vertex1 = random.choice(range(numberOfVertices))
        vertex2 = random.choice(range(numberOfVertices))
        cost = random.choice(range(1000))
        if not graph.findEdgeBetweenVertices(vertex1, vertex2):
            graph.addEdge(vertex1, vertex2, cost)
            numberOfAddedEdges += 1
    return graph

