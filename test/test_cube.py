from kiwisolver import Solver
import numpy as np
from magiccube import Cube
from magiccube.cube_base import Face, PieceType
from magiccube.cube_move import CubeMove
from magiccube.cube_piece import Color
import pytest
import random

from magiccube.solver.basic.basic_solver import BasicSolver, SolverException

def test_reset():
    c = Cube(3)
    c.check_consistency()
    c.rotate("R' D'")
    c.check_consistency()
    c.reset()
    assert c.is_done()

def test_12_moves():
    c = Cube(3)
    c.check_consistency()
    for i in range(12):
        c.rotate("R' D' R D")
    c.check_consistency()
    assert c.is_done()

def test_12_moves_2d():
    c = Cube(2)
    c.check_consistency()
    for i in range(12):
        c.rotate("R' D' R D")
    c.check_consistency()
    assert c.is_done()


def test_all_rotations():
    c = Cube(3)
    c.rotate("R R' L L' B B' F F' U U' D D'")
    c.check_consistency()
    assert c.is_done()

def test_rotations_4x():
    c = Cube(4)
    c.rotate("R R'")
    c.check_consistency()
    assert c.is_done()

    c.rotate("2R")
    c.check_consistency()
    assert c.get_face_flat(Face.F)==[
        Color.G,Color.G,Color.W,Color.G,
        Color.G,Color.G,Color.W,Color.G,
        Color.G,Color.G,Color.W,Color.G,
        Color.G,Color.G,Color.W,Color.G,
        ]

    c.reset()
    c.rotate("Uw")
    assert c.get_face_flat(Face.F)==[
        Color.O,Color.O,Color.O,Color.O,
        Color.O,Color.O,Color.O,Color.O,
        Color.G,Color.G,Color.G,Color.G,
        Color.G,Color.G,Color.G,Color.G,
        ]

    c.check_consistency()

def test_all_rotations_2d():
    c = Cube(2)
    c.rotate("R R' L L' B B' F F' U U' D D'")
    c.check_consistency()
    assert c.is_done()

def test_is_done():
    c = Cube(3)
    assert c.is_done()
    c.rotate("R")
    assert not c.is_done()
    c.reset()
    assert c.is_done()

def test_print_pattern1():
    c = Cube(3)
    c.rotate("R R L' L' B B F' F' U U D' D'")
    c.check_consistency()
    print(c)

def test_print_pattern2():
    c = Cube(3)
    c.rotate("R' L U D' F B' R' L")
    c.check_consistency()
    print(c)

def test_print_2d():
    c = Cube(2)
    c.check_consistency()
    print(c)

def test_print_4d():
    c = Cube(4)
    c.check_consistency()
    print(c)

def test_history():
    c = Cube(3)
    moves = "R' L U D' F B' R' L"
    c.rotate(moves)
    assert c.history(to_str=True) == moves

def test_reverse():
    c = Cube(3)
    moves = "R' L U D' F B' R' L"
    c.rotate(moves)
    assert c.reverse_history(to_str=True) == "L' R B F' D U' L' R"
    c.rotate(c.reverse_history())
    assert c.is_done()

def test_scramble():
    c = Cube(3)
    c.scramble(num_steps=50)
    print(c)
    assert(not c.is_done())

def test_scramble_2d():
    c = Cube(2)
    c.scramble(num_steps=50)
    print(c)
    assert(not c.is_done())

def test_get_piece():
    c = Cube(3)
    piece = c.get_piece((2,0,0))
    assert piece.get_piece_color(Face.R.get_axis())==Color.O
    assert piece.get_piece_color(Face.D.get_axis())==Color.W
    assert piece.get_piece_color(Face.B.get_axis())==Color.B

    piece = c.get_piece((0,2,2))
    assert piece.get_piece_color(Face.L.get_axis())==Color.R
    assert piece.get_piece_color(Face.U.get_axis())==Color.Y
    assert piece.get_piece_color(Face.F.get_axis())==Color.G


