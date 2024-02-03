import pennylane as qml
import numpy as np

#1
dev = qml.device("default.qubit", wires=1)
@qml.qnode(dev)
def apply_z_to_plus():
    """Write a circuit that applies PauliZ to the |+> state and returns
    the state.

    Returns:
        array[complex]: The state of the qubit after the operations.
    """
    qml.Hadamard(wires=0)
    qml.PauliZ(wires=0)
    
    return qml.state()


#2
dev = qml.device("default.qubit", wires=1)
@qml.qnode(dev)
def fake_z():
    """Use RZ to produce the same action as Pauli Z on the |+> state.

    Returns:
        array[complex]: The state of the qubit after the operations.
    """
    qml.Hadamard(wires=0)
    qml.RZ(3.14159265359, wires=0)
    
    return qml.state()


#3
@qml.qnode(dev)
def many_rotations():
    """Implement the circuit depicted above and return the quantum state.

    Returns:
        array[complex]: The state of the qubit after the operations.
    """
    qml.Hadamard(wires=0)
    qml.S(wires=0)
    qml.adjoint(qml.T(wires=0))
    qml.RZ(.3,wires=0)
    qml.adjoint(qml.S(wires=0))
    
    
    return qml.state()


#4
dev = qml.device('default.qubit', wires=3)
@qml.qnode(dev)
def just_enough_ts():
    """Implement an equivalent circuit as the above with the minimum number of 
    T and T^\dagger gates required.

    Returns:
        array[float]: The measurement outcome probabilities.
    """
    qml.Hadamard(wires=0)
    qml.Hadamard(wires=1)
    qml.Hadamard(wires=2)
    
    qml.S(wires=0)
    qml.T(wires=1)
    qml.adjoint(qml.T(wires=2))
    
    qml.Hadamard(wires=0)
    qml.Hadamard(wires=1)
    qml.Hadamard(wires=2)
    
    qml.adjoint(qml.S(wires=0))
    qml.S(wires=1)
    qml.adjoint(qml.S(wires=2))
    
    qml.S(wires=1)
    qml.adjoint(qml.T(wires=2))
    
    
    qml.Hadamard(wires=0)
    qml.Hadamard(wires=1)
    qml.Hadamard(wires=2)

    return qml.probs(wires=[0, 1, 2])


# FILL IN THE CORRECT VALUES FOR THE ORIGINAL CIRCUIT
#original_depth = 8
#original_t_count = 13
#original_t_depth = 6

# FILL IN THE CORRECT VALUES FOR THE NEW, OPTIMIZED CIRCUIT
#optimal_depth = 6
#optimal_t_count = 3
#optimal_t_depth = 2

#4