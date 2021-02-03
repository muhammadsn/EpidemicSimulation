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


        dmin = 1
        ncenter = 0
        for n in pos:
            x, y = pos[n]
            d = (x - X/2) ** 2 + (y - X/2) ** 2
            if d < dmin:
                ncenter = n
                dmin = d


        nx.set_node_attributes(self.network, {ncenter: True}, "infected")
        infection = nx.get_node_attributes(self.network, "infected")
        # print(infection)
        # print(ncenter)
        # color by path length from node near center
        p = dict(nx.single_source_shortest_path_length(self.network, ncenter))

        plt.figure(figsize=(5, 5))
        nx.draw_networkx_edges(self.network, pos, nodelist=[ncenter], alpha=0.4)
        nx.draw_networkx_nodes(
            self.network,
            pos,
            nodelist=list(p.keys()),
            node_size=20,
            node_color='#000000',  #list(p.values()),
            # cmap= 'Reds',
            # cmap=plt.cm.Reds_r,
        )

        plt.xlim(0, X)
        plt.ylim(0, Y)
        # plt.axis("off")
        xticks = [x for x in range(X)]
        yticks = [x for x in range(Y)]
        plt.xticks(ticks=xticks)
        plt.yticks(ticks=yticks)
        plt.grid()
        plt.show()


    def get_network(self):
        return self.network

    def get_nodes(self):
        return self.nodes

    def get_edges(self):
        return self.edges

    def get_nodes_count(self):
        return self.v_size

    def get_edges_count(self):
        return self.E_size
