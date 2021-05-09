import numpy as np
import scipy.stats as sts


def estimate_stddev_of_normal_distribution(sample):
    sample = np.array(sample)
    n = sample.shape[0]

    sample.sort()

    middle = n / 2
    up_to = int(np.floor(middle))

    standard_normal_ppf = sts.norm(loc=0, scale=1).ppf

    res = 0
    denominator = 0

    for i in range(1, up_to):
        res += sample[n - i - 1] - sample[i]
        denominator += standard_normal_ppf((n - i - 1) / n) - standard_normal_ppf(i / n)

    res /= denominator

    return res
