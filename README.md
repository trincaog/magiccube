# MagicCube: A NxNxN Rubik Cube implementation

A fast implementation of the Rubik Cube based in Python 3.x.

Makes it easy to create cubes of various sizes (2x2x2, 3x3x3, 4x4x4, 6x6x6, ...., 100x100x100).

Fast rotation speed when compared with other Python implementations, which makes it suitable for Rubik Cube simulations.

Includes:

- Simple solver for the 3x3x3 cube.
- Move optimizer which reduces the number of moves.

## Installation

```sh
pip install magiccube
```

## Usage

```python
import magiccube

# 3x3x3 Cube
cube = magiccube.Cube(3,"YYYYYYYYYRRRRRRRRRGGGGGGGGGOOOOOOOOOBBBBBBBBBWWWWWWWWW")
print(cube)
```

![Cube](https://trincaopub.s3.amazonaws.com/imgs/magiccube/cube3x3.png)

```python
# Rotate the cube
cube.rotate("R' L2 U D' F B'2 R' L")

# Solve the 3x3x3 cube
from magiccube import BasicSolver
solver = BasicSolver(cube)
solver.solve()

# Complex moves 6x6x6 Cube
cube = magiccube.Cube(6)
cube.rotate("Lw") # L wide rotation
cube.rotate("Lw'") # L wide counter-rotation
cube.rotate("Lw2") # 2x L wide rotation
cube.rotate("3L") # 3rd line L rotation
cube.rotate("3Lw") # 3rd line L wide rotation
cube.rotate("3Lw'2") # 2x 3rd line L wide counter-rotation

# Get cube state
print("State:", cube.get())
# Get cube state in Kociemba order
print("State (Kociemba):", cube.get_kociemba_facelet_colors())
```

## Documentation and Examples

- [Code Samples](https://github.com/trincaog/magiccube/tree/main/examples)
- [API Documentation](https://trincaog.github.io/magiccube/magiccube/cube.html)

## Supported Moves and Notation

Uses SIGN notation, including advanced extensions.

### Basic moves

|Move |                                                             |
|-----|-------------------------------------------------------------|
|L L' | Clockwise/Counterclockwise cube rotation of the LEFT face.  |
|R R' | Clockwise/Counterclockwise cube rotation of the RIGHT face. |
|D D' | Clockwise/Counterclockwise cube rotation of the DOWN face.  |
|U U' | Clockwise/Counterclockwise cube rotation of the UP face.    |
|F F' | Clockwise/Counterclockwise cube rotation of the FRONT face. |
|B B' | Clockwise/Counterclockwise cube rotation of the BACK face.  |

### Advanced Moves

|Move |                                                             |
|-----|-------------------------------------------------------------|
|X X' | Cube rotation on X axis. X is the axis that points from LEFT to the RIGHT face.|
|Y Y' | Cube rotation on Y axis. Y is the axis that points from DOWN to the UP face.|
|Z Z' | Cube rotation on Z axis. Z is the axis that points from BACK to the FRONT face.|
|M M' | Rotation of the center layer on the X axis.|
|E E' | Rotation of the center layer on the Y axis.|
|S S' | Rotation of the center layer on the Z axis.|
|Fw Fw'| Wide rotation of 2 layers.|
|3Fw 3Fw' | Wide rotation of 3 layers.|
|3F 3F' | Rotation of the 3rd layer.|
|F2 F'2 | 2x rotation.|

## Cube Coordinates

- Cube coordinates are expressed as a tuple of x,y,z.
- (0,0,0) is the piece on the LEFT,DOWN,BACK corner.
- In a 3x3x3, (2,2,2) is the piece on the RIGHT,UP,FRONT corner.

## Solver

The solver uses the [beginner method](https://ruwix.com/the-rubiks-cube/how-to-solve-the-rubiks-cube-beginners-method/) to solve the cube

## Move Optimizer

The move optimizer does the following optimizations:

- Eliminates redundant moves (ex: L L L L)
- Converts 3x moves to the inverse (ex: F F F -> F')
- Eliminates cube rotations (ex: Y F -> R)

## Development

Install `pyenv`

```sh
curl https://pyenv.run | bash
```

Setup the environment using `pyenv`

```sh
pyenv install 3.11
pyenv virtualenv 3.11 cube
pyenv local cube
pip install -r requirements.txt
direnv allow
```

Install commit hooks

```sh
pre-commit install
```
