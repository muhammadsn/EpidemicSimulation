from Simulator import Simulator
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def paper_1(t, n=2500, beta=0.1, _r_0=2.5, _delta=1):
    sqrt_n = np.sqrt(n)
    frac_1 = (sqrt_n - 1) / (sqrt_n + 1)
    frac_power = (2 * beta * (np.sqrt(_delta * np.pi) * _r_0) ** 3 * t) / sqrt_n
    frac_power = - frac_power
    e_to_the_power = np.exp(frac_power)
    denominator = e_to_the_power * frac_1 + 1

    return n * ((2 / denominator) - 1) ** 2


def paper_2(t, n=2500, beta=0.1, _r_0=2.5, _delta=1, _n=50):
    sqrt_n = np.sqrt(n)
    frac_1 = (sqrt_n - 1) / (sqrt_n + 1)
    frac_power = (2 * beta * (np.sqrt(_delta * np.pi) * _r_0 * _n) * t) / sqrt_n
    frac_power = - frac_power
    e_to_the_power = np.exp(frac_power)
    denominator = e_to_the_power * frac_1 + 1

    return n * ((2 / denominator) - 1) ** 2


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
        # plt.plot(df['t'].tolist(), df[f'b{b}'].tolist(), label=f'BETA = {b}', color=colors[beta_vals.index(b)])

    # plt.legend()
    # plt.show()



if __name__ == '__main__':
    # runner()
    #
    vec_func1 = np.vectorize(paper_1)
    vec_func2 = np.vectorize(paper_2)
    x = np.array(range(100))
    y1 = vec_func1(x)
    y2 = vec_func2(x)

    plt.plot(x, y1)
    plt.plot(x, y2)
    plt.show()