from sorting import *
from num_gen import *
from Nth_Element import *
import time

# __________HYBRID_SORT__________
print("Hybrid merge-insert sort\n__________________________\n")
list_size = int(input("Enter the size of the list: "))
threshold = int(input("Enter the threshold value: "))
arr = generate(list_size)
start = time.time()
merge_insert_hybrid_sort(arr.copy(), threshold)
end = time.time()
print("Time taken for merge-insert hybrid sort: ", 1000* (end-start), "ms")

# __________QUICK_SELECT__________
test = [3, 41, 16, 25, 63, 52, 40]
x = 3
print(f"The {x} smallest is: {quick_select(test, x)}")