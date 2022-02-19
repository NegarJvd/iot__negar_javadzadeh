import random
from node import Node


# import stddraw


def define_nodes(count, x_range, y_range):
    nodes_list = []

    for i in range(count):
        x = random.randint(0, x_range)
        y = random.randint(0, y_range)
        node = Node(i, x, y)
        nodes_list.append(node)

    return nodes_list


def add_neighbors_to_nodes(nodes_list, count):
    for node in nodes_list:
        neighbors = random.sample([n for n in nodes_list if n.id != node.id], count)
        node.add_neighbors_list(neighbors)


def main():
    nodes = define_nodes(20, 100, 100)
    add_neighbors_to_nodes(nodes, 6)

    # stddraw.setXscale(-20, 120)
    # stddraw.setYscale(-20, 120)
    #
    # stddraw.setPenColor(stddraw.BLUE)
    # stddraw.line(0, 0, 100, 0)
    # stddraw.line(0, 0, 0, 100)

    for node in nodes:
        print("node:")
        print(node)

        print("neighbors: ")
        for n in node.neighbor_nodes:
            print(n)

        # node.draw_node()
        print("================================")

    # stddraw.show()


if __name__ == '__main__':
    main()

# Negar Javadzadeh 975361009
