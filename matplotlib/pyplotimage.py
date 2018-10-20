import matplotlib.pyplot as plt
from matplotlib.image import imread

def main():

    img = imread('deep-learning.jpg')

    plt.imshow(img)
    plt.show()

if __name__ == '__main__':
    main()
