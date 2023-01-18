import time
start = time.time()

from dolfin import *
import numpy as np
import json
import matplotlib.pyplot as plt
import scipy as sp

import dolfin as df
# -------------------------------------------------------------------
# MPI functions -----------------------------------------------------
# -------------------------------------------------------------------
comm = MPI.comm_world
rank = MPI.rank(comm)


def mprint(*argv):
    if rank == 0:
        out = ""
        for arg in argv:
            out = out + str(arg)
        # this forces program to output when run in parallel
        print(out, flush=True)


# In[3]:



# -------------------------------------------------------------------
# Set some common FEniCS flags --------------------------------------
# -------------------------------------------------------------------
set_log_level(50)
parameters["form_compiler"]["optimize"] = True
parameters["form_compiler"]["cpp_optimize"] = True

mesh = Mesh()
with XDMFFile("mesh/tetra.xdmf") as infile:
    infile.read(mesh)

# Function space, trial and test functions
elem_P = VectorElement('Lagrange', mesh.ufl_cell(), 2)
elem_R = VectorElement('Real', mesh.ufl_cell(), 0)
elem = MixedElement([elem_P, elem_R, elem_R, elem_R, elem_R, elem_R, elem_R, elem_R, elem_R, elem_R, elem_R, elem_R, elem_R, elem_R, elem_R, elem_R, elem_R])
V = FunctionSpace(mesh, elem)

u_, U_1, C_1, U_2, C_2, U_3, C_3, U_4, C_4, U_5, C_5, U_6, C_6, U_7, C_7, U_8, C_8 = TrialFunctions(V)
du, dU1, dC1, dU2, dC2, dU3, dC3, dU4, dC4, dU5, dC5, dU6, dC6, dU7, dC7, dU8, dC8  = TestFunctions(V)    
    
    
mprint(V.dim())
