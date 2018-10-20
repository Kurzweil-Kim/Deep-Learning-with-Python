# -*- coding: utf-8 -8-
import numpy as np

def NAND(x1, x2):

    x = np.array([x1, x2])
    w = np.array([-0.5, -0.5])
    b = 0.7
    tmp = np.sum(x * w) + b

    if tmp <= 0:
        return 0
    elif tmp > 0:
        return 1

def OR(x1, x2):

    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.3
    tmp = np.sum(x * w) + b

    if tmp <= 0:
        return 0
    elif tmp > 0:
        return 1

def XNOR(x1, x2):

    s1 = NAND(x1, x2)
    s2 = OR(x1, x2)
    y = NAND(s1, s2)

    return y

def main():

    print(XNOR(0, 0))
    print(XNOR(1, 0))
    print(XNOR(0, 1))
    print(XNOR(1, 1))

if __name__ == '__main__':
    main()
