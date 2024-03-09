class Edge(object):
    def __init__(self, vertex1, vertex2, cost,  id = None):
        self._vertex1 = vertex1
        self._vertex2 = vertex2
        self._cost = cost
        self._id = id


    def get_vertex1(self):
        return self._vertex1


    def get_vertex2(self):
        return self._vertex2

    def get_cost(self):
        return self._cost


    def get_id(self):
        return self._id

    def __eq__(self, other):
        return self._vertex1 == other.get_vertex1 and self._vertex2 == other.get_vertex2

class Vertex(object):
    def __init__(self, id):
        self._id = id


    def ID(self):
        return self._id

class VertexRelation(object):
    def __init__(self):
        self._inVertices = []
        self._outVertices = []

    @property
    def get_in_vertices(self):
        return self._inVertices
    @property
    def get_out_vertices(self):
        return self._outVertices

    @get_in_vertices.setter
    def set_in_vertices(self, other):
        self._inVertices = other
    @get_out_vertices.setter
    def set_out_vertices(self, other):
        self._outVertices = other