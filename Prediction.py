import numpy as np

def sigmoid(z):
    return 1 / (1 + np.exp(-z))

def predict(Theta1, Theta2, X):
    m = X.shape[0]
    
    X = np.insert(X, 0, 1, axis=1)  # Shape: (m, 785)

    # Forward propagation
    z2 = np.dot(X, Theta1.T)  
    a2 = sigmoid(z2)

    a2 = np.insert(a2, 0, 1, axis=1)  # Shape: (m, 101)

    z3 = np.dot(a2, Theta2.T)
    a3 = sigmoid(z3)  # Output layer

    return np.argmax(a3, axis=1)  #predicted digit

