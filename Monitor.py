import networkx as nx
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


class Monitor:

    def __init__(self, simulation):
        self.simulation = simulation

        plt.figure(figsize=(5, 5))
        nx.draw_networkx_edges(self.network, pos, nodelist=[ncenter], alpha=0.4)
        nx.draw_networkx_nodes(
            self.network,
            pos,
            nodelist=list(p.keys()),
            node_size=20,
            node_color='#000000',  # list(p.values()),
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
