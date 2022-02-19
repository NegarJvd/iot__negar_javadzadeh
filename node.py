# import stddraw


class Node:
    def __init__(self, _id, _x, _y):
        self.id = _id
        self.x = _x
        self.y = _y
        self.neighbor_nodes = []

    def __str__(self):
        return str(self.id) + ' => ' + '(' + str(self.x) + ', ' + str(self.y) + ')'

    def add_neighbor(self, neighbor):
        self.neighbor_nodes.append(neighbor)

    def add_neighbors_list(self, neighbors_list):
        self.neighbor_nodes += neighbors_list

    # def draw_node(self):
    #     stddraw.setPenRadius(0.01)
    #
    #     stddraw.setPenColor(stddraw.RED)
    #     stddraw.point(self.x, self.y)
    #     stddraw.show(200)
    #
    #     for neighbor in self.neighbor_nodes:
    #         stddraw.setPenColor(stddraw.BLACK)
    #         stddraw.point(neighbor.x, neighbor.y)
    #         stddraw.show(200)
    #
    #         stddraw.line(self.x, self.y, neighbor.x, neighbor.y)
    #         stddraw.show(200)

# Negar Javadzadeh 975361009
