import numpy as np

def count_values_in_bins(data, bin_edges):

    temp = np.zeros(bin_edges.shape[0] - 1)

    for i in range(1, len(bin_edges)):
        bin_0 = bin_edges[i - 1]
        bin_1 = bin_edges[i]

        print(f"bin is {bin_0} bin_1 {bin_1}")

        for j in range(len(data)):
            if i == len(bin_edges)-1:
                if data[j] >= bin_0 and data[j] <= bin_1:
                    temp[i - 1] += 1
            else:
                if data[j] >= bin_0 and data[j] < bin_1:
                    temp[i - 1] += 1
    return temp