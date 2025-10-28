from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit, transpile
from qiskit.quantum_info import Operator
from math import pi
import numpy as np
from qiskit.providers.basic_provider import BasicSimulator


def simon():
    """
    Implement the Simon's algorithm using the given oracle in the question.
    Args: 
        None
    Return:
        qcirc: QuantumCircuit of your implementation of Simon's algorithm
    """

    qcirc = None
    ############################################################################
    # Student code begin
    ############################################################################

    qcirc = QuantumCircuit(8)
    qcirc.h(0)
    qcirc.h(1)
    qcirc.h(2)
    qcirc.h(3)
    qcirc.cx(0, 4)
    qcirc.cx(1, 5)
    qcirc.cx(2, 6)
    qcirc.cx(3, 7)
    qcirc.cx(1, 5)
    qcirc.cx(1, 7)
    qcirc.h(0)
    qcirc.h(1)
    qcirc.h(2)
    qcirc.h(3)

    ############################################################################
    # Student code end
    ############################################################################

    return qcirc


def calculate_secret():
    """
    Calculate the secret string of the given oracle. (This can be hard coded!)
    Args:
        None
    Return:
        s: str of the secret string of the function 
    """

    s = ""
    ############################################################################
    # Student code begin
    ############################################################################

    s = "1010"

    ############################################################################
    # Student code end
    ############################################################################

    return s
