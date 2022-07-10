import re
from magiccube.constants import CubeFace

class CubeMove():
    """Cube movement class
    Ex: F B' 2R 3Rw'
    """
    regex_pattern = re.compile("^([0-9]*)([LRDUBF])([w]?)([']?)$")

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
        wide=(result[2]=="w")
        is_reversed=(result[3]=="'")
        face=CubeFace.create(result[1])

        if result[0]=="" and not wide:
            layer=1
        elif result[0] == "" and wide:
            layer=2
        elif result[0] == "1" and wide:
            raise Exception("wide movement not allowed for 1 layer")
        else:
            layer=int(result[0])
        move=CubeMove(face, is_reversed, wide, layer)
        return move

    def reverse(self):
        """return the reverse move"""
        return CubeMove(self.face, not self.is_reversed, self.wide, self.layer)

    def __str__(self):
        return ("" if self.layer==1 else str(self.layer)) + \
            self.face.name + \
            ("w" if self.wide else "") + \
            ("'" if self.is_reversed else "")
            