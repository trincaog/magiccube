"""Cube Move implementation"""
from enum import Enum
import re

from magiccube.cube_base import CubeException


class CubeMoveType(Enum):
    """Cube Move Type"""

    L = "L"
    R = "R"
    D = "D"
    U = "U"
    B = "B"
    F = "F"
    X = "X"
    Y = "Y"
    Z = "Z"
    M = "M"
    E = "E"
    S = "S"

    @staticmethod
    def create(move_str: str):
        # pylint: disable=too-many-return-statements
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
        if move_str in ("X", 'x'):
            return CubeMoveType.X
        if move_str in ("Y", 'y'):
            return CubeMoveType.Y
        if move_str in ("Z", 'z'):
            return CubeMoveType.Z
        if move_str == "M":
            return CubeMoveType.M
        if move_str == "E":
            return CubeMoveType.E
        if move_str == "S":
            return CubeMoveType.S
        raise CubeException("invalid CubeMoveType " + str(move_str))

    def get_axis(self):
        """Return axis of movement (x=0, y=1, z=2)"""
        if self in (CubeMoveType.L, CubeMoveType.R, CubeMoveType.M, CubeMoveType.X):
            return 0
        if self in (CubeMoveType.D, CubeMoveType.U, CubeMoveType.E, CubeMoveType.Y):
            return 1
        if self in (CubeMoveType.B, CubeMoveType.F, CubeMoveType.S, CubeMoveType.Z):
            return 2
        raise CubeException("invalid CubeMoveType" +
                            str(self.value))  # pragma: no cover

    def is_cube_rotation(self):
        """Return True if the movement type is a whole cube rotation on any of the X,Y,Z axis"""
        return self in (CubeMoveType.X, CubeMoveType.Y, CubeMoveType.Z)


class CubeMove():
    """Cube movement class
    Ex: F B' 2R 3Rw'
    """

    __slots__ = ('type', 'is_reversed', 'wide', 'layer', 'count')

    _regex_pattern = re.compile(
        "^(?:([0-9]*)(([LRDUBF])([w]?)|([xyzXYZMES]))([']?)(2?))$")

    # pylint: disable=too-many-positional-arguments
    def __init__(self, move_type: CubeMoveType, is_reversed: bool = False, wide: bool = False, layer: int = 1, count: int = 1):
        self.type = move_type
        """CubeMoveType"""

        self.is_reversed = is_reversed
        """True if the move is reversed (counter clock wise)"""

        self.wide = wide
        """True if the move is wide (2+ layers)"""

        self.layer = layer
        """Layer of the move (1-N)"""

        self.count = count
        """Number of repetitions of the move"""

    @staticmethod
    def _create_move(result, special_move):
        if special_move is not None:
            is_reversed = result[-2] == "'"
            if special_move in ("X", "x"):
                return CubeMove(CubeMoveType.X, is_reversed)
            if special_move in ("Y", "y"):
                return CubeMove(CubeMoveType.Y, is_reversed)
            if special_move in ("Z", "z"):
                return CubeMove(CubeMoveType.Z, is_reversed)
            if special_move == "M":
                return CubeMove(CubeMoveType.M, is_reversed)
            if special_move == "E":
                return CubeMove(CubeMoveType.E, is_reversed)
            if special_move == "S":
                return CubeMove(CubeMoveType.S, is_reversed)

            raise CubeException(
                "Invalid special move")  # pragma: no cover
        move_type = CubeMoveType.create(result[2])
        wide = result[3] == "w"
        is_reversed = result[-2] == "'"

        if result[0] == "" and not wide:
            layer = 1
        elif result[0] == "" and wide:
            layer = 2
        else:
            layer = int(result[0])

        move = CubeMove(move_type, is_reversed, wide, layer)
        return move

    @staticmethod
    def create(move_str: str):
        """Create a CubeMove from string representation"""
        # pylint: disable=too-many-return-statements

        result_match = CubeMove._regex_pattern.match(move_str)
        if result_match is None:
            raise CubeException("invalid movement " + str(move_str))
        result = result_match.groups()
        special_move = result[4]
        move_count = result[-1]

        move = CubeMove._create_move(result, special_move)
        move.count = int(move_count) if move_count else 1
        return move

    def reverse(self):
        """return the reverse move"""
        return CubeMove(self.type, not self.is_reversed, self.wide, self.layer, count=self.count)

    def __str__(self):
        if (self.wide and self.layer == 2)\
                or (not self.wide and self.layer == 1):
            layer = ""
        else:
            layer = self.layer  # pragma: no cover
        wide = "w" if self.wide else ""
        reversed_move = "'" if self.is_reversed else ""
        count = "" if int(self.count) == 1 else int(self.count)
        string = f"{layer}{self.type.name}{wide}{reversed_move}{count}"
        return string.replace("'2", "2")

    def __repr__(self):
        return str(self)  # pragma: no cover

    def __eq__(self, other):
        if isinstance(other, CubeMove):
            return (
                self.layer == other.layer and self.type == other.type
                and self.wide == other.wide and self.is_reversed == other.is_reversed
            )
        return False

    def __hash__(self):
        return hash(tuple([self.type, self.is_reversed, self.wide, self.layer]))
