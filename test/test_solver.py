import pytest

import random
from magiccube.cube import Cube
from magiccube.cube_base import CubeColor
from magiccube.solver.basic.basic_solver import BasicSolver

def test_solve():
    cube = Cube(hist=False, size=3)
    solver = BasicSolver(cube)

    random.seed(42)
    cube.scramble(num_steps=50, wide=False)

    solver.solve()
    assert cube.is_done()


def test_solve_white_cross():
    init_stages = ["stage_recenter_down","stage_recenter_front",
        "stage_white_cross_bw","stage_recenter_front_o1",
        "stage_white_cross_rw","stage_recenter_front_b1",
        "stage_white_cross_gw","stage_recenter_front_r1",
        "stage_white_cross_ow","stage_recenter_front_g1",
    ]

    cube = Cube(hist=False, size=3)
    solver = BasicSolver(cube, init_stages=init_stages)

    random.seed(42)
    cube.scramble(num_steps=50, wide=False)

    solver.solve()

    # white cross
    c,p=cube.find_piece("BW")
    assert c==(1,0,0) , c
    assert p.get_piece_colors_str()=="WB",p.get_piece_colors_str()

    c,p=cube.find_piece("GW")
    assert c==(1,0,2) , c
    assert p.get_piece_colors_str()=="WG",p.get_piece_colors_str()

    c,p=cube.find_piece("RW")
    assert c==(0,0,1) , c
    assert p.get_piece_colors_str()=="RW",p.get_piece_colors_str()
    c,p=cube.find_piece("OW")
    assert c==(2,0,1) , c
    assert p.get_piece_colors_str()=="OW",p.get_piece_colors_str()


def test_solve_white_corners():
    init_stages = ["stage_recenter_down","stage_recenter_front",
"stage_white_cross_bw","stage_recenter_front_o1",
"stage_white_cross_rw","stage_recenter_front_b1",
"stage_white_cross_gw","stage_recenter_front_r1",
"stage_white_cross_ow","stage_recenter_front_g1",
"stage_white_corner_gow","stage_recenter_front_o2",
"stage_white_corner_bow","stage_recenter_front_b2",
"stage_white_corner_brw","stage_recenter_front_r2",
"stage_white_corner_grw","stage_recenter_front_g2",
    ]

    cube = Cube(hist=False, size=3)
    solver = BasicSolver(cube, init_stages=init_stages)

    random.seed(42)
    cube.scramble(num_steps=50, wide=False)

    solver.solve()

    # white cross
    c,p=cube.find_piece("BW")
    assert c==(1,0,0) , c
    assert p.get_piece_colors_str()=="WB",p.get_piece_colors_str()

    c,p=cube.find_piece("GW")
    assert c==(1,0,2) , c
    assert p.get_piece_colors_str()=="WG",p.get_piece_colors_str()

    c,p=cube.find_piece("RW")
    assert c==(0,0,1) , c
    assert p.get_piece_colors_str()=="RW",p.get_piece_colors_str()
    c,p=cube.find_piece("OW")
    assert c==(2,0,1) , c
    assert p.get_piece_colors_str()=="OW",p.get_piece_colors_str()

    # white corners

    c,p=cube.find_piece("GOW")
    assert c==(2,0,2) , c
    assert p.get_piece_colors_str()=="OWG",p.get_piece_colors_str()
    c,p=cube.find_piece("BOW")
    assert c==(2,0,0) , c
    assert p.get_piece_colors_str()=="OWB",p.get_piece_colors_str()
    c,p=cube.find_piece("BRW")
    assert c==(0,0,0) , c
    assert p.get_piece_colors_str()=="RWB",p.get_piece_colors_str()
    c,p=cube.find_piece("GRW")
    assert c==(0,0,2) , c
    assert p.get_piece_colors_str()=="RWG",p.get_piece_colors_str()





