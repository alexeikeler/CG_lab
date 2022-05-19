import numpy as np
import matplotlib.gridspec as gridspec
from matplotlib import pyplot as plt


# Клас для малювання
class Plotter:

    def __init__(self, fig, gridspec_n: int, gridspec_m: int):
        self.fig = fig
        self.gs = gridspec.GridSpec(gridspec_n, gridspec_m)

    def handmade_contour(
            self,
            x: np.ndarray,
            y: np.ndarray,
            z: np.ndarray,
            line_type: str,
            xlabel: str,
            ylabel: str,
            title: str,
            colormap: str,
            fill_ctr: bool
    ) -> None:

        ax = self.fig.add_subplot(self.gs[:, :2])
        length = len(z)

        colormaps = {
            "Greys": plt.cm.Greys(np.linspace(0, 1, length)),
            "Purples": plt.cm.Purples(np.linspace(0, 1, length)),
            "Blues": plt.cm.Blues(np.linspace(0, 1, length)),
            "Greens": plt.cm.Greens(np.linspace(0, 1, length)),
            "Oranges": plt.cm.Oranges(np.linspace(0, 1, length)),
            "Reds": plt.cm.Reds(np.linspace(0, 1, length))
        }

        colors = colormaps.get(colormap)

        for i, sub_array in enumerate(z):
            ax.plot(x, sub_array, line_type, color=colors[i])

        # Якщо параметр fill_ctr = True - зафарбовуємо область утворену лініями
        if fill_ctr:
            for i in range(length-1):
                plt.fill_between(x, z[i], z[i + 1], color=colors[i], alpha=0.6)

        ax.set_xlabel(xlabel)
        ax.set_ylabel(ylabel)
        ax.set_title(title)

        ax.set_xlim(np.min(x), np.max(x))
        ax.set_ylim(np.min(z), np.max(z))

        ax.grid()

    # метод класу для малювання тривимірного графіка
    def plot_surface(
            self,
            x: np.ndarray,
            y: np.ndarray,
            z: np.ndarray,
            colormap: str,
            xlabel: str,
            ylabel: str,
            zlabel: str,
            title: str
    ) -> None:
        
        # Графіки на полотні із сіткою 3х3 розподілені нерівномірно.
        # Тобто 2/3 місця приділено графіку з ізолініями та 1/3 тривимірному графіку.
        # Такий розподіл місця на полотні можливий завдяки класу GridSpec, 
        # що безпосередньо розбиває місце на полотні, 
        # та подальшою маніпуляцією зі зрізами, що відповідають місцю на сітці.

        ax = self.fig.add_subplot(self.gs[:, 2], projection='3d')

        ax.plot_surface(x, y, z, cmap=colormap)

        ax.set_title(title)

        ax.set_xlabel(xlabel)
        ax.set_ylabel(ylabel)
        ax.set_zlabel(zlabel)

