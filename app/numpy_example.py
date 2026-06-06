import time

import numpy as np

plain_list = list(range(500_000_000))
# print(plain_list)

# time how long it takes to loop through the plain list
start = time.time()
result = [x*2 for x in plain_list]
end = time.time()
total_time = end - start
print(f"Python list took:: {total_time:.2f} seconds")

# Numpy vectorized operation
numpy_array = np.array(plain_list)
start = time.time()
new_result = numpy_array*2
end = time.time()
total_time = end - start
print(f"Numpy array took: {total_time:.2f} seconds")

#Hypothetical sales data for January

january_sales = np.array([
    120, 135, 98, 142, 167, 88, 95,
    201, 178, 156, 134, 189, 145, 112,
    167, 198, 223, 145, 167, 134, 189,
    201, 178, 156, 134, 189, 145, 112,
    167, 198, 223
])


