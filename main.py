from Simulator import Simulator
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def formula_in_paper_1(t, n=5000, r_0=5, beta=0.8, delta=0.25):
    a = np.sqrt(n)
    b = (a - 1) / (a + 1)
    c = -((2 * beta * (np.sqrt(delta * np.pi) * r_0) ** 3 * t) / a)
    d = np.exp(c)
    e = d * b + 1
    return n * ((2 / e) - 1) ** 2


def formula_in_paper_2(t, n=5000, r_0=5, beta=0.8, delta=0.25, eta=19):
    a = np.sqrt(n)
    b = (a - 1) / (a + 1)
    c = -((2 * beta * (np.sqrt(delta * np.pi) * r_0 * eta) * t) / a)
    d = np.exp(c)
    e = d * b + 1
    return n * ((2 / e) - 1) ** 2


def runner():
    iterations = 50
    params = dict()
    params['X'] = 100                       # Width of Experiment Area
    params['Y'] = 200                       # Length of Experiment Area
    params['DELTA'] = 0.25                  # Density of population in Area Unit
    params['BETA'] = 0.1                    # Infection Rate (P_INFECT)
    params['R0'] = 5                        # Radius
    params['MaxTimeSteps'] = 120            # Maximum Time steps to track node infection process
    colors = ['red', 'green', 'blue']
    beta_vals = [0.1, 0.5, 0.8]

    a = Simulator(params=params)
    df = pd.DataFrame(columns=['t', 'b0.1', 'b0.5', 'b0.8'])
    df['t'] = np.arange(0, params['MaxTimeSteps'])
    df['b0.1'] = df['b0.5'] = df['b0.8'] = 0.0

    for b in beta_vals:
        for i in range(iterations):
            print(f"[Iteration = {i}| BETA = {b}]==================")
            a.simulate(monitor=False, beta=b)
            result = a.get_results()
            df[f'b{b}'] += result['i']
        df[f'b{b}'] = df[f'b{b}'] / iterations
        df.to_json('results.json', orient='table')




if __name__ == '__main__':
    runner()

    res = pd.read_json('results.json', orient="table")
    plt.plot(res['t'], res['b0.1'], label=r'My Simulation $\beta$ = 0.1', color='red')
    plt.plot(res['t'], res['b0.5'], label=r'My Simulation $\beta$ = 0.5', color='green')
    plt.plot(res['t'], res['b0.8'], label=r'My Simulation $\beta$ = 0.8', color='blue')

    vec_func1 = np.vectorize(formula_in_paper_1)
    vec_func2 = np.vectorize(formula_in_paper_2)
    x = np.array(range(120))
    y1 = vec_func1(x)
    y2 = vec_func2(x)

    plt.plot(x, y1, label="First Paper Formula", color="teal")
    plt.plot(x, y2, label="Second Paper Formula", color="orange")

    plt.xlabel("Time")
    plt.ylabel("Infected")
    # plt.title(r"I(t) curves for different values of $\beta$")
    plt.title(r"I(t) curves for $\beta$ = 0.8")
    plt.grid(axis='y')
    plt.legend()
    plt.show()