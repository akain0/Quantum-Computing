from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit, transpile


def deutsch_f1_oracle():
    '''
    Implement the ORACLE of Deutsch algorithm for the following function:
    f(0) = 0, f(1) = 0
    Args: 
        None
    Return:
        qcirc: QuantumCircuit of your implementation of the ORACLE of Deutsch algorithm for function f
    '''

    qcirc = None
    ############################################################################
    # Student code begin
    ############################################################################

    qcirc = QuantumCircuit(2)

    ############################################################################
    # Student code end
    ############################################################################

    return qcirc


def deutsch_f2_oracle():
    '''
    Implement the ORACLE of Deutsch algorithm for the following function:
    f(0) = 1, f(1) = 0
    Args: 
        None
    Return:
        qcirc: QuantumCircuit of your implementation of the ORACLE of Deutsch algorithm for function f
    '''

    qcirc = None
    ############################################################################
    # Student code begin
    ############################################################################

    qcirc = QuantumCircuit(2)
    qcirc.x(1)
    qcirc.cx(0,1)
    


    ############################################################################
    # Student code end
    ############################################################################

    return qcirc


def deutsch_f3_oracle():
    '''
    Implement the ORACLE of Deutsch algorithm for the following function:
    f(0) = 0, f(1) = 1
    Args: 
        None
    Return:
        qcirc: QuantumCircuit of your implementation of the ORACLE of Deutsch algorithm for function f
    '''

    qcirc = None
    ############################################################################
    # Student code begin
    ############################################################################

    qcirc = QuantumCircuit(2)
    qcirc.cx(0, 1)

    ############################################################################
    # Student code end
    ############################################################################

    return qcirc


def deutsch_f4_oracle():
    '''
    Implement the ORACLE of Deutsch algorithm for the following function:
    f(0) = 1, f(1) = 1
    Args: 
        None
    Return:
        qcirc: QuantumCircuit of your implementation of the ORACLE of Deutsch algorithm for function f
    '''
   
    qcirc = None
    ############################################################################
    # Student code begin
    ############################################################################

    qcirc = QuantumCircuit(2)
    qcirc.x(1)
    

    ############################################################################
    # Student code end
    ############################################################################

    return qcirc


def deutsch_jozsa_oracle():
    '''
    Given g(x) where
        g(x) = 0 if x is even
        g(x) = 1 if x is odd
    Implement the ORACLE of Deutsch-Jozsa algorithm for function g(x)
    Args: 
        None
    Return:
        qcirc: QuantumCircuit of your implementation of the ORACLE of Deutsch-Jozsa algorithm circuit for g(x)
    '''

    qcirc = None
    ############################################################################
    # Student code begin
    ############################################################################

    qcirc = QuantumCircuit(5)
    qcirc.cx(0,4)
    


    ############################################################################
    # Student code end
    ############################################################################

    return qcirc
