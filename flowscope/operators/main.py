import scipy.sparse as sp
import pandas as pd
from operators import U_const, P_pred, E, LazyMatrixOperator

# Domain: x ∈ {0,1}
U0 = U_const(2, 0)
U1 = U_const(2, 1)
P0 = P_pred(2, lambda x: x == 0)
Pn0 = P_pred(2, lambda x: x != 0)

# Label space: 5 labels
E12 = E(1, 2, 5)
E13 = E(1, 3, 5)
E24 = E(2, 4, 5)
E34 = E(3, 4, 5)
E44 = E(4, 4, 5)

# Identity operator on variable domain
I2 = LazyMatrixOperator(sp.eye(2))

# Compose LOS transition matrix
T = (
    (P0 @ E12).as_matrix() +
    (Pn0 @ E13).as_matrix() +
    (U0 @ E24).as_matrix() +
    (U1 @ E34).as_matrix() +
    (I2 @ E44).as_matrix()
)


# print(P0)
# print(E12)
# print((P0 @ E12))
# print((Pn0 @ E13).as_matrix())
# print((U0 @ E24).as_matrix())

# Optional: visualize or use T
df = pd.DataFrame(T.todense())
print(df)
