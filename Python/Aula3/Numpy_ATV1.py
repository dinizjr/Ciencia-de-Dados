import numpy as np

#x = np.eye((10), dtype=int)
#print(x)

'''arr = [4,95,37,64,42,19,38,46,83,48,67,98,21,10,88,55]
arr2 = np.sort(arr)
x = arr2[np.where(np.logical_and(arr2 > 35, arr2 < 56))]
print(x)'''

'''arr = [1]
arr1 = np.zeros((1,3), dtype=int)
arr1[::1] = arr
x = np.flip(np.flip(arr1,1),1)
print(x)'''

f = np.random.uniform(0,100)
#print(f)
x = np.unique(f)
print(x)

