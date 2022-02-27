import numpy as np
import sys
import matplotlib

from typing import Tuple
from matplotlib import pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar

from PyQt5 import uic, QtWidgets

from src.plotter import Plotter
from src.default_values import Defaults
from src.function import function

uimain = Defaults.UI_PATH
form, base = uic.loadUiType(uifile=uimain)
matplotlib.use("QT5Agg")


class MainWindow(form, base):

    def __init__(self):

        super(base, self).__init__()
        self.setupUi(self)

        self.plot_style = Defaults.DEFAULT_PLOT_STYLE
        self.plot_type = Defaults.DEFAULT_PLOT_TYPE
        self.plot_color = Defaults.DEFAULT_PLOT_COLOR

        self.__setup_default_gui_values()
        self.__connect_canvas()
        self.__connect_widgets()

        self.setWindowTitle(Defaults.WINDOW_TITLE)

    def __connect_canvas(self):

        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        self.toolbar = NavigationToolbar(self.canvas, self)

        lay = QtWidgets.QVBoxLayout(self.plot_widget)
        lay.addWidget(self.toolbar)
        lay.addWidget(self.canvas)

    def __connect_widgets(self) -> None:

        self.plot_graph_button.clicked.connect(self.process_draw_button_click)

        self.line_color_combo_box.activated[str].connect(self.__set_line_color)
        self.line_style_combo_box.activated[str].connect(self.__set_line_style)
        self.plot_style_combo_box.activated[str].connect(self.__set_plot_style)

    def __setup_default_gui_values(self):

        self.function_body_text_edit.setPlainText(Defaults.FUNCTION_NAME)

        self.start_spinbox.setMinimum(Defaults.MIN_START_SB_VAL)
        self.start_spinbox.setMaximum(Defaults.MAX_START_SB_VAL)
        self.start_spinbox.setValue(Defaults.DEFAULT_START_SB_VAL)

        self.end_spinbox.setMinimum(Defaults.MIN_END_SB_VAL)
        self.end_spinbox.setMaximum(Defaults.MAX_END_SB_VAL)
        self.end_spinbox.setValue(Defaults.DEFAULT_END_SB_VAL)

        self.step_spinbox.setMinimum(Defaults.MIN_STEP_SB_VAL)
        self.step_spinbox.setMaximum(Defaults.MAX_STEP_SB_VAL)
        self.step_spinbox.setValue(Defaults.DEFAULT_STEP_SB_VAL)

        self.line_color_combo_box.addItems(
            Defaults.PLOT_LINE_COLORS
        )
        self.line_style_combo_box.addItems(
            Defaults.PLOT_LINE_STYLES.keys()
        )
        self.plot_style_combo_box.addItems(
            Defaults.PLOT_STYLES
        )
        self.plot_style_combo_box.setCurrentText(
            self.plot_type
        )

    def __set_line_color(self, line_color: str):
        self.plot_color = line_color

    def __set_line_style(self, line_style: str):
        self.plot_style = Defaults.PLOT_LINE_STYLES[line_style]

    def __set_plot_style(self, plot_type: str):
        self.plot_type = plot_type

    def __get_func_values(self) -> Tuple[np.ndarray, np.ndarray]:

        b: float = 12.6
        start: float = self.start_spinbox.value()
        end: float = self.end_spinbox.value()
        step: float = self.step_spinbox.value()

        x: np.ndarray = np.arange(start, end, step, dtype='float32')
        y: np.ndarray = function(x, b)

        return x, y

    def __perform_plotting(self):

        x, y = self.__get_func_values()
        print(x, y)
        Plotter.plot_function(
            self.canvas, self.figure,
            x, y,
            self.start_spinbox.value(), self.end_spinbox.value(),
            self.plot_style, self.plot_color,
            Defaults.FUNCTION_NAME,Defaults.DEFAULT_PLOT_TITLE,
            Defaults.DEFAULT_PLOT_XLABEL, Defaults.DEFAULT_PLOT_YLABEL,
            self.plot_type
        )

    def process_draw_button_click(self):
        self.__perform_plotting()


if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
