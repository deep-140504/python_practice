import numpy as np

dtype = [('name', 'U10'), ('age', 'i4'), ('height', 'f4')]
arr = np.array([('a', 21, 5.6), ('b', 22, 5.7), ('c', 23, 5.8)], dtype=dtype)

arr = np.core.records.fromarrays(arr.transpose(), dtype=dtype + [('name_age', 'U13')])

arr['name_age'] = arr['name'] + " " + arr['age'].astype(str)

print(arr)
