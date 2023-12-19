import magiccube

# Create the cube
cube = magiccube.Cube(4, state="""
    YYYYYYYYYYYYGGGG
    GGGWRRRRRRRRRRRR
    OOOOGGGWGGGWGGGW
    YBBBOOOOOOOOOOOO
    RRRRYBBBYBBBYBBB
    WWWBWWWBWWWBWWWB
    """)

# Make some cube rotations
cube.rotate("U' R'")

# Print the cube
print(cube)
