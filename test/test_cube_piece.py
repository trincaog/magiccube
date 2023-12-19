
import pytest
from magiccube.cube_base import Color, CubeException, PieceType
from magiccube.cube_piece import CubePiece


def test_create_piece_nok():
    with pytest.raises(CubeException):
        CubePiece()


def test_rotate():
    c = CubePiece(colors=[Color.O, Color.W, Color.B])
    c.rotate_piece(0)
    assert (c.get_piece_colors() == (Color.O, Color.B, Color.W))

    c = CubePiece(colors=[Color.O, Color.W, Color.B])
    with pytest.raises(CubeException):
        c.rotate_piece(3)


def test_get_piece_type():
    c = CubePiece(colors=[Color.O, Color.W, Color.B])
    assert c.get_piece_type() == PieceType.CORNER

    c = CubePiece(colors=[Color.O, Color.W, None])
    assert c.get_piece_type() == PieceType.EDGE

    c = CubePiece(colors=[Color.O, None, None])
    assert c.get_piece_type() == PieceType.CENTER

    with pytest.raises(CubeException):
        c = CubePiece(colors=[None, None, None])
        c.get_piece_type()
