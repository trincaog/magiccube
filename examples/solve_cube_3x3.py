"""
Example usage of the basic cube solver.
"""

import random
from magiccube.cube import Cube
from magiccube.solver.basic.basic_solver import BasicSolver

random.seed(42)
cube = Cube(hist=False, size=3)
solver = BasicSolver(cube)

# Solve the cube N times
for _ in range(5):
    # Reset & Scramble the cube
    cube.reset()
    initial_moves = cube.scramble(num_steps=50)

    # Print the cube
    print("Initial cube:", initial_moves)
    print(cube)

    # Solve the cube
    actions = solver.solve()
    print("Solution actions:", actions)

    assert cube.is_done()
