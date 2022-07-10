"""Rubik Cube implementation"""
from typing import Dict,List, Tuple
import random
import numpy as np
from magiccube.cube_base import CubeColor, CubeFace
from magiccube.cube_piece import CubeCoordinates, CubePiece
from magiccube.cube_move import CubeMove
from magiccube.cube_print import CubePrintStr

class Cube:
    """Rubik Cube implementation"""

    __slots__=("size","_store_history","_cube_face_indexes","_cube_piece_indexes",
    "_cube_piece_indexes_inv","cube","_history")

    def __init__(self, size: int=3, hist=True):

        if size<=1:
            raise Exception("Cube size must be >= 2")

        self.size = size
        self._store_history = hist
        self._cube_face_indexes = [
            [[(0,y,z) for z in range(self.size)]
                for y in reversed(range(self.size))], #L
            [[(self.size-1,y,z) for z in reversed(range(self.size))]
                for y in reversed(range(self.size))], #R
            [[(x,0,z) for x in range(self.size)]
                for z in reversed(range(self.size))], #D
            [[(x, self.size-1, z) for x in range(self.size)]
                for z in range(self.size)], #U
            [[(x,y,0) for x in reversed(range(self.size))]
                for y in reversed(range(self.size))], #B
            [[(x,y,self.size-1) for x in range(self.size)]
                for y in reversed(range(self.size))], #F
        ]

        self._cube_piece_indexes = [
            (x,y,z)
            for z in range(self.size)
            for y in range(self.size)
            for x in range(self.size)
            if self._is_outer_position(x,y,z)
        ]
        self._cube_piece_indexes_inv={v:idx for idx,v in enumerate(self._cube_piece_indexes)}

        self.reset()

    def _is_outer_position(self,_z:int,_y:int,_x:int)->bool:
        """Test if the coordinates indicate and outer cube position"""
        return _x==0 or _x==self.size-1 \
            or _y==0 or _y==self.size-1 \
            or _z==0 or _z==self.size-1 # dont include center pieces

    def reset(self):
        """Reset the cube to the initial configuration"""
        initial_cube = [
            [[CubePiece(self.size, (x, y, z))
              if self._is_outer_position(x,y,z) else None
              for x in range(self.size)]
             for y in range(self.size)]
            for z in range(self.size)
        ]
        self.cube = np.array(initial_cube, dtype=np.object_)
        self._history = []

    def scramble(self, num_steps:int=50, wide=None) -> List[str]:
        """Scramble the cube with random moves.
        By default scramble only uses wide moves to cubes with size >=4."""
        
        if wide is None and self.size<=3:
            wide=False
        elif wide is None and self.size>3:
            wide=True
        
        possible_moves = [
            CubeFace.B,CubeFace.F,
            CubeFace.L,CubeFace.R,
            CubeFace.D,CubeFace.U,
        ]
        movements = [CubeMove(
            random.choice(possible_moves),
            random.choice([False,True]),
            random.choice([False,True]) if wide else False,
            random.randint(1,self.size) if wide else 1
            )
            for _ in range(num_steps)]

        movements_list = [str(x) for x in movements]
        movements_str = " ".join(movements_list)
        self.rotate(movements_str)
        return movements_list

    def find_piece(self, colors:str) -> Tuple[CubeCoordinates, CubePiece]:
        """Find the piece with given colors"""
        colors = "".join(sorted(colors))
        for coord, piece in self.get_all_pieces().items():
            if colors == piece.get_piece_colors_str(no_loc=True):
                return coord,piece
        raise Exception ("piece not found " + colors)

    def get_face(self, face:CubeFace)->List[List[CubeColor]]:
        """Get face colors in a multi-dim array"""
        face_indexes = self._cube_face_indexes[face.value]
        res = []
        for line in face_indexes:
            line_color = [self.cube[index].get_piece_color(face.get_axis()) for index in line]
            res.append(line_color)
        return res

    def get_face_flat(self, face:CubeFace)->List[CubeColor]:
        """Get face colors in a flat array"""
        res = self.get_face(face)
        res = list(np.array(res).flatten())
        return res

    def get_all_faces(self) -> Dict[CubeFace,List[List[CubeColor]]]:
        """Get the CubePiece of all cube faces"""
        faces = {f:self.get_face(f) for f in CubeFace}
        return faces

    def get_piece(self, coordinates: CubeCoordinates) -> CubePiece:
        """Get the CubePiece at a given coordinate"""
        return self.cube[coordinates]

    def get_all_pieces(self)->Dict[CubeCoordinates,CubePiece]:
        """Return a dictionary of coordinates:CubePiece"""
        res = [self.cube[x] for x in self._cube_piece_indexes]

        res = {
            (xi,yi,zi): piece 
                for xi,x in enumerate(self.cube)
                for yi,y in enumerate(x)
                for zi,piece in enumerate(y)
                if xi==0 or xi==self.size-1
                or yi==0 or yi==self.size-1
                or zi==0 or zi==self.size-1 # dont include center pieces
        }
        return res

    def _move_to_index(self, move:CubeMove):
        """return the indexes affted by a given CubeMove"""
        if move.layer>self.size:
            raise Exception("invalid layer " + str(move.layer))

        if move.layer==-1:
            move.layer=self.size

        if move.face in (CubeFace.R, CubeFace.U, CubeFace.F):
            if move.wide:
                return tuple(range(self.size - move.layer,self.size))
            else:
                return (self.size - move.layer,)
        else:
            if move.wide:
                return tuple(range(move.layer))
            else:
                return (move.layer-1,)


    def _get_direction(self,move:CubeMove)->int:
        """get the rotation direction for a give CubeMove"""
        if move.face in (CubeFace.R,CubeFace.D,CubeFace.F):
            direction = -1
        elif move.face in (CubeFace.L,CubeFace.U,CubeFace.B):
            direction = 1
        else:
            raise Exception("invalid move face " + str(move.face))

        if move.is_reversed:
            direction=direction*-1
        return direction

    def _rotate_once(self, move:CubeMove):
        if self._store_history:
            self._history.append(move)

        axis = move.face.get_axis()
        indexes = self._move_to_index(move)
        direction = self._get_direction(move)
        for index in indexes:
            rotation_plane=tuple(slice(None) if i!=axis else index for i in range(3))

            plane = self.cube[rotation_plane]
            rotated_plane = np.rot90(plane, direction)
            self.cube[rotation_plane] = rotated_plane
            for piece in self.cube[rotation_plane].flatten():
                if piece is not None:
                    piece.rotate_piece(axis)

    def rotate(self, movements: str):
        """Make one cube movement"""
        for movement_str in movements.split(" "):
            if movement_str == "":
                continue

            move = CubeMove.create(movement_str)
            self._rotate_once(move)


    def is_done(self):
        """Returns True if the Cube is done"""
        for face_name in CubeFace:
            face = self.get_face_flat(face_name)
            if any(x != face[0] for x in face):
                return False
        return True

    def check_consistency(self, raise_exception = True):
        """Check the cube for internal consistency"""
        for face_name in CubeFace:
            face = self.get_face(face_name)
            if any((x is None for x in face)):
                if raise_exception:
                    raise Exception("cube is not consistent on face "+ str(face_name))
                return False
            return True

    def history(self):
        """Return the movement history of the cube"""
        history_str = [str(x) for x in self._history]
        return " ".join(history_str)

    def reverse_history(self):
        """Return the list of moves to revert the cube history"""
        return " ".join([str(x.reverse()) for x in reversed(self._history)])

    def __repr__(self):
        return str(self.cube)

    def __str__(self):
        printer = CubePrintStr(self)
        return printer.print_cube()
