from magiccube.solver.basic.solver_base import Condition, ConditionAction

stage_recenter_down = (
    ConditionAction((
        Condition(101, ("*",)),
    ), "", False),
    ConditionAction((
        Condition(121, ("*",)),
    ), "X X", False),
    ConditionAction((
        Condition(110, ("*",)),
    ), "X", False),
    ConditionAction((
        Condition(112, ("*",)),
    ), "X'", False),
    ConditionAction((
        Condition(11, ("*",)),
    ), "Z'", False),
    ConditionAction((
        Condition(211, ("*",)),
    ), "Z", False),
)

stage_recenter_front = (
    ConditionAction((
        Condition(110, ("*",)),
    ), "Y Y", False),
    ConditionAction((
        Condition(112, ("*",)),
    ), "", False),
    ConditionAction((
        Condition(11, ("*",)),
    ), "Y'", False),
    ConditionAction((
        Condition(211, ("*",)),
    ), "Y", False),
)

stage_white_cross = (
    ConditionAction((
        Condition(100, ("W*",)),
    ), "", False),
    ConditionAction((
        Condition(100, ("*W",)),
    ), "B D' R D", False),
    ConditionAction((
        Condition(201, ("W*",)),
    ), "R' B'", False),
    ConditionAction((
        Condition(201, ("*W",)),
    ), "R' D' R D", False),
    ConditionAction((
        Condition(102, ("W*",)),
    ), "F F U U B B", False),
    ConditionAction((
        Condition(102, ("*W",)),
    ), "F' D' R' D", False),
    ConditionAction((
        Condition(1, ("W*",)),
    ), "L B", False),
    ConditionAction((
        Condition(1, ("*W",)),
    ), "L D L' D'", False),
    ConditionAction((
        Condition(210, ("*W",)),
    ), "D' R D", False),
    ConditionAction((
        Condition(210, ("W*",)),
    ), "B'", False),
    ConditionAction((
        Condition(212, ("*W",)),
    ), "D' R' D", False),
    ConditionAction((
        Condition(212, ("W*",)),
    ), "D D F D D", False),
    ConditionAction((
        Condition(12, ("*W",)),
    ), "D L D'", False),
    ConditionAction((
        Condition(12, ("W*",)),
    ), "D D F' D D", False),
    ConditionAction((
        Condition(10, ("*W",)),
    ), "D L' D'", False),
    ConditionAction((
        Condition(10, ("W*",)),
    ), "B", False),
    ConditionAction((
        Condition(120, ("W*",)),
    ), "B B", False),
    ConditionAction((
        Condition(120, ("*W",)),
    ), "B' D' R D", False),
    ConditionAction((
        Condition(221, ("W*",)),
    ), "U' B D L' D'", False),
    ConditionAction((
        Condition(221, ("*W",)),
    ), "U' B B", False),
    ConditionAction((
        Condition(122, ("W*",)),
    ), "U U B B", False),
    ConditionAction((
        Condition(122, ("*W",)),
    ), "U' D' R D B'", False),
    ConditionAction((
        Condition(21, ("W*",)),
    ), "U B D L' D'", False),
    ConditionAction((
        Condition(21, ("*W",)),
    ), "U B B", False),
)

