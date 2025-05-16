import numpy as np
import scipy.sparse as sp
from scipy.sparse.linalg import LinearOperator as ScipyLinearOperator


# === Base LOS Operator ===
class LOSOperator(ScipyLinearOperator):
    def __init__(self, shape, dtype=np.float64):
        super().__init__(dtype=dtype, shape=shape)

    def __matmul__(self, other):
        return TensorProductOperator(self, other)


# === Wrapper for lazy matrix operator ===
class LazyMatrixOperator(LOSOperator):
    def __init__(self, matrix):
        self._matrix = sp.csr_matrix(matrix)
        shape = self._matrix.shape
        super().__init__(shape)

    def __str__(self):
        return str(self._matrix.todense())

    def _matvec(self, v):
        return self._matrix @ v

    def as_matrix(self):
        return self._matrix


# === Tensor product operator ===
class TensorProductOperator(LOSOperator):
    def __init__(self, A: LOSOperator, B: LOSOperator):
        self.A = A
        self.B = B
        shape = (A.shape[0] * B.shape[0], A.shape[1] * B.shape[1])
        super().__init__(shape)

    def __str__(self):
        return str(self.as_matrix().todense())

    def _matvec(self, v):
        kron = sp.kron(self.A.as_matrix(), self.B.as_matrix())
        return kron @ v

    def as_matrix(self):
        return sp.kron(self.A.as_matrix(), self.B.as_matrix())
