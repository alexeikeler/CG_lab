import numpy as np


# Функція з варіанта №16.
# Спочатку ми намагаємося обчислити значення для масиву у
# за допомогою векторизованих операцій із бібліотеки numpy.
# Якщо відбувається помилка в процесі обчислення,
# її перехоплює блок except виводить відповідне повідомлення
# та повертає None.
def function(x: np.ndarray, b: float):# -> np.ndarray | None:

    try:
        y = 15.28 * np.power(np.abs(x), -1.5) + np.cos(np.log(np.abs(x)) + b)
        return y

    except Exception as e:
        print(f'Error in function evaluation:\n{repr(e)}')
        return None