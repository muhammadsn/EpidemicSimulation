import numpy as np
from scipy.integrate import odeint
from NetworkGen import NetworkGenerator as ng

class Simulator:
    N = 0
    susceptible = 0
    infected = 0
    p_infect = 0.0

    def __init__(self, params):
        self.N = params['X']

        




    def infect(self, t, e):
