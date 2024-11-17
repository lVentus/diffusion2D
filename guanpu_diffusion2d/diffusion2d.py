"""
Solving the two-dimensional diffusion equation

Example acquired from https://scipython.com/book/chapter-7-matplotlib/examples/the-two-dimensional-diffusion-equation/
"""
import numpy as np
import matplotlib.pyplot as plt
from .output import create_plot, output_plots

def solve(dx=0.1, dy=0.1, D=4.0):
    # Default physical and simulation parameters
    w, h = 10.0, 10.0
    T_cold, T_hot = 300, 700
    nsteps = 101
    n_output = [0, 10, 50, 100]

    # Number of discrete mesh points in X and Y directions
    nx, ny = int(w / dx), int(h / dy)

    # Computing a stable time step
    dx2, dy2 = dx * dx, dy * dy
    dt = dx2 * dy2 / (2 * D * (dx2 + dy2))

    print("dt = {}".format(dt))

    u0 = T_cold * np.ones((nx, ny))
    u = u0.copy()

    # Initial conditions - circle of radius r centered at (cx, cy) (mm)
    r = min(h, w) / 4.0
    cx = w / 2.0
    cy = h / 2.0
    r2 = r ** 2
    for i in range(nx):
        for j in range(ny):
            p2 = (i * dx - cx) ** 2 + (j * dy - cy) ** 2
            if p2 < r2:
                u0[i, j] = T_hot

    def do_timestep(u_nm1, u, D, dt, dx2, dy2):
        # Propagate with forward-difference in time, central-difference in space
        u[1:-1, 1:-1] = u_nm1[1:-1, 1:-1] + D * dt * (
                (u_nm1[2:, 1:-1] - 2 * u_nm1[1:-1, 1:-1] + u_nm1[:-2, 1:-1]) / dx2
                + (u_nm1[1:-1, 2:] - 2 * u_nm1[1:-1, 1:-1] + u_nm1[1:-1, :-2]) / dy2)

        u_nm1 = u.copy()
        return u_nm1, u

    fig_counter = 0
    fig = plt.figure()

    # Time loop
    for n in range(nsteps):
        u0, u = do_timestep(u0, u, D, dt, dx2, dy2)

        # Create figure
        if n in n_output:
            fig_counter += 1
            im = create_plot(u, fig, fig_counter, T_cold, T_hot, n, dt)  # Using the create_plot function

    # Plot output figures
    output_plots(fig, im)  # Pass colorbar information
