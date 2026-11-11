import math
import numpy as np
import pyvista as pv


plotter = pv.Plotter()
plotter.add_axes(interactive=True)


# Vector detail display
plotter.add_text(
    "Static Vector: [1.00 0.00 0.00]\n"
    "Dynamic Vector: [0.00 1.00 0.00]\n"
    "Cross Product: [0.00 0.00 1.00]",
    position="upper_left",
    font_size=12,
    color="black",
    name="vector_details"
)


# Vector Initialization
start_pos = [0.0, 0.0, 0.0]
angle = 0.0

static_vector = np.array([1.0, 0.0, 0.0])
dynamic_vector = np.array([0.0, 1.0, 0.0])
cross_vector = np.cross(static_vector, dynamic_vector)

vector_directions = [
    static_vector,
    dynamic_vector,
    cross_vector
]


# Arrow creation and plot addition
arrows = []

for direction in vector_directions:
    magnitude = np.linalg.norm(direction)
    arrow = pv.Arrow(
        start=start_pos,
        direction=direction,
        scale=magnitude
    )
    arrows.append(arrow)

actors = [
    plotter.add_mesh(arrow, color=color)
    for arrow, color in zip(arrows, ["red", "green", "blue"])
]


def update_plot(step: int) -> None:
    # 3 degree increment
    global angle
    angle += math.pi / 60

    # Updated vector calculation
    new_dynamic_vector = np.array([
        np.sin(angle),
        np.cos(angle),
        0.0
    ])

    new_cross_product = np.cross(
        static_vector,
        new_dynamic_vector
    )

    new_vector_directions = [
        static_vector,
        new_dynamic_vector,
        new_cross_product
    ]

    plotter.add_text(
        f"Static Vector: {np.array2string(static_vector, precision=2, floatmode='fixed')}\n"
        f"Dynamic Vector: {np.array2string(new_dynamic_vector, precision=2, floatmode='fixed')}\n"
        f"Cross Product: {np.array2string(new_cross_product, precision=2, floatmode='fixed')}",
        position="upper_left",
        font_size=12,
        color="black",
        name="vector_details"
    )

    # Updated plot arrows
    for actor, direction in zip(actors, new_vector_directions):
        magnitude = np.linalg.norm(direction)

        # Hiding the cross-product arrow if its vector has near-zero magnitude
        if magnitude < 1e-8:
            actor.SetVisibility(False)
            continue

        actor.SetVisibility(True)

        arrow = pv.Arrow(
            start=start_pos,
            direction=direction,
            scale=magnitude
        )

        actor.mapper.dataset = arrow

    # Print the timer step to verify animation is running
    if step % 10 == 0:
        print("Animation step:", step)

    # Render the updated scene
    plotter.render()


# Initialize the render-window interactor
# Model doesn't update without this line
plotter.iren.initialize()

# Sets the animation and number of model updates
# Currently set to updating the graph every 30 ms, very frequent
# 30 ms makes the animation freeze up, keeping it so the animation is smooth
plotter.add_timer_event(
    max_steps=1000000000,
    duration=30,
    callback=update_plot
)

plotter.show()