def test_get_all_faces():
    c = Cube(3)
    faces = c.get_all_faces()
    assert np.all(np.array(faces[Face.F]).flatten()==Color.G)
    assert np.all(np.array(faces[Face.B]).flatten()==Color.B)
    assert np.all(np.array(faces[Face.L]).flatten()==Color.R)
    assert np.all(np.array(faces[Face.R]).flatten()==Color.O)
    assert np.all(np.array(faces[Face.U]).flatten()==Color.Y)
    assert np.all(np.array(faces[Face.D]).flatten()==Color.W)

def test_get_all_pieces():
    c=Cube(3)
    pieces = c.get_all_pieces()
    assert len(pieces) == 26

    c=Cube(4)
    pieces = c.get_all_pieces()
    assert len(pieces) == 56

def test_move():
    c = Cube(3)
    c.rotate("L")
    assert c.get_piece((1,0,0)).get_piece_colors()==(None,Color.W,Color.B)
    assert c.get_piece((0,0,0)).get_piece_colors()==(Color.R,Color.G,Color.W)
    assert c.get_piece((0,0,2)).get_piece_colors()==(Color.R,Color.G,Color.Y)

def test_move_special_rot():
    c = Cube(3)
    c.rotate("X'")
    assert c.get_piece((2,2,2)).get_piece_colors()==(Color.O,Color.B,Color.Y)
    c.reset()
    c.rotate("Y")
    assert c.get_piece((2,2,2)).get_piece_colors()==(Color.B,Color.Y,Color.O)
    c.reset()
    c.rotate("Z")
    assert c.get_piece((2,2,2)).get_piece_colors()==(Color.Y,Color.R,Color.G)

def test_move_special_mid():
    c = Cube(3)
    c.rotate("M")
    assert c.get_piece((1,2,2)).get_piece_colors()==(None,Color.B,Color.Y)
    c.rotate("E'")
    assert c.get_piece((2,1,2)).get_piece_colors()==(Color.B,None,Color.O)
    c.rotate("S")
    assert c.get_piece((2,2,1)).get_piece_colors()==(Color.Y,Color.R,None)

def test_move_noloc():
    c = Cube(3)
    c.rotate("L")
    assert c.get_piece((1,0,0)).get_piece_colors(no_loc=True)==(Color.B,Color.W)
    assert c.get_piece((0,0,0)).get_piece_colors(no_loc=True)==(Color.G,Color.R,Color.W)
    assert c.get_piece((0,0,2)).get_piece_colors(no_loc=True)==(Color.G,Color.R,Color.Y)



def test_move_outcome():
    c = Cube(3)
    c.rotate("B'")
    print(c)
    assert c.get_piece((0,2,0)).get_piece_colors_str()=='WRB'
    assert c.get_piece((0,0,0)).get_piece_colors_str()=='WOB'

    c = Cube(3)
    c.rotate("F")
    print(repr(c))
    print(c)
    assert c.get_piece((2,0,2)).get_piece_colors_str()=='YOG'
    assert c.get_piece((0,0,2)).get_piece_colors_str()=='WOG'

    c = Cube(3)
    c.rotate("R")
    assert c.get_piece((2,0,0)).get_piece_colors_str()=='OBY'
    assert c.get_piece((2,0,2)).get_piece_colors_str()=='OBW'

    c = Cube(3)
    c.rotate("L")
    assert c.get_piece((0,0,1)).get_piece_colors_str()=='RG'
    assert c.get_piece((0,0,0)).get_piece_colors_str()=='RGW'
    assert c.get_piece((0,0,2)).get_piece_colors_str()=='RGY'

    c = Cube(3)
    c.rotate("D")
    assert c.get_piece((2,0,0)).get_piece_colors_str()=='GWO',c.get_piece((2,0,0)).get_piece_colors_str()
    assert c.get_piece((2,0,2)).get_piece_colors_str()=='GWR'

    c = Cube(3)
    c.rotate("U")
    assert c.get_piece((0,2,0)).get_piece_colors_str()=='GYR'
    assert c.get_piece((0,2,2)).get_piece_colors_str()=='GYO'

