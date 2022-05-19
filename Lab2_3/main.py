# Підключаємо необхідні бібліотеки
import numpy as np
import sys
import matplotlib

from matplotlib import pyplot as plt
# noinspection PyUnresolvedReferences
from matplotlib.backends.backend_qt5agg import FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
# noinspection PyUnresolvedReferences
from PyQt5 import uic, QtWidgets

from src.config import Config
from src.function import function
from src.plotter import Plotter

# Вказуємо шлях до головної форми
main_window_ui = Config.UI_PATH
form, base = uic.loadUiType(uifile=main_window_ui)
matplotlib.use("QT5Agg")


# Клас основної форми
class Application(form, base):

    def __init__(self):

        super(base, self).__init__()
        self.setupUi(self)

        self.__setup_config()

        self.__connect_canvas()
        self.__connect_buttons()
        self.__connect_combo_boxes()

        self.colormap = Config.COLORMAPS[0]
        self.line_type = Config.LINE_TYPES[0]

    # налаштування значень за замовчуванням
    def __setup_config(self):

        self.x_left_border_dsb.setMinimum(Config.MIN_X_LEFT_BORDER)
        self.x_left_border_dsb.setMaximum(Config.MAX_X_LEFT_BORDER)
        self.x_left_border_dsb.setValue(Config.DEFAULT_X_LEFT_BORDER)

        self.x_right_border_dsb.setMinimum(Config.MIN_X_RIGHT_BORDER)
        self.x_right_border_dsb.setMaximum(Config.MAX_X_RIGHT_BORDER)
        self.x_right_border_dsb.setValue(Config.DEFAULT_X_RIGHT_BORDER)

        self.x_step_dsb.setMinimum(Config.MIN_X_STEP)
        self.x_step_dsb.setMaximum(Config.MAX_X_STEP)
        self.x_step_dsb.setValue(Config.DEFAULT_X_STEP)

        self.y_left_border_dsb.setMinimum(Config.MIN_Y_LEFT_BORDER)
        self.y_left_border_dsb.setMaximum(Config.MAX_Y_LEFT_BORDER)
        self.y_left_border_dsb.setValue(Config.DEFAULT_Y_LEFT_BORDER)

        self.y_right_border_dsb.setMinimum(Config.MIN_Y_RIGHT_BORDER)
        self.y_right_border_dsb.setMaximum(Config.MAX_Y_RIGHT_BORDER)
        self.y_right_border_dsb.setValue(Config.DEFAULT_Y_RIGHT_BORDER)

        self.y_step_dsb.setMinimum(Config.MIN_Y_STEP)
        self.y_step_dsb.setMaximum(Config.MAX_Y_STEP)
        self.y_step_dsb.setValue(Config.DEFAULT_Y_STEP)

    # Створення полотна фігури та сітки, підключення до віджета.
    def __connect_canvas(self):

        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        self.toolbar = NavigationToolbar(self.canvas, self)

        lay = QtWidgets.QVBoxLayout(self.contour_widget)
        lay.addWidget(self.toolbar)
        lay.addWidget(self.canvas)

        self.plotter = Plotter(self.figure, Config.GRIDSPEC_N, Config.GRIDSPEC_M)

    # Підключення кнопок до функцій обробки
    def __connect_buttons(self) -> None:

        self.draw_button.clicked.connect(
            self.process_draw_button_clicked
        )

    # Підключення і заповнення комбо - боксів
    def __connect_combo_boxes(self) -> None:

        self.colormap_combo_box.addItems(
            Config.COLORMAPS
        )

        self.colormap_combo_box.activated[str].connect(
            self.__set_colormap
        )

        self.line_style_combo_box.addItems(
            Config.LINE_TYPES
        )

        self.line_style_combo_box.activated[str].connect(
            self.__set_line_type
        )

    # Обробники подій для зміни кольору графіків, стилю лінії та маркування.
    def __set_colormap(self, colormap: str) -> None:
        self.colormap = colormap

    def __set_line_type(self, line_type: str) -> None:
        self.line_type = line_type

    def __fill_contour_status(self) -> bool:
        return self.fill_contour_check_box.isChecked()

    # Обробник подій для натискання кнопки draw_button (Draw).
    def process_draw_button_clicked(self) -> None:
        
        # Зчитування значень із боксів.
        xl, xr, xst = self.x_left_border_dsb.value(), self.x_right_border_dsb.value(), self.x_step_dsb.value()
        yl, yr, yst = self.y_left_border_dsb.value(), self.y_right_border_dsb.value(), self.y_step_dsb.value()
        fill_ctr = self.__fill_contour_status()

        # Створення масивів із координатами.
        x, y = np.arange(xl, xr, xst), np.arange(yl, yr, yst)
        x_mesh, y_mesh = np.meshgrid(x, y)
        z = function(x_mesh, y_mesh)

        # Процес малювання.
        self.figure.clf()

        self.plotter.handmade_contour(
            x,
            y,
            z,
            self.line_type,
            Config.CONTOUR_PLOT_X_LABEL,
            Config.CONTOUR_PLOT_Y_LABEL,
            Config.CONTOUR_PLOT_TITLE,
            self.colormap,
            fill_ctr
        )

        self.plotter.plot_surface(
            x_mesh,
            y_mesh,
            z,
            self.colormap,
            Config.PLOT_3D_X_LABEL,
            Config.PLOT_3D_Y_LABEL,
            Config.PLOT_3D_Z_LABEL,
            Config.PLOT_3D_TITLE
        )

        self.canvas.draw()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    app_win = Application()
    app_win.show()
    sys.exit(app.exec_())
