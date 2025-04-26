"""Cube Piece implementation"""
from typing import List, Optional, Tuple
import numpy as np
from magiccube.cube_base import Color, Coordinates, CubeException, PieceType


class CubePiece:
    """Piece of the Cube (aka Cubelet)"""

    __slots__ = ('_colors',)

    def __init__(self, cube_size: Optional[int] = None, position: Optional[Coordinates] = None,
                 colors: Optional[List[Optional[Color]]] = None):
        if cube_size is not None and position is not None:
            self._colors = self._build_piece_colors(cube_size, position)
        elif colors is not None and len(colors) == 3:
            self._colors = np.array(colors)
        else:
            raise CubeException(
                "Can't create CubePiece. Either position or color must be specified.")

    def _build_piece_colors(self, cube_size: int, position: Coordinates) -> np.ndarray:
        """Creates the default piece colors"""
        (_z, _y, _x) = position

        if _x == 0:
            x_color = Color.O
        elif _x == cube_size-1:
            x_color = Color.R
        else:
            x_color = None

        if _y == 0:
            y_color = Color.Y
        elif _y == cube_size-1:
            y_color = Color.W
        else:
            y_color = None

        if _z == 0:
            z_color = Color.B
        elif _z == cube_size-1:
            z_color = Color.G
        else:
            z_color = None

        colors = [x_color, y_color, z_color]
        return np.array(colors)

    def get_piece_color(self, axis) -> Color:
        """Return the CuberPiece color of a given axis"""
        return self._colors[axis]

    def get_piece_colors_str(self, no_loc=False) -> str:
        """Return a  string with the colors for xyz axis"""
        colors = self.get_piece_colors(no_loc=no_loc)
        color_names = [c.name for c in colors if c is not None]
        return "".join(color_names)

    def get_piece_colors(self, no_loc=False) -> Tuple[Optional[Color], ...]:
        """Return CubeColors of the piece. Order is XYZ"""
        x_color = self.get_piece_color(0)
        y_color = self.get_piece_color(1)
        z_color = self.get_piece_color(2)
        colors = [x_color, y_color, z_color]

        if no_loc:
            colors = [c for c in colors if c is not None]
            colors = sorted(colors)

        return tuple(colors)

    def set_piece_color(self, axis: int, color: Color):
        """Set the piece colors"""
        self._colors[axis] = color

    def rotate_piece(self, axis: int) -> None:
        """Rotate the piece colors according to a given movement"""

        if axis == 0:  # LR
            indexes = [0, 2, 1]
            self._colors = self._colors[indexes]
        elif axis == 1:  # DU
            indexes = [2, 1, 0]
            self._colors = self._colors[indexes]
        elif axis == 2:  # BF
            indexes = [1, 0, 2]
            self._colors = self._colors[indexes]
        else:
            raise CubeException("bad rotation type")

    def get_piece_type(self) -> PieceType:
        """Return the piece type (ex: EDGE, CORNER, CENTER)"""
        sides = [c for c in self._colors if c is not None]
        num_sides = len(sides)
        if num_sides == 3:
            return PieceType.CORNER
        if num_sides == 2:
            return PieceType.EDGE
        if num_sides == 1:
            return PieceType.CENTER
        raise CubeException("Invalid Piece with num_sides="+str(num_sides))

    def __repr__(self):
        return str(self.get_piece_colors_str())

    def __str__(self):
        return str(self.get_piece_colors_str())  # pragma:no cover

    def __lt__(self, other):
        return self._colors < other._colors  # pragma:no cover