stage_white_corner = (
    ConditionAction((
        Condition(20, ("W**",)),
    ), "F' U U F", True),
    ConditionAction((
        Condition(20, ("*W*",)),
    ), "U U R U' R' ", True),
    ConditionAction((
        Condition(20, ("**W",)),
    ), "R U U R'", True),
    ConditionAction((
        Condition(220, ("W**",)),
    ), "U' R U U R'", True),
    ConditionAction((
        Condition(220, ("*W*",)),
    ), "U R U' R' ", True),
    ConditionAction((
        Condition(220, ("**W",)),
    ), "F' U F", True),
    ConditionAction((
        Condition(222, ("W**",)),
    ), "U' F' U F", True),
    ConditionAction((
        Condition(222, ("*W*",)),
    ), "R U' R'   ", True),
    ConditionAction((
        Condition(222, ("**W",)),
    ), "U R U' R'", True),
    ConditionAction((
        Condition(22, ("W**",)),
    ), "R U' R'", True),
    ConditionAction((
        Condition(22, ("*W*",)),
    ), "U' R U' R'", True),
    ConditionAction((
        Condition(22, ("**W",)),
    ), "U F' U U F", True),
    ConditionAction((
        Condition(0, ("W**",)),
    ), "B' U B    ", True),
    ConditionAction((
        Condition(0, ("*W*",)),
    ), "B' U' B U ", True),
    ConditionAction((
        Condition(0, ("**W",)),
    ), "B' U' B U ", True),
    ConditionAction((
        Condition(200, ("W**",)),
    ), "R' U' R   ", True),
    ConditionAction((
        Condition(200, ("*W*",)),
    ), "B U B'    ", True),
    ConditionAction((
        Condition(200, ("**W",)),
    ), "B U B'   ", True),
    ConditionAction((
        Condition(202, ("W**",)),
    ), "R U R'", True),
    ConditionAction((
        Condition(202, ("*W*",)),
    ), "", False),
    ConditionAction((
        Condition(202, ("**W",)),
    ), "R U' R'", True),
    ConditionAction((
        Condition(2, ("W**",)),
    ), "L' U' L ", True),
    ConditionAction((
        Condition(2, ("*W*",)),
    ), "L' U' L  ", True),
    ConditionAction((
        Condition(2, ("**W",)),
    ), "L' U L   ", True),
)

stage_2nd_layer = (
    ConditionAction((
        Condition(221, ("OB", "GO", "RG", "BR")),
        # ),"Y' U U U' L' U L U F U' F' Y",   True),
    ), "Y' U U U R U' R' U' F' U F Y",   True),
    ConditionAction((
        Condition(221, ("BO", "OG", "GR", "RB")),
    ), "U",   True),
    ConditionAction((
        Condition(120, ("OB", "GO", "RG", "BR")),
    ), "U U", True),
    ConditionAction((
        Condition(120, ("BO", "OG", "GR", "RB")),
    ), "Y' U' U R U' R' U' F' U F Y", True),
    ConditionAction((
        Condition(21, ("OB", "GO", "RG", "BR")),
    ), "Y' U R U' R' U' F' U F Y",  True),
    ConditionAction((
        Condition(21, ("BO", "OG", "GR", "RB")),
    ), "U'",  True),
    ConditionAction((
        Condition(122, ("BO", "OG", "GR", "RB")),
    ), "U' L' U L U F U' F'", True),
    ConditionAction((
        Condition(122, ("OB", "GO", "RG", "BR")),
    ), "U' L' U L U F U' F'", False),
    ConditionAction((
        Condition(212, ("BO", "OB", "OG", "GO", "GR", "RG", "RB", "BR")),
    ), "U R U' R' U' F' U F", True),
    ConditionAction((
        Condition(12, ("BO", "OG", "GR", "RB")),
    ), "U' L' U L U F U' F'", True),
    ConditionAction((
        Condition(12, ("OB", "GO", "RG", "BR")),
    ), "", False),
    ConditionAction((
        Condition(10, ("BO", "OB", "OG", "GO", "GR", "RG", "RB", "BR")),
    ), "Y' U' L' U L U F U' F' Y", True),
    ConditionAction((
        Condition(210, ("BO", "OB", "OG", "GO", "GR", "RG", "RB", "BR")),
    ), "Y U R U' R' U' F' U F Y'", True),
)

