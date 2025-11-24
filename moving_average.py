import numpy as np

def moving_average(signal, window_size):

    k = (window_size - 1) // 2
    n = signal.shape[0]

    new_signal = np.zeros(n)

    for i in range(n):
        low_bound = max(0, i - k)
        upper_bound = min(n, i + k + 1) 

        window = signal[low_bound:upper_bound]
        avg_value = np.mean(window)

        new_signal[i] = avg_value

    return new_signal


