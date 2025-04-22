
from typing import List
from magiccube.cube_move import CubeMove

# Cube rotation config
_cube_rotations = {
    "Y": {
        "F": "R",
        "R": "B",
        "B": "L",
        "L": "F",
        "U": "U",
        "D": "D",
        "M": "S",
        "E": "E",
        "S": "M'",
    },
    "Y'": {
        "F": "L",
        "L": "B",
        "B": "R",
        "R": "F",
        "U": "U",
        "D": "D",
        "M": "S'",
        "E": "E",
        "S": "M",
    },
    "X": {
        "F": "D",
        "D": "B",
        "B": "U",
        "U": "F",
        "L": "L",
        "R": "R",
        "M": "M",
        "E": "S'",
        "S": "E",
    },
    "X'": {
        "F": "U",
        "U": "B",
        "B": "D",
        "D": "F",
        "L": "L",
        "R": "R",
        "M": "M",
        "E": "S",
        "S": "E'",
    },
    "Z": {
        "U": "L",
        "L": "D",
        "D": "R",
        "R": "U",
        "F": "F",
        "B": "B",
        "M": "E",
        "E": "M'",
        "S": "S",
    },
    "Z'": {
        "U": "R",
        "R": "D",
        "D": "L",
        "L": "U",
        "F": "F",
        "B": "B",
        "M": "E'",
        "E": "M",
        "S": "S",
    },
}


def _build_convertions():
    """Build convertion structure"""
    def convert_moves(moves):
        return (
            {CubeMove.create(k): CubeMove.create(v) for k, v in moves.items()} |
            {CubeMove.create(k).reverse(): CubeMove.create(v).reverse()
             for k, v in moves.items()}
        )

    convertions = {CubeMove.create(rot): convert_moves(
        moves) for rot, moves in _cube_rotations.items()}
    return convertions


cube_rotations = _build_convertions()


class MoveOptimizer:
    """Optimizes a sequence of moves
    Removes reversed moves. Ex L R R' L'
    Converts tripple moves with an inverse. Ex: U U U -> U'
    Removes cube rotations.
    """

    def __init__(self):
        pass

    def optimize(self, moves: List[CubeMove]) -> List[CubeMove]:
        """Returns the optimized moves"""
        optimized_moves: List[CubeMove] = []
        current_cube_rotations: List[CubeMove] = []

        for move in moves:
            if move.type.is_cube_rotation():
                current_cube_rotations.append(move)
                continue

            for rot in reversed(current_cube_rotations):
                cube_rotation = cube_rotations[rot]
                move = cube_rotation[move]

            if len(optimized_moves) > 0 and move.reverse() == optimized_moves[-1]:
                optimized_moves.pop()
            elif len(optimized_moves) > 1 and move == optimized_moves[-1] and move == optimized_moves[-2]:
                optimized_moves.pop()
                optimized_moves.pop()
                optimized_moves.append(move.reverse())
            else:
                optimized_moves.append(move)
        return optimized_moves