def test_solve_2nd_layer():
    init_stages = ["stage_recenter_down","stage_recenter_front",
"stage_white_cross_bw","stage_recenter_front_o1",
"stage_white_cross_rw","stage_recenter_front_b1",
"stage_white_cross_gw","stage_recenter_front_r1",
"stage_white_cross_ow","stage_recenter_front_g1",
"stage_white_corner_gow","stage_recenter_front_o2",
"stage_white_corner_bow","stage_recenter_front_b2",
"stage_white_corner_brw","stage_recenter_front_r2",
"stage_white_corner_grw","stage_recenter_front_g2",
"stage_2nd_layer_gr","stage_recenter_front_o3",
"stage_2nd_layer_go","stage_recenter_front_b3",
"stage_2nd_layer_bo","stage_recenter_front_r3",
"stage_2nd_layer_br","stage_recenter_front_g3",
    ]

    cube = Cube(hist=False, size=3)
    solver = BasicSolver(cube, init_stages=init_stages)

    random.seed(42)
    cube.scramble(num_steps=50, wide=False)

    solver.solve()

    # white cross
    c,p=cube.find_piece("BW")
    assert c==(1,0,0) , c
    assert p.get_piece_colors_str()=="WB",p.get_piece_colors_str()

    c,p=cube.find_piece("GW")
    assert c==(1,0,2) , c
    assert p.get_piece_colors_str()=="WG",p.get_piece_colors_str()

    c,p=cube.find_piece("RW")
    assert c==(0,0,1) , c
    assert p.get_piece_colors_str()=="RW",p.get_piece_colors_str()
    c,p=cube.find_piece("OW")
    assert c==(2,0,1) , c
    assert p.get_piece_colors_str()=="OW",p.get_piece_colors_str()

    # white corners

    c,p=cube.find_piece("GOW")
    assert c==(2,0,2) , c
    assert p.get_piece_colors_str()=="OWG",p.get_piece_colors_str()
    c,p=cube.find_piece("BOW")
    assert c==(2,0,0) , c
    assert p.get_piece_colors_str()=="OWB",p.get_piece_colors_str()
    c,p=cube.find_piece("BRW")
    assert c==(0,0,0) , c
    assert p.get_piece_colors_str()=="RWB",p.get_piece_colors_str()
    c,p=cube.find_piece("GRW")
    assert c==(0,0,2) , c
    assert p.get_piece_colors_str()=="RWG",p.get_piece_colors_str()


    # 2nd layer
    c,p=cube.find_piece("BO")
    assert c==(2,1,0) , c
    assert p.get_piece_colors_str()=="OB",p.get_piece_colors_str()

    c,p=cube.find_piece("GO")
    assert c==(2,1,2) , c
    assert p.get_piece_colors_str()=="OG",p.get_piece_colors_str()

    c,p=cube.find_piece("GR")
    assert c==(0,1,2) , c
    assert p.get_piece_colors_str()=="RG",p.get_piece_colors_str()

    c,p=cube.find_piece("BR")
    assert c==(0,1,0) , c
    assert p.get_piece_colors_str()=="RB",p.get_piece_colors_str()




