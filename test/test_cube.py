import numpy as np
from magiccube import Cube
from magiccube.cube_base import CubeFace, PieceType
from magiccube.cube_move import CubeMove
from magiccube.cube_piece import CubeColor
import pytest
import random

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
    assert piece.get_piece_color(CubeFace.R.get_axis())==CubeColor.O
    assert piece.get_piece_color(CubeFace.D.get_axis())==CubeColor.W
    assert piece.get_piece_color(CubeFace.B.get_axis())==CubeColor.B

    piece = c.get_piece((0,2,2))
    assert piece.get_piece_color(CubeFace.L.get_axis())==CubeColor.R
    assert piece.get_piece_color(CubeFace.U.get_axis())==CubeColor.Y
    assert piece.get_piece_color(CubeFace.F.get_axis())==CubeColor.G


def test_get_all_faces():
    c = Cube(3)
    faces = c.get_all_faces()
    assert np.all(np.array(faces[CubeFace.F]).flatten()==CubeColor.G)
    assert np.all(np.array(faces[CubeFace.B]).flatten()==CubeColor.B)
    assert np.all(np.array(faces[CubeFace.L]).flatten()==CubeColor.R)
    assert np.all(np.array(faces[CubeFace.R]).flatten()==CubeColor.O)
    assert np.all(np.array(faces[CubeFace.U]).flatten()==CubeColor.Y)
    assert np.all(np.array(faces[CubeFace.D]).flatten()==CubeColor.W)

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
    assert c.get_piece((1,0,0)).get_piece_colors()==(None,CubeColor.W,CubeColor.B)
    assert c.get_piece((0,0,0)).get_piece_colors()==(CubeColor.R,CubeColor.G,CubeColor.W)
    assert c.get_piece((0,0,2)).get_piece_colors()==(CubeColor.R,CubeColor.G,CubeColor.Y)

def test_move_special_rot():
    c = Cube(3)
    c.rotate("X'")
    assert c.get_piece((2,2,2)).get_piece_colors()==(CubeColor.O,CubeColor.B,CubeColor.Y)
    c.reset()
    c.rotate("Y")
    assert c.get_piece((2,2,2)).get_piece_colors()==(CubeColor.B,CubeColor.Y,CubeColor.O)
    c.reset()
    c.rotate("Z")
    assert c.get_piece((2,2,2)).get_piece_colors()==(CubeColor.Y,CubeColor.R,CubeColor.G)

def test_move_special_mid():
    c = Cube(3)
    c.rotate("M")
    assert c.get_piece((1,2,2)).get_piece_colors()==(None,CubeColor.B,CubeColor.Y)
    c.rotate("E'")
    assert c.get_piece((2,1,2)).get_piece_colors()==(CubeColor.B,None,CubeColor.O)
    c.rotate("S")
    assert c.get_piece((2,2,1)).get_piece_colors()==(CubeColor.Y,CubeColor.R,None)

def test_move_noloc():
    c = Cube(3)
    c.rotate("L")
    assert c.get_piece((1,0,0)).get_piece_colors(no_loc=True)==(CubeColor.B,CubeColor.W)
    assert c.get_piece((0,0,0)).get_piece_colors(no_loc=True)==(CubeColor.G,CubeColor.R,CubeColor.W)
    assert c.get_piece((0,0,2)).get_piece_colors(no_loc=True)==(CubeColor.G,CubeColor.R,CubeColor.Y)



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

if __name__ == "__main__" :
    pytest.main()
    pass
