# Підключаємо необхідні бібліотеки
import numpy as np
import sys
import matplotlib

from typing import Tuple
from matplotlib import pyplot as plt
# noinspection PyUnresolvedReferences
from matplotlib.backends.backend_qt5agg import FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
# noinspection PyUnresolvedReferences
from PyQt5 import uic, QtWidgets

from src.plotter import Plotter
from src.default_values import Defaults
from src.function import function

# Вказуємо шлях до головної форми
uimain = Defaults.UI_PATH
form, base = uic.loadUiType(uifile=uimain)
matplotlib.use("QT5Agg")


class MainWindow(form, base):

    def __init__(self):

        super(base, self).__init__()
        self.setupUi(self)

        # вказуємо стиль, тип та колір графіка
        self.plot_point_style = Defaults.DEFAULT_POINT_STYLE
        self.plot_type = Defaults.DEFAULT_PLOT_TYPE
        self.plot_color = Defaults.DEFAULT_PLOT_COLOR

        # У наступних класах ми підключаємо до форми віджети
        # та виставляємо значення за замовчуванням
        self.__setup_default_gui_values()
        self.__connect_canvas()
        self.__connect_widgets()

        # Вказуємо назву вікна основної форми
        self.setWindowTitle(Defaults.WINDOW_TITLE)

    def __connect_canvas(self) -> None:

        # створюємо область для малювання,
        # місце на якому функція буде намальована
        # і меню з інструментами
        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        self.toolbar = NavigationToolbar(self.canvas, self)

        lay = QtWidgets.QVBoxLayout(self.plot_widget)
        lay.addWidget(self.toolbar)
        lay.addWidget(self.canvas)

    def __connect_widgets(self) -> None:

        # Приєднуємо віджети до їх обробників
        self.plot_graph_button.clicked.connect(self.process_draw_button_click)

        self.line_color_combo_box.activated[str].connect(self.__set_line_color)
        self.point_types_combobox.activated[str].connect(self.__set_plot_point_style)
        self.plot_style_combo_box.activated[str].connect(self.__set_plot_style)

    def __setup_default_gui_values(self) -> None:

        # Виставляємо значення за замовчуванням для віджетів

        # У текстовому полі вводимо функцію для варіанта №16
        self.function_body_text_edit.setPlainText(Defaults.FUNCTION_NAME + '12.60)')

        # Задаємо мінімальне, максимальне значення за замовчуванням для
        # початку інтервалу
        self.start_spinbox.setMinimum(Defaults.MIN_START_SB_VAL)
        self.start_spinbox.setMaximum(Defaults.MAX_START_SB_VAL)
        self.start_spinbox.setValue(Defaults.DEFAULT_START_SB_VAL)

        # Задаємо мінімальне значення, максимальне значення,
        # та значення за замовчуванням для кінця інтервалу
        self.end_spinbox.setMinimum(Defaults.MIN_END_SB_VAL)
        self.end_spinbox.setMaximum(Defaults.MAX_END_SB_VAL)
        self.end_spinbox.setValue(Defaults.DEFAULT_END_SB_VAL)

        # Задаємо мінімальне значення, максимальне значення
        # та значення за замовчуванням
        # для кроку графіка
        self.step_spinbox.setMinimum(Defaults.MIN_STEP_SB_VAL)
        self.step_spinbox.setMaximum(Defaults.MAX_STEP_SB_VAL)
        self.step_spinbox.setValue(Defaults.DEFAULT_STEP_SB_VAL)

        # Задаємо мінімальне значення, максимальне значення
        # та значення за замовчуванням
        # для коефіцієнту b
        self.b_value_spinbox.setMinimum(Defaults.MIN_B_COEF_SB_VAL)
        self.b_value_spinbox.setMaximum(Defaults.MAX_B_COEF_SB_VAL)
        self.b_value_spinbox.setValue(Defaults.DEFAULT_B_COEF_SB_VAL)

        self.point_size_spinbox.setMinimum(Defaults.MIN_POINT_SIZE)
        self.point_size_spinbox.setMaximum(Defaults.MAX_POINT_SIZE)
        self.point_size_spinbox.setValue(Defaults.DEFAULT_POINT_SIZE)

        # Встановлення допустимих значень для кольорів функції
        self.line_color_combo_box.addItems(
            Defaults.POINT_COLORS
        )

        # Встановлення допустимих значень
        # для вигляду графіка функції
        self.point_types_combobox.addItems(
            Defaults.POINT_STYLES
        )

        # Встановлення допустимих значень для виду полотна
        self.plot_style_combo_box.addItems(
            Defaults.PLOT_STYLES
        )

        # Встановлюємо тип графіка вибраний у комбобоксі
        self.plot_style_combo_box.setCurrentText(
            self.plot_type
        )

    # Наступні три функції є оборотниками подій,
    # що укладаються у:
    # 1. Виборі кольору для графіка функціїю
    # 2. Виду лінії функції.
    # 3. Загального вигляду графіка.
    def __set_line_color(self, line_color: str) -> None:
        self.plot_color = line_color

    def __set_plot_point_style(self, plot_point_style: str) -> None:
        self.plot_point_style = plot_point_style

    def __set_plot_style(self, plot_type: str) -> None:
        self.plot_type = plot_type

    def __get_func_values(self) -> Tuple[np.ndarray, np.ndarray, float]:

        # Тут ми отримуємо початок та кінець інтервалу для графіка,
        # а також його крок.
        start: float = self.start_spinbox.value()
        end: float = self.end_spinbox.value()
        step: float = self.step_spinbox.value()
        b_coefficient: float = self.b_value_spinbox.value()

        # Формуємо масиви, що відповідають координатам точок.
        # Масив х створюємо за допомогою функції np.arange()
        # в яку передаємо початок, кінець та крок інтервалу.
        # Масив y створюємо шляхом передачі масиву х у функцію function
        # яка є функцією з варіанту № 16.
        x: np.ndarray = np.arange(start, end, step, dtype='float32')
        y: np.ndarray = function(x, b_coefficient)

        return x, y, b_coefficient

    def __perform_plotting(self) -> None:

        # Oтримуємо масиви з координатами х та у.
        x, y, b = self.__get_func_values()

        # За допомогою класу Plotter та його методу plot_function
        # малюємо нашу функцію із зазначеними параметрами.
        temp = Defaults.FUNCTION_NAME + f'{b})'
        self.function_body_text_edit.setPlainText(temp)

        Plotter.plot_function(
            self.canvas, self.figure,
            x, y,
            self.start_spinbox.value(), self.end_spinbox.value(),
            self.plot_point_style, self.plot_color,
            temp, self.point_size_spinbox.value(),
            Defaults.DEFAULT_PLOT_XLABEL, Defaults.DEFAULT_PLOT_YLABEL,
            self.plot_type
        )

    # Функція обробки натискання на кнопку Draw.
    def process_draw_button_click(self) -> None:
        self.__perform_plotting()


if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
