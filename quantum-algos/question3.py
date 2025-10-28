from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit
from math import pi
import numpy as np

pi = np.pi

def bv_ideal():
    '''
    Implement the Bernstein Vazirani (BV) algorithm circuit with an oracle function with a secrete key of "0101010"
    Args: 
        None
    Return:
        qcirc: A QuantumCircuit object of your implementation of BV algorithm
    '''
    qcirc = None

    ############################################################################
    # Student code begin
    ############################################################################

    qcirc = QuantumCircuit(8)
    qcirc.x(7)
    for i in range(8):
        qcirc.h(i)
    
    one_index = [1, 3, 5]
    for idx in one_index:
        qcirc.cx(idx, 7)

    for i in range(8):
        qcirc.h(i)

   
    ############################################################################
    # Student code end
    ############################################################################

    return qcirc

def bv_noisy():
    '''
    Recreate your BV circuit with all H gates replaced with U(pi/2, pi/16, pi)

    Args: 
        None
    Return:
        qcirc: A QuantumCircuit object of your implementation of BV algorithm with simulated noise
    '''
    qcirc = None
    
    ############################################################################
    # Student code begin
    ############################################################################

    qcirc = QuantumCircuit(8)
    qcirc.x(7)
    for i in range(8):
        qcirc.u(pi/2, pi/16, pi, i)
    
    one_index = [1, 3, 5]
    for idx in one_index:
        qcirc.cx(idx, 7)

    for i in range(8):
        qcirc.u(pi/2, pi/16, pi, i)

    ############################################################################
    # Student code end
    ############################################################################

    return qcirc