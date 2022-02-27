import numpy as np
from matplotlib import pyplot as plt


class Plotter:

    @staticmethod
    def plot_function(canvas, figure,
                      x: np.ndarray, y: np.ndarray,
                      start: float, end: float,
                      line_style: str, color_: str,
                      label_: str, title_: str,
                      xlabel_: str, ylabel_: str,
                      type_: str) -> None:

        # Установка типа графика
        plt.style.use(type_)

        # Если количество элементов массивов x и y различно возбужаем ошибку.
        if x.shape != y.shape:
            raise ValueError('x and y must have same shape and number of elements!')

        # Очистка графика
        figure.clf()
        # Рисуем функцию с задаными параметрами
        plt.plot(x, y, line_style, color=color_, label=label_)

        # Установка титульного значения и меток по оси X и Y и легенды
        plt.title(title_)
        plt.xlabel(xlabel_)
        plt.ylabel(ylabel_)
        plt.legend()

        # Установка граничных значения по осям X и Y при начальном отображении графика
        plt.xlim(end, start)
        plt.ylim(min(y), max(y))

        # Масштаб графика
        plt.yscale('symlog', linthresh=0.01)

        # Умещение графика на холст
        plt.tight_layout()

        # Вывод графика на холсте
        canvas.draw()
