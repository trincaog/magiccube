import magiccube

# Create the cube
cube = magiccube.Cube(3)

# Make some cube rotations
cube.rotate("R' L U D' F B' R' L")

# Print the cube
print(cube)

# Reset to the initial position
cube.reset()

# Scramble the cube
cube.scramble()

# Print the cube
print(cube)

# Print the move history
print("Moves: ", cube.history())

# Print the moves to reverse the cube history
cube.rotate(cube.reverse_history())

# Check that the cube is done
assert cube.is_done()

# Print the cube
print(cube)
