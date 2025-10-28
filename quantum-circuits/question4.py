from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit, transpile
from qiskit.providers.basic_provider import BasicSimulator


def encoder(x: int=0, y: int=0, n=4):
    """
    An encoder to convert two n-bit nonnegative integers (uint) x and y to a 2n-qubit QuantumCircuit.
    This encoder will be used by autograder.
    """
    assert x >= 0 and x < 2**n and isinstance(n,int), f"Your input x must be an integer in the range [0,{(2**n)-1}]."
    assert y >= 0 and y < 2**n and isinstance(n,int), f"Your input y must be an integer in the range [0,{(2**n)-1}]."

    qc = QuantumCircuit(n*2)
    
    for i in range(n):
        if x >= 2**(n-i-1):
            qc.x(n-i-1)
            x -= 2**(n-i-1)

    for i in range(n):
        if y >= 2**(n-i-1):
            qc.x(2*n-i-1)
            y -= 2**(n-i-1)
    
    return qc
    

def decoder(qc: QuantumCircuit, n=4):
    """
    A decoder to convert a QuantumCircuit to an n-bit nonnegative integer from the simulation histogram
    by measuring the first n qubits in the quantum circuit.
    The result should be deterministic on a noise-free machine, hence shot=1 is used for simulation.
    This decoder will be used by autograder.
    """
    assert n >= 1
    assert isinstance(qc, QuantumCircuit)
    assert qc.num_qubits >= n

    n_qubits = qc.num_qubits
    n_clbits = max(n, qc.num_clbits)

    qr = QuantumRegister(n_qubits)
    cr = ClassicalRegister(n_clbits)
    qc_base = QuantumCircuit(qr, cr)
    qc = qc_base.compose(qc)

    simulator = BasicSimulator()
    qc.measure(list(range(n)), list(range(n)))
    cc = transpile(qc, simulator)
    job = simulator.run(cc, shots=1)
    result = list(job.result().get_counts(cc).keys())[0]

    z = 0
    for i in range(n):
        z += int(result[i])*2**(n-i-1)

    return z


def quantum_and():
    """
    An N-qubit quantum circuit which calculates the AND result of input1 on [q0] and input2 on [q1],
    The output will be measured on [q0].
    You need to decide the amount of additional qubits needed to implement the function.
    The function must be compatible with the provided encoder(n=1) and decoder(n=1).
    N must be either 2 or 3.
    Args: 
        None
    Return:
        qc: Your QuantumCircuit
    """

    qc = None
    ############################################################################
    # Student code begin
    ############################################################################

    qr, cr = QuantumRegister(3), ClassicalRegister(1)
    qc = QuantumCircuit(qr, cr)
    qc.ccx(qr[0], qr[1], qr[2])
    qc.reset(qr[0])
    qc.cx(qr[2], qr[0])
    qc.measure(qr[0], cr[0])

    ############################################################################
    # Student code end
    ############################################################################

    return qc


def quantum_or():
    """
    An N-qubit quantum circuit which calculates the OR result of input1 on [q0] and input2 on [q1],
    The output will be measured on [q0].
    You need to decide the amount of additional qubits needed to implement the function.
    The function must be compatible with the provided encoder(n=1) and decoder(n=1).
    N must be either 2 or 3.
    Args: 
        None
    Return:
        qc: Your QuantumCircuit
    """

    qc = None
    ############################################################################
    # Student code begin
    ############################################################################
    # 0 0 0, 0 1 1, 1 0 1, 1 1 1
    qr, cr = QuantumRegister(3), ClassicalRegister(1)
    qc = QuantumCircuit(qr, cr)
    qc.x(qr[0])
    qc.x(qr[1])
    qc.ccx(qr[0], qr[1], qr[2])
    qc.x(qr[2])
    qc.reset(qr[0])
    qc.cx(qr[2], qr[0])
    qc.measure(qr[0], cr[0])


   

    ############################################################################
    # Student code end
    ############################################################################

    return qc

def quantum_xor():
    """
    An N-qubit quantum circuit which calculates the XOR result of input1 on [q0] and input2 on [q1],
    The output will be measured on [q0].
    You need to decide the amount of additional qubits needed to implement the function.
    The function must be compatible with the provided encoder(n=1) and decoder(n=1).
    N must be either 2 or 3.
    Args: 
        None
    Return:
        qc: Your QuantumCircuit
    """

    qc = None
    ############################################################################
    # Student code begin
    ############################################################################

    qr, cr = QuantumRegister(2), ClassicalRegister(1)
    qc = QuantumCircuit(qr, cr)
    qc.cx(qr[0], qr[1])
    qc.reset(qr[0])
    qc.cx(qr[1], qr[0])
    qc.measure(qr[0], cr[0])


    ############################################################################
    # Student code end
    ############################################################################

    return qc


