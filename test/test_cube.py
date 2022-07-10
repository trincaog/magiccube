from cube import Cube
import numpy as np
from cube.cube_piece import CubeColor, CubeFace

def test_reset():
    rcube = Cube(3)
    rcube.check_consistency()
    rcube.rotate("R' D'")
    rcube.check_consistency()
    rcube.reset()
    assert rcube.is_done()

def test_12_moves():
    rcube = Cube(3)
    rcube.check_consistency()
    for i in range(12):
        rcube.rotate("R' D' R D")
    rcube.check_consistency()
    assert rcube.is_done()

def test_12_moves_2d():
    rcube = Cube(2)
    rcube.check_consistency()
    for i in range(12):
        rcube.rotate("R' D' R D")
    rcube.check_consistency()
    assert rcube.is_done()


def test_all_rotations():
    rcube = Cube(3)
    rcube.rotate("R R' L L' B B' F F' U U' D D'")
    rcube.check_consistency()
    assert rcube.is_done()

def test_all_rotations_2d():
    rcube = Cube(2)
    rcube.rotate("R R' L L' B B' F F' U U' D D'")
    rcube.check_consistency()
    assert rcube.is_done()

def test_is_done():
    rcube = Cube(3)
    assert rcube.is_done()
    rcube.rotate("R")
    assert not rcube.is_done()
    rcube.reset()
    assert rcube.is_done()

def test_print_pattern1():
    rcube = Cube(3)
    rcube.rotate("R R L' L' B B F' F' U U D' D'")
    rcube.check_consistency()
    print(rcube)

def test_print_pattern2():
    rcube = Cube(3)
    rcube.rotate("R' L U D' F B' R' L")
    rcube.check_consistency()
    print(rcube)

def test_print_2d():
    rcube = Cube(2)
    rcube.check_consistency()
    print(rcube)

def test_print_4d():
    rcube = Cube(4)
    rcube.check_consistency()
    print(rcube)

def test_history():
    rcube = Cube(3)
    moves = "R' L U D' F B' R' L"
    rcube.rotate(moves)
    assert rcube.history() == moves

def test_reverse():
    rcube = Cube(3)
    moves = "R' L U D' F B' R' L"
    rcube.rotate(moves)
    assert rcube.reverse_history() == "L' R B F' D U' L' R"
    rcube.rotate(rcube.reverse_history())
    assert rcube.is_done()

def test_scramble():
    rcube = Cube(3)
    steps = rcube.scramble(num_steps=50)
    print(rcube)
    assert(not rcube.is_done())

def test_scramble_2d():
    rcube = Cube(2)
    steps = rcube.scramble(num_steps=50)
    print(rcube)
    assert(not rcube.is_done())

def test_get_piece():
    rcube = Cube(3)
    piece = rcube.get_piece((2,0,0))
    assert piece.get_piece_color(CubeFace.R)==CubeColor.O
    assert piece.get_piece_color(CubeFace.D)==CubeColor.W
    assert piece.get_piece_color(CubeFace.B)==CubeColor.B

    piece = rcube.get_piece((0,2,2))
    assert piece.get_piece_color(CubeFace.L)==CubeColor.R
    assert piece.get_piece_color(CubeFace.U)==CubeColor.Y
    assert piece.get_piece_color(CubeFace.F)==CubeColor.G


def test_get_all_faces():
    rcube = Cube(3)
    faces = rcube.get_all_faces()
    assert np.all(np.array(faces[CubeFace.F]).flatten()==CubeColor.G)
    assert np.all(np.array(faces[CubeFace.B]).flatten()==CubeColor.B)
    assert np.all(np.array(faces[CubeFace.L]).flatten()==CubeColor.R)
    assert np.all(np.array(faces[CubeFace.R]).flatten()==CubeColor.O)
    assert np.all(np.array(faces[CubeFace.U]).flatten()==CubeColor.Y)
    assert np.all(np.array(faces[CubeFace.D]).flatten()==CubeColor.W)

def test_get_all_pieces():
    rcube=Cube(3)
    pieces = rcube.get_all_pieces()
    assert len(pieces) == 26

    rcube=Cube(4)
    pieces = rcube.get_all_pieces()
    assert len(pieces) == 56

def test_move_outcome():
    rcube = Cube(3)
    rcube.rotate("B'")
    print(rcube)
    assert rcube.get_piece((2,0,0)).get_piece_colors()==(CubeColor.Y,CubeColor.O,CubeColor.B)
    assert rcube.get_piece((0,0,0)).get_piece_colors()==(CubeColor.W,CubeColor.O,CubeColor.B)

    rcube = Cube(3)
    rcube.rotate("F")
    print(rcube)
    assert rcube.get_piece((2,0,2)).get_piece_colors()==(CubeColor.Y,CubeColor.O,CubeColor.G)
    assert rcube.get_piece((0,0,2)).get_piece_colors()==(CubeColor.W,CubeColor.O,CubeColor.G)

    rcube = Cube(3)
    rcube.rotate("R")
    assert rcube.get_piece((2,0,0)).get_piece_colors()==(CubeColor.O,CubeColor.B,CubeColor.Y)
    assert rcube.get_piece((2,0,2)).get_piece_colors()==(CubeColor.O,CubeColor.B,CubeColor.W)

    rcube = Cube(3)
    rcube.rotate("L")
    assert rcube.get_piece((0,0,0)).get_piece_colors()==(CubeColor.R,CubeColor.G,CubeColor.W)
    assert rcube.get_piece((0,0,2)).get_piece_colors()==(CubeColor.R,CubeColor.G,CubeColor.Y)

    rcube = Cube(3)
    rcube.rotate("D")
    assert rcube.get_piece((2,0,0)).get_piece_colors()==(CubeColor.G,CubeColor.W,CubeColor.O)
    assert rcube.get_piece((2,0,2)).get_piece_colors()==(CubeColor.G,CubeColor.W,CubeColor.R)

    rcube = Cube(3)
    rcube.rotate("U")
    assert rcube.get_piece((0,2,0)).get_piece_colors()==(CubeColor.G,CubeColor.Y,CubeColor.R)
    assert rcube.get_piece((0,2,2)).get_piece_colors()==(CubeColor.G,CubeColor.Y,CubeColor.O)

def test_print_simple_move():
    rcube = Cube(3)
    rcube.rotate("D")
    print(rcube)

def test_wide_move():
    rcube = Cube(10)
    rcube.scramble(seed=333, num_steps=2000)
    rcube.rotate(rcube.reverse_history())
    assert rcube.is_done()

if __name__ == "__main__" :
    #test_get_all_pieces()
    #test_print_simple_move()
    #test_wide_move()
    #test_get_piece()
    pass