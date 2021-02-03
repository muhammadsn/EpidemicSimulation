import networkx as nx
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from NetworkGen import NetworkGenerator as NG


class Monitor:
    simulation = None
    simulation_network = None

    def __init__(self):
        pass

    def show_network(self, simulation, X, Y, t):
        self.simulation = simulation
        self.simulation_network = simulation.get_network()
        nodes = self.simulation.get_nodes()
        node_color_map = []
        for node in self.simulation_network:
            if self.simulation.get_node_attr(node, "I"):
                node_color_map.append('#ff0000')
            else:
                node_color_map.append('#000000')

        plt.figure(figsize=(5, 5))
        # nx.draw_networkx_edges(self.simulation_network, nodes, alpha=0.4)
        nx.draw(
            self.simulation_network,
            nodes,
            nodelist=list(nodes.keys()),
            node_size=20,
            node_color=node_color_map,
            # with_labels=True
        )

        plt.xlim(0, X)
        plt.ylim(0, Y)
        # plt.axis("off")
        xticks = [x for x in range(X)]
        yticks = [x for x in range(Y)]
        plt.xticks(ticks=xticks)
        plt.yticks(ticks=yticks)
        # plt.title(f"Infected Nodes in t = {str(t)}")
        plt.grid()
        plt.show()
