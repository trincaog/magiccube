from dataclasses import dataclass
from typing import List, Tuple
from magiccube.cube_base import Color, ColorOrientation, Coordinates
from magiccube.cube_move import CubeMove
from magiccube.cube_piece import CubePiece


class SolverException(Exception):
    """Exception raised when the solver fails to find a solution"""


@dataclass
class Condition:
    """Defines the conditions to trigger an action
    The conditions are based on:
        - The piece location (coordinates )
        - The piece colors orientation on the XYZ axis
          The color condition may be '*' to indicate any color
    """
    @staticmethod
    def position_to_coord(position: int) -> Coordinates:
        """Convert integer position to CubeCoordinates"""
        x = position//100
        y = (position - x*100)//10
        z = position-x*100-y*10
        return (x, y, z)

    def __init__(self, position: int, accepted_colors_str: Tuple[str, ...]):
        self.coordinate_condition = Condition.position_to_coord(position)
        color_condition = []

        # build the pattern condition
        for accepted_color in accepted_colors_str:
            color_condition.append(tuple((
                None if color_str == "*" else Color.create(color_str)
                for color_str in accepted_color
            )))

        self.color_condition: List[ColorOrientation] = color_condition  # type: ignore # noqa

    def _is_color_match(self, orientation_pattern: ColorOrientation, color: ColorOrientation) -> bool:
        """ Return True if the piece colors match the orientation pattern """

        filtered_color = [c for c in color if c is not None]
        for i, orientation_color in enumerate(orientation_pattern):
            if orientation_color is None:
                continue
            if orientation_color != filtered_color[i]:
                return False
        return True

    def is_match(self, target_coordinates: Coordinates, target_piece: CubePiece):
        """ Return True if the the piece coordinates and color orientation match the PatternCondition  """

        assert len(self.color_condition[0]
                   ) == target_piece.get_piece_type().value

        if target_coordinates != self.coordinate_condition:
            return False

        for accepted_color in self.color_condition:

            if self._is_color_match(accepted_color, target_piece.get_piece_colors()):  # type: ignore # noqa
                return True
        return False

    def __str__(self):  # pragma:no cover
        return f"PatternCondition: {self.coordinate_condition} {self.color_condition}"


@dataclass
class ConditionAction:
    """Defines a list of actions to be triggered when the conditions are matched"""

    def __init__(self, conditions: Tuple[Condition, ...], action: str, is_continue: bool):
        self.conditions = conditions

        action_list_str = action.split(" ")
        action_list = [CubeMove.create(a) for a in action_list_str if a != ""]

        self.action = action_list
        self.is_continue = is_continue

    def _is_any_match(self, coordinates: Coordinates, piece: CubePiece):
        """Return True if the piece coordinates+color orientation match any of the conditions"""
        result = any((condition.is_match(coordinates, piece)
                     for condition in self.conditions))
        return result

    def is_match(self, pieces: List[Tuple[Coordinates, CubePiece]]):
        """Return True if the given pieces match the pattern conditions"""
        assert len(pieces) == len(self.conditions)
        result = not any((not self._is_any_match(coord, piece)
                         for coord, piece in pieces))
        return result


class SolverStage:
    """Defines an individual solver stage.
    target_colors describe the pieces in which the conditions (cond_actions) are going to be checked against.
    """

    def __init__(self, target_colors: Tuple[str, ...], cond_actions: Tuple[ConditionAction, ...], name=None, debug=False):
        self.target_colors = target_colors
        self.cond_actions = cond_actions
        self.debug = debug
        self.name = name

    def get_moves(self, target_pieces: List[Tuple[Coordinates, CubePiece]]) -> Tuple[List[CubeMove], bool]:
        """Run through the stage conditions and check for match.
        Return the matched action."""
        for p_cond_action in self.cond_actions:
            if p_cond_action.is_match(target_pieces):
                return p_cond_action.action, p_cond_action.is_continue
        raise SolverException(
            f"{self.name}: no valid conditions found for the pieces: {target_pieces}")  # pragma:no cover

    def __str__(self):  # pragma:no cover
        return f"Stage:{self.name} | {self.target_colors}"

    def __repr__(self):  # pragma:no cover
        return f"Stage:{self.name} | {self.target_colors}"
