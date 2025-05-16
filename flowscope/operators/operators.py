import numpy as np
from base import LazyMatrixOperator


def U_const(domain_size, c):
    """U(x ← c): All states map to constant c"""
    mat = np.zeros((domain_size, domain_size))
    mat[:, c] = 1
    return LazyMatrixOperator(mat)


def U_increment(domain_size):
    """U(x ← x + 1 mod domain)"""
    mat = np.zeros((domain_size, domain_size))
    for i in range(domain_size):
        mat[i, (i + 1) % domain_size] = 1
    return LazyMatrixOperator(mat)


def U_random(domain_size, values):
    """U(x ?= {a,b,...}): Uniformly random assignment"""
    mat = np.zeros((domain_size, domain_size))
    p = 1 / len(values)
    for v in values:
        mat[:, v] += p
    return LazyMatrixOperator(mat)


def P_pred(domain_size, predicate):
    """P(predicate): Projection matrix from predicate on index"""
    mat = np.zeros((domain_size, domain_size))
    for i in range(domain_size):
        if predicate(i):
            mat[i, i] = 1
    return LazyMatrixOperator(mat)


def E(from_label, to_label, num_labels):
    """E(ℓ₁, ℓ₂): Transfer control from ℓ₁ to ℓ₂"""
    mat = np.zeros((num_labels - 1, num_labels - 1))
    mat[from_label - 1, to_label - 1] = 1
    return LazyMatrixOperator(mat)
