# diffusion2D

## Instructions for Students

Please follow the instructions in [pypi_exercise.md](https://github.com/Simulation-Software-Engineering/Lecture-Material/blob/main/03_building_and_packaging/pypi_exercise.md).

The code used in this exercise is based on [Chapter 7 of the book "Learning Scientific Programming with Python"](https://scipython.com/book/chapter-7-matplotlib/examples/the-two-dimensional-diffusion-equation/).

---

## Project Description

The `diffusion2D` project simulates the 2D heat diffusion equation using a finite difference method. It demonstrates how heat diffuses over a square plate with customizable parameters, such as thermal diffusivity, grid resolution, and initial temperature distribution.

The project is modular, with clear separation of the solver and plotting functions. It serves as an exercise for learning Python packaging and distribution techniques.

---

## Installing the Package

### Using pip3 to Install from PyPI

Once the package is published to PyPI, you can install it with:

```bash
pip install guanpu_diffusion2d
```

### Required Dependencies

The following dependencies are required to use this package:

- **Python** >= 3.6
- **NumPy**
- **Matplotlib**

These dependencies will be installed automatically if you use `pip` to install the package.

---

## Running this Package

After installing the package, you can run the 2D diffusion simulation directly by importing and calling the `solve()` function:

```python
from guanpu_diffusion2d import diffusion2d

# Run the simulation with default parameters
diffusion2d.solve()

# Customize parameters (e.g., grid size, thermal diffusivity)
diffusion2d.solve(dx=0.05, dy=0.05, D=2.0)
```

---

## Citing
just cite plz