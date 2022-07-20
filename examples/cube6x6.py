import magiccube

# Create the cube
cube = magiccube.Cube(6)

# Print the cube
print(cube)

# Make some cube rotations
cube.rotate("Rw' Lw 3Uw'")

# Print the cube
print(cube)

# Reset to the initial position
cube.reset()

# Scramble the cube
cube.scramble()

# Print the move history
print("Moves: ", cube.history())

# Print the moves to reverse the cube history
cube.rotate(cube.reverse_history())

# Check that the cube is done
assert cube.is_done()
