import numpy as np

def clean_and_scale_scores(scores, min_score, max_score):
    temp_array = scores.astype(float)
    if scores.ndim == 1:
        for i in range(len(scores)):
            temp = temp_array[i]
            if temp > max_score:
                temp_array[i] = max_score
            elif temp < min_score:
                temp_array[i] = min_score
            temp_array[i] = (temp_array[i] - min_score) / (max_score - min_score)
        return temp_array
    elif scores.ndim == 2:
        for i in range(scores.shape[0]):
            for j in range(scores.shape[1]):
                temp = temp_array[i, j]
                if temp > max_score:
                    temp_array[i, j] = max_score
                elif temp < min_score:
                    temp_array[i, j] = min_score
                temp_array[i, j] = (temp_array[i, j] - min_score) / (max_score - min_score)
        return temp_array