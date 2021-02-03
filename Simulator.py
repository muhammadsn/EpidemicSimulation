import numpy as np
from scipy.integrate import odeint
from NetworkGen import NetworkGenerator as NG

class Simulator:
    network = None
    N = 0
    susceptible = dict()
    infected = dict()

    p_infect = 0.0

    def __init__(self, params):
        self.network = NG(params['X'], params['Y'], params['DELTA'])
        first_infected = self.set_initial_infected()
        self.p_infect = params['BETA']
        self.susceptible = {self.network.get_nodes_list()}
        self.infected = {self.network.get_nodes_with_attr("infected", True)}

    def set_initial_infected(self):
        d_min = 1
        first_infected = 0
        nodes = self.network.get_nodes()
        X = self.network.get_Map_X()
        Y = self.network.get_Map_Y()
        for n in nodes:
            x, y = nodes[n]
            d = (x - X / 2) ** 2 + (y - Y / 2) ** 2
            if d < d_min:
                first_infected = n
                d_min = d
        self.network.set_node_attr({first_infected: True}, "infected")
        return first_infected

    def infect(self, t, e):
        pass
