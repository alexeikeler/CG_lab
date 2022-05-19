from dataclasses import dataclass
from typing import Tuple


# Клас, який містить значення за замовчуванням.
@dataclass
class Config:

    UI_PATH: str = 'ui/lab2_app.ui'

    DEFAULT_X_LEFT_BORDER: float = -2.0
    MIN_X_LEFT_BORDER: float = -100.0
    MAX_X_LEFT_BORDER: float = 100.0

    DEFAULT_X_RIGHT_BORDER: float = -1.0
    MIN_X_RIGHT_BORDER: float = -100.0
    MAX_X_RIGHT_BORDER: float = 100.0

    DEFAULT_X_STEP: float = 0.1
    MIN_X_STEP: float = 0.0
    MAX_X_STEP: float = 100.0

    DEFAULT_Y_LEFT_BORDER: float = -2.0
    MIN_Y_LEFT_BORDER: float = -100.0
    MAX_Y_LEFT_BORDER: float = 100.0

    DEFAULT_Y_RIGHT_BORDER: float = -1.0
    MIN_Y_RIGHT_BORDER: float = -100.0
    MAX_Y_RIGHT_BORDER: float = 100.0

    DEFAULT_Y_STEP: float = 0.1
    MIN_Y_STEP: float = 0.0
    MAX_Y_STEP: float = 100.0

    DEFAULT_LL_LEFT_BORDER: float = -1.0
    MIN_LL_LEFT_BORDER: float = -10.0
    MAX_LL_LEFT_BORDER: float = 10.0

    DEFAULT_LL_RIGHT_BORDER: float = 1.0
    MIN_LL_RIGHT_BORDER: float = -10.0
    MAX_LL_RIGHT_BORDER: float = 10.0

    DEFAULT_LL_STEP: float = 0.1
    MIN_LL_STEP: float = 0.01
    MAX_LL_STEP: float = 100.0

    GRIDSPEC_N: int = 3
    GRIDSPEC_M: int = 3

    COLORMAPS: Tuple[str] = (
        'Greys', 'Purples', 'Blues', 'Greens', 'Oranges', 'Reds'
    )

    LINE_TYPES: Tuple[str] = ('-', '--', '-.', '.')

    CONTOUR_PLOT_X_LABEL: str = 'x'
    CONTOUR_PLOT_Y_LABEL: str = 'z'
    CONTOUR_PLOT_TITLE: str = r'$\mathrm{f(x, y) = 15.28*|x|^{-1.5} + cos(ln(|x|) + y)}$'

    COLORBAR_TITLE: str = 'f(x,y) values'
    COLORBAR_XAXIS_TICK_PADDING: int = 15

    PLOT_3D_X_LABEL: str = 'x'
    PLOT_3D_Y_LABEL: str = 'y'
    PLOT_3D_Z_LABEL: str = 'z'
    PLOT_3D_TITLE: str = r'$\mathrm{f(x, y) = 15.28*|x|^{-1.5} + cos(ln(|x|) + y)}$'



