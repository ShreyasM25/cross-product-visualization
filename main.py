import numpy as np
import pyvista as pv

plotter = pv.Plotter()
plotter.add_axes(interactive=True)

static_vector = np.array([1.0, 0.0, 0.0])
dynamic_vector = np.array([0.0, 1.0, 0.0])
cross_vector = np.cross(static_vector, dynamic_vector)

vector_directions = np.vstack([static_vector, dynamic_vector, cross_vector])
angle = 0.0

arrows = []
for direction in directions:
    arrow = pv.Arrow(start=[0, 0, 0], direction=direction, scale="auto")
    plot_arrows.append(arrow)

actors = []
arrow_colors = ["red", "green", "blue"]
for i in range(len(arrows)):
    plotter.add_mesh(arrows[i], color=arrow_colors[i])
actors = [
    plotter.add_mesh(arrow, color=color)
    for arrow, color in zip(arrows, ["red", "green", "blue"])
]

def update_plot():
    

plotter.show()