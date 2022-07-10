"""Cube Piece implementation"""
import numpy as np
from magiccube.cube_base import PieceColor, CubeColor, CubeCoordinates, PieceType

class CubePiece:
    """Piece of the Cube (aka Cubelet)"""

    __slots__ = ('_colors',)

    def __init__(self, cube_size: int, position:CubeCoordinates):
        #self.initial_position = position
        self._colors = self._build_piece_colors(cube_size, position)

    def _build_piece_colors(self, cube_size:int, position:CubeCoordinates) ->np.ndarray:
        (_z,_y,_x)=position

        if _x == 0:
            x_color = CubeColor.R
        elif _x == cube_size-1:
            x_color = CubeColor.O
        else:
            x_color=None
        
        if _y == 0:
            y_color = CubeColor.W
        elif _y == cube_size-1:
            y_color = CubeColor.Y
        else:
            y_color = None
        
        if _z == 0:
            z_color = CubeColor.B
        elif _z == cube_size-1:
            z_color = CubeColor.G
        else:
            z_color = None
        
        colors =  [x_color,y_color, z_color]
        colors =  np.array(colors)
        return colors

    def get_piece_color(self, axis)->CubeColor:
        """Return the CuberPiece color of a given axis"""
        return self._colors[axis]

    def get_piece_colors_str(self, no_loc=False)->str:
        """Return a  string with the colors for xyz axis"""
        colors = self.get_piece_colors(no_loc=no_loc)
        colors = [c.name for c in colors if c is not None]
        return "".join(colors)

    def get_piece_colors(self, no_loc=False)->PieceColor:
        """Return CubeColors of the piece. Order is XYZ"""
        x_color = self.get_piece_color(0)
        y_color = self.get_piece_color(1)
        z_color = self.get_piece_color(2)
        colors = [x_color,y_color,z_color]

        if no_loc:
            colors = [c for c in colors if c is not None]
            colors = sorted(colors)

        return tuple(colors)

    def rotate_piece(self, axis:int) -> None:
        """Rotate the piece colors according to a given movement"""

        if axis==0: #LR
            indexes = [0,2,1]
            self._colors = self._colors[indexes]
        elif axis==1: #DU
            indexes = [2,1,0]
            self._colors = self._colors[indexes]
        elif axis==2: #BF
            indexes = [1,0,2]
            self._colors = self._colors[indexes]
        else:
            raise Exception("bad rotation type")

    def get_piece_type(self)->PieceType:
        """Return the piece type (ex: EDGE, CORNER, CENTER)"""
        sides = [c for c in self._colors if c is not None]
        num_sides = len(sides)
        if num_sides==3:
            return PieceType.CORNER
        if num_sides==2:
            return PieceType.EDGE
        if num_sides==1:
            return PieceType.CENTER
        if num_sides==0:
            return PieceType.INNER
        assert False, "Invalid Piece with num_sides="+str(num_sides)

    def __repr__(self):
        return str(self.get_piece_colors_str())

    def __str__(self):
        return str(self.get_piece_colors_str())

    def __lt__(self, other):
        return self._colors < other._colors