stage_top_cross = (
    ConditionAction((
        Condition(120, ("Y*",)),  # B - OK=Y*
        Condition(221, ("*Y",)),  # R - OK=*Y
        Condition(122, ("Y*",)),  # F - OK=Y*
        Condition(21, ("*Y",)),  # L - OK=*Y
    ), "", False),
    ConditionAction((
        Condition(120, ("Y*",)),  # B - OK=Y*
        Condition(221, ("*Y",)),  # R - OK=*Y
        Condition(122, ("*Y",)),  # F - OK=Y* NOK
        Condition(21, ("Y*",)),  # L - OK=*Y NOK
    ), "U'", True),
    ConditionAction((
        Condition(120, ("*Y",)),  # B - OK=Y* NOK
        Condition(221, ("*Y",)),  # R - OK=*Y
        Condition(122, ("Y*",)),  # F - OK=Y*
        Condition(21, ("Y*",)),  # L - OK=*Y NOK
    ), "U U", True),
    ConditionAction((
        Condition(120, ("*Y",)),  # B - OK=Y* NOK
        Condition(221, ("Y*",)),  # R - OK=*Y NOK
        Condition(122, ("Y*",)),  # F - OK=Y*
        Condition(21, ("*Y",)),  # L - OK=*Y
    ), "U", True),
    ConditionAction((  # L shape
        Condition(120, ("Y*",)),  # B - OK=Y*
        Condition(221, ("Y*",)),  # R - OK=*Y NOK
        Condition(122, ("*Y",)),  # F - OK=Y* NOK
        Condition(21, ("*Y",)),  # L - OK=*Y
    ), "F R U R' U' F'", True),
    ConditionAction((
        Condition(120, ("Y*",)),  # B - OK=Y*
        Condition(221, ("Y*",)),  # R - OK=*Y NOK
        Condition(122, ("Y*",)),  # F - OK=Y*
        Condition(21, ("Y*",)),  # L - OK=*Y NOK
    ), "U", True),
    ConditionAction((  # LINE shape
        Condition(120, ("*Y",)),  # B - OK=Y* NOK
        Condition(221, ("*Y",)),  # R - OK=*Y
        Condition(122, ("*Y",)),  # F - OK=Y* NOK
        Condition(21, ("*Y",)),  # L - OK=*Y
    ), "F R U R' U' F'", False),
    ConditionAction((  # NONE
        Condition(120, ("*Y",)),  # B - OK=Y* NOK
        Condition(221, ("Y*",)),  # R - OK=*Y
        Condition(122, ("*Y",)),  # F - OK=Y* NOK
        Condition(21, ("Y*",)),  # L - OK=*Y
    ), "F R U R' U' F'", True),
)

stage_order_top_cross = (
    ConditionAction((
        Condition(120, ("YB",)),  # B - OK=Y*
        Condition(221, ("OY",)),  # R - OK=*Y
        Condition(122, ("YG",)),  # F - OK=Y*
        Condition(21, ("RY",)),  # L - OK=*Y
    ), "", False),
    ConditionAction((
        Condition(120, ("YB",)),  # B - OK=Y*
        Condition(221, ("OY",)),  # R - OK=*Y
        Condition(122, ("GY",)),  # F - OK=Y*
        Condition(21, ("YR",)),  # L - OK=*Y
    ), "R U R' U R U U R' U", False),

    ConditionAction((
        Condition(120, ("YR",)),  # B - OK=Y*
        Condition(221, ("BY",)),  # R - OK=*Y
        Condition(122, ("GY",)),  # F - OK=Y*
        Condition(21, ("YO",)),  # L - OK=*Y
    ), "R U R' U R U U R' U   U'", False),

    ConditionAction((
        Condition(120, ("YO",)),  # B - OK=Y*
        Condition(221, ("BY",)),  # R - OK=*Y
        Condition(122, ("YG",)),  # F - OK=Y*
        Condition(21, ("RY",)),  # L - OK=*Y
    ), "U U R U R' U R U U R' U U U", False),

    ConditionAction((
        Condition(120, ("YR",)),  # B - OK=Y*
        Condition(221, ("OY",)),  # R - OK=*Y
        Condition(122, ("YG",)),  # F - OK=Y*
        Condition(21, ("BY",)),  # L - OK=*Y
    ), "U' R U R' U R U U R' U U", False),

    ConditionAction((
        Condition(120, ("YO",)),  # B - OK=Y*
        Condition(221, ("RY",)),  # R - OK=*Y
        Condition(122, ("YG",)),  # F - OK=Y*
        Condition(21, ("BY",)),  # L - OK=*Y
    ), "U R U R' U R U U R' U", False),


    ConditionAction((
        Condition(120, ("YR",)),  # B - OK=Y*
        Condition(221, ("BY",)),  # R - OK=*Y
        Condition(122, ("YG",)),  # F - OK=Y*
        Condition(21, ("OY",)),  # L - OK=*Y
    ), "R U R' U R U U R' U U'", False),

    ConditionAction((
        Condition(120, ("YB",)),  # B - OK=Y*
        Condition(221, ("RY",)),  # R - OK=*Y
        Condition(122, ("YG",)),  # F - OK=Y*
        Condition(21, ("OY",)),  # L - OK=*Y
    ), "R U R' U R U U R' U", True),

    ConditionAction((
        Condition(120, ("YG",)),  # B - OK=Y*
        Condition(221, ("**",)),  # R - OK=*Y
        Condition(122, ("**",)),  # F - OK=Y*
        Condition(21, ("**",)),  # L - OK=*Y
    ), "U U", True),
    ConditionAction((
        Condition(120, ("**",)),  # B - OK=Y*
        Condition(221, ("GY",)),  # R - OK=*Y
        Condition(122, ("**",)),  # F - OK=Y*
        Condition(21, ("**",)),  # L - OK=*Y
    ), "U", True),
    ConditionAction((
        Condition(120, ("**",)),  # B - OK=Y*
        Condition(221, ("**",)),  # R - OK=*Y
        Condition(122, ("**",)),  # F - OK=Y*
        Condition(21, ("GY",)),  # L - OK=*Y
    ), "U'", True),
)


