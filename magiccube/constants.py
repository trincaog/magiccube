from enum import Enum
from typing import Tuple

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

CubeCoordinates=Tuple[int,int,int]
