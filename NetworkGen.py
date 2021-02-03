import networkx as nx
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random


class NetworkGenerator:
    network = nx.Graph()
    nodes = {}
    edges = []
    N = 0
    E = 0

    def __init__(self, X, Y, Density):
        self.X = X
        self.Y = Y
        self.DELTA = Density
        self.N = int(self.X * self.Y * self.DELTA)
        self.R0 = 1 / self.DELTA
        self.nodes = {i: (random.uniform(0, self.X), random.uniform(0, self.Y)) for i in range(self.N)}
        self.build()


    def build(self):
        self.network = nx.random_geometric_graph(n=self.N, radius=self.R0, pos=self.nodes)
        self.edges = self.network.edges
        self.E = len(self.network.edges)
        nx.set_node_attributes(self.network, False, "infected")





        # infection = nx.get_node_attributes(self.network, "infected")
        # p = dict(nx.single_source_shortest_path_length(self.network, ncenter))


    def set_node_attr(self, node_value_dict, attr):
        nx.set_node_attributes(self.network, node_value_dict, attr)

    def get_nodes_with_attr(self, attr, value):
        nodes_status = nx.get_node_attributes(self.network, attr)
        result = []
        for n in nodes_status:
            if nodes_status[n] == value:
                result.append(n)
        return result

    def get_node_neighbours(self, node):
        return self.network.neighbors(node)

    def get_network(self):
        return self.network

    def get_nodes(self):
        return self.nodes

    def get_nodes_list(self):
        return self.nodes.keys()

    def get_edges(self):
        return self.edges

    def get_nodes_count(self):
        return self.N

    def get_edges_count(self):
        return self.E

    def get_Map_X(self):
        return self.X

    def get_Map_Y(self):
        return self.Y
