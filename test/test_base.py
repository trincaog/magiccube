import pytest
from magiccube.cube import CubeException
from magiccube.cube_base import Face
from magiccube.cube_piece import Color


def test_face_create():
    assert Face.create("F") == Face.F
    assert Face.create("B") == Face.B
    assert Face.create("L") == Face.L
    assert Face.create("R") == Face.R
    assert Face.create("U") == Face.U
    assert Face.create("D") == Face.D

    with pytest.raises(CubeException):
        Face.create("X")


def test_color_create():
    assert Color.create("R") == Color.R
    assert Color.create("O") == Color.O
    assert Color.create("B") == Color.B
    assert Color.create("G") == Color.G
    assert Color.create("Y") == Color.Y
    assert Color.create("W") == Color.W

    with pytest.raises(CubeException):
        Color.create("X")


if __name__ == "__main__":
    pytest.main()
