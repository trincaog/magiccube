import re

from cube.constants import CubeFace

class CubeMove():
    """Cube movement class
    Ex: F B' 2R 3Rw'
    """
    regex_pattern = re.compile("^([0-9]*)([LRDUBF])([w]?)([']?)$")

    def __init__(self, face:CubeFace, reversed:bool, wide:bool=False, layer:int=1):
        self.face=face
        self.reversed=reversed
        self.wide=wide
        self.layer=layer

    @staticmethod
    def create(move_str):
        """Create a CubeMove from string representation"""
        result = CubeMove.regex_pattern.match(move_str)
        if result is None:
            raise Exception("invalid movement" + str(move_str))
        result=result.groups()
        wide=True if result[2]=="w" else False
        reversed=True if result[3]=="'" else False
        face=CubeFace.create(result[1])

        if result[0]=="" and not wide:
            layer=1
        elif result[0] == "" and wide:
            layer=2
        else:
            layer=int(result[0])
        move=CubeMove(face, reversed, wide, layer)
        return move

    def reverse(self):
        """return the reverse move"""
        return CubeMove(self.face, not self.reversed, self.wide, self.layer)

    def __str__(self):
        return ("" if self.layer==1 else str(self.layer)) + \
            self.face.name + \
            ("w" if self.wide else "") + \
            ("'" if self.reversed else "")

        
