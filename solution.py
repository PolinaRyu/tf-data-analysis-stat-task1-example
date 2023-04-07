import pandas as pd
import numpy as np
from scipy import stats


chat_id = 503882767 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> float:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    x = x*2/43/43 - stats.laplace.rvs(size=len(x))
    return x.mean() # Ваш ответ