stage_order_top_corners = (
    ConditionAction((
        Condition(20, ("RYB", "BRY", "YBR",)),
        Condition(220, ("OYB", "BOY", "YBO",)),
        Condition(222, ("OYG", "GOY", "YGO",)),
        Condition(22, ("RYG", "GRY", "YGR",)),
    ), "", False),

    ConditionAction((
        Condition(20, ("RYB", "BRY", "YBR",)),
        Condition(220, ("***",)),
        Condition(222, ("***",)),
        Condition(22, ("***",)),
    ), "Y Y U R U' L' U R' U' L Y Y", True),

    ConditionAction((
        Condition(20, ("***",)),
        Condition(220, ("OYB", "BOY", "YBO",)),
        Condition(222, ("***",)),
        Condition(22, ("***",)),
    ), "Y U R U' L' U R' U' L Y'", True),

    ConditionAction((
        Condition(20, ("***",)),
        Condition(220, ("***",)),
        Condition(222, ("OYG", "GOY", "YGO",)),
        Condition(22, ("***",)),
    ), "U R U' L' U R' U' L", True),

    ConditionAction((
        Condition(20, ("***",)),
        Condition(220, ("***",)),
        Condition(222, ("***",)),
        Condition(22, ("RYG", "GRY", "YGR",)),
    ), "Y' U R U' L' U R' U' L Y", True),

    ConditionAction((
        Condition(20, ("***",)),
        Condition(220, ("***",)),
        Condition(222, ("***",)),
        Condition(22, ("***",)),
    ), "U R U' L' U R' U' L", True),

)

stage_turn_top_corners = (
    ConditionAction((
        Condition(20, ("RYB",)),
        Condition(220, ("OYB",)),
        Condition(222, ("OYG",)),
        Condition(22, ("RYG",)),
    ), "", False),
    ConditionAction((
        Condition(20, ("BYO",)),
        Condition(220, ("GYO",)),
        Condition(222, ("GYR",)),
        Condition(22, ("BYR",)),
    ), "U", False),
    ConditionAction((
        Condition(20, ("OYG",)),
        Condition(220, ("RYG",)),
        Condition(222, ("RYB",)),
        Condition(22, ("OYB",)),
    ), "U U", False),
    ConditionAction((
        Condition(20, ("GYR",)),
        Condition(220, ("BYR",)),
        Condition(222, ("BYO",)),
        Condition(22, ("GYO",)),
    ), "U'", False),
    ConditionAction((
        Condition(20, ("***",)),
        Condition(220, ("***",)),
        Condition(222, ("*B*", "*R*", "*G*", "*O*",)),
        Condition(22, ("***",)),
    ), "R' D' R D R' D' R D", True),
    ConditionAction((
        Condition(20, ("***",)),
        Condition(220, ("***",)),
        Condition(222, ("*Y*",)),
        Condition(22, ("***",)),
    ), "U", True),


)
