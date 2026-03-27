import numpy as np


A = np.array([
    [-1, 1, 1, 1],
    [2, 1, 2, 3],
    [3, 2, 1, 2],
    [4, 3, 2, 1]
], dtype=float)

B = np.array([4, 1, 1, -5], dtype=float)
n = len(B)


def cramer(A, B):
    det_A = np.linalg.det(A)
    if det_A == 0:
        return "Система вироджена"
    X = []
    for i in range(n):
        Ai = A.copy()
        Ai[:, i] = B
        X.append(np.linalg.det(Ai) / det_A)
    return X


def gaussian_elimination(A, B):
    A = A.copy()
    B = B.copy()

    for i in range(n):
        max_row = np.argmax(abs(A[i:, i])) + i
        A[[i, max_row]] = A[[max_row, i]]
        B[[i, max_row]] = B[[max_row, i]]

        for j in range(i + 1, n):
            factor = A[j, i] / A[i, i]
            A[j, i:] -= factor * A[i, i:]
            B[j] -= factor * B[i]

    X = np.zeros(n)
    for i in range(n - 1, -1, -1):
        X[i] = (B[i] - np.dot(A[i, i + 1:], X[i + 1:])) / A[i, i]
    return X


def gauss_jordan(A, B):
    A = A.copy()
    B = B.copy()

    for i in range(n):
        B[i] /= A[i, i]
        A[i] = A[i] / A[i, i]
        for j in range(n):
            if j != i:
                factor = A[j, i]
                A[j] -= factor * A[i]
                B[j] -= factor * B[i]
    return B


def inverse_matrix_method(A, B):
    inv_A = np.linalg.inv(A)
    return np.dot(inv_A, B)


print("Метод Крамера:", np.round(cramer(A, B), 4))
print("Метод Гауса:", np.round(gaussian_elimination(A, B), 4))
print("Метод Жордано-Гауса:", np.round(gauss_jordan(A, B), 4))
print("Метод оберненої матриці:", np.round(inverse_matrix_method(A, B), 4))