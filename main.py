import math
import numpy as np
import pyvista as pv

plotter = pv.Plotter()
plotter.add_axes()

start_pos = [0.0, 0.0, 0.0]
angle = 0.0

static_vector = np.array([1.0, 0.0, 0.0])
dynamic_vector = np.array([0.0, 1.0, 0.0])
cross_vector = np.cross(static_vector, dynamic_vector)

vector_directions = np.vstack([static_vector, dynamic_vector, cross_vector])

arrows = []
for direction in vector_directions:
    arrow = pv.Arrow(start=start_pos, direction=direction, scale="auto")
    arrows.append(arrow)

actors = [
    plotter.add_mesh(arrow, color=color)
    for arrow, color in zip(arrows, ["red", "green", "blue"])
]

def update_plot() -> None:
    global angle
    global start_pos
    angle += (1/90) * math.pi

    new_dynamic_vector = np.array([np.sin(angle), np.cos(angle), 0.0])
    new_cross_product = np.cross(static_vector, new_dynamic_vector)

    new_vector_directions = [static_vector, new_dynamic_vector, new_cross_product]

    for i in range(len(actors)):
        arrow = pv.Arrow(start=start_pos, direction=new_vector_directions[i])
        actors[i].mapper.dataset = arrow

    plotter.render()

plotter.add_timer_event(max_steps=0, duration=10, callback=lambda step: update_plot())
plotter.show()