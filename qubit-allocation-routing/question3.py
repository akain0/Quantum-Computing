
from qiskit import QuantumCircuit, transpile
from qiskit.transpiler import CouplingMap
from qiskit.circuit.library import CUGate
import math
import numpy as np


def cx_ideal():
    """
    A noise-free cx gate implemented using a qiskit.circuit.Gate object
    Hint: use CUGate
    Args:
        None
    Return:
        studentGate: qiskit.circuit.Gate
    """
    studentGate = None
    ############################################################################
    # Student code begin
    ############################################################################

    studentGate = CUGate(np.pi, 0, 0, 0)
    
    ############################################################################
    # Student code end
    ############################################################################

    return studentGate

def return_noisy_cnot(p):
    theta = 2*np.arcsin(np.sqrt(p))
    return CUGate(theta, 0, 0, 0)

def cx_p95():
    """
    A noisy cx gate of p=0.95 according to the definition in the
    jupyter notebook implemented using a qiskit.circuit.Gate object
    Hint: use CUGate
    Args:
        None
    Return:
        studentGate: qiskit.circuit.Gate
    """
    studentGate = None
    ############################################################################
    # Student code begin
    ############################################################################

    
    studentGate = return_noisy_cnot(0.95)

    ############################################################################
    # Student code end
    ############################################################################

    return studentGate

def cx_p70():
    """
    A noisy cx gate of p=0.70 according to the definition in the
    jupyter notebook implemented using a qiskit.circuit.Gate object
    Hint: use CUGate
    Args:
        None
    Return:
        studentGate: qiskit.circuit.Gate
    """
    studentGate = None
    ############################################################################
    # Student code begin
    ############################################################################

    studentGate = return_noisy_cnot(0.7)
    
    ############################################################################
    # Student code end
    ############################################################################

    return studentGate


def q3c_edge_gates():
    """
    Implement the cx gates on each edge according to q3c device topology,
    each key denotes a bidirectional edge of the device
    Args:
        None
    Return:
        edge_gates: dict[str, qiskit.circuit.Gate]
    """
    edge_gates = {
        "01": None,
        "12": None,
        "23": None,
        "03": None,
    }
    ############################################################################
    # Student code begin
    ############################################################################
    edge_noise_values = [0.99, 0.9, 0.8, 0.75]
    for i, (key, value) in enumerate(edge_gates.items()):
        edge_gates[key] = return_noisy_cnot(edge_noise_values[i])

    ############################################################################
    # Student code end
    ############################################################################

    return edge_gates

def perform_swap_using_cnots(qc, edge_gates, qubit_a, qubit_b, edge_key):
    """
    Perform SWAP(qubit_a, qubit_b) using 3-CNOT sequence
    """
    qc.append(edge_gates[edge_key], [qubit_a, qubit_b]) 
    qc.append(edge_gates[edge_key], [qubit_b, qubit_a])  
    qc.append(edge_gates[edge_key], [qubit_a, qubit_b])

def q3c_device_qubit_route_mapping():
    """
    The logical qubits (int) to physical qubits (int) mapping for qubit
    allocation
    Args:
        None
    Return:
        qubit_mapping: dict[int, int]
    """
    qubit_mapping = None
    ############################################################################
    # Student code begin
    ############################################################################
    
    qubit_mapping = {
        0: 1,  
        1: 0,  
        2: 2, 
        3: 3  
    }

    ############################################################################
    # Student code end
    ############################################################################

    return qubit_mapping


def q3c_device_compatible_physical_circuit():
    """
    Your implementation physical quantum circuit based on the logical circuit
    and device topology q3c_device_topology.png
    Args:
        None
    Return:
        qc: QuantumCircuit
    """
    qc = None
    ############################################################################
    # Student code begin
    ############################################################################
    
    qc = QuantumCircuit(4)
    edge_gates = q3c_edge_gates()

    qc.append(edge_gates['01'], [1, 0])  
    qc.append(edge_gates['12'], [1, 2])  
    
    perform_swap_using_cnots(qc, edge_gates, 0, 1, '01')  
    
    qc.append(edge_gates['03'], [0, 3])  
    perform_swap_using_cnots(qc, edge_gates, 0, 1, '01')  

    ############################################################################
    # Student code end
    ############################################################################

    return qc


def q3c_device_qubit_read_mapping():
    """
    Your physical qubits (int) to logical qubits (int) mapping for information
    recovery
    Args:
        None
    Return:
        qubit_mapping: dict[int, int]
    """
    qubit_mapping = None
    ############################################################################
    # Student code begin
    ############################################################################
   
    qubit_mapping = {
        0: 1, 
        1: 0,
        2: 2,  
        3: 3   
    }
    
    ############################################################################
    # Student code end
    ############################################################################

    return qubit_mapping


def q3d_edge_gates():
    """
    Implement the cx gates on each edge according to q3d device topology,
    each key denotes a bidirectional edge of the device
    Args:
        None
    Return:
        edge_gates: dict[str, qiskit.circuit.Gate]
    """
    edge_gates = {
        "01": None,
        "12": None,
        "13": None,
        "34": None,
    }
    ############################################################################
    # Student code begin
    ############################################################################

    edge_noise_values = [0.85, 0.825, 0.975, 0.99]
    for i, (key, value) in enumerate(edge_gates.items()):
        edge_gates[key] = return_noisy_cnot(edge_noise_values[i])

    ############################################################################
    # Student code end
    ############################################################################

    return edge_gates


def q3d_device_qubit_route_mapping():
    """
    The logical qubits (int) to physical qubits (int) mapping for qubit
    allocation
    Args:
        None
    Return:
        qubit_mapping: dict[int, int]
    """
    qubit_mapping = None
    ############################################################################
    # Student code begin
    ############################################################################
    
    qubit_mapping = {
        0: 1,  
        1: 0,
        2: 2, 
        3: 3   
    }
    

    ############################################################################
    # Student code end
    ############################################################################

    return qubit_mapping


def q3d_device_compatible_physical_circuit():
    """
    Your implementation physical quantum circuit based on the logical circuit
    and device topology q3d_device_topology.png
    Args:
        None
    Return:
        qc: QuantumCircuit
    """
    qc = None
    ############################################################################
    # Student code begin
    ############################################################################
    
    
    qc = QuantumCircuit(5)
    edge_gates = q3d_edge_gates()
    qc.append(edge_gates['13'], [1, 3])
    qc.append(edge_gates['12'], [1, 2])
    qc.append(edge_gates['01'], [1, 0])
    
    ############################################################################
    # Student code end
    ############################################################################

    return qc


def q3d_device_qubit_read_mapping():
    """
    Your physical qubits (int) to logical qubits (int) mapping for information
    recovery
    Args:
        None
    Return:
        qubit_mapping: dict[int, int]
    """
    qubit_mapping = None
    ############################################################################
    # Student code begin
    ############################################################################
    
    
    qubit_mapping = {
        1: 0, 
        0: 1, 
        2: 2, 
        3: 3,  
        4: None  
    }
    
    ############################################################################
    # Student code end
    ############################################################################

    return qubit_mapping