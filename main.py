# Author: Negar Javadzadeh 975361009

import random

from graph import *


def define_nodes(count, x_range, y_range):
    nodes_list = []
    points_list = []
    graph = Graph()

    for i in range(count):
        x = random.randint(0, x_range)
        y = random.randint(0, y_range)
        node = Node(i, x, y)
        nodes_list.append(node)
        points_list.append((x, y))
        graph.add_node(i)

    return {
        'nodes_list': nodes_list,
        'points_list': points_list,
        'graph': graph
    }


def add_neighbors_to_nodes(nodes_list, count, graph):
    for node in nodes_list:
        neighbors = random.sample([n for n in nodes_list if n.id != node.id], count)
        node.add_neighbors_list(neighbors)

        for neighbor in neighbors:
            graph.connect(node.id, neighbor.id)


def main():
    start_id = int(input("start node id: "))
    end_id = int(input("end node id: "))

    definition = define_nodes(20, 100, 100)
    start = Node(1, 0, 0)
    end = Node(2, 1, 1)
    nodes = definition['nodes_list']
    graph = definition['graph']
    add_neighbors_to_nodes(nodes, 6, graph)

    # print nodes
    for node in nodes:
        if node.id == start_id:
            start = node

        if node.id == end_id:
            end = node

        print("node:")
        print(node)

        print("neighbors: ")
        for n in node.neighbor_nodes:
            print(n)

        print("================================")

    # print path
    print("direct path: \n", end in start.neighbor_nodes)
    print("shortest path: ")
    print_shortest_path_bfs(graph, start_id, end_id)


if __name__ == '__main__':
    main()
