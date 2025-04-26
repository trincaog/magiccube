"""Stdout Cube Print implementation"""
import os
from enum import Enum
from typing import Union
from magiccube.cube_base import Color, Face

C_RESET = "\x1b[0;0m"
C_GREEN = "\x1b[48;5;40m\x1b[38;5;232m"
C_BLUE = "\x1b[48;5;21m\x1b[38;5;7m"
C_RED = "\x1b[48;5;196m\x1b[38;5;232m"
C_ORANGE = "\x1b[48;5;208m\x1b[38;5;232m"
C_YELLOW = "\x1b[48;5;226m\x1b[38;5;232m"
C_WHITE = "\x1b[48;5;248m\x1b[38;5;232m"


class Terminal(Enum):
    """Type of terminal for displaying the cube"""
    default = 0
    """default terminal - no colors"""
    x256 = 1
    """xterm-256color - colors supported"""


class CubePrintStr:
    """Prints a cube to stdout"""
    _xterm256_color_map = {
        Color.G: C_GREEN,
        Color.B: C_BLUE,
        Color.R: C_RED,
        Color.O: C_ORANGE,
        Color.Y: C_YELLOW,
        Color.W: C_WHITE,
    }

    def __init__(self, cube, terminal: Union[Terminal, None] = None):
        self._cube = cube
        if terminal is not None:
            self.term = terminal
        else:
            self.term = Terminal.x256 if os.environ.get(
                "TERM") == "xterm-256color" else Terminal.default

    def _format_color(self, color: Color):
        """Format color to TTY
        Only print colors on supported terminals (xterm-256color)
        """
        formated_color = " " + color.name + " "

        if self.term == Terminal.x256:
            formated_color = CubePrintStr._xterm256_color_map.get(
                color, "") + formated_color + C_RESET

        return formated_color

    def _print_top_down_face(self, cube, face):
        result = ""
        for index, color in enumerate(cube.get_face_flat(face)):
            if index % cube.size == 0:
                result += (" " * ((3*cube.size)))

            result += self._format_color(color)

            if index % cube.size == cube.size-1:
                result += (" " * ((2*3*cube.size)))
                result += "\n"
        return result

    def print_cube(self):
        "Print the cube to stdout"
        cube = self._cube

        # flatten middle layer
        print_order_mid = zip(cube.get_face(Face.L), cube.get_face(Face.F),
                              cube.get_face(Face.R), cube.get_face(Face.B))

        # TOP
        result = self._print_top_down_face(cube, Face.U)
        # MID
        for line in print_order_mid:
            for line_index, face_line in enumerate(line):
                for face_line_index, color in enumerate(face_line):
                    result += self._format_color(color)

                    if face_line_index % cube.size == cube.size-1:
                        result += ""
                if line_index == 3:
                    result += "\n"

        # BOTTOM
        result += self._print_top_down_face(cube, Face.D)
        return result
