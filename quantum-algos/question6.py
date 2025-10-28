from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit
import math
import numpy as np

"""
In this question, you need to design quantum circuits to generate the given quantum states in Dirac's notations.
For each part, return a QuantumCircuit object that corresponds to the given state $\ket{\psi}$.
The Dirac's notations should be understood in Qiskit little-endian ordering.
You may not use the `initialize` instruction.
You can only use the following gates: `h, x, y, z, s, t, u, cu, rx, ry, rz, cx, crx, cry, crz, ccx`
"""

def q6a():
    '''
    Construct the quantum circuit to generate
        $$\ket{\psi}= \frac{1}{2}\ket{00} + \frac{1}{2}\ket{01} + \frac{1}{2}\ket{10} + \frac{1}{2}\ket{11}$$
    Args: 
        None
    Return:
        qcirc: your QuantumCircuit object
    '''

    qcirc = None

    ############################################################################
    # Student code begin
    ############################################################################

    qcirc = QuantumCircuit(2)
    for i in range(2):
        qcirc.h(i)
        

    ############################################################################
    # Student code end
    ############################################################################

    return qcirc


def q6b():
    '''
    Construct the quantum circuit to generate
        $$\ket{\psi}= \frac{1}{2}\ket{010} + \frac{\sqrt{3}}{2}\ket{101}$$
    Args: 
        None
    Return:
        qcirc: your QuantumCircuit object
    '''

    qcirc = None

    ############################################################################
    # Student code begin
    ############################################################################

    qcirc = QuantumCircuit(3)
    theta = 2 * np.arctan(np.sqrt(3))  
    qcirc.ry(theta, 0)
    
    qcirc.cx(0, 2)  
    qcirc.x(0)      
    qcirc.cx(0, 1)  
    qcirc.x(0) 

    ############################################################################
    # Student code end
    ############################################################################

    return qcirc


def q6c():
    '''
    Construct the quantum circuit to generate
        $$\ket{\psi}= \frac{1}{\sqrt{2}}\ket{01} - \frac{1}{\sqrt{2}}\ket{10}$$
    Args: 
        None
    Return:
        qcirc: your QuantumCircuit object
    '''

    qcirc = None

    ############################################################################
    # Student code begin
    ############################################################################

    qcirc = QuantumCircuit(2)
    qcirc.h(1)
    qcirc.x(0)
    qcirc.cx(1,0)
    qcirc.z(0)

    ############################################################################
    # Student code end
    ############################################################################

    return qcirc


def q6d():
    '''
    Construct the quantum circuit to generate
        $$\ket{\psi}= \frac{1}{2}\ket{0001} + \frac{i}{2}\ket{0010} - \frac{1}{2}\ket{0100} - \frac{i}{2}\ket{1000}$$
    Args: 
        None
    Return:
        qcirc: your QuantumCircuit object
    '''

    qcirc = None

    ############################################################################
    # Student code begin
    ############################################################################
    qcirc = QuantumCircuit(4)
    
    ############################################################################
    # Student code end  
    ############################################################################

    return qcirc


def q6e():
    '''
    Construct the quantum circuit to generate
        $$\ket{\psi}= \frac{1}{\sqrt(3)}\ket{001} + \frac{1}{\sqrt(3)}\ket{010} + \frac{1}{\sqrt(3)}\ket{100}$$
    Args: 
        None
    Return:
        qcirc: your QuantumCircuit object
    '''

    qcirc = None

    ############################################################################
    # Student code begin
    ############################################################################

    qcirc = QuantumCircuit(3)
    theta1 = 2 * np.arcsin(np.sqrt(1/3))
    qcirc.ry(theta1, 0)
    
    qcirc.x(0)  
    qcirc.cry(2 * np.arcsin(np.sqrt(1/2)), 0, 1)
    qcirc.x(0) 
    qcirc.x(0)
    qcirc.x(1)
    qcirc.ccx(0, 1, 2)  
    qcirc.x(0)
    qcirc.x(1)

    ############################################################################
    # Student code end
    ############################################################################

    return qcirc
