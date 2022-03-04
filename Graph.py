# Author: Negar Javadzadeh 975361009

import math

from node import Node


class Graph:
    def __init__(self):
        self.adj = {}
        self.nodes = {}

    def add_node(self, id):
        self.adj[id] = []
        self.nodes[id] = Node(id, 0, 0)

    def connect(self, id1, id2):
        self.adj[id1].append(id2)

    def get(self, id):
        return self.nodes[id]


def init_graph(graph, source):
    for v in graph.nodes.values():
        v.prev = None
        v.visited = 0
        v.dist = math.inf
    graph.get(source).dist = 0


def shortest_path_bfs_initializer(graph, source):
    init_graph(graph, source)
    queue = [graph.get(source)]
    while not len(queue) == 0:
        curr = queue.pop(0)
        curr.visited = 1

        for v in graph.adj[curr.id]:
            node_form = graph.get(v)
            if node_form.visited == 0:
                node_form.prev = curr
                node_form.dist = curr.dist + 1
                queue.append(node_form)
        curr.visited = 2


def shortest_path_bfs(graph, source, target):
    shortest_path_bfs_initializer(graph, source)
    ans = []
    source = graph.get(source)
    target = graph.get(target)
    while target is not source:
        ans.append(target)
        target = target.prev
    ans.append(source)
    ans.reverse()
    return ans


def print_shortest_path_bfs(graph, source, target):
    path = shortest_path_bfs(graph, source, target)
    for i in range(len(path) - 1):
        print(str(path[i].id), "->", end=" ")
    print(str(path[len(path) - 1].id))
