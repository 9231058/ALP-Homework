# In The Name of God
# =======================================
# [] File Name : karmarkar.py
#
# [] Creation Date : 17-01-2020
#
# [] Created By : Parham Alvani <parham.alvani@gmail.com>
# =======================================
import numpy as np

# min z = x1 + 3x2 - 3x3
# s.t.
# x2 - x3 = 0
# x1 + x2 + x3 = 1
# xi >= 0

c = np.array([1, 3, -3])
A = np.array([[0, 1, -1]])
current = np.array([1/3, 1/3, 1/3])
teta = 0.25


def transform(current):
    D = np.diag(current)
    Ap = np.matmul(A, D)
    cp = np.matmul(D, c.T)
    n = Ap.shape[1]
    P = np.append(Ap, np.ones((1, n)), axis=0)
    core = np.linalg.inv(np.matmul(P, P.T))
    d = np.matmul(np.identity(n) - np.matmul(np.matmul(P.T, core), P), cp)
    print(f'direction {d}')
    y = np.full((n), 1/n) - teta * d / (np.linalg.norm(d) * (n * (n - 1)) ** 0.5)
    print(f'y = {y}')
    r = np.matmul(D, y)
    return r / np.dot(np.ones(n), r)


if __name__ == '__main__':
    for _ in range(10):
        print(f'z = {np.dot(current, c)} for {current}')
        current = transform(current)
