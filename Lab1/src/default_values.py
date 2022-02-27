from dataclasses import dataclass
from matplotlib import pyplot as plt


#@dataclass
class Defaults:

    UI_PATH: str = 'ui/lab1_main_window.ui'

    WINDOW_TITLE: str = 'Лабораторная работа № 1'

    FUNCTION_NAME: str = '15.28 * |x|^(-1.5) + cos(ln(|x|) + b'

    MIN_START_SB_VAL: float = -100.0
    MAX_START_SB_VAL: float = 100.0
    DEFAULT_START_SB_VAL: float = 1.23

    MIN_END_SB_VAL: float = -100
    MAX_END_SB_VAL: float = 100
    DEFAULT_END_SB_VAL: float = -2.4

    MIN_STEP_SB_VAL: int = -10.0
    MAX_STEP_SB_VAL: int = 100.0
    DEFAULT_STEP_SB_VAL: int = -0.06

    DEFAULT_PLOT_COLOR: str = 'blue'
    DEFAULT_PLOT_STYLE: str = '-'
    DEFAULT_PLOT_TYPE: str = 'seaborn'
    DEFAULT_PLOT_TITLE: str = 'Function graph'
    DEFAULT_PLOT_XLABEL: str = 'x'
    DEFAULT_PLOT_YLABEL: str = 'y'

    PLOT_LINE_STYLES: dict = {
        'Solid line style': '-',
        'Dashed line style': '--',
        'Dash-dot line style': '-.',
        'Dotted line style': ':'
    }

    PLOT_LINE_COLORS: tuple = (
        'blue', 'red', 'green', 'cyan',
        'magenta', 'yellow', 'black', 'white'
    )

    PLOT_STYLES: tuple = tuple(
        plt.style.available
    )
