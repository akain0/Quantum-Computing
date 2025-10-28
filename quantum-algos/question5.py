from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit, transpile
from qiskit.providers.basic_provider import BasicSimulator

def grover(n: int):
    '''
    This function output Grover's algorithm circuit for a specific target. 
    Implement the circuit for applying Rotation phase + Inversion around the mean n times,
    where n is a positive integer.
    Args: 
        n: int of the number of times to apply (rotation + inversion)
    Return:
        qcirc: QuantumCircuit of your implementation of Grover's algorithm
    '''
    qcirc = None

    ############################################################################
    # Student code begin
    ############################################################################
    q = 3
    qcirc = QuantumCircuit(q)

    for i in range(q):
        qcirc.h(i)

    for i in range(n):
        # rotate
        qcirc.x(0)
        qcirc.h(2)
        qcirc.ccx(0,1,2)
        qcirc.h(2)
        qcirc.x(0)

        # invert around mean
        for j in range(q):
            qcirc.h(j)

        for k in range(q):
            qcirc.x(k)

        qcirc.h(2)
        qcirc.ccx(0,1,2)
        qcirc.h(2)

        for k in range(q):
            qcirc.x(k)

        for j in range(q):
            qcirc.h(j)
    


    ############################################################################
    # Student code end
    ############################################################################

    return qcirc


def target_state():
    """
    What is the target state found by the Grover's circuit?
    Args:
        None
    Return:
        s: str of the target state
    """

    s = ""
    ############################################################################
    # Student code begin
    ############################################################################

    s = "110"

    ############################################################################
    # Student code end
    ############################################################################

    return s


def post_processing(grover_qcirc):
    '''
    Args:
        grover_qcirc: QuantumCircuit returned by your grover function with input n
    Return:
        prob: float of the probability of finding the target state by running grover's algorithm n times
    '''
    n_counts = 1024
    prob = None
    ############################################################################
    # Student code begin
    ############################################################################
    grover_qcirc.measure_all()
    sim = BasicSimulator()
    res = sim.run(grover_qcirc, counts = n_counts).result()
    counts = res.get_counts()
    print(counts)
    target = target_state()
    val = counts[target]
    prob = float(val/n_counts)

    ############################################################################
    # Student code end
    ############################################################################

    return prob

#post_processing(grover(3))