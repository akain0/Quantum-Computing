from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit, transpile
from qiskit.providers.basic_provider import BasicSimulator
import numpy as np
import matplotlib.pyplot as plt

pi = np.pi

def test():
    arr = np.matrix([-1/np.sqrt(8), 1/np.sqrt(8), 1/np.sqrt(8),1/np.sqrt(8),1/np.sqrt(8),1/np.sqrt(8),1/np.sqrt(8),1/np.sqrt(8)]).transpose()
    diffusion = np.matrix([[-3/4, 1/4, 1/4, 1/4, 1/4, 1/4, 1/4, 1/4],
                     [1/4, -3/4, 1/4, 1/4, 1/4, 1/4, 1/4, 1/4],
                     [1/4, 1/4, -3/4, 1/4, 1/4, 1/4, 1/4, 1/4],
                     [1/4, 1/4, 1/4, -3/4, 1/4, 1/4, 1/4, 1/4],
                     [1/4, 1/4, 1/4, 1/4, -3/4, 1/4, 1/4, 1/4],
                     [1/4, 1/4, 1/4, 1/4, 1/4, -3/4, 1/4, 1/4],
                     [1/4, 1/4, 1/4, 1/4, 1/4, 1/4, -3/4, 1/4],
                     [1/4, 1/4, 1/4, 1/4, 1/4, 1/4, 1/4, -3/4]])
    arr2 = np.matrix(np.matmul(diffusion, arr))
    arr3 = np.multiply(arr2, np.matrix([-1, 1, 1, 1, 1, 1, 1, 1]).transpose())
    print(arr3)
    arr4 = np.matrix(np.matmul(diffusion, arr3))
    print(arr4)
    print(np.linalg.norm(arr4))
    print(0.97227182**2)
test()

def test2():
    qr = QuantumRegister(3)
    cr = ClassicalRegister(3)
    qc = QuantumCircuit(qr, cr)
    qc.h(qr[0])
    qc.cx(qr[0], qr[1])
    qc.cx(qr[0], qr[2])
    qc.barrier()
    qc.z(qr[0])
    qc.x(qr[1])
    qc.barrier()
    qc.cx(qr[2], qr[0])
    qc.cx(qr[2], qr[1])
    qc.h(qr[2])
    qc.swap(qr[0], qr[2])
    qc.measure(qr, cr)
    simulator = BasicSimulator()
    results = simulator.run(qc, n_counts = 1024).result()
    counts=results.get_counts()
    print(counts)
test2()
def q2a():
    """
    Calculate the probability of finding the target state based on the instruction
    Args: 
        None
    Return:
        p: your float of probability
    """

    p = -1

    ############################################################################
    # Student code begin
    ############################################################################
    n_counts = 1024
    qr = QuantumRegister(4, 'q')
    cr = ClassicalRegister(4, 'c')
    
    '''
    qc.h(0)
    qc.h(1)
    qc.h(2)
    qc.h(3)
    qc.id(0)
    qc.x(1)
    qc.y(2)
    qc.z(3)
    '''

    circuit = QuantumCircuit(qr, cr)
    circuit.h(qr[0])
    circuit.h(qr[1])
    circuit.h(qr[2])
    circuit.h(qr[3])
    circuit.id(qr[0])
    circuit.x(qr[1])
    circuit.y(qr[2])
    circuit.z(qr[3])
    circuit.measure(qr, cr)

    simulator = BasicSimulator()
    job = simulator.run(circuit, counts = n_counts)
    counts = job.result().get_counts()
    p = counts['1010']/n_counts
    
    ############################################################################
    # Student code end
    ############################################################################

    return p


def q2b():
    """
    Calculate the probability of finding the target state based on the instruction
    Args: 
        None
    Return:
        p: your float of probability
    """
    
    p = -1
    n_counts = 1024
    ############################################################################
    # Student code begin
    ############################################################################
    qr = QuantumRegister(3, 'q')
    cr = ClassicalRegister(3, 'c')
    qc = QuantumCircuit(qr, cr)
    qc.h(qr[0])
    qc.cx(qr[0], qr[1])
    qc.cx(qr[1],qr[2])
    qc.measure(qr, cr)

    simulator = BasicSimulator()
    sim = simulator.run(qc, counts = n_counts)
    counts = sim.result().get_counts()

    query_counts = 0
    for key, value in counts.items():
        if str(key[0]) == "1":
            query_counts+=value
    print(counts)
    print(query_counts)
    p=query_counts/n_counts
    ############################################################################
    # Student code end
    ############################################################################

    return p


def q2c():
    """
    Calculate the probability of finding the target state based on the instruction
    Args: 
        None
    Return:
        p: your float of probability
    """

    p = -1

    ############################################################################
    # Student code begin
    ############################################################################
    n_counts = 1024
    qr = QuantumRegister(6)
    cr = ClassicalRegister(6)
    qc = QuantumCircuit(qr, cr)

    qc.x(qr[5])
    qc.h(qr[0])
    qc.h(qr[1])
    qc.h(qr[2])
    qc.h(qr[3])
    qc.h(qr[4])
    qc.h(qr[5])
    qc.cx(qr[0], qr[5])
    qc.cx(qr[1], qr[5])
    qc.cx(qr[2], qr[5])
    qc.h(qr[0])
    qc.h(qr[1])
    qc.h(qr[2])
    qc.h(qr[3])
    qc.h(qr[4])
    qc.h(qr[5])

    qc.measure(qr, cr)

    simulator = BasicSimulator()
    sim = simulator.run(qc, counts = n_counts)
    counts = sim.result().get_counts()
    query_counts = 0
    for key, value in counts.items():
        if str(key[:3]) == "010":
            query_counts+=value
    print(counts)
    print(query_counts)
    p = query_counts/n_counts
    ############################################################################
    # Student code end
    ############################################################################

    return p


def q2d():
    """
    Calculate the probability of finding the target state based on the instruction
    Args: 
        None
    Return:
        p: your float of probability
    """

    p = -1

    ############################################################################
    # Student code begin
    ############################################################################
    n_counts = 1024
    qr = QuantumRegister(2)
    cr = ClassicalRegister(2)
    qc = QuantumCircuit(qr, cr)
    qc.u(pi/2, pi/4, -pi, qr[1])
    qc.cx(qr[1],qr[0])
    qc.u(0, 0, -pi/4, qr[0])
    qc.cx(qr[1],qr[0])
    qc.u(pi/2, 0, -3*pi/4, qr[0])
    qc.swap(qr[0],qr[1])
    qc.measure(qr, cr)

    simulator = BasicSimulator()
    sim = simulator.run(qc, counts = n_counts)
    counts = sim.result().get_counts()
    
    query_counts = 0
    for key, value in counts.items():
        if str(key[0]) == "0" or str(key[0]) == "1":
            query_counts += value
    print(counts)
    print(query_counts)
    p = query_counts/n_counts
    ############################################################################
    # Student code end
    ############################s################################################

    return p

