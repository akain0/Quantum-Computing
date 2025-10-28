from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit, transpile
from qiskit.providers.basic_provider import BasicSimulator
import math 
def qubit_preparation(n):
    """
    Prepare enough qubits based on the length of the information to be sent.
    Args:
        n: int of length of classical_information
    Return:
        qcirc: QuantumCircuit of prepared qubits
    """

    qcirc = None
    ############################################################################
    # Student code begin
    ############################################################################
    num_pairs = math.ceil(n / 2)
    total_qubits = 2 * num_pairs
    qcirc = QuantumCircuit(total_qubits)
    
    for i in range(num_pairs):
        alice_qubit = i 
        bob_qubit = i + num_pairs  
        
        qcirc.h(alice_qubit)
        qcirc.cx(alice_qubit, bob_qubit)
    
    qcirc.barrier()
    ############################################################################
    # Student code end
    ############################################################################

    return qcirc


def qubit_encoding(prepared_qubits, classical_information):
    """
    Based on the Super Dense Coding principle, Alice can only use the first ceil(n/2) qubits of the prepared qubits.
    Args:
        prepared_qubits: QuantumCircuit of prepared qubits
        classical_information: str
    Return:
        qcirc: QuantumCircuit of encoded qubits
    """

    qcirc = None
    ############################################################################
    # Student code begin
    ############################################################################
    qcirc = prepared_qubits.copy()
    for i in range(0, len(classical_information), 2):
        alice_qubit = i//2
        if i + 1 < len(classical_information):
            string = classical_information[i:i+2]
        else:
            string = classical_information[i] + '0'
        
        if string == '01':
            qcirc.x(alice_qubit)
        elif string == '10':
            qcirc.z(alice_qubit)
        elif string == '11':
            qcirc.z(alice_qubit)
            qcirc.x(alice_qubit)


    ############################################################################
    # Student code end
    ############################################################################

    return qcirc

def qubit_decoding(encoded_qubits, n):
    """
    Bob restores the classical information using the encoded qubits 
    Args:
        encoded_qubits: QuantumCircuit of encoded qubits
        n: int of length of classical_information
    Return:
        restored_information: str
    """

    restored_information = ""
    ############################################################################
    # Student code begin
    ############################################################################

    qcirc = encoded_qubits.copy()
    num_pairs = math.ceil(n / 2)
    total_qubits = qcirc.num_qubits
    
    creg = ClassicalRegister(total_qubits)
    qcirc.add_register(creg)
    
    for i in range(num_pairs):
        alice_qubit = i
        bob_qubit = i + num_pairs
        
        qcirc.cx(alice_qubit, bob_qubit)
        qcirc.h(alice_qubit)
        
        qcirc.measure(alice_qubit, creg[alice_qubit])
        qcirc.measure(bob_qubit, creg[bob_qubit])
    
    sim = BasicSimulator()
    result = sim.run(qcirc, shots=1024).result()
    counts = result.get_counts()
    
    most_frequent = max(counts.keys(), key=lambda x: counts[x])
    
    restored_information = ""
    for pair_idx in range(num_pairs):
        alice_qubit = pair_idx
        bob_qubit = pair_idx + num_pairs
        
        alice_bit = most_frequent[-(alice_qubit + 1)]
        bob_bit = most_frequent[-(bob_qubit + 1)]
        
        restored_information += alice_bit + bob_bit
    
    ############################################################################
    # Student code end
    ############################################################################

    return restored_information[:n]  

