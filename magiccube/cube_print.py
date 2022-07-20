"""Stdout Cube Print implementation"""
from magiccube.cube_base import CubeColor,CubeFace

C_BG="\x1b[48;5;231m"
#C_RESET="\x1b[49m\x1b[38;5;7m"
C_RESET="\x1b[0;0m"

class CubePrintStr:
    """Prints a cube to stdout"""
    _color_map = {
        CubeColor.G: "\x1b[48;5;40m\x1b[38;5;232m",
        CubeColor.B: "\x1b[48;5;21m\x1b[38;5;7m",
        CubeColor.R: "\x1b[48;5;196m\x1b[38;5;232m",
        CubeColor.O: "\x1b[48;5;208m\x1b[38;5;232m",
        CubeColor.Y: "\x1b[48;5;226m\x1b[38;5;232m",
        CubeColor.W: "\x1b[48;5;248m\x1b[38;5;232m",
    }

    def __init__(self, cube):
        self.cube = cube

    def _format_color(self, color:CubeColor):
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
        print_order_mid = zip(cube.get_face(CubeFace.L), cube.get_face(CubeFace.F),
                              cube.get_face(CubeFace.R), cube.get_face(CubeFace.B))

        # TOP
        result = self._print_top_down_face(cube, CubeFace.U)
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
        result += self._print_top_down_face(cube, CubeFace.D)
        return result
