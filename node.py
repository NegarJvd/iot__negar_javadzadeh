# Author: Negar Javadzadeh 975361009


class Node:
    def __init__(self, _id, _x, _y):
        self.id = _id
        self.x = _x
        self.y = _y
        self.neighbor_nodes = []
        self.dist = None
        self.prev = None
        self.visited = None

    def __str__(self):
        return str(self.id) + ' => ' + '(' + str(self.x) + ', ' + str(self.y) + ')'

    def add_neighbor(self, neighbor):
        self.neighbor_nodes.append(neighbor)

    def add_neighbors_list(self, neighbors_list):
        self.neighbor_nodes += neighbors_list

    def add_x(self, x):
        self.x = x

    def add_y(self, y):
        self.y = y
