
import numpy as np
import numpy.typing as npt
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.providers.basic_provider import BasicSimulator

class QuantumAgent(object):
    def __init__(self):
        self.backend = BasicSimulator()


    def generate_basis(self, n):
        """
        Creates a randomly chosen basis of size n for the agent to use
        0 for Computational basis (X)
        1 for Hadamard basis (Z)
        Save the basis using variable self.basis
        Args:
            n: int
        Return:
            None
        """

        self.basis = None
        ############################################################################
        # Student code begin
        ############################################################################
        self.basis = np.random.randint(2, size = n)
        ############################################################################
        # Student code end
        ############################################################################


    def encode_message(self, message):
        """
        Creates an array of single-qubit quantum circuits according to the message
        Args:
            message: list[int]
        Return:
            None
        """
        n = len(message)
        self.qubits = []
        self.generate_basis(n=n)
        for i in range(n):
            qc = QuantumCircuit(1)
            s = message[i]
            b = self.basis[i]
            ############################################################################
            # Student code begin
            ############################################################################
            if s == 1:
                qc.x(0)
            if b == 1:
                qc.h(0)

            ############################################################################
            # Student code end
            ############################################################################
            self.qubits.append(qc)


    def decode_qubits(self, qubits):
        """
        Decode the classical message using the input n qubits using a randomly chosen basis of size n
        Args:
            qubits: list[QuantumCircuit]
        return:
            None
        """
        n=len(qubits)
        self.recovered_message = np.zeros(n).astype(np.int8)
        self.generate_basis(n=n)
        for i in range(n):
            qc = QuantumCircuit(1,1)
            qc = qc.compose(qubits[i])
            b = self.basis[i]

            ############################################################################
            # Student code begin
            ############################################################################

            if b == 1:
                qc.h(0)

            ############################################################################
            # Student code end
            ############################################################################
            qc.measure(0,0)
            result = self.backend.run(run_input=qc, shots=1).result()
            self.recovered_message[i] += int(list(result.get_counts().keys())[0])
            

def bb84(message: npt.ArrayLike, alice: QuantumAgent, bob: QuantumAgent, eve: QuantumAgent=None):

    n = len(message)

    alice.encode_message(message=message)
    if eve is None:
        bob.decode_qubits(alice.qubits)
    else:
        eve.decode_qubits(alice.qubits)
        eve.encode_message(eve.recovered_message)
        bob.decode_qubits(eve.qubits)

    I_mask = alice.basis==bob.basis

    if len(I_mask) < np.floor(n/2):
        return False
    else:
        pass

    restricted_original_message = message[I_mask]
    restricted_recovered_message = bob.recovered_message[I_mask]

    U_mask = restricted_original_message==restricted_recovered_message

    return (np.sum(U_mask) >= np.floor(np.sum(I_mask)/2))

