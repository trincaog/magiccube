"""Stdout Cube Print implementation"""
from colorama import Back
from magiccube.cube_base import CubeColor,CubeFace

class CubePrintStr:
    """Prints a cube to stdout"""
    _color_map = {
        CubeColor.G: Back.GREEN,
        CubeColor.B: Back.BLUE,
        CubeColor.R: Back.RED,
        CubeColor.O: Back.LIGHTMAGENTA_EX,
        CubeColor.Y: Back.YELLOW,
        CubeColor.W: Back.WHITE,
    }

    def __init__(self, cube):
        self.cube = cube

    def _format_color(self, color:CubeColor):
        """Format color to TTY"""
        return CubePrintStr._color_map.get(color, "") + " " + color.name + " "+Back.RESET

    def _print_face(self, cube, face):
        result =""
        for index,color in enumerate(cube.get_face_flat(face)):
            if index % cube.size == 0:
                result += (" " * ((3*cube.size+1)))

            result += self._format_color(color)

            if index % cube.size == cube.size-1:
                result += "\n"
        return result

    def print_cube(self):
        "Print the cube to stdout"
        cube = self.cube

        # flatten midle layer
        print_order_mid = zip(cube.get_face(CubeFace.L), cube.get_face(CubeFace.F),
                              cube.get_face(CubeFace.R), cube.get_face(CubeFace.B))

        # TOP
        result = self._print_face(cube, CubeFace.U)
        # MID
        for line in print_order_mid:
            for line_index,face_line in enumerate(line):
                for face_line_index,color in enumerate(face_line):
                    result += self._format_color(color)

                    if face_line_index % cube.size == cube.size-1:
                        result += "|"
                if line_index == 3:
                    result += "\n"

        # BOTTOM
        result += self._print_face(cube, CubeFace.D)
        return result
