from typing import List, Tuple
from magiccube.cube import Cube, CubeException
from magiccube.optimizer.move_optimizer import MoveOptimizer
from magiccube.solver.basic.solver_base import SolverException, SolverStage
from magiccube.solver.basic.solver_stages import ConditionAction, stage_recenter_down, stage_recenter_front, stage_white_cross, \
    stage_white_corner, stage_2nd_layer, stage_top_cross, stage_order_top_cross, \
    stage_order_top_corners, stage_turn_top_corners


stages = {
    "stage_recenter_down": (("W",), stage_recenter_down),
    "stage_recenter_front": (("G",), stage_recenter_front),

    "stage_white_cross_bw": (("BW",), stage_white_cross),
    "stage_recenter_front_o1": (("O",), stage_recenter_front),
    "stage_white_cross_rw": (("RW",), stage_white_cross),
    "stage_recenter_front_b1": (("B",), stage_recenter_front),
    "stage_white_cross_gw": (("GW",), stage_white_cross),
    "stage_recenter_front_r1": (("R",), stage_recenter_front),
    "stage_white_cross_ow": (("OW",), stage_white_cross),
    "stage_recenter_front_g1": (("G",), stage_recenter_front),

    "stage_white_corner_gow": (("GOW",), stage_white_corner),
    "stage_recenter_front_o2": (("O",), stage_recenter_front),
    "stage_white_corner_bow": (("BOW",), stage_white_corner),
    "stage_recenter_front_b2": (("B",), stage_recenter_front),
    "stage_white_corner_brw": (("BRW",), stage_white_corner),
    "stage_recenter_front_r2": (("R",), stage_recenter_front),
    "stage_white_corner_grw": (("GRW",), stage_white_corner),
    "stage_recenter_front_g2": (("G",), stage_recenter_front),

    "stage_2nd_layer_gr": (("GR",), stage_2nd_layer),
    "stage_recenter_front_o3": (("O",), stage_recenter_front),
    "stage_2nd_layer_go": (("GO",), stage_2nd_layer),
    "stage_recenter_front_b3": (("B",), stage_recenter_front),
    "stage_2nd_layer_bo": (("BO",), stage_2nd_layer),
    "stage_recenter_front_r3": (("R",), stage_recenter_front),
    "stage_2nd_layer_br": (("BR",), stage_2nd_layer),
    "stage_recenter_front_g3": (("G",), stage_recenter_front),

    "stage_top_cross": (("YG", "YR", "YB", "YO"), stage_top_cross),

    "stage_order_top_cross": (("YG", "YR", "YB", "YO"), stage_order_top_cross),
    "stage_order_top_corners": (("YRG", "YRB", "YBO", "YGO"), stage_order_top_corners),
    "stage_turn_top_corners": (("YRG", "YRB", "YBO", "YGO"), stage_turn_top_corners),
}


class BasicSolver:

    def __init__(self, cube: Cube, init_stages=None):
        if cube.size != 3:
            raise SolverException("Solver only works with 3x3x3 cube")
        self.cube = cube
        self.stages: List[SolverStage] = []
        self.default_debug = False
        self.max_iterations_per_stage = 12

        if init_stages is None:
            for name, stage in stages.items():
                self.add(
                    name=name, target_colors=stage[0], pattern_condition_actions=stage[1], debug=self.default_debug)
        else:
            for init_stage in init_stages:
                self.add(name=init_stage, target_colors=stages[init_stage][0],
                         pattern_condition_actions=stages[init_stage][1], debug=self.default_debug)

    def _solve_pattern_stage(self, stage: SolverStage) -> List[str]:
        """Solve one stage of the cube"""

        full_actions = []
        iteration = 0

        while iteration < self.max_iterations_per_stage:
            iteration += 1
            target_pieces = [self.cube.find_piece(
                target_color) for target_color in stage.target_colors]

            if stage.debug:  # pragma:no cover
                print("solve_stage start:", stage.name,
                      stage.target_colors, target_pieces)
                print(self.cube)

            actions, is_continue = stage.get_moves(target_pieces)

            self.cube.rotate(actions)
            full_actions += actions

            if stage.debug:  # pragma:no cover
                print("solve_stage end:", stage.name,
                      target_pieces, actions, is_continue)
                print(self.cube)

            if not is_continue:
                # stage is complete
                break

        if iteration >= self.max_iterations_per_stage:
            raise SolverException(f"stage iteration limit exceeded: {stage}")

        return full_actions

    def solve(self, optimize=True):
        """Solve the cube by running all the registered pattern stages"""
        try:
            full_actions = []
            for stage in self.stages:
                if stage.debug:  # pragma:no cover
                    print("starting stage", stage)
                actions = self._solve_pattern_stage(stage)
                full_actions += actions

            if optimize:
                full_actions = MoveOptimizer().optimize(full_actions)

            return full_actions
        except CubeException as e:
            raise SolverException("unable to solve cube", e) from e

    def add(self, name, target_colors: Tuple[str, ...], pattern_condition_actions: Tuple[ConditionAction, ...], debug=False):
        """Add a stage to the solver."""
        self.stages.append(SolverStage(
            target_colors, pattern_condition_actions, name=name, debug=debug))
        return self
