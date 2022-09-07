"""[XLearning] Base plotting functions for style settings.
(1) For presentations
(2) For publications
"""

# Author: Rongting Huang
# rthuang@connect.hku.hk
# Date: 2022/09/07
# update: 2022/09/07


"""
Ref:
Creating Reproducible, Publication-Quality Plots with Matplotlib and Seaborn
http://www.jesshamrick.com/2016/04/13/reproducible-plots/

Making publication-quality figures in Python (Part I): Fig and Axes
https://towardsdatascience.com/making-publication-quality-figures-in-python-part-i-fig-and-axes-d86c3903ad9b

https://github.com/huangyh09/hilearn/blob/master/hilearn/plot/base_plot.py
"""

import numpy as np
import matplotlib
import matplotlib.pyplot as plt

# codes for ggplot like backgroud
# http://messymind.net/making-matplotlib-look-like-ggplot/
# Or simply import seaborn

favorite_colors=["deepskyblue", "limegreen", "orangered", "cyan", "magenta", 
                 "gold", "blueviolet", "dodgerblue", "greenyellow", "tomato",
                 "turquoise", "orchid", "darkorange", "mediumslateblue"]


xlearn_colors1 = ['#4796d7', '#f79e54', '#79a702', '#df5858', '#556cab', 
                  '#de7a1f', '#ffda5c', '#4b595c', '#6ab186', '#bddbcf', 
                  '#daad58', '#488a99', '#f79b78', '#ffba00']

xlearn_colors2 = ['#4796d7', '#f79e54', '#79a702', '#df5858', '#556cab', 
                  '#de7a1f', '#ffda5c', '#4b595c', '#6ab186', '#bddbcf', 
                  '#daad58', '#488a99', '#f79b78', '#ffba00']                  

#seaborn_colors = seaborn.color_palette("hls", 8)

def set_colors(color_list=xlearn_colors1):
    """
    Replace the color list in matplotlib color_cycle
    Examples
    --------
    .. plot::
        >>> import xlearning
        >>> import numpy as np
        >>> import matplotlib.pyplot as plt
        >>> _colors = xlearning.plot.set_colors(xlearning.plot.xlearn_colors1)
        >>> xx = np.arange(65)
        >>> for i in range(14):
        >>>     plt.plot(xx, np.sin(xx)-i, label="%s" %_colors[i])
        >>> plt.legend()
        >>> plt.xlim(0, 100)
        >>> plt.show()
    """
    matplotlib.rcParams['axes.prop_cycle'] = matplotlib.cycler(color=color_list)
    return color_list


def set_frame(ax, top=False, right=False, bottom=True, left=True):
    """Example of setting the frame of the plot box.
    Parameters
    ----------
    ax: matplotlib Axes
        The Axes object containing the plot
    top, right, bottom, left: bool
        If True, keep the frame
    Examples
    --------
    .. plot::
        >>> import numpy as np
        >>> import matplotlib.pyplot as plt
        >>> from xlearning.plot import set_frame
        >>> ax = plt.subplot(1, 1, 1)
        >>> plt.plot(np.arange(0, 10, 0.1), np.sin(np.arange(0, 10, 0.1)))
        >>> set_frame(ax, top=False, right=False, bottom=True, left=True)
    """
    ax.spines['top'].set_visible(top)
    ax.spines['right'].set_visible(right)
    ax.spines['bottom'].set_visible(bottom)
    ax.spines['left'].set_visible(left)
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')
    ax.get_xaxis().set_tick_params(direction='out')
    ax.get_yaxis().set_tick_params(direction='out')
    return ax


def set_style(label_size=12, grid_alpha=0.3):
    """
    Set the figure style on fontsize for ticks, label, title and legend
    Parameters
    ----------
    label_size: float
        The size for labels, and proportional to ticks, legend, and title
    grid_alpha: float
        The transparency of grid with value from 0 (fully transparent) to 1
    Examples
    --------
    .. plot::
        >>> import numpy as np
        >>> import matplotlib.pyplot as plt
        >>> from xlearning.plot import set_style
        >>> set_style(label_size=12, grid_alpha=0.3)
        >>> plt.plot(np.arange(0, 10, 0.1), np.sin(np.arange(0, 10, 0.1)))
        >>> plt.title("Proper font size for publication")
    """
    if grid_alpha is not None and grid_alpha >= 0 and grid_alpha <= 1:
        matplotlib.rcParams.update({"axes.grid" : True, "grid.alpha": grid_alpha})
    matplotlib.rcParams['xtick.labelsize'] = label_size
    matplotlib.rcParams['ytick.labelsize'] = label_size
    matplotlib.rcParams['legend.fontsize'] = label_size * 1.1
    matplotlib.rcParams['axes.labelsize'] = label_size * 1.1
    matplotlib.rcParams['axes.titlesize'] = label_size * 1.2
    matplotlib.rcParams['axes.titleweight'] = 'bold'