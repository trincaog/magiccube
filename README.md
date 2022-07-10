# MagicCube

A Rubik Cube NxNxN implementation
=================================

Installation
---------------
pip install magiccube

Usage
----------
```python
import magiccube

# 3x3x3 Cube
cube = magiccube.Cube(3)
cube.rotate("R' L U D' F B' R' L")
print(cube)

# 6x6x6 Cube
cube = magiccube.Cube(6)
cube.rotate("Rw' Lw 3Uw'")
print(cube)

# Scramble cube
cube.scramble()
print("Moves: ", cube.history())

```








