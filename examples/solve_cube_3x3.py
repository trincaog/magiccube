import random
from magiccube.cube import Cube
from magiccube.solver.basic.basic_solver import BasicSolver

def main():
    random.seed(42)
    cube = Cube(hist=False, size=3)
    solver = BasicSolver(cube)

    # Solve the cube 100 times
    for _ in range(100):
        # Reset & Scramble the cube
        cube.reset()
        initial_moves = cube.scramble(num_steps=50, wide=False)

        print("Initial cube:", initial_moves)
        print(cube)

        # Solve the cube
        actions = solver.solve()
        print("Solution actions:", " ".join(actions))
        print()

main()
