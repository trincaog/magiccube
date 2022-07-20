import random
from magiccube.cube import Cube
from magiccube.solver.basic.basic_solver import BasicSolver

def perf_test_cube():
    random.seed(42)
    cube = Cube(hist=False, size=3)
    solver = BasicSolver(cube)

    action_count_list=[]

    for _ in range(1000):
        # Reset & Scramble the cube
        cube.reset()
        initial_moves = cube.scramble(num_steps=100)

        # Solve the cube
        actions = solver.solve()
        action_count_list.append(len(actions))

    print("Max  actions", max(action_count_list))
    print("Mean actions", sum(action_count_list)/len(action_count_list))
    print("Min  actions", min(action_count_list))


if __name__ == "__main__" :
    perf_test_cube()
    pass
