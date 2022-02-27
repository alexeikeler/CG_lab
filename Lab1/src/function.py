import numpy as np


def function(x: np.ndarray, b: float) -> np.ndarray | None:

    try:
        y = 15.28 * np.power(np.abs(x), -1.5) + np.cos(np.log(np.abs(x)) + b)
        return y
    except Exception as e:
        print(f'Error in function evaluation:\n{repr(e)}')
        return None
