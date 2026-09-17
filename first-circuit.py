import pennylane as qml
from pennylane import numpy as np

# A "device" is what actually runs the circuit -- here, a classical simulator of 1 qubit.
dev = qml.device("default.qubit", wires=1)

@qml.qnode(dev)
def circuit(angle):
    # Start in state |0>. RY rotates the qubit by `angle` radians around the Y axis.
    qml.RY(angle, wires=0)
    # Measure the expectation value of the Z operator.
    # This returns a number in [-1, 1]: -1 means "always measured 0", +1 means "always measured 1".
    return qml.expval(qml.PauliZ(0))

# Try a few angles and see how the measurement changes
for angle in [0, np.pi / 4, np.pi / 2, np.pi]:
    result = circuit(angle)
    print(f"angle = {angle:.3f} rad  ->  <Z> = {result:.3f}")

print("\nCircuit diagram:")
print(qml.draw(circuit)(np.pi / 2))