def test_find():
    c = Cube(3)
    c.rotate("R")
    print(c)
    coord,_=c.find_piece("GOY")
    assert coord == (2,2,0)
    coord,_=c.find_piece("BRW")
    assert coord == (0,0,0)


def test_print_simple_move():
    c = Cube(3)
    print(c)
    print(repr(c))
    print("XXXXXXXXXXXXXXXXXXXXXX")
    c.rotate("F")
    print(repr(c))
    print(c)

def test_wide_move():
    c = Cube(3)

    c.reset()
    c.rotate("Fw")
    c.rotate(c.reverse_history())
    assert c.is_done()

    c.reset()
    c.rotate("1Fw")
    c.rotate(c.reverse_history())
    assert c.is_done()

    c.reset()
    c.rotate("2Fw")
    c.rotate(c.reverse_history())
    assert c.is_done()


def test_scramble_wide_move():
    c = Cube(6)
    random.seed(42)
    c.scramble(num_steps=500, wide=True)
    c.rotate(c.reverse_history())
    assert c.is_done()

def test_get_piece_type():
    c = Cube(3)
    assert c.get_piece(coordinates=(0,0,2)).get_piece_type()==PieceType.CORNER
    assert c.get_piece(coordinates=(1,0,1)).get_piece_type()==PieceType.CENTER
    assert c.get_piece(coordinates=(2,1,2)).get_piece_type()==PieceType.EDGE
    inner = c.get_piece(coordinates=(1,1,1))
    assert inner is None or inner.get_piece_type()==PieceType.INNER

def test_set_cube():
    c = Cube(3)
    c.set("YYYYYYYYYRRRRRRRRRGGGGGGGGGOOOOOOOOOBBBBBBBBBWWWWWWWWW")
    assert c.is_done()

def test_set_cube_4x():
    c = Cube(4)
    c.set("YYYYYYYYYYYYYYYYRRRRRRRRRRRRRRRRGGGGGGGGGGGGGGGGOOOOOOOOOOOOOOOOBBBBBBBBBBBBBBBBWWWWWWWWWWWWWWWW")
    assert c.is_done()

def test_set_cube_initial_state():
    c = Cube(3, state="YYYYYYGGGGGWRRRRRROOOGGWGGWYBBOOOOOORRRYBBYBBWWBWWBWWB")
    c.rotate("U' R'")

    assert c.is_done()

def test_set_cube_initial_state_4X():
    c = Cube(4, state="""
    YYYYYYYYYYYYGGGG
    GGGWRRRRRRRRRRRR
    OOOOGGGWGGGWGGGW
    YBBBOOOOOOOOOOOO
    RRRRYBBBYBBBYBBB
    WWWBWWWBWWWBWWWB
    """)
    c.rotate("U' R'")

    assert c.is_done()

def test_set_cube_not_done():
    c = Cube(3)
    c.set("""
       RBB BYO GGO
       YRO YRW WWW
       YYB GGW BRW
       YYR OOW GGW
       YYG BBR OOG
       RGO RWO RBB
       """)
    c.rotate("D' B' R' F' L' U'")

    assert c.is_done()

def test_set_cube_bad_cube():
    c = Cube(3)
    c.set("""
       RBB BYO OGG
       YRO YRW WWW
       YYB GGW BRW
       YYR OOW GGW
       YYG BBR OOG
       RGO RWO RBB
       """)
    solver = BasicSolver(c)
    with pytest.raises(SolverException):
        solver.solve()


if __name__ == "__main__" :
    #pytest.main()
    test_move()
    pass
