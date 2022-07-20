"""Cube Move implementation"""
from enum import Enum
import re

class CubeMoveType(Enum):
    L="L"
    R="R"
    D="D"
    U="U"
    B="B"
    F="F"
    X="X"
    Y="Y"
    Z="Z"
    M="M"
    E="E"
    S="S"

    @staticmethod
    def create(move_str:str):
        """Create a CubeMoveType"""
        if move_str == "L":
            return CubeMoveType.L
        if move_str == "R":
            return CubeMoveType.R
        if move_str == "D":
            return CubeMoveType.D
        if move_str == "U":
            return CubeMoveType.U
        if move_str == "B":
            return CubeMoveType.B
        if move_str == "F":
            return CubeMoveType.F
        if move_str == "X":
            return CubeMoveType.X
        if move_str == "Y":
            return CubeMoveType.Y
        if move_str == "Z":
            return CubeMoveType.Z
        if move_str == "M":
            return CubeMoveType.M
        if move_str == "E":
            return CubeMoveType.E
        if move_str == "S":
            return CubeMoveType.S
        raise Exception("invalid CubeMoveType " + str(move_str))

    def get_axis(self):
        """Return axis of movement (x=0, y=1, z=2)"""
        if self in (CubeMoveType.L,CubeMoveType.R,CubeMoveType.M,CubeMoveType.X):
            return 0
        if self in (CubeMoveType.D, CubeMoveType.U,CubeMoveType.E,CubeMoveType.Y):
            return 1
        if self in (CubeMoveType.B, CubeMoveType.F,CubeMoveType.S,CubeMoveType.Z):
            return 2
        raise Exception("invalid CubeMoveType" + str(self.value))

    def is_cube_rotation(self):
        return self in (CubeMoveType.X, CubeMoveType.Y, CubeMoveType.Z)

class CubeMove():
    """Cube movement class
    Ex: F B' 2R 3Rw'
    """

    __slots__ = ('type','is_reversed', 'wide','layer')

    regex_pattern = re.compile("^(?:([0-9]*)([LRDUBF])([w]?)([']?)|([XYZMES])([']?))$")

    def __init__(self, type:CubeMoveType, is_reversed:bool=False, wide:bool=False, layer:int=1):
        self.type=type
        self.is_reversed=is_reversed
        self.wide=wide
        self.layer=layer

    @staticmethod
    def create(move_str:str):
        """Create a CubeMove from string representation"""
        result = CubeMove.regex_pattern.match(move_str)
        if result is None:
            raise Exception("invalid movement " + str(move_str))
        result=result.groups()
        special_move = result[4]
        if special_move is not None:
            is_reversed=(result[5]=="'")
            if special_move=="X":
                return CubeMove(CubeMoveType.X, is_reversed)
            elif special_move=="Y":
                return CubeMove(CubeMoveType.Y, is_reversed)
            elif special_move=="Z":
                return CubeMove(CubeMoveType.Z, is_reversed)
            if special_move=="M":
                return CubeMove(CubeMoveType.M, is_reversed)
            elif special_move=="E":
                return CubeMove(CubeMoveType.E, is_reversed)
            elif special_move=="S":
                return CubeMove(CubeMoveType.S, is_reversed)
            else:
                assert False, "Invalid special move"
        else:
            type=CubeMoveType.create(result[1])
            wide=(result[2]=="w")
            is_reversed=(result[3]=="'")

            if result[0]=="" and not wide:
                layer=1
            elif result[0] == "" and wide:
                layer=2
            else:
                layer=int(result[0])
        
            move=CubeMove(type, is_reversed, wide, layer)
            return move

    def reverse(self):
        """return the reverse move"""
        return CubeMove(self.type, not self.is_reversed, self.wide, self.layer)

    def __str__(self):
        if (self.wide and self.layer==2)\
        or (not self.wide and self.layer==1):
            layer=""
        else:
            layer=self.layer
        wide="w" if self.wide else ""
        reversed_move="'" if self.is_reversed else ""
        return f"{layer}{self.type.name}{wide}{reversed_move}"
            
    def __repr__(self):
        return str(self)


    def __eq__(self, other):
        if (isinstance(other, CubeMove)):
            return self.layer == other.layer and self.type == other.type and self.wide == other.wide and self.is_reversed == other.is_reversed
        return False

    def __hash__(self):
        return hash(tuple([self.type,self.is_reversed,self.wide,self.layer]))
