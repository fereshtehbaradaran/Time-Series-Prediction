import numpy
import math
from preprocess import *

def makeMatrix_X_Y(data, n):
    x = []
    y = []
    for i in range(n, len(data)):
        row = [1] + [data[i - j] for j in range(n, 0, -1)]
        x.append(row)
        y.append(data[i])

    return x, y


def makeMatrix_W(x, y):
    return numpy.dot(numpy.dot(numpy.linalg.inv(numpy.dot(numpy.transpose(x), x)), numpy.transpose(x)), y)


def findNextY(x_vector, w):
    return numpy.dot(x_vector, w)


def findPredicted_Y(x, w):
    return numpy.dot(x, w)


def doTheProces(fileName, numberOfWindow):
    result = []
    norms = []
    for i in range(4):
        data = getData(fileName, i + 2)
        x, y = makeMatrix_X_Y(data, numberOfWindow)
        w = makeMatrix_W(x, y)
        x_vector = [1] + [float(data[len(data) - j]) for j in range(numberOfWindow, 0, -1)]
        result.append(findNextY(x_vector, w))
        norms.append(calculateNorm(y, findPredicted_Y(x, w)))

    return result, norms


def calculateNorm(y, predicted_y):
    norm = 0
    for i in range(len(y)):
        norm += ((predicted_y[i] - y[i]) / y[i]) ** 2
    return math.sqrt(norm)