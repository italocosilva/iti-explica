import numpy as np
import matplotlib.pyplot as plt

def plot_function(function):
    # Gerar os dados dentro do espaço desejado
    x = np.linspace(-10, 10, 1000)
    y = np.linspace(-10, 10, 1000)
    X, Y = np.meshgrid(x, y)
    Z = function(X, Y)

    # Plotar o gráfico para vermos
    fig, ax = plt.subplots(figsize=(8, 6))
    contour = ax.contourf(X, Y, Z, 50, cmap='coolwarm')
    lines = ax.contour(X, Y, Z, 10, colors='black', linewidths=0.5)
    cbar = fig.colorbar(contour, ax=ax)
    cbar.set_label('Function Value')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_title("2D Contour Plot with Local Minimum")
    ax.scatter(8.33, -6.47, marker="x", color="red")

    return ax