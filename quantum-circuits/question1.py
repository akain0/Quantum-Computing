from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit
import numpy as np
pi = np.pi
"""
In this question you need to construct the quantum circutis for each part according to the figures provided.
For each part, follow the instructions and return a QuantumCircuit object.
"""


def q1a():
    """
    Construct the quantum circuit shown in Question 1 Part A
    Args: 
        None
    Return:
        qc: your QuantumCircuit object
    """

    
    qc = None
    ############################################################################
    # Student code begin
    ############################################################################

    qc = QuantumCircuit(4)
    qc.h(0)
    qc.h(1)
    qc.h(2)
    qc.h(3)
    qc.id(0)
    qc.x(1)
    qc.y(2)
    qc.z(3)

    ############################################################################
    # Student code end
    ############################################################################
    return qc


def q1b():
    

    qc = None
    ############################################################################
    # Student code begin
    ############################################################################

    qc = QuantumCircuit(3)
    qc.h(0)
    qc.cx(0, 1)
    qc.cx(1,2)



    ############################################################################
    # Student code end
    ############################################################################
    return qc


def q1c():
    """
    Construct the quantum circuit shown in Question 1 Part C
    Args: 
        None
    Return:
        qc: your QuantumCircuit object
    """

    qc = None
    ############################################################################
    # Student code begin
    ############################################################################

    qc = QuantumCircuit(6)
    qc.x(5)
    qc.h(0)
    qc.h(1)
    qc.h(2)
    qc.h(3)
    qc.h(4)
    qc.h(5)
    qc.cx(0, 5)
    qc.cx(1, 5)
    qc.cx(2, 5)
    qc.h(0)
    qc.h(1)
    qc.h(2)
    qc.h(3)
    qc.h(4)
    qc.h(5)


    ############################################################################
    # Student code end
    ############################################################################
    return qc


def q1d():
    """
    Construct the quantum circuit shown in Question 1 Part D
    Args: 
        None
    Return:
        qc: your QuantumCircuit object
    """

    qc = None
    ############################################################################
    # Student code begin
    ############################################################################

    qc = QuantumCircuit(2)
    qc.u(pi/2, pi/4, -pi, 1)
    qc.cx(1,0)
    qc.u(0, 0, -pi/4, 0)
    qc.cx(1,0)
    qc.u(pi/2, 0, -3*pi/4, 0)
    qc.swap(0,1)

    ############################################################################
    # Student code end
    ############################################################################
    return qc

    
