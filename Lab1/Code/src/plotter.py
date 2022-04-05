import numpy as np
from matplotlib import pyplot as plt


class Plotter:

    @staticmethod
    def plot_function(canvas, figure,
                      x: np.ndarray, y: np.ndarray,
                      start: float, end: float,
                      plot_point_style: str, color_: str,
                      label_: str, point_size: int,
                      xlabel_: str, ylabel_: str,
                      type_: str) -> None:

        # Установка типу графіка
        plt.style.use(type_)

        # Якщо кількість елементів масивів x та y по-різному порушуємо помилку.
        if x.shape != y.shape:
            raise ValueError('x and y must have same shape and number of elements!')

        # Очистка графіка
        figure.clf()

        # Малюємо координатні осі
        plt.axhline(y=0, c='black')
        plt.axvline(x=0, c='black')


        # Малюємо функцію із заданими параметрами
        crds = zip(x,y)

        for coord_x, coord_y in crds:
            plt.scatter(coord_x, coord_y, color=color_, s=point_size, marker=plot_point_style)

        # Установка титульного значення та міток по осі X та Y та легенди
        plt.title(label_)
        plt.xlabel(xlabel_)
        plt.ylabel(ylabel_)
        #plt.legend()

        # Установка титульного значення та міток по осі X та Y та легенди
        plt.xlim(end, start)
        plt.ylim(min(y), max(y))

        # Масштаб графіка
        plt.yscale('symlog', linthresh=0.01)

        # Вміщення графіка на полотно
        plt.tight_layout()

        # Виведення графіка на полотні
        canvas.draw()
