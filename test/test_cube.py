import os
import random
from unittest import mock
import pytest
import numpy as np
from magiccube import Cube
from magiccube.cube import CubeException
from magiccube.cube_base import Face, PieceType
from magiccube.cube_move import CubeMove, CubeMoveType
from magiccube.cube_piece import Color, CubePiece

from magiccube.solver.basic.basic_solver import BasicSolver, SolverException


def test_cube_size_1():
    with pytest.raises(CubeException):
        Cube(1)


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
    for _ in range(12):
        c.rotate("R' D' R D")
    c.check_consistency()
    assert c.is_done()


def test_12_moves_2d():
    c = Cube(2)
    c.check_consistency()
    for _ in range(12):
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
    assert c.get_face_flat(Face.F) == [
        Color.G, Color.G, Color.Y, Color.G,
        Color.G, Color.G, Color.Y, Color.G,
        Color.G, Color.G, Color.Y, Color.G,
        Color.G, Color.G, Color.Y, Color.G,
    ]

    c.reset()
    c.rotate("Uw")
    assert c.get_face_flat(Face.F) == [
        Color.R, Color.R, Color.R, Color.R,
        Color.R, Color.R, Color.R, Color.R,
        Color.G, Color.G, Color.G, Color.G,
        Color.G, Color.G, Color.G, Color.G,
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


def test_pattern1():
    c = Cube(3)
    c.rotate("R R L' L' B B F' F' U U D' D'")
    c.check_consistency()


def test_pattern2():
    c = Cube(3)
    c.rotate("R' L U D' F B' R' L")
    c.check_consistency()


def test_history_str():
    c = Cube(3)
    moves = "R' L U D' F B' R' L"
    c.rotate(moves)
    assert c.history(to_str=True) == moves


def test_history():
    c = Cube(5)
    moves = [CubeMove(CubeMoveType.R, False), CubeMove(
        CubeMoveType.F, True), CubeMove(CubeMoveType.D, False, wide=True, layer=2)]
    c.rotate(moves)
    assert c.history() == moves


def test_reverse():
    c = Cube(3)
    moves = "R' L U D' F B' R' L"
    c.rotate(moves)
    assert c.reverse_history(to_str=True) == "L' R B F' D U' L' R"
    c.rotate(c.reverse_history())
    assert c.is_done()


def test_reverse_multiplicative_moves():
    c = Cube(3)
    moves = "R' L2"
    c.rotate(moves)
    assert c.reverse_history(to_str=True) == "L2 R"
    c.rotate(c.reverse_history())
    assert c.is_done()


def test_scramble_3x3():
    c = Cube(3)
    c.scramble(num_steps=50)
    assert not c.is_done()


def test_scramble_2x2():
    c = Cube(2)
    c.scramble(num_steps=50)
    assert not c.is_done()


def test_scramble_4x4():
    c = Cube(4)
    c.scramble(num_steps=50)
    assert not c.is_done()


def test_get_piece():
    c = Cube(3)
    piece = c.get_piece((2, 0, 0))
    assert piece.get_piece_color(Face.R.get_axis()) == Color.R
    assert piece.get_piece_color(Face.D.get_axis()) == Color.Y
    assert piece.get_piece_color(Face.B.get_axis()) == Color.B

    piece = c.get_piece((0, 2, 2))
    assert piece.get_piece_color(Face.L.get_axis()) == Color.O
    assert piece.get_piece_color(Face.U.get_axis()) == Color.W
    assert piece.get_piece_color(Face.F.get_axis()) == Color.G


def test_get_all_faces():
    c = Cube(3)
    faces = c.get_all_faces()
    assert np.all(np.array(faces[Face.F]).flatten() == Color.G)
    assert np.all(np.array(faces[Face.B]).flatten() == Color.B)
    assert np.all(np.array(faces[Face.L]).flatten() == Color.O)
    assert np.all(np.array(faces[Face.R]).flatten() == Color.R)
    assert np.all(np.array(faces[Face.U]).flatten() == Color.W)
    assert np.all(np.array(faces[Face.D]).flatten() == Color.Y)


def test_get_all_pieces():
    c = Cube(3)
    pieces = c.get_all_pieces()
    assert len(pieces) == 26

    c = Cube(4)
    pieces = c.get_all_pieces()
    assert len(pieces) == 56


def test_move():
    c = Cube(3)
    c.rotate("L")
    assert c.get_piece((1, 0, 0)).get_piece_colors() == (
        None, Color.Y, Color.B)
    assert c.get_piece((0, 0, 0)).get_piece_colors() == (
        Color.O, Color.G, Color.Y)
    assert c.get_piece((0, 0, 2)).get_piece_colors() == (
        Color.O, Color.G, Color.W)


def test_move_special_rot():
    c = Cube(3)
    c.rotate("X'")
    assert c.get_piece((2, 2, 2)).get_piece_colors() == (
        Color.R, Color.B, Color.W)
    c.reset()
    c.rotate("Y")
    assert c.get_piece((2, 2, 2)).get_piece_colors() == (
        Color.B, Color.W, Color.R)
    c.reset()
    c.rotate("Z")
    assert c.get_piece((2, 2, 2)).get_piece_colors() == (
        Color.W, Color.O, Color.G)


def test_move_special_mid():
    c = Cube(3)
    c.rotate("M")
    assert c.get_piece((1, 2, 2)).get_piece_colors() == (
        None, Color.B, Color.W)
    c.rotate("E'")
    assert c.get_piece((2, 1, 2)).get_piece_colors() == (
        Color.B, None, Color.R)
    c.rotate("S")
    assert c.get_piece((2, 2, 1)).get_piece_colors() == (
        Color.W, Color.O, None)


def test_move_noloc():
    c = Cube(3)
    c.rotate("L")
    assert c.get_piece((1, 0, 0)).get_piece_colors(
        no_loc=True) == (Color.B, Color.Y)
    assert c.get_piece((0, 0, 0)).get_piece_colors(
        no_loc=True) == (Color.G, Color.O, Color.Y)
    assert c.get_piece((0, 0, 2)).get_piece_colors(
        no_loc=True) == (Color.G, Color.O, Color.W)


def test_move_outcome():
    c = Cube(3)
    c.rotate("B'")
    assert c.get_piece((0, 2, 0)).get_piece_colors_str() == 'YOB'
    assert c.get_piece((0, 0, 0)).get_piece_colors_str() == 'YRB'

    c = Cube(3)
    c.rotate("F")
    assert c.get_piece((2, 0, 2)).get_piece_colors_str() == 'WRG'
    assert c.get_piece((0, 0, 2)).get_piece_colors_str() == 'YRG'

    c = Cube(3)
    c.rotate("R")
    assert c.get_piece((2, 0, 0)).get_piece_colors_str() == 'RBW'
    assert c.get_piece((2, 0, 2)).get_piece_colors_str() == 'RBY'

    c = Cube(3)
    c.rotate("L")
    assert c.get_piece((0, 0, 1)).get_piece_colors_str() == 'OG'
    assert c.get_piece((0, 0, 0)).get_piece_colors_str() == 'OGY'
    assert c.get_piece((0, 0, 2)).get_piece_colors_str() == 'OGW'

    c = Cube(3)
    c.rotate("D")
    assert c.get_piece((2, 0, 0)).get_piece_colors_str(
    ) == 'GYR', c.get_piece((2, 0, 0)).get_piece_colors_str()
    assert c.get_piece((2, 0, 2)).get_piece_colors_str() == 'GYO'

    c = Cube(3)
    c.rotate("U")
    assert c.get_piece((0, 2, 0)).get_piece_colors_str() == 'GWO'
    assert c.get_piece((0, 2, 2)).get_piece_colors_str() == 'GWR'


def test_find():
    c = Cube(3)
    c.rotate("R")
    coord, _ = c.find_piece("GRW")
    assert coord == (2, 2, 0)
    coord, _ = c.find_piece("BOY")
    assert coord == (0, 0, 0)


@mock.patch.dict(os.environ, {"TERM": "none"})
def test_print_simple_move():

    c = Cube(3)
    c.rotate("F")

    assert str(c) == \
        "          W  W  W                   \n" + \
        "          W  W  W                   \n" + \
        "          O  O  O                   \n" + \
        " O  O  Y  G  G  G  W  R  R  B  B  B \n" + \
        " O  O  Y  G  G  G  W  R  R  B  B  B \n" + \
        " O  O  Y  G  G  G  W  R  R  B  B  B \n" + \
        "          R  R  R                   \n" + \
        "          Y  Y  Y                   \n" + \
        "          Y  Y  Y                   \n"


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
    assert c.get_piece(coordinates=(0, 0, 2)
                       ).get_piece_type() == PieceType.CORNER
    assert c.get_piece(coordinates=(1, 0, 1)
                       ).get_piece_type() == PieceType.CENTER
    assert c.get_piece(coordinates=(2, 1, 2)
                       ).get_piece_type() == PieceType.EDGE
    inner = c.get_piece(coordinates=(1, 1, 1))
    assert inner is None or inner.get_piece_type() == PieceType.INNER


def test_set_cube():
    c = Cube(3)
    c.set("YYYYYYYYYRRRRRRRRRGGGGGGGGGOOOOOOOOOBBBBBBBBBWWWWWWWWW")
    assert c.is_done()


def test_set_cube_invalid():
    c = Cube(3)
    with pytest.raises(CubeException):
        c.set("YYYYYYYYYRRRRRRRRRGGGGGGGGGOOOOOOOOOBBBBBBBBBWWWWWWWWWYYYYYYYYYYYY")


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


def test_get_cube():
    c = Cube(3)
    assert c.get() == "WWWWWWWWWOOOOOOOOOGGGGGGGGGRRRRRRRRRBBBBBBBBBYYYYYYYYY"
    c.rotate("U")
    assert c.get() == "WWWWWWWWWGGGOOOOOORRRGGGGGGBBBRRRRRROOOBBBBBBYYYYYYYYY"

    state = "YYYYYYYYYRRRRRRRRRGGGGGGGGGOOOOOOOOOBBBBBBBBBWWWWWWWWW"
    c = Cube(3)
    c.set(state)
    assert c.get() == state


def test_inconsistent_cube():
    c = Cube(3)

    # pylint: disable=protected-access
    c._cube[0, 0, 0] = CubePiece(colors=[None, None, None])
    with pytest.raises(CubeException):
        c.check_consistency()


def test_bad_direction():
    c = Cube(3)
    with pytest.raises(CubeException):
        # pylint: disable=protected-access
        c._get_direction(CubeMove(None))  # type: ignore


def test_mes_move_even_cube():
    c = Cube(4)
    with pytest.raises(CubeException):
        c.rotate("M")


def test_invalid_slice():
    c = Cube(4)
    with pytest.raises(CubeException):
        # pylint: disable=protected-access
        c._move_to_slice(CubeMove(CubeMoveType.L, layer=-1))

    with pytest.raises(CubeException):
        # pylint: disable=protected-access
        c._move_to_slice(CubeMove(CubeMoveType.L, layer=5))


def test_rotate_twice():
    c = Cube(3)
    c.rotate("U2")
    assert c.get_face_flat(Face.F) == [
        Color.B, Color.B, Color.B,
        Color.G, Color.G, Color.G,
        Color.G, Color.G, Color.G,
    ]
    c.rotate("U'2")
    assert c.is_done()

    c.rotate("D2")
    assert c.get_face_flat(Face.F) == [
        Color.G, Color.G, Color.G,
        Color.G, Color.G, Color.G,
        Color.B, Color.B, Color.B,
    ]
    c.rotate("D'2")
    assert c.is_done()

    c.rotate("L2")
    assert c.get_face_flat(Face.F) == [
        Color.B, Color.G, Color.G,
        Color.B, Color.G, Color.G,
        Color.B, Color.G, Color.G,
    ]
    c.rotate("L'2")
    assert c.is_done()

    c.rotate("R2")
    assert c.get_face_flat(Face.F) == [
        Color.G, Color.G, Color.B,
        Color.G, Color.G, Color.B,
        Color.G, Color.G, Color.B,
    ]
    c.rotate("R'2")
    assert c.is_done()

    c.rotate("F2")
    assert c.get_face_flat(Face.U) == [
        Color.W, Color.W, Color.W,
        Color.W, Color.W, Color.W,
        Color.Y, Color.Y, Color.Y,
    ]
    c.rotate("F'2")
    assert c.is_done()

    c.rotate("B2")
    assert c.get_face_flat(Face.U) == [
        Color.Y, Color.Y, Color.Y,
        Color.W, Color.W, Color.W,
        Color.W, Color.W, Color.W,
    ]
    c.rotate("B'2")
    assert c.is_done()


def test_get_kociemba_facelet_positions():
    c = Cube(3)

    assert c.get_kociemba_facelet_positions(
    ) == 'UUUUUUUUURRRRRRRRRFFFFFFFFFDDDDDDDDDLLLLLLLLLBBBBBBBBB'

    moves = 'R F U'
    c.rotate(moves)

    assert c.get_kociemba_facelet_positions(
    ) == 'LUULUULFFUBBURRFRRURRFFFDDDRRRDDBDDBFFFLLDLLBLLDUBBUBB'


def test_get_kociemba_facelet_colors():
    c = Cube(3)

    assert c.get_kociemba_facelet_colors(
    ) == 'WWWWWWWWWRRRRRRRRRGGGGGGGGGYYYYYYYYYOOOOOOOOOBBBBBBBBB'

    moves = 'R F U'
    c.rotate(moves)

    assert c.get_kociemba_facelet_colors(
    ) == 'OWWOWWOGGWBBWRRGRRWRRGGGYYYRRRYYBYYBGGGOOYOOBOOYWBBWBB'


def test_undo():
    c = Cube(3)
    c.rotate("U F B")
    assert not c.is_done()
    assert c.history(to_str=True) == "U F B"
    c.undo(2)
    assert c.history(to_str=True) == "U"
    c.undo()
    assert c.history(to_str=True) == ""
    assert c.is_done()


def test_undo_fail_history_disabled():
    c = Cube(3, hist=False)
    c.rotate("U F B")
    with pytest.raises(CubeException):
        c.undo(1)


def test_undo_fail_too_many_undos():
    c = Cube(3)
    c.rotate("U F B")
    with pytest.raises(CubeException):
        c.undo(4)


def test_history_disabled():
    c = Cube(3, hist=False)
    c.rotate("U F B")
    assert c.history() == []
    assert c.reverse_history() == []


if __name__ == "__main__":
    pytest.main()
