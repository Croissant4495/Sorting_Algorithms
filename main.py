import time
from sorting import *
from num_gen import generate
import matplotlib.pyplot as plt
from matplotlib.table import Table


list_sizes = [1000, 2000, 5000, 7000, 10000, 20000, 50000, 100000]
function_handle = [insertion_sort, bubble_sort, selection_sort, merge_sort, quick_sort, heap_sort]
#                                   cols                 rows: algo
time_arr = [[0 for i in range(len(list_sizes))] for j in range(len(function_handle))]      

for j in range(len(list_sizes)):
    arr = generate(list_sizes[j])
    for i in range(len(function_handle)):
        begin = time.time()
        function_handle[i](arr.copy())
        end = time.time()
        time_arr[i][j] = 1000*(end-begin)


algorithms = ['Insertion Sort', 'Bubble Sort', 'Selection Sort', 'Merge Sort', 'Quick Sort', 'Heap Sort']
for i in range(len(algorithms)):
    print(f"{algorithms[i]}: {time_arr[i]}")


# __________PLOTTING__________
colors = ['red', 'blue', 'green', 'purple', 'orange', 'black']
# Plot each algorithm separately
plt.figure(figsize=(8, 6))
for i, algo in enumerate(algorithms):
    plt.plot(list_sizes, time_arr[i], marker='o', linestyle='-', color=colors[i], label=algo)

# Labels and title
plt.xlabel('Number of Elements')
plt.ylabel('Time Taken (mili-seconds)')
plt.title('Sorting Algorithm Performance')
plt.xticks(list_sizes)
plt.legend()
plt.grid(True)

# Show plot
header = ['Algorithm'] + [str(size) for size in list_sizes]
table_data = []

for i, algorithm in enumerate(algorithms):
    row = [algorithm] + [f"{time:.4f}" for time in time_arr[i]]
    table_data.append(row)

# Create a plot with a table
fig, ax = plt.subplots(figsize=(10, 6))  # Adjust the figure size to fit the table
ax.axis('off')  # Turn off the axis

table = Table(ax, bbox=[0, 0, 1, 1])
nrows, ncols = len(table_data), len(header)

for col, header_text in enumerate(header):
    table.add_cell(0, col, width=1.0/ncols, height=0.1, text=header_text, loc='center', facecolor='lightgrey')

for row, data in enumerate(table_data):
    for col, cell_data in enumerate(data):
        table.add_cell(row+1, col, width=1.0/ncols, height=0.1, text=cell_data, loc='center')

# Add the table to the plot
ax.add_table(table)

# Display the table
plt.show()


