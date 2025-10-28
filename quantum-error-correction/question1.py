from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit, transpile
from qiskit.providers.basic_provider import BasicSimulator


def encoder():
    """
    Your implementation of bit-flip QEC encoder that works for both 1 bit-flip error and 2 bit-flip errors
    Args:
        None
    Return:
        QuantumCircuit
    """

    qc = QuantumCircuit(3)
    ############################################################################
    # Student code begin
    ############################################################################
    qc.cx(0,1)
    qc.cx(0,2)
    
    ############################################################################
    # Student code end
    ############################################################################

    return qc

def decoder1():
    """
    Your implementation of bit-flip QEC decoder that works for 1 bit-flip error
    Args:
        None
    Return:
        QuantumCircuit
    """
    
    qc = None
    ############################################################################
    # Student code begin
    ############################################################################
    qr = QuantumRegister(5)
    cr = ClassicalRegister(2)
    qc = QuantumCircuit(qr, cr)
    qc.cx(qr[0], qr[3]) 
    qc.cx(qr[1], qr[3])
    qc.cx(qr[1], qr[4]) 
    qc.cx(qr[2], qr[4])
    qc.measure(qr[3], cr[0])
    qc.measure(qr[4], cr[1]) 

    qc.x(qr[0]).c_if(cr, 1)  
    qc.x(qr[2]).c_if(cr, 2) 
    qc.x(qr[1]).c_if(cr, 3)  

    qc.cx(qr[0], qr[2])  
    qc.cx(qr[0], qr[1])
    
    ############################################################################
    # Student code end
    ############################################################################
    return qc

def decoder2():
    """
    Your implementation of bit-flip QEC decoder that works for 2 bit-flip errors
    Args:
        None
    Return:
        QuantumCircuit
    """

    qc = None
    ############################################################################
    # Student code begin
    ############################################################################
    qr = QuantumRegister(5)
    cr = ClassicalRegister(2)
    qc = QuantumCircuit(qr, cr)
    qc.cx(qr[0], qr[3]) 
    qc.cx(qr[1], qr[3])
    qc.cx(qr[1], qr[4]) 
    qc.cx(qr[2], qr[4])
    qc.measure(qr[3], cr[0])
    qc.measure(qr[4], cr[1]) 

    qc.x(qr[1]).c_if(cr, 1)   
    qc.x(qr[2]).c_if(cr, 1)
    qc.x(qr[0]).c_if(cr, 2)
    qc.x(qr[1]).c_if(cr, 2)
    
    qc.x(qr[0]).c_if(cr, 3)
    qc.x(qr[2]).c_if(cr, 3)
    
    qc.cx(qr[0], qr[2])
    qc.cx(qr[0], qr[1])
    
    
    ############################################################################
    # Student code end
    ############################################################################

    return qc
