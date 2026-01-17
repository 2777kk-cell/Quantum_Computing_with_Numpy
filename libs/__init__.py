import os, sys
import uuid
import numpy
import numpy as np
from numpy import array, matrix, zeros, ones, eye, pi
from numpy import matmul, kron, hstack, vstack
from numpy import sin, cos, log2, pi, e
from numpy import allclose
from functools import reduce
from itertools import *


"""**Basis Vectors**"""
# Z Basis | all these basis vectors are orthonormal by virtue
KET_0 =array([[1.],  [0.]])
KET_1 =array([[0.],  [1.]])

# X Basis or Hadamard Basis
KET_XP = (KET_0 + KET_1)/np.sqrt(2)
KET_XM = (KET_0 - KET_1)/np.sqrt(2)

# Y Basis
KET_YP = (KET_0 + 1j*KET_1)/np.sqrt(2)
KET_YM = (KET_0 - 1j*KET_1)/np.sqrt(2)



###### ----------------------------- ######
"""**Pauli's  Matrices(not scaled in $hslash$)**"""

PauliX     =  array([[complex(0., 0.), complex(1., 0.)],
                     [complex(1., 0.), complex(0., 0.)]])

PauliY     =  array([[complex(0., 0.), -complex(0., 1.)],
                     [complex(0., 1.), complex(0., 0.)]])

PauliZ     =  array([[complex(1., 0.), -complex(0., 0.)],
                     [complex(0., 0.), -complex(1., 0.)]])


##Order: Source -> S, Target -> T (General 2 qubit)
CX = array([[1., 0., 0., 0.],
              [0., 1., 0., 0.],
              [0., 0., 0., 1.],
              [0., 0., 1., 0.]])


CZ = array([[1.,0.,0.,0.],
            [0.,1.,0.,0.],
            [0.,0.,1.,0.],
            [0.,0.,0.,-1.]])




X = array([[0, 1,],[1, 0]])
Y = array([[0, -1j,],[1j, 0]])
Z = array([[1, 0,],[0, -1]])
H = array([[1, 1.,],[1, -1]])/pow(2, 0.5)
P = array([[1, 0.],[0, complex(0, 1)]])
S = array([[1, 0.],[0, -1]])


Z_BASIS_KET_DICT = {0 : KET_0, 1: KET_1}

def apply_gate(gate, vector_dict, control, target):
    """
    Waring: User defined/custom function: 
    ***always run from numpy import allclose, array***
    before running/using this method. also define 
    KET_1 = array([[0], [1]]).
    ***NOT TO BE USED OUT OF SCOPE OF THIS LIBRARY***
    ##
    ## gate: 2x2 numpy array;
    ## vector_dict -> typically {<int>: numpy-array-2x1}
    ## control -> int -> must be within key set of vector_dict
    ## target -> int -> must be within key set of vector_dict
    """
    if allclose(vector_dict[control], KET_1):
        vector_dict[target] = matmul(gate, vector_dict[target])
        
    return vector_dict

    
def two_qubit_operation(n, gate, source_qubit, target_qubit):
    In =  eye(2**n)
    try:
        CX_Matrix = list()
        for i_n in In:
            r=int( "".join([str(int(x)) for x in i_n.tolist()][::-1]), 2)
            ik = int(np.log2(r))
            xik = bin(ik)[2:].zfill(n)
            bits_dict = {i: int(x_) for i, x_ in enumerate(xik)}
            basis_ket_dict = {k: Z_BASIS_KET_DICT[v] for k, v in bits_dict.items()}
            plain_ket = reduce(kron, list(basis_ket_dict.values()))
            ######           
            gate_operated_dict = apply_gate(gate, basis_ket_dict, source_qubit, target_qubit)
            ######
            x_operated_ket = reduce(kron, list(gate_operated_dict.values()))
            CX_Matrix.append(matmul(plain_ket, x_operated_ket.T))

        return sum(CX_Matrix)
      
    except:
        raise Exception("TBA")

