from NetworkGen import NetworkGenerator as ng
# from SIMonitor import MonitoredSI


def main():
    param = dict()
    param['X'] = 30
    param['Y'] = 30
    param['DELTA'] = 0.5
    param['BETA'] = 0.1                    # Infection Rate (P_INFECT)
    param['TransmissionRate'] = 5          # Mean Node Degree
    param['NetworkGenAlg'] = 'BA'          # The Algorithm to generate network ['BA', 'ER', 'RA']

    a = ng()
    # print(rc['results'])


if __name__ == '__main__':
    main()