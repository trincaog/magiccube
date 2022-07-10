import magiccube

cube = magiccube.Cube(6)

cube.rotate("Rw' Lw 3Uw'")
print(cube)

cube.scramble()
#print(cube)
print("Moves: ", cube.history())

cube.rotate(cube.reverse_history())
assert cube.is_done()