def quantum_adder():
    """
    An N-qubit quantum circuit which adds input1 on [q0,q1,q2,q3] and input2 on [q4,q5,q6,q7],
    The output will be measured on [q0,q1,q2,q3].
    You need to decide the amount of additional qubits needed to implement the function.
    The function must be compatible with the provided encoder(n=4) and decoder(n=4).
    N must satisfy the following constraint: 8 <= N <= 16.
    Args: 
        None
    Return:
        qc: Your QuantumCircuit
    """

    qc = None
    ############################################################################
    # Student code begin
    ############################################################################

    qr, cr = QuantumRegister(13), ClassicalRegister(4)
    qc = QuantumCircuit(qr, cr)
    # op 1
    qc.ccx(qr[0], qr[4], qr[9])
    qc.cx(qr[0], qr[4])
    qc.ccx(qr[4], qr[8], qr[9])
    qc.cx(qr[4], qr[8])
    qc.cx(qr[0], qr[4])
    # op 2
    qc.ccx(qr[1], qr[5], qr[10])
    qc.cx(qr[1], qr[5])
    qc.ccx(qr[5], qr[9], qr[10])
    qc.cx(qr[5], qr[9])
    qc.cx(qr[1], qr[5])
    # op 3
    qc.ccx(qr[2], qr[6], qr[11])
    qc.cx(qr[2], qr[6])
    qc.ccx(qr[6], qr[10], qr[11])
    qc.cx(qr[6], qr[10])
    qc.cx(qr[2], qr[6])
    # op 4
    qc.ccx(qr[3], qr[7], qr[12])
    qc.cx(qr[3], qr[7])
    qc.ccx(qr[7], qr[11], qr[12])
    qc.cx(qr[7], qr[11])
    qc.cx(qr[3], qr[7])

    # reset, move
    qc.reset(qr[0])
    qc.reset(qr[1])
    qc.reset(qr[2])
    qc.reset(qr[3])
    qc.cx(qr[8], qr[0])
    qc.cx(qr[9], qr[1])
    qc.cx(qr[10], qr[2])
    qc.cx(qr[11], qr[3])

    # measure
    qc.measure(qr[0], cr[0])
    qc.measure(qr[1], cr[1])
    qc.measure(qr[2], cr[2])
    qc.measure(qr[3], cr[3])
    ############################################################################
    # Student code end
    ############################################################################

    return qc


def encoder_signed(x: int=0, y: int=0, n=4):
    """
    An encoder to convert two n-bit integers x and y to a 2n-qubit QuantumCircuit.
    This encoder will be used by autograder.
    Args:
        x: int of input 1
        y: int of input 2
        n: int of input size
    Return:
        qc: your QuantumCircuit
    """
    assert x >= -2**(n-1) and x < 2**(n-1) and isinstance(n,int), f"Your input x must be an integer in the range [{-2**(n-1)},{2**(n-1)-1}]."
    assert y >= -2**(n-1) and y < 2**(n-1) and isinstance(n,int), f"Your input y must be an integer in the range [{-2**(n-1)},{2**(n-1)-1}]."

    qc = QuantumCircuit(n*2)
    ############################################################################
    # Student code begin
    ############################################################################
    if x < 0:
        x = 2**n + x  
    if y < 0:
        y = 2**n + y  
        
    for i in range(n):
        if x >= 2**(n-i-1):
            qc.x(n-i-1)
            x -= 2**(n-i-1)
    
    for i in range(n):
        if y >= 2**(n-i-1):
            qc.x(2*n-i-1)
            y -= 2**(n-i-1)

    ############################################################################
    # Student code end
    ############################################################################    
    
    return qc
    

def decoder_signed(qc: QuantumCircuit, n=4):
    """
    A decoder to convert a QuantumCircuit to an n-bit integer from the simulation histogram
    by measuring the first n qubits in the quantum circuit.
    The result should be deterministic on a noise-free machine, hence shot=1 is used for simulation.
    Args:
        qc: QuantumCircuit
        n: int of input size
    Return:
        z: int of your decode result
    """
    assert n >= 1
    assert isinstance(qc, QuantumCircuit)
    assert qc.num_qubits >= n

    n_qubits = qc.num_qubits
    n_clbits = max(n, qc.num_clbits)

    qr = QuantumRegister(n_qubits)
    cr = ClassicalRegister(n_clbits)
    qc_base = QuantumCircuit(qr, cr)
    qc = qc_base.compose(qc)

    simulator = BasicSimulator()
    qc.measure(list(range(n)), list(range(n)))
    cc = transpile(qc, simulator)
    job = simulator.run(cc, shots=1)
    result = list(job.result().get_counts(cc).keys())[0]

    z = 0
    ############################################################################
    # Student code begin
    ############################################################################
    for i in range(n):
        z += int(result[i]) * 2**(n-i-1)
    
    if int(result[0]) == 1:  
        z = z - 2**n
    ############################################################################
    # Student code end
    ############################################################################    
    
    return z


def test_your_implementation(x: int, y: int, n: int, quantum_calculation_circuit: QuantumCircuit=None, encoder_func=encoder, decoder_func=decoder):
    """
    Args:
        x: int of input uint x
        y: int of input uint y
        n: int of input size
        quantum_logic_circuit: QuantumCircuit of optional input of your quantum operation circuit function
    return:
        output: int of calculation result
    """
    assert isinstance(x, int)
    assert isinstance(y, int)
    assert isinstance(n, int) and n>=1
    assert quantum_calculation_circuit is None or isinstance(quantum_calculation_circuit, QuantumCircuit)

    if quantum_calculation_circuit is not None:
        n_qubits = max(2*n, len(quantum_calculation_circuit.qubits))
        n_clbits = max(n, len(quantum_calculation_circuit.clbits))
    else:
        n_qubits = 2*n
        n_clbits = n
    
    qr = QuantumRegister(n_qubits)
    cr = ClassicalRegister(n_clbits)
    qc = QuantumCircuit(qr, cr)

    qc = qc.compose(encoder_func(x, y, n))
    if quantum_calculation_circuit is not None:
        qc = qc.compose(quantum_calculation_circuit)
    return decoder_func(qc, n)
print(bin(2)[2:])