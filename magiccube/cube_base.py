"""Base types for Cube implementation"""

from enum import Enum
from typing import Optional, Tuple

class CubeFace(Enum):
    """Representation of a Cube Face"""
    L=0
    R=1
    D=2
    U=3
    B=4
    F=5

    def get_axis(self):
        """Return axis of movement (x=0, y=1, z=2)"""
        if self in (CubeFace.L,CubeFace.R):
            return 0
        if self in (CubeFace.D, CubeFace.U):
            return 1
        if self in (CubeFace.B, CubeFace.F):
            return 2
        raise Exception("invalid face" + str(self.value))

    @staticmethod
    def create(face_str:str):
        """Create a CubeFace"""
        if face_str == "L":
            return CubeFace.L
        if face_str == "R":
            return CubeFace.R
        if face_str == "D":
            return CubeFace.D
        if face_str == "U":
            return CubeFace.U
        if face_str == "B":
            return CubeFace.B
        if face_str == "F":
            return CubeFace.F
        raise Exception("invalid face " + str(face_str))

class CubeColor(Enum):
    """Representation of the color of a Cube Piece"""
    R=0
    O=1
    W=2
    Y=3
    B=4
    G=5

    def __lt__(self, other):
        return self.name < other.name

    @staticmethod
    def create(color_str:str):
        """Create a CubeColor"""
        if color_str == "R":
            return CubeColor.R
        if color_str == "O":
            return CubeColor.O
        if color_str == "W":
            return CubeColor.W
        if color_str == "Y":
            return CubeColor.Y
        if color_str == "B":
            return CubeColor.B
        if color_str == "G":
            return CubeColor.G
        raise Exception("invalid color " + str(color_str))

CubeCoordinates=Tuple[int,int,int]
PieceColor = Tuple[Optional[CubeColor], Optional[CubeColor], Optional[CubeColor]]

class PieceType(Enum):
    """Type of piece"""
    CORNER=3
    EDGE=2
    CENTER=1
    INNER=0
