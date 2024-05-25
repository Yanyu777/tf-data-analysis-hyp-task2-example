import pandas as pd
import numpy as np
from scipy.stats import ks_2samp


chat_id = 775883383 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    ks_stat, p_value = ks_2samp(x.flatten(), y.flatten())
    alpha = 0.1
    
    return p_value < alpha # Ваш ответ, True или False

historical_data = pd.read_csv('/content/drive/MyDrive/Master/Master2/DataAnalysis/HW/HW9/historical_data.csv').values[:, 1:]
modified_data_type_1 = pd.read_csv('/content/drive/MyDrive/Master/Master2/DataAnalysis/HW/HW9/modified_data_of_type_1.csv').values[:, 1:]
modified_data_type_2 = pd.read_csv('/content/drive/MyDrive/Master/Master2/DataAnalysis/HW/HW9/modified_data_of_type_2.csv').values[:, 1:]
modified_data_type_3 = pd.read_csv('/content/drive/MyDrive/Master/Master2/DataAnalysis/HW/HW9/modified_data_of_type_3.csv').values[:, 1:]

result_type_0 = solution(historical_data, historical_data)
result_type_1 = solution(historical_data, modified_data_type_1)
result_type_2 = solution(historical_data, modified_data_type_2)
result_type_3 = solution(historical_data, modified_data_type_3)

print("Historical vs Historical:", result_type_0)
print("Historical vs Modified Type 1:", result_type_1)
print("Historical vs Modified Type 2:", result_type_2)
print("Historical vs Modified Type 3:", result_type_3)
