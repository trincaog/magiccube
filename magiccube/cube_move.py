"""Cube Move implementation"""
import re
from magiccube.cube_base import CubeFace

class CubeMove():
    """Cube movement class
    Ex: F B' 2R 3Rw'
    """

    __slots__ = ('face', 'is_reversed', 'wide','layer')

    regex_pattern = re.compile("^(?:([0-9]*)([LRDUBF])([w]?)([']?)|([XYZ])([']?))$")

    def __init__(self, face:CubeFace, is_reversed:bool, wide:bool=False, layer:int=1):
        self.face=face
        self.is_reversed=is_reversed
        self.wide=wide
        self.layer=layer

    @staticmethod
    def create(move_str:str):
        """Create a CubeMove from string representation"""
        result = CubeMove.regex_pattern.match(move_str)
        if result is None:
            raise Exception("invalid movement" + str(move_str))
        result=result.groups()
        special_move = result[4]
        if special_move is not None:
            is_reversed=(result[5]=="'")
            if special_move=="X":
                return CubeMove(CubeFace.R, is_reversed, True, layer=-1)
            elif special_move=="Y":
                return CubeMove(CubeFace.U, is_reversed, True, layer=-1)
            elif special_move=="Z":
                return CubeMove(CubeFace.F, is_reversed, True, layer=-1)
            else:
                assert False, "Invalid special move"
        else:
            face=CubeFace.create(result[1])
            wide=(result[2]=="w")
            is_reversed=(result[3]=="'")

            if result[0]=="" and not wide:
                layer=1
            elif result[0] == "" and wide:
                layer=2
            else:
                layer=int(result[0])
        
            move=CubeMove(face, is_reversed, wide, layer)
            return move

    def reverse(self):
        """return the reverse move"""
        return CubeMove(self.face, not self.is_reversed, self.wide, self.layer)

    def __str__(self):
        if (self.wide and self.layer==2)\
        or (not self.wide and self.layer==1):
            layer=""
        else:
            layer=self.layer
        wide="w" if self.wide else ""
        reversed_move="'" if self.is_reversed else ""
        return f"{layer}{self.face.name}{wide}{reversed_move}"
            