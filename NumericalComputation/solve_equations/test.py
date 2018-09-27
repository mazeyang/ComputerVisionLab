#!/usr/bin/python3
from homework_2.solve_equations import EquationsSolver
import numpy as np


def main():
    dim = 100
    A = np.zeros((dim, dim), dtype='f8')
    for i in range(dim):
        for j in range(dim):
            if i == j:
                A[i, j] = 2
            elif np.abs(i - j) == 1:
                A[i, j] = -1
    b = np.ones((dim, 1), dtype='f8')

    # compare the answers (Gauss, Jacobi, Gauss_Seidel and SOR method)

    xg = EquationsSolver.solve(A, b, method='gauss')
    xj = EquationsSolver.solve(A, b, method='jacobi')
    xgs = EquationsSolver.solve(A, b, method='gauss_seidel')
    xt = EquationsSolver.solve(A, b, method='sor')
    for i in range(dim):
        print('%4d: [gauss: %8.2f]\t[jacobi: %8.2f]\t[gauss_seidel: %8.2f]\t[sor: %8.2f]\t'
              % (i+1, xg[i, 0], xj[i, 0], xgs[i, 0], xt[i, 0]))
    #
    # times = 19
    # w = 1.75
    # for i in range(times):
    #     print('omega: ', w)
    #     x = EquationsSolver.solve(A, b, method='sor', omega=w)
    #     w += 0.0125
    #     # for i in range(dim):
    #     #     print(x[i, 0], ' ', xt[i, 0])

    # Here is other data to test the top four methods

    # A = np.random.randint(0, 10, (dim, dim)) + np.eye(dim)
    # x = np.arange(1, dim + 1).reshape((dim, 1))
    # b = A.dot(x)
    # x = EquationsSolver.solve(A, b, method='Gauss')
    # x = EquationsSolver.solve(A, b, method='LU')

    # A, x, b = model.generate_data()

    # LU data 1
    # A = np.array([[2, 1, 5], [4, 1, 12], [-2, -4, 5]], dtype='f8')
    # x = np.array([[1], [-1], [2]], dtype='f8')
    # b = np.array([[11], [27], [12]], dtype='f8')

    # chase data 1
    # A = np.array([[2, 1, 0, 0], [1/2, 2, 1/2, 0], [0, 1/2, 2, 1/2], [0, 0, 1, 2]])
    # x = np.array([[-13/45], [7/90], [-1/45], [1/90]])
    # b = np.array([[-1/2], [0], [0], [0]])

    # chase data 2
    # A = np.array([[3, 1, 0, 0], [1, 4, 1, 0], [0, 2, 5, 2], [0, 0, 2, 6]])
    # x = np.array([[1], [3], [-2], [1]])
    # b = np.array([[6], [11], [-2], [2]])

    # square root data 1
    # A = np.array([[4, 2, -2], [2, 2, -3], [-2, -3, 14]])
    # x = np.array([[2], [2], [1]])
    # b = np.array([[10], [5], [4]])

    # x2 = EquationsSolver.solve(A, b)
    # print(x2)
    # print(x)


if __name__ == '__main__':
    main()
