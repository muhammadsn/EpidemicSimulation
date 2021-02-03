from Simulator import Simulator


def main():
    params = dict()
    params['X'] = 30
    params['Y'] = 30
    params['DELTA'] = 0.5
    params['BETA'] = 0.1                    # Infection Rate (P_INFECT)
    params['TransmissionRate'] = 5          # Mean Node Degree
    params['NetworkGenAlg'] = 'BA'          # The Algorithm to generate network ['BA', 'ER', 'RA']

    a = Simulator(params=params)
    # print(rc['results'])


if __name__ == '__main__':
    main()