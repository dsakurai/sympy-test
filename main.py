#!/usr/bin/env python

import sympy as sp
from sympy.vector import CoordSys3D

E_x, E_y, E_z = sp.symbols('E_x E_y E_z')

N = CoordSys3D('N')

E = E_x * N.i + E_y * N.j + E_z * N.k

# For simplicity, we set its x-coordinate to 0. This is mathematically not necessary.
E_x_is_zero = sp.Eq(E_x, 0)

solution = sp.solve([E_x_is_zero], [E_x])

print(solution)