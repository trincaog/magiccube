"""Stdout Cube Print implementation"""
from magiccube.cube_base import Color,Face

C_BG="\x1b[48;5;231m"
#C_RESET="\x1b[49m\x1b[38;5;7m"
C_RESET="\x1b[0;0m"

class CubePrintStr:
    """Prints a cube to stdout"""
    _color_map = {
        Color.G: "\x1b[48;5;40m\x1b[38;5;232m",
        Color.B: "\x1b[48;5;21m\x1b[38;5;7m",
        Color.R: "\x1b[48;5;196m\x1b[38;5;232m",
        Color.O: "\x1b[48;5;208m\x1b[38;5;232m",
        Color.Y: "\x1b[48;5;226m\x1b[38;5;232m",
        Color.W: "\x1b[48;5;248m\x1b[38;5;232m",
    }

    def __init__(self, cube):
        self.cube = cube

    def _format_color(self, color:Color):
        """Format color to TTY"""
        return CubePrintStr._color_map.get(color, "") + " " + color.name + " "+C_RESET

    def _print_top_down_face(self, cube, face):
        result =""
        for index,color in enumerate(cube.get_face_flat(face)):
            if index % cube.size == 0:
                result += C_BG+(" " * ((3*cube.size)))+C_RESET

            result += self._format_color(color)

            if index % cube.size == cube.size-1:
                result += C_BG+(" " * ((2*3*cube.size)))+C_RESET
                result += "\n"
        return result

    def print_cube(self):
        "Print the cube to stdout"
        cube = self.cube

        # flatten midle layer
        print_order_mid = zip(cube.get_face(Face.L), cube.get_face(Face.F),
                              cube.get_face(Face.R), cube.get_face(Face.B))

        # TOP
        result = self._print_top_down_face(cube, Face.U)
        # MID
        for line in print_order_mid:
            for line_index,face_line in enumerate(line):
                for face_line_index,color in enumerate(face_line):
                    result += self._format_color(color)

                    if face_line_index % cube.size == cube.size-1:
                        result += ""
                if line_index == 3:
                    result += "\n"

        # BOTTOM
        result += self._print_top_down_face(cube, Face.D)
        return result
