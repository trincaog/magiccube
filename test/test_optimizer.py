

import pytest
from magiccube.cube_move import CubeMove
from magiccube.optimizer.move_optimizer import MoveOptimizer


# def test_optimize_rev():
#     moves = [CubeMove.create(m) for m in "Y Z S M E U' L L L' L' F F F F R' Y' Y".split(" ")]
#     o_moves = MoveOptimizer().optimize(moves)
#     print(o_moves)

def test_optimize_rev():
    moves = [CubeMove.create(m) for m in "F L L L' L' R".split(" ")]
    o_moves = MoveOptimizer().optimize(moves)
    o_moves = " ".join([str(m) for m in o_moves])
    assert o_moves=="F R"

def test_optimize_4x():
    moves = [CubeMove.create(m) for m in "F L L L L R".split(" ")]
    o_moves = MoveOptimizer().optimize(moves)
    o_moves = " ".join([str(m) for m in o_moves])
    assert o_moves=="F R"

def test_optimize_3x():
    moves = [CubeMove.create(m) for m in "F L L L R".split(" ")]
    o_moves = MoveOptimizer().optimize(moves)
    o_moves = " ".join([str(m) for m in o_moves])
    assert o_moves=="F L' R"

def test_optimize_cube_rot():
    moves = [CubeMove.create(m) for m in "F Y L Z L".split(" ")]
    o_moves = MoveOptimizer().optimize(moves)
    o_moves = " ".join([str(m) for m in o_moves])
    assert o_moves=="F F D"


if __name__ == "__main__" :
    pytest.main()
    pass
