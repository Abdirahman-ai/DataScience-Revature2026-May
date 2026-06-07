import time

import numpy as np

plain_list = list(range(1_000_000))
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

print("========= January sales ========")
print(january_sales)
print(f"Total time: {np.sum(january_sales):.2f} seconds")
print(f"Average time: {np.mean(january_sales):.2f} seconds")
print(f"Max time: {np.max(january_sales):.2f} seconds")
print(f"Min time: {np.min(january_sales):.2f} seconds")
print(f"Standard deviation: {np.std(january_sales):.2f} seconds")
print(f"Median: {np.median(january_sales):.2f} seconds")


# Operating on the entire dataset
# We expect busisness to boom 15% in february, so lets estimate those sales numbers
february_sales = january_sales * 1.15
print(f"\n Estimated February sales: {february_sales} seconds")


# BOOLEAN INDEXING - a way to filter the list
# Which days in Jan had sales above average?
above_avg_sales = january_sales > np.mean(january_sales)
print(f"\n Days with above avg sales: {above_avg_sales}")

num_above_avg = np.sum(above_avg_sales) #True == 1, False == 0
print(f"\n Number of above avg sales: {num_above_avg}")
print(f"{num_above_avg} out of {len(january_sales)} had above everage sales")