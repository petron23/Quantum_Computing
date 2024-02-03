import pennylane as qml
import numpy as np


#1
dev = qml.device("default.qubit", wires=1)
U = np.array([[1, 1], [1, -1]]) / np.sqrt(2)

@qml.qnode(dev)
def varied_initial_state(state):
    """Complete the function such that we can apply the operation U to
    either |0> or |1> depending on the input argument flag.
    
    Args:
        state (int): Either 0 or 1. If 1, prepare the qubit in state |1>,
            otherwise, leave it in state 0.
  
    Returns:
        array[complex]: The state of the qubit after the operations.
    """
    
    if state == 1:
        qml.PauliX(wires=0)
        qml.QubitUnitary(U, wires=0)
    else:
        qml.QubitUnitary(U, wires=0)
    
    return qml.state()



#2
dev = qml.device("default.qubit", wires=1)

@qml.qnode(dev)
def apply_hadamard():    
    qml.Hadamard(wires=0)
    return qml.state()


#3
dev = qml.device("default.qubit", wires=1)

@qml.qnode(dev)
def apply_hadamard_to_state(state):
    """Complete the function such that we can apply the Hadamard to
    either |0> or |1> depending on the input argument flag.
    
    Args:
        state (int): Either 0 or 1. If 1, prepare the qubit in state |1>,
            otherwise, leave it in state 0.
    
    Returns:
        array[complex]: The state of the qubit after the operations.
    """
    U = np.array([[1, 1], [1, -1]]) / np.sqrt(2)

    if state == 1:
        qml.PauliX(wires=0)
        
    qml.Hadamard(wires=0)
    
    return qml.state()


#4

dev = qml.device("default.qubit", wires=1)
@qml.qnode(dev)
def apply_hxh(state):
 
    if state == 1:
        qml.PauliX(wires=0)
 
    qml.Hadamard(wires=0)
    qml.PauliX(wires=0)
    qml.Hadamard(wires=0)
    
    return qml.state()


