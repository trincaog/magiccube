import random
import numpy as np
from cube.constants import CubeFace
from cube.cube_piece import CubePiece
from cube.cube_move import CubeMove
from cube.cube_print import CubePrintStr

class Cube:

    def __init__(self, size: int, hist=True):
        self.size = size
        self._history = []
        self._store_history=hist
        self._cube_face_indexes = [
            [[(0, y, z) for z in range(self.size)] for y in reversed(range(self.size))], #L
            [[(self.size-1, y, z) for z in reversed(range(self.size))] for y in reversed(range(self.size))], #R
            [[(x, 0, z) for x in range(self.size)] for z in reversed(range(self.size))], #D
            [[(x, self.size-1, z) for x in range(self.size)] for z in range(self.size)], #U
            [[(x, y, 0) for x in reversed(range(self.size))] for y in reversed(range(self.size))], #B
            [[(x, y, self.size-1) for x in range(self.size)] for y in reversed(range(self.size))], #F
        ]

        self._cube_piece_indexes = [
            (x, y, z)
            for x in range(self.size)
            for y in range(self.size)
            for z in range(self.size)
            if self._is_outer_position(x,y,z)
        ]
        self._cube_piece_indexes_inv={v:idx for idx,v in enumerate(self._cube_piece_indexes)}

        self.reset()

    def _is_outer_position(self,x:int,y:int,z:int)->bool:
        """Test if the coordinates indicate and outer cube position"""
        return x==0 or x==self.size-1 or y==0 or y==self.size-1 or z==0 or z==self.size-1 # dont include center pieces

    def reset(self):
        """Reset the cube to the initial configuration"""
        initial_cube = [
            [[CubePiece(self.size, (x, y, z))
              if self._is_outer_position(x,y,z) else None
              for z in range(self.size)]
             for y in range(self.size)]
            for x in range(self.size)
        ]
        self.cube = np.array(initial_cube, dtype=np.object_)

    def scramble(self, num_steps:int=50, seed:int=42):
        """Scramble the cube with random moves"""
        random.seed(seed)

        possible_moves = [
            CubeFace.L,CubeFace.R,
            CubeFace.D,CubeFace.U,
            CubeFace.B,CubeFace.F,
        ]
        movements = [CubeMove(
            random.choice(possible_moves),
            random.choice([False,True]),
            random.choice([False,True]),
            random.randint(1,self.size)
            )
            for _ in range(num_steps)]
        for move in movements:
            self._rotate_once(move)

    def get_face(self, face:CubeFace)->list:
        """Get face colors in a multi-dim array"""
        res = [
                [
                    self.cube[index].get_piece_color(face) 
                    for index in face_indexes
                ] for face_indexes in self._cube_face_indexes[face.value]
            ]
        return res

    def get_face_flat(self, face:CubeFace)->list:
        """Get face colors in a flat array"""
        res = self.get_face(face)
        res = list(np.array(res).flatten())
        return res

    def get_all_faces(self) -> dict[CubeFace,list[CubePiece]]:
        """Get the CubePiece of all cube faces"""
        faces = {f:self.get_face(f) for f in CubeFace}
        return faces

    def get_piece(self, coordinates: tuple) -> CubePiece:
        """Get the CubePiece at a given coordinate"""
        return self.cube[coordinates]

    def get_all_pieces(self)->dict[tuple,CubePiece]:
        """Return a dictionary of coordinates:CubePiece"""
        res = [self.cube[x] for x in self._cube_piece_indexes]
        
        res = {
            (xi,yi,zi): piece for xi,x in enumerate(self.cube) for yi,y in enumerate(x) for zi,piece in enumerate(y) 
            if xi==0 or xi==self.size-1 or yi==0 or yi==self.size-1 or zi==0 or zi==self.size-1 # dont include center pieces
        }
        return res

    def move_to_index(self, move:CubeMove):
        """return the indexes affted by a given CubeMove"""
        if move.layer>self.size:
            raise Exception("invalid layer " + str(move.layer))
        elif move.face in (CubeFace.R, CubeFace.U, CubeFace.F):
            if move.wide:
                return tuple(range(self.size - move.layer,self.size))
            else:
                return (self.size - move.layer,)
        else:
            if move.wide:
                return tuple(range(move.layer))
            else:
                return (move.layer-1,)


    def get_direction(self,move:CubeMove):
        """get the rotation direction for a give CubeMove"""
        if move.face in (CubeFace.L,CubeFace.U,CubeFace.B):
            dir = 1
        elif move.face in (CubeFace.R,CubeFace.D,CubeFace.F):
            dir = -1
        else:
            raise Exception("invalid move face " + str(move.face))

        if move.reversed:
            dir=dir*-1
        return dir

    def _rotate_once(self, move:CubeMove):
        if self._store_history:
            self._history.append(move)

        axis = move.face.get_axis()
        indexes = self.move_to_index(move)
        direction = self.get_direction(move)
        for index in indexes:
            rotation_plane=tuple([slice(None) if i!=axis else index for i in range(3)])

            self.cube[rotation_plane] = np.rot90(self.cube[rotation_plane], direction)
            for piece in self.cube[rotation_plane].flatten():
                if piece is not None:
                    piece.rotate_piece(axis,direction)

    def rotate(self, movements: str):
        """Make one cube movement"""
        for movement_str in movements.split(" "):
            if movement_str == "":
                continue
            else:
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
                else:
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
        return str([[[piece for piece in l2] for l2 in l1] for l1 in self.cube])

    def __str__(self):
        printer = CubePrintStr(self)
        return printer.print_cube()


