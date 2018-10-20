# -*- coding: utf-8 -*-
import numpy as np

def main():

    A = np.array([[1, 2], [3, 4]])

    print(A)
    print(A.shape)
    print(A.dtype)

    B = np.array([[3, 0], [0, 6]])

    print(A + B)
    print(A * B)
    print(A * 10)

if __name__ == '__main__':
    main()
