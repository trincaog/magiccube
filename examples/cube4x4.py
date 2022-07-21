import magiccube

# Create the cube
cube = magiccube.Cube(4,state="""
    YYYYYYYYYYYYGGGG
    GGGWRRRRRRRRRRRR
    OOOOGGGWGGGWGGGW
    YBBBOOOOOOOOOOOO
    RRRRYBBBYBBBYBBB
    WWWBWWWBWWWBWWWB
    """)

# Print the cube
print(cube)

# Make some cube rotations
cube.rotate("U' R'")


