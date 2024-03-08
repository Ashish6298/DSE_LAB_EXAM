import numpy as np
# Create arrays
a = np.array([1, 2, 3, 4, 5])
b = np.array([6, 7, 8, 9, 10])
print("Array a", a)
print("Array b", b)
print("Sum of array a and b", np.add(a,b))
print("Difference of array a and b", np.subtract(a,b))
print("Product of arrays a and b", np.multiply(a,b))
print("Division of arrays a and b", np.divide(a,b))
print("Square root of array a:",np.sqrt(a))
print("Exponential of array a:",np.exp(a))
print("Minimum value of array a:",np.min(a))
print("Maximum value of array b:",np.max(b))
print("Mean of array a:",np.mean(a))
print("Standard deviation of array b:",np.std(b))
print("Sum of elements in array a:",np.sum(a))
c=np.array([[1,2],[3,4],[5,6]])
print("Array c:")
print(c)
print("Reshaped array c:")
print(np.reshape(c,(2,3)))
d=np.array([[1,2,3],[4,5,6]])
print("Array d:")
print(d)
print("Transposed array d:")
print(np.transpose(d))





# Output:
# Array a [1 2 3 4 5]
# Array b [ 6 7 8 9 10]
# Sum of array a and b [ 7 9 11 13 15]
# Difference of array a and b [-5 -5 -5 -5 -5]
# Product of arrays a and b [ 6 14 24 36 50]
# Division of arrays a and b [0.16666667 0.28571429 0.375 0.44444444 0.5 ]
# Square root of array a: [1. 1.41421356 1.73205081 2. 2.23606798]
# Exponential of array a: [ 2.71828183 7.3890561 20.08553692 54.59815003 148.4131591 ]
# Minimum value of array a: 1
# Maximum value of array b: 10
# Mean of array a: 3.0
# Standard deviation of array b: 1.4142135623730951
# Sum of elements in array a: 15
# Array c:
# [[1 2]
# [3 4]
# [5 6]]
# Reshaped array c:
# [[1 2 3]
# [4 5 6]]
# Array d:
# [[1 2 3]
# [4 5 6]]
# Transposed array d:
# [[1 4]
# [2 5]
# [3 6]]