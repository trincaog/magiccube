"""Rubik Cube implementation"""
from typing import Dict, List, Optional, Tuple, Union
import random
import numpy as np
from magiccube.cube_base import Color, CubeException, Face
from magiccube.cube_piece import Coordinates, CubePiece
from magiccube.cube_move import CubeMove, CubeMoveType
from magiccube.cube_print import CubePrintStr


class Cube:
    """Rubik Cube implementation"""

    __slots__ = ("size", "_store_history", "_cube_face_indexes", "_cube_piece_indexes",
                 "_cube_piece_indexes_inv", "_cube", "_history")

    def __init__(self, size: int = 3, state: Optional[str] = None, hist: Optional[bool] = True):

        if size <= 1:
            raise CubeException("Cube size must be >= 2")

        self.size = size
        """Cube size"""

        self._store_history = hist

        # record the indexes of every cube face
        self._cube_face_indexes = [
            [[(0, y, z) for z in range(self.size)]
                for y in reversed(range(self.size))],  # L
            [[(self.size-1, y, z) for z in reversed(range(self.size))]
                for y in reversed(range(self.size))],  # R
            [[(x, 0, z) for x in range(self.size)]
                for z in reversed(range(self.size))],  # D
            [[(x, self.size-1, z) for x in range(self.size)]
                for z in range(self.size)],  # U
            [[(x, y, 0) for x in reversed(range(self.size))]
                for y in reversed(range(self.size))],  # B
            [[(x, y, self.size-1) for x in range(self.size)]
                for y in reversed(range(self.size))],  # F
        ]

        # record the indexes of every cube piece
        self._cube_piece_indexes = [
            (x, y, z)
            for z in range(self.size)
            for y in range(self.size)
            for x in range(self.size)
            if self._is_outer_position(x, y, z)
        ]
        self._cube_piece_indexes_inv = {
            v: idx for idx, v in enumerate(self._cube_piece_indexes)}

        self.reset()
        if state is not None:
            self.set(state)

    def _is_outer_position(self, _x: int, _y: int, _z: int) -> bool:
        """Test if the coordinates indicate and outer cube position"""
        return _x == 0 or _x == self.size-1 \
            or _y == 0 or _y == self.size-1 \
            or _z == 0 or _z == self.size-1  # dont include center pieces

    def reset(self):
        """Reset the cube to the initial configuration"""
        initial_cube = [
            [[CubePiece(self.size, (x, y, z))
              if self._is_outer_position(x, y, z) else None
              for x in range(self.size)]
             for y in range(self.size)]
            for z in range(self.size)
        ]
        self._cube = np.array(initial_cube, dtype=np.object_)
        self._history = []

    def set(self, image: str):
        """Sets the cube state.

        Parameters
        ----------
        image: str
        Colors of every cube face in the following order: UP, LEFT, FRONT, RIGHT, BACK, DOWN.
        Spaces and newlines are ignored.

        Example:
        YYYYYYYYY RRRRRRRRR GGGGGGGGG OOOOOOOOO BBBBBBBBB WWWWWWWWW
        """
        image = image.replace(" ", "")
        image = image.replace("\n", "")

        if len(image) != 6*self.size*self.size:
            raise CubeException(
                "Cube state has an invalid size. Should be: " + str(6*self.size*self.size))

        img = [Color.create(x) for x in image]

        self.reset()
        for i, color in enumerate(img):
            face = i // (self.size**2)
            remain = i % (self.size**2)
            if face == 0:  # U
                _x = remain % self.size
                _y = self.size-1
                _z = remain//self.size
                self.get_piece((_x, _y, _z)).set_piece_color(1, color)
            elif face == 5:  # D
                _x = remain % self.size
                _y = 0
                _z = self.size-(remain//self.size)-1
                self.get_piece((_x, _y, _z)).set_piece_color(1, color)
            elif face == 1:  # L
                _x = 0
                _y = self.size-(remain//self.size)-1
                _z = remain % self.size
                self.get_piece((_x, _y, _z)).set_piece_color(0, color)
            elif face == 3:  # R
                _x = self.size-1
                _y = self.size-(remain//self.size)-1
                _z = self.size-(remain % self.size)-1
                self.get_piece((_x, _y, _z)).set_piece_color(0, color)
            elif face == 4:  # B
                _x = self.size-(remain % self.size)-1
                _y = self.size-(remain//self.size)-1
                _z = 0
                self.get_piece((_x, _y, _z)).set_piece_color(2, color)
            elif face == 2:  # F
                _x = remain % self.size
                _y = self.size-(remain//self.size)-1
                _z = self.size-1
                self.get_piece((_x, _y, _z)).set_piece_color(2, color)

    def get(self, face_order: Optional[List[Face]] = None):
        """
        Get the cube state as a string with the colors of every cube face in the following order: UP, LEFT, FRONT, RIGHT, BACK, DOWN.

        Example: YYYYYYYYYRRRRRRRRRGGGGGGGGGOOOOOOOOOBBBBBBBBBWWWWWWWWW
        """

        if face_order is None:
            face_order = [Face.U, Face.L, Face.F, Face.R, Face.B, Face.D]

        res = []
        for face in face_order:
            res += self.get_face_flat(face)
        return "".join([x.name for x in res])

    def scramble(self, num_steps: int = 50, wide: Optional[bool] = None) -> List[CubeMove]:
        """Scramble the cube with random moves.
        By default scramble only uses wide moves to cubes with size >=4."""

        movements = self.generate_random_moves(num_steps=num_steps, wide=wide)
        self.rotate(movements)
        return movements

    def generate_random_moves(self, num_steps: int = 50, wide: Optional[bool] = None) -> List[CubeMove]:
        """Generate a list of random moves (but don't apply them).
        By default scramble only uses wide moves to cubes with size >=4."""

        if wide is None and self.size <= 3:
            wide = False
        elif wide is None and self.size > 3:
            wide = True

        possible_moves = [
            CubeMoveType.L, CubeMoveType.R,  # CubeMoveType.M,
            CubeMoveType.D, CubeMoveType.U,  # CubeMoveType.E,
            CubeMoveType.B, CubeMoveType.F,  # CubeMoveType.S,
        ]
        movements = [CubeMove(
            random.choice(possible_moves),
            random.choice([False, True]),  # reversed
            random.choice([False, True]) if wide else False,  # wide
            random.randint(1, self.size//2) if wide else 1  # layer
        )
            for _ in range(num_steps)]

        return movements

    def find_piece(self, colors: str) -> Tuple[Coordinates, CubePiece]:
        """Find the piece with given colors"""
        colors = "".join(sorted(colors))
        for coord, piece in self.get_all_pieces().items():
            if colors == piece.get_piece_colors_str(no_loc=True):
                return coord, piece
        raise CubeException("piece not found " + colors)

    def get_face(self, face: Face) -> List[List[Color]]:
        """Get face colors in a multi-dim array"""
        face_indexes = self._cube_face_indexes[face.value]
        res = []
        for line in face_indexes:
            line_color = [self._cube[index].get_piece_color(
                face.get_axis()) for index in line]
            res.append(line_color)
        return res

    def get_face_flat(self, face: Face) -> List[Color]:
        """Get face colors in a flat array"""
        res = self.get_face(face)
        return list(np.array(res).flatten())

    def get_all_faces(self) -> Dict[Face, List[List[Color]]]:
        """Get the CubePiece of all cube faces"""
        faces = {f: self.get_face(f) for f in Face}
        return faces

    def get_piece(self, coordinates: Coordinates) -> CubePiece:
        """Get the CubePiece at a given coordinate"""
        return self._cube[coordinates]

    def get_all_pieces(self) -> Dict[Coordinates, CubePiece]:
        """Return a dictionary of coordinates:CubePiece"""
        result = {
            (xi, yi, zi): piece
            for xi, x in enumerate(self._cube)
            for xi, x in enumerate(self._cube)
            for yi, y in enumerate(x)
            for zi, piece in enumerate(y)
            if xi == 0 or xi == self.size-1
            or yi == 0 or yi == self.size-1
            or zi == 0 or zi == self.size-1  # dont include center pieces
        }
        return result

    def _move_to_slice(self, move: CubeMove) -> slice:
        """return the slices affected by a given CubeMove"""

        if not (move.layer >= 1 and move.layer <= self.size):
            raise CubeException("invalid layer " + str(move.layer))

        if move.type in (CubeMoveType.R, CubeMoveType.U, CubeMoveType.F):
            if move.wide:
                return slice(self.size - move.layer, self.size)

            return slice(self.size - move.layer, self.size - move.layer+1)

        if move.type in (CubeMoveType.L, CubeMoveType.D, CubeMoveType.B):
            if move.wide:
                return slice(0, move.layer)

            return slice(move.layer-1, move.layer)

        if move.type in (CubeMoveType.M, CubeMoveType.E, CubeMoveType.S):
            if self.size % 2 != 1:
                raise CubeException(
                    "M,E,S moves not allowed for even size cubes")

            return slice(self.size//2, self.size//2+1)

        # move.type in (CubeMoveType.X, CubeMoveType.Y, CubeMoveType.Z):
        return slice(0, self.size)

    def _get_direction(self, move: CubeMove) -> int:
        """get the rotation direction for a give CubeMove"""
        if move.type in (CubeMoveType.R, CubeMoveType.D, CubeMoveType.F, CubeMoveType.E, CubeMoveType.S, CubeMoveType.X, CubeMoveType.Z):
            direction = -1
        elif move.type in (CubeMoveType.L, CubeMoveType.U, CubeMoveType.B, CubeMoveType.M, CubeMoveType.Y):
            direction = 1
        else:
            raise CubeException("invalid move face " + str(move.type))

        if move.is_reversed:
            direction = direction*-1
        return direction

    def _rotate_once(self, move: CubeMove) -> None:
        """Make one cube movement"""
        if self._store_history:
            self._history.append(move)

        axis = move.type.get_axis()
        slices = self._move_to_slice(move)
        direction = self._get_direction(move)
        count = move.count

        for _ in range(count):
            rotation_plane = tuple(
                slice(None) if i != axis else slices for i in range(3))
            rotation_axes = tuple(i for i in range(3) if i != axis)

            plane = self._cube[rotation_plane]
            rotated_plane = np.rot90(plane, direction, axes=(
                rotation_axes[0], rotation_axes[1]))
            self._cube[rotation_plane] = rotated_plane
            for piece in self._cube[rotation_plane].flatten():
                if piece is not None:
                    piece.rotate_piece(axis)

    def rotate(self, movements: Union[str, List[CubeMove]]) -> None:
        """Make multiple cube movements"""
        if isinstance(movements, str):
            movements_list = [CubeMove.create(
                move_str) for move_str in movements.split(" ") if move_str != ""]
        else:
            movements_list = movements

        for move in movements_list:
            self._rotate_once(move)

    def is_done(self) -> bool:
        """Returns True if the Cube is done"""
        for face_name in Face:
            face = self.get_face_flat(face_name)
            if any(x != face[0] for x in face):
                return False
        return True

    def check_consistency(self) -> bool:
        """Check the cube for internal consistency"""
        for face_name in Face:
            face = self.get_face_flat(face_name)
            if any((x is None for x in face)):
                raise CubeException(
                    "cube is not consistent on face " + str(face_name))
        return True

    def history(self, to_str: bool = False) -> Union[str, List[CubeMove]]:
        """Return the movement history of the cube"""
        if to_str:
            return " ".join([str(x) for x in self._history])

        return self._history

    def reverse_history(self, to_str: bool = False) -> Union[str, List[CubeMove]]:
        """Return the list of moves to revert the cube history"""
        reverse = [x.reverse() for x in reversed(self._history)]
        if to_str:
            return " ".join([str(x) for x in reverse])

        return reverse

    def get_kociemba_facelet_colors(self) -> str:
        """Return the string representation of the cube facelet colors in Kociemba order.
        The order is: U, R, F, D, L, B.

        Ex: WWWWWWWWWRRRRRRRRRGGGGGGGGGYYYYYYYYYOOOOOOOOOBBBBBBBBB."""
        return self.get(face_order=[Face.U, Face.R, Face.F, Face.D, Face.L, Face.B])

    def get_kociemba_facelet_positions(self) -> str:
        """Return the string representation of the cube facelet positions in Kociemba order.
        The order is: U, R, F, D, L, B.

        Ex: UUUUUUUUURRRRRRRRRFFFFFFFFFDDDDDDDDDLLLLLLLLLBBBBBBBBB."""
        facelets = self.get_kociemba_facelet_colors()

        for color, face in (
                ('W', 'U'), ('Y', 'D'),
                ('G', 'F'), ('O', 'L'),
        ):
            facelets = facelets.replace(color, face)

        return facelets

    def undo(self, num_moves: int = 1) -> None:
        """Undo the last num_moves"""
        if not self._store_history:
            raise CubeException("can't undo on a cube without history enabled")

        if num_moves > len(self._history):
            raise CubeException("not enough history to undo")

        reverse_moves = self.reverse_history()[:num_moves]
        self.rotate(reverse_moves)

        for _ in range(2*num_moves):
            self._history.pop()

    def __repr__(self):
        return str(self._cube)

    def __str__(self):
        printer = CubePrintStr(self)
        return printer.print_cube()
