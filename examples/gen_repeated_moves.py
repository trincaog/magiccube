from multiprocessing import Pool
import random
import time

from matplotlib.pyplot import axis, grid
import magiccube
import pandas as pd

cube_size=4
min_moves=1
max_moves=10
total_results = {}

def apply_sequence(cube, moves):
    cube.reset()
    for i in range(1000_000):
        cube.rotate(moves)
        if cube.is_done():
            return i+1
    assert False, "couldnt go back to begining"


def test_sequence_of_n_moves(n_moves, num_tests=1_000):
    # Create the cube
    cube = magiccube.Cube(cube_size)
    results=[]
    random.seed(42)
    start_time = time.perf_counter()
    for i in range(num_tests):
        # Scramble the cube
        moves = cube.generate_random_moves(num_steps=n_moves)
        num_rounds = apply_sequence(cube, moves)
        #results.append(str(num_rounds) + " " + " ".join([str(x) for x in moves]))
        results.append(num_rounds)
    end_time = time.perf_counter()
    duration = end_time-start_time
    return n_moves,duration,results



with Pool(8) as pool:
    imap_results = pool.imap_unordered(test_sequence_of_n_moves, range(min_moves,max_moves+1))
    for n_moves,duration,imap_result in imap_results:
        print(f"sequence_of_n_moves {n_moves} took: {round(duration, ndigits=3)}")
        total_results[n_moves]= imap_result

        df = pd.DataFrame(data=total_results)
        df.to_csv("~/rubik_moves.csv", sep=";")
