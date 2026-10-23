import math
import numpy as np
import pyvista as pv

vector_origins = np.array([[0, 0, 0], [0, 0, 0], [0, 0, 0]])

static_vector = np.array([[1, 0, 0]])
dynamic_vector = np.array([[0, 1, 0]])
vector_directions = np.array([[]])

plotter = pv.Plotter()

#plotter.add_mesh(
#    grid,
#    scalars="Height",
#    lighting=False,
#    show_edges=True,
#    scalar_bar_args={"title": "Height"},
#    clim=[-1, 1],
#)
angle = (1/6) * np.pi
rotational_matrix_y = np.array([
    [np.cos(angle), 0, np.sin(angle)],
    [0, 1, 0],
    [-np.sin(angle), 0, np.cos(angle)]
    ])

plotter.open_gif("vectors.gif")

nframe = 100000000
for phase in np.linspace(0, 2 * np.pi, nframe + 1)[:nframe]:

    dynamic_vector = dynamic_vector @ rotational_matrix_y
    reactive_vector = np.cross(static_vector, dynamic_vector)

    vector_directions = np.vstack([static_vector, dynamic_vector, reactive_vector])
    plotter.add_arrows(vector_origins, vector_directions)

    plotter.write_frame()

plotter.close()