import magiccube

cube = magiccube.Cube(3)

cube.rotate("R' L U D' F B' R' L")
print(cube)

cube.scramble()
print(cube)
print("Moves: ", cube.history())

cube.rotate(cube.reverse_history())
assert cube.is_done()

