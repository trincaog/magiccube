from magiccube.cube import Cube
from magiccube.cube_print import C_BLUE, C_GREEN, C_ORANGE, C_RED, C_RESET, C_WHITE, C_YELLOW, CubePrintStr, Terminal


def test_print_2d():
    c = Cube(2)
    printer = CubePrintStr(c, terminal=Terminal.x256)
    cube_str = printer.print_cube()
    print(cube_str)
    assert cube_str == \
        f"      {C_WHITE} W {C_RESET}{C_WHITE} W {C_RESET}            \n" + \
        f"      {C_WHITE} W {C_RESET}{C_WHITE} W {C_RESET}            \n" + \
        f"{C_ORANGE} O {C_RESET}{C_ORANGE} O {C_RESET}" + \
        f"{C_GREEN} G {C_RESET}{C_GREEN} G {C_RESET}" + \
        f"{C_RED} R {C_RESET}{C_RED} R {C_RESET}" + \
        f"{C_BLUE} B {C_RESET}{C_BLUE} B {C_RESET}\n" + \
        f"{C_ORANGE} O {C_RESET}{C_ORANGE} O {C_RESET}" + \
        f"{C_GREEN} G {C_RESET}{C_GREEN} G {C_RESET}" + \
        f"{C_RED} R {C_RESET}{C_RED} R {C_RESET}" + \
        f"{C_BLUE} B {C_RESET}{C_BLUE} B {C_RESET}\n" + \
        f"      {C_YELLOW} Y {C_RESET}{C_YELLOW} Y {C_RESET}            \n" + \
        f"      {C_YELLOW} Y {C_RESET}{C_YELLOW} Y {C_RESET}            \n"


def test_print_2d_no_term():
    c = Cube(2)
    printer = CubePrintStr(c, terminal=Terminal.default)
    cube_str = printer.print_cube()
    print(cube_str)
    assert cube_str == \
        "       W  W             \n" + \
        "       W  W             \n" + \
        " O  O  G  G  R  R  B  B \n" + \
        " O  O  G  G  R  R  B  B \n" + \
        "       Y  Y             \n" + \
        "       Y  Y             \n"
