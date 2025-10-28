# Quantum Computing Assignments

This repository contains implementations for various quantum computing problems organized into different modules. The codebase uses Qiskit for quantum circuit construction and simulation.

## Project Structure

```
quantum-algos/           # Quantum algorithms implementations
quantum-circuits/        # Basic quantum circuit constructions
quantum-error-correction/ # Error correction protocols
qubit-allocation-routing/ # Quantum circuit compilation and routing
```

## Modules Overview

### Quantum Algorithms (quantum-algos/)

- **`question1.py`**: Super Dense Coding protocol implementation
- **`question2.py`**: Deutsch and Deutsch-Jozsa algorithms
- **`question3.py`**: Bernstein-Vazirani algorithm (ideal and noisy)
- **`question4.py`**: Simon's algorithm
- **`question5.py`**: Grover's search algorithm
- **`question6.py`**: Quantum state preparation circuits

### Quantum Circuits (quantum-circuits/)

- **`question1.py`**: Basic quantum circuit constructions
- **`question2.py`**: Quantum probability calculations
- **`question3.py`**: BB84 quantum key distribution protocol
- **`question4.py`**: Quantum logic gates and arithmetic operations

### Quantum Error Correction (quantum-error-correction/)

- **`question1.py`**: Bit-flip error correction codes
- **`question2.py`**: Phase-flip error correction codes
- **`question3.py`**: QAOA (Quantum Approximate Optimization Algorithm) for Max-Cut

### Qubit Allocation and Routing (qubit-allocation-routing/)

- **`question1.py`**: Circuit decomposition with different basis gates
- **`question2.py`**: Coupling map analysis and SWAP insertion
- **`question3.py`**: Device-specific circuit compilation with noise models
- **`utils.py`**: Utility functions for benchmark circuits and qubit mapping

## Key Features

### Algorithms Implemented
- **Super Dense Coding**: Quantum communication protocol for transmitting classical information
- **Deutsch-Jozsa**: Quantum algorithm for determining function properties
- **Bernstein-Vazirani**: Hidden string problem solver
- **Simon's Algorithm**: Period finding algorithm
- **Grover's Search**: Quantum search algorithm
- **BB84 Protocol**: Quantum key distribution

### Error Correction
- Bit-flip and phase-flip quantum error correction codes
- Support for single and double error correction
- QAOA implementation for combinatorial optimization

### Circuit Compilation
- Quantum circuit transpilation to different basis gate sets
- Coupling map optimization for various device topologies
- SWAP gate insertion analysis
- Noise-aware circuit compilation

### Utilities
- Benchmark circuit loader from QASM files
- Physical to logical qubit mapping
- Encoder/decoder functions for quantum arithmetic

## Dependencies

- **Qiskit**: Quantum computing framework
- **NumPy**: Numerical computations
- **NetworkX**: Graph operations (for QAOA)
- **Matplotlib**: Plotting utilities

## Usage Examples

### Running Grover's Algorithm
```python
from quantum_algos.question5 import grover, post_processing

# Create Grover circuit with 3 iterations
grover_circuit = grover(3)
probability = post_processing(grover_circuit)
```

### Super Dense Coding
```python
from quantum_algos.question1 import qubit_preparation, qubit_encoding, qubit_decoding

# Prepare entangled qubits
prepared = qubit_preparation(4)
# Encode classical information
encoded = qubit_encoding(prepared, "1101")
# Decode the information
decoded = qubit_decoding(encoded, 4)
```

### Circuit Compilation Analysis
```python
from qubit_allocation_routing.question2 import average_depth_change, average_nswap_change

# Analyze circuit depth changes across different coupling maps
depth_changes = average_depth_change()
swap_counts = average_nswap_change()
```

## Benchmark Circuits

The repository includes quantum benchmark circuits in QASM format:
- **`BV-10.qasm`**, **`BV-15.qasm`**: Bernstein-Vazirani circuits
- **`qaoa10_depth2.qasm`**: QAOA circuit
- **`QV9.qasm`**: Quantum Volume circuit

These are used for testing compilation and routing algorithms across different device topologies.

## Installation

1. Install Qiskit and dependencies:
```bash
pip install qiskit numpy networkx matplotlib
```

2. Clone this repository:
```bash
git clone <repository-url>
cd quantum-computing
```

3. Run individual modules:
```bash
python quantum-algos/question1.py
```

## License

This project is part of academic coursework for quantum computing studies.