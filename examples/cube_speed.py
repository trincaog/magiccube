import time
from magiccube.cube import Cube

from magiccube.cube_move import CubeMove


num_executions = 100
# pylint: disable=line-too-long
moves = "D' B B' D L' D' F F' F B F' B' R D' L' D' F' B F' F U' U' L B' R D' D L' R B R' F' L B' D' U D U B R L R B B' L' L B' B L' R' F L L F U' L' U B L' L' U D' R' L' D D' B D' B B' B D F L' B F' F' F D R B' R F' L R' R F' F R' R U B D U U B R B' D B' F' U D' D L U B U F B U' B B U F B U' U U B' R' R' D' F B' B' R' U' F' R' U' L D' D' F' D F' L' R' L B U' D' D' L B F F R L' U U' B R' R' D' R L D D' L' D' L' D L' B D D' F D' U' B L' L B U' R L' B' B' F F D F' R' B U U' D' U' F D D' D L' L' B' L R' D B' B R F' R R' D' U D D L D' R L' L' B L' D L D D R U' B' F R L' R' L L' L F' U' B' L D' F D' R L' D F L R' F' B F' F L F' L R B U' U B' F U' D' L' R L' D' R F' L D B B R' B' D U D U' U F L D' D D' F' B' L' F' L' R B L' F U' B' F D' U' R' D' B B' B B' R' L' U' U' U B B' U' F' F' D' F' L' R' F' F F' F B' R' U L F F U' F D U R U U D U B U' D' B' F' B' R' D B R' L D' B' B R U' B R B B B D' D' B' F B L U' L U R L L' L' B' F U L L' D F F B D' F' L' U D F F D' B R' L' U U' L D' B F D D' B' B B F R' D' F' D' R B D' L F' D' B' D D D' U R' L F D' D B' D U' R' U' U U F' D L D' U' D' F' U L' B D B R B L R' L R R' U F' B' U L L F' U L' L' F' R D F U F D R' U R U' L R D' D' R' R' R' R' D B' B' D' U U' B' U' L R D' B F F' L' D' L F F D' L' B L' F' U' B B D' U F R' D U' R' B' D' F D' D F L U' L' F B F' U' U D L L U' U' F U F D D L R R D R D' D F L D' L' U' B U' R' F' F' B' U' L B' L R' B F' U' L' D' R' R R U' R D' D L' U U B R' B' F D' R' B R' B L' L B' R' D' F' F D L' F' U' D D R F L L B R U D' R' U' L U' U' F' L' F' U' F' L' U' F U B' U' U D' L D' D' B' B R' U F' U' U' U' L' L' B' D U' B' R R' D R F' R' F F' D R R' B' B F R B' B' R' U' U' B' R' F B D' D U B U' D' R F' B L' F' L U' U F' R' B B U D' R' B F U R D' B' R D' F' R' B' B' R' R' R D L D L' U' R' L' U' U U' L D' L R F L' D F B' L F F' R B U F' B R B' L' R R' L R D F D' R' F' R F D' D R' F' B' U' B' D' L' L' F B D U' R B R' D U R F' F U B B' F U B U L L F' B' D L' B' L' B' F L' D' D' U L' F U' U' R U F D' R' U' U D' R L U U D' R' R F' R U' F' U' L' D' F B' B' L' L D' L' B' D' D R D' R' L F F F' F F U R D' L B' U B' U' U L F' F F U B B R' R' L' L' B' B B F' U R' D F' F' F' D B' B U' D' U' B' D' B' L' B' D D' F' L' D D F' B D' D' B' R' U L B' R' R B' U' F L U R R' D D' D L D' L' D' U F L R' R' D L R' R' D U' R F' F U F' U' D' B' D' R B' L' B F U' D' R' L R L R U' R' F' R D D' D U' F' F' B L F L L' D' U' F B L U L' R D R' R F' F R' B D D' U F' R D' F' F U L' U R B' F' U R' F R' L' B F' B' R B' R D' B R L' B' B D F' L' L' D' D D' B B' F'"
moves = [CubeMove.create(x) for x in moves.split(" ")]
num_moves = len(moves)

# Create cube
cube = Cube(hist=False, size=3)

# warm up
cube.reset()
start_time = time.perf_counter()
cube.rotate(moves)
end_time = time.perf_counter()


cube.reset()


# Solve the cube N times
start_time = time.perf_counter()
for _ in range(num_executions):
    cube.rotate(moves)
end_time = time.perf_counter()

duration = end_time-start_time
total_moves = num_executions*num_moves
time_per_move = duration/total_moves

print("total moves:", duration)
print("time (sec):", duration)
print("avg time per move (ms):", time_per_move*1000)
print("moves/sec", 1/time_per_move)
