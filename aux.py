import numpy as np


def calculate_mse(estimated_parameters, true_parameter):
    estimated_parameters = np.array(estimated_parameters)
    n = estimated_parameters.shape[0]

    res = 0

    for i in range(n):
        res += (estimated_parameters[i] - true_parameter) ** 2

    return res
