from typing import Tuple
import numpy as np
from magiccube.constants import CubeColor, CubeCoordinates, CubeFace

class CubePiece:

    def __init__(self, cube_size: int, position:CubeCoordinates):
        self.initial_position = position
        self._colors = self._build_piece_colors(cube_size, position)
        self._initial_colors = self._build_piece_colors(cube_size, self.initial_position)

    def _build_piece_colors(self, cube_size:int, position:CubeCoordinates) ->np.ndarray:
        (x,y,z)=position

        colors = [
            CubeColor.R if x == 0 else None,# L
            CubeColor.O if x == cube_size-1 else None,# R
            CubeColor.W if y == 0 else None,# D
            CubeColor.Y if y == cube_size-1 else None,# U
            CubeColor.B if z == 0 else None,# B
            CubeColor.G if z == cube_size-1 else None,# F
        ]
        colors =  np.array(colors)
        return colors

    def get_piece_color(self, face: CubeFace)->CubeColor:
        """Return the CuberPiece color of a given CubeFace"""
        return self._colors[face.value]

    def get_piece_colors(self)->Tuple[CubeColor,CubeColor,CubeColor]:
        """Return a tuple of CubeColor for x,y,z axis"""
        x = self.get_piece_color(CubeFace.L) \
            if self.get_piece_color(CubeFace.L) is not None \
            else self.get_piece_color(CubeFace.R)
        y = self.get_piece_color(CubeFace.D) \
            if self.get_piece_color(CubeFace.D) is not None \
            else self.get_piece_color(CubeFace.U)
        z = self.get_piece_color(CubeFace.B) \
            if self.get_piece_color(CubeFace.B) is not None \
            else self.get_piece_color(CubeFace.F)
        return (x,y,z)

    def rotate_piece(self, axis:int, direction) -> None:
        """Rotate the piece colors according to a given movement"""

        if   axis==0 and direction==1: #L R'
            indexes = [0,1,5,4,2,3] # LR DU BF
            self._colors = self._colors[indexes]
        elif axis==0 and direction==-1: #L' R
            indexes = [0,1,4,5,3,2] # LR DU BF
            self._colors = self._colors[indexes]
        elif axis==1 and direction==-1: #U' D
            indexes = [4,5,2,3,1,0] # LR DU BF
            self._colors = self._colors[indexes]
        elif axis==1 and direction==1: #U, D'
            indexes = [5,4,2,3,0,1] # LR DU BF
            self._colors = self._colors[indexes]
        elif axis==2 and direction==1: #F', B
            indexes = [3,2,0,1,4,5] # LR DU BF
            self._colors = self._colors[indexes]
        elif axis==2 and direction==-1: #F, B'
            indexes = [2,3,1,0,4,5] # LR DU BF
            self._colors = self._colors[indexes]
        else:
            raise Exception("bad rotation type")

    def __repr__(self):
        return str(self.initial_position)

    def __str__(self):
        return str(self.get_piece_colors())

