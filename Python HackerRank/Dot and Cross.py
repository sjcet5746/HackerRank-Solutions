#Written by Gskd
import numpy

Order = int(input())
Array1 = numpy.array([], dtype=int)
Array2 = numpy.array([], dtype=int)

for i in range(Order):
    Array1_elements = input().split()
    Array1 = numpy.append(Array1, Array1_elements)

for i in range(Order):
    Array2_elements = input().split()
    Array2 = numpy.append(Array2, Array2_elements)

Array1.shape = (Order, Order)
Array1 = Array1.astype(int)

Array2.shape = (Order, Order)
Array2 = Array2.astype(int)

Matrix_multiplication = numpy.dot(Array1, Array2)
print(Matrix_multiplication)
