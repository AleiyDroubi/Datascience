import numpy as np

arr = np.array([1, 2, 3, 4, 5])
tuple_arr = np.array((1, 2, 3, 4, 5))

print(arr)
print(tuple_arr) # same as arr
print(type(arr))

#0d array
arr0 = np.array(42)
print(arr0)
print(arr0.ndim) # number of dimensions
#1d array
arr1 = np.array([1, 2, 3, 4, 5])
print(arr1)
print(arr1.ndim)
#2d array
arr2 = np.array([[1, 2, 3], [4, 5, 6]])
print(arr2)
print(arr2.ndim)
#3d array
arr3 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(arr3)
print(arr3.ndim)
# higher dimensional arrays
arr4 = np.array([1, 2, 3, 4], ndmin=5)
print(arr4)