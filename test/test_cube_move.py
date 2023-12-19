
import pytest
from magiccube.cube_base import CubeException
from magiccube.cube_move import CubeMove, CubeMoveType


def test_create_move():
    assert CubeMoveType.create("L") == CubeMoveType.L
    assert CubeMoveType.create("R") == CubeMoveType.R
    assert CubeMoveType.create("U") == CubeMoveType.U
    assert CubeMoveType.create("D") == CubeMoveType.D
    assert CubeMoveType.create("F") == CubeMoveType.F
    assert CubeMoveType.create("B") == CubeMoveType.B

    assert CubeMoveType.create("M") == CubeMoveType.M
    assert CubeMoveType.create("E") == CubeMoveType.E
    assert CubeMoveType.create("S") == CubeMoveType.S

    assert CubeMoveType.create("X") == CubeMoveType.X
    assert CubeMoveType.create("Y") == CubeMoveType.Y
    assert CubeMoveType.create("Z") == CubeMoveType.Z

    with pytest.raises(CubeException):
        CubeMoveType.create("A")


def test_create_move_str():
    assert CubeMove.create("F") == CubeMove(CubeMoveType.F)
    assert CubeMove.create("B") == CubeMove(CubeMoveType.B)
    assert CubeMove.create("L") == CubeMove(CubeMoveType.L)
    assert CubeMove.create("R") == CubeMove(CubeMoveType.R)
    assert CubeMove.create("D") == CubeMove(CubeMoveType.D)
    assert CubeMove.create("U") == CubeMove(CubeMoveType.U)

    with pytest.raises(CubeException):
        CubeMove.create("AAAA")


def test_move_eq():
    assert CubeMove.create("F") == CubeMove.create("F")
    assert CubeMove.create("B") != 1
