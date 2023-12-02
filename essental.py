import numpy as np 
import matplotlib.pyplot as plt
class essental:
    def __init__(self):
        pass
    def plot_2d(f, x_min, x_max):
        """
        Plots a 2D graph of a given function.

        Parameters:
        f (function): The function to be plotted.
        x_min (float): The minimum value of the x-axis.
        x_max (float): The maximum value of the x-axis.
        """
        x = np.linspace(x_min, x_max, 1000)
        y = f(x)
        plt.plot(x, y)
        plt.show()

    def plot_3d( f ,x_min, x_max, y_min, y_max):
        """ Plots a 3D graph of a given function.
        
        Parameters:
        f (function): The function to be plotted.
        x_min (float): The minimum value of the x-axis.
        x_max (float): The maximum value of the x-axis.
        y_min (float): The minimum value of the y-axis.
        y_max (float): The maximum value of the y-axis."""
        x = np.linspace(x_min, x_max, 1000)
        y = np.linspace(y_min, y_max, 1000)
        X, Y = np.meshgrid(x, y)
        Z = f
        fig = plt.figure()
        ax = fig.gca(projection='3d')
        ax.plot_surface(X, Y, Z, cmap=plt.cm.jet)
        plt.show()

    def plot_3d_contour( f ,x_min, x_max, y_min, y_max):
        x = np.linspace(x_min, x_max, 1000)
        y = np.linspace(y_min, y_max, 1000)
        X, Y = np.meshgrid(x, y)
        Z = f
        fig = plt.figure()
        ax = fig.gca(projection='3d')
        ax.contour(X, Y, Z, cmap=plt.cm.jet)
        plt.show()
    