def test_solve_top_cross():
    init_stages = ["stage_recenter_down","stage_recenter_front",
"stage_white_cross_bw","stage_recenter_front_o1",
"stage_white_cross_rw","stage_recenter_front_b1",
"stage_white_cross_gw","stage_recenter_front_r1",
"stage_white_cross_ow","stage_recenter_front_g1",
"stage_white_corner_gow","stage_recenter_front_o2",
"stage_white_corner_bow","stage_recenter_front_b2",
"stage_white_corner_brw","stage_recenter_front_r2",
"stage_white_corner_grw","stage_recenter_front_g2",
"stage_2nd_layer_gr","stage_recenter_front_o3",
"stage_2nd_layer_go","stage_recenter_front_b3",
"stage_2nd_layer_bo","stage_recenter_front_r3",
"stage_2nd_layer_br","stage_recenter_front_g3",
"stage_top_cross","stage_order_top_cross",
    ]

    cube = Cube(hist=False, size=3)
    solver = BasicSolver(cube, init_stages=init_stages)

    random.seed(42)
    cube.scramble(num_steps=50, wide=False)

    solver.solve()

    # white cross
    c,p=cube.find_piece("BW")
    assert c==(1,0,0) , c
    assert p.get_piece_colors_str()=="WB",p.get_piece_colors_str()

    c,p=cube.find_piece("GW")
    assert c==(1,0,2) , c
    assert p.get_piece_colors_str()=="WG",p.get_piece_colors_str()

    c,p=cube.find_piece("RW")
    assert c==(0,0,1) , c
    assert p.get_piece_colors_str()=="RW",p.get_piece_colors_str()
    c,p=cube.find_piece("OW")
    assert c==(2,0,1) , c
    assert p.get_piece_colors_str()=="OW",p.get_piece_colors_str()

    # white corners

    c,p=cube.find_piece("GOW")
    assert c==(2,0,2) , c
    assert p.get_piece_colors_str()=="OWG",p.get_piece_colors_str()
    c,p=cube.find_piece("BOW")
    assert c==(2,0,0) , c
    assert p.get_piece_colors_str()=="OWB",p.get_piece_colors_str()
    c,p=cube.find_piece("BRW")
    assert c==(0,0,0) , c
    assert p.get_piece_colors_str()=="RWB",p.get_piece_colors_str()
    c,p=cube.find_piece("GRW")
    assert c==(0,0,2) , c
    assert p.get_piece_colors_str()=="RWG",p.get_piece_colors_str()


    # 2nd layer
    c,p=cube.find_piece("BO")
    assert c==(2,1,0) , c
    assert p.get_piece_colors_str()=="OB",p.get_piece_colors_str()

    c,p=cube.find_piece("GO")
    assert c==(2,1,2) , c
    assert p.get_piece_colors_str()=="OG",p.get_piece_colors_str()

    c,p=cube.find_piece("GR")
    assert c==(0,1,2) , c
    assert p.get_piece_colors_str()=="RG",p.get_piece_colors_str()

    c,p=cube.find_piece("BR")
    assert c==(0,1,0) , c
    assert p.get_piece_colors_str()=="RB",p.get_piece_colors_str()

    # TOP cross

    p=cube.get_piece((1,2,2))
    assert p.get_piece_colors()==(None,CubeColor.Y,CubeColor.G),p.get_piece_colors_str()

    p=cube.get_piece((2,2,1))
    assert p.get_piece_colors()==(CubeColor.O,CubeColor.Y,None),p.get_piece_colors_str()

    p=cube.get_piece((1,2,0))
    assert p.get_piece_colors()==(None,CubeColor.Y,CubeColor.B),p.get_piece_colors_str()

    p=cube.get_piece((0,2,1))
    assert p.get_piece_colors()==(CubeColor.R,CubeColor.Y,None),p.get_piece_colors_str()



