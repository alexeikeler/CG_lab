import matplotlib.markers
from typing import List
from matplotlib import pyplot as plt


# Клас для стандартних значень,
# які виставляються при запуску програми.
class Defaults:

    UI_PATH: str = 'ui/lab1_main_window.ui'

    WINDOW_TITLE: str = 'Лабораторная работа № 1'

    FUNCTION_NAME: str = 'y = 15.28 * |x|^(-1.5) + cos(ln(|x|) + '

    MIN_START_SB_VAL: float = -100.0
    MAX_START_SB_VAL: float = 100.0
    DEFAULT_START_SB_VAL: float = 1.23

    MIN_END_SB_VAL: float = -100
    MAX_END_SB_VAL: float = 100
    DEFAULT_END_SB_VAL: float = -2.4

    MIN_STEP_SB_VAL: int = -10.0
    MAX_STEP_SB_VAL: int = 100.0
    DEFAULT_STEP_SB_VAL: int = -0.06

    MIN_B_COEF_SB_VAL: float = -100.0
    MAX_B_COEF_SB_VAL: float = 100.0
    DEFAULT_B_COEF_SB_VAL: float = 12.6

    MIN_POINT_SIZE = 1
    MAX_POINT_SIZE = 100
    DEFAULT_POINT_SIZE = 10

    DEFAULT_PLOT_COLOR: str = 'blue'
    DEFAULT_PLOT_TYPE: str = 'seaborn'
    DEFAULT_POINT_STYLE: str = 'o'

    DEFAULT_PLOT_TITLE: str = 'Function graph'
    DEFAULT_PLOT_XLABEL: str = 'x'
    DEFAULT_PLOT_YLABEL: str = 'y'

    POINT_COLORS: tuple = (
        'blue', 'red', 'green', 'cyan',
        'magenta', 'yellow', 'black', 'white'
    )

    POINT_STYLES: List[str] = matplotlib.markers.MarkerStyle.filled_markers
    PLOT_STYLES: List[str] = plt.style.available
