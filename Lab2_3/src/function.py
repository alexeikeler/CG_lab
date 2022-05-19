import numpy as np
from typing import Optional


def function(x: np.ndarray, y: np.ndarray) -> Optional[np.ndarray]:

    try:
        z = 15.28 * np.power(np.abs(x), -1.5) + np.cos(np.log(np.abs(x)) + y)
        return z

    except Exception as e:
        print(f'Error in function evaluation:\n{repr(e)}')
        return None