def test_solve_top_corners():
    init_stages = ["stage_recenter_down","stage_recenter_front",
"stage_white_cross_bw","stage_recenter_front_o1",
"stage_white_cross_rw","stage_recenter_front_b1",
"stage_white_cross_gw","stage_recenter_front_r1",
"stage_white_cross_ow","stage_recenter_front_g1",
"stage_white_corner_gow","stage_recenter_front_o2",
"stage_white_corner_bow","stage_recenter_front_b2",
"stage_white_corner_brw","stage_recenter_front_r2",
"stage_white_corner_grw","stage_recenter_front_g2",
"stage_2nd_layer_gr","stage_recenter_front_o3",
"stage_2nd_layer_go","stage_recenter_front_b3",
"stage_2nd_layer_bo","stage_recenter_front_r3",
"stage_2nd_layer_br","stage_recenter_front_g3",
"stage_top_cross",
"stage_order_top_cross",
"stage_order_top_corners",
"stage_turn_top_corners",
    ]

    cube = Cube(hist=False, size=3)
    solver = BasicSolver(cube, init_stages=init_stages)

    random.seed(42)
    cube.scramble(num_steps=50, wide=False)

    solver.solve()
    assert cube.is_done()

    # white cross
    c,p=cube.find_piece("BW")
    assert c==(1,0,0) , c
    assert p.get_piece_colors_str()=="WB",p.get_piece_colors_str()

    c,p=cube.find_piece("GW")
    assert c==(1,0,2) , c
    assert p.get_piece_colors_str()=="WG",p.get_piece_colors_str()

    c,p=cube.find_piece("RW")
    assert c==(0,0,1) , c
    assert p.get_piece_colors_str()=="RW",p.get_piece_colors_str()
    c,p=cube.find_piece("OW")
    assert c==(2,0,1) , c
    assert p.get_piece_colors_str()=="OW",p.get_piece_colors_str()

    # white corners

    c,p=cube.find_piece("GOW")
    assert c==(2,0,2) , c
    assert p.get_piece_colors_str()=="OWG",p.get_piece_colors_str()
    c,p=cube.find_piece("BOW")
    assert c==(2,0,0) , c
    assert p.get_piece_colors_str()=="OWB",p.get_piece_colors_str()
    c,p=cube.find_piece("BRW")
    assert c==(0,0,0) , c
    assert p.get_piece_colors_str()=="RWB",p.get_piece_colors_str()
    c,p=cube.find_piece("GRW")
    assert c==(0,0,2) , c
    assert p.get_piece_colors_str()=="RWG",p.get_piece_colors_str()


    # 2nd layer
    c,p=cube.find_piece("BO")
    assert c==(2,1,0) , c
    assert p.get_piece_colors_str()=="OB",p.get_piece_colors_str()

    c,p=cube.find_piece("GO")
    assert c==(2,1,2) , c
    assert p.get_piece_colors_str()=="OG",p.get_piece_colors_str()

    c,p=cube.find_piece("GR")
    assert c==(0,1,2) , c
    assert p.get_piece_colors_str()=="RG",p.get_piece_colors_str()

    c,p=cube.find_piece("BR")
    assert c==(0,1,0) , c
    assert p.get_piece_colors_str()=="RB",p.get_piece_colors_str()

    # TOP cross

    p=cube.get_piece((1,2,2))
    assert p.get_piece_colors()==(None,CubeColor.Y,CubeColor.G),p.get_piece_colors_str()

    p=cube.get_piece((2,2,1))
    assert p.get_piece_colors()==(CubeColor.O,CubeColor.Y,None),p.get_piece_colors_str()

    p=cube.get_piece((1,2,0))
    assert p.get_piece_colors()==(None,CubeColor.Y,CubeColor.B),p.get_piece_colors_str()

    p=cube.get_piece((0,2,1))
    assert p.get_piece_colors()==(CubeColor.R,CubeColor.Y,None),p.get_piece_colors_str()

    # TOP corners

    c,p=cube.find_piece("RYB")
    assert c==(0,2,0) , c
    assert p.get_piece_colors_str(no_loc=True)=="BRY",p.get_piece_colors_str()

    c,p=cube.find_piece("OYB")
    assert c==(2,2,0) , c
    assert p.get_piece_colors_str(no_loc=True)=="BOY",p.get_piece_colors_str()

    c,p=cube.find_piece("OYG")
    assert c==(2,2,2) , c
    assert p.get_piece_colors_str(no_loc=True)=="GOY",p.get_piece_colors_str()

    c,p=cube.find_piece("RYG")
    assert c==(0,2,2) , c
    assert p.get_piece_colors_str(no_loc=True)=="GRY",p.get_piece_colors_str()





if __name__ == "__main__" :
    pytest.main()
    pass