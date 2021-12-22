import numpy
import time

def insertion_sort(arr):
    for i in range(1, len(arr)):
        k = arr[i]
        j = i - 1
        while j >= 0 and k < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = k

arr = numpy.random.randint(0, 1000, 1000)
start_time = time.time()
insertion_sort(arr)
end_time = time.time()
time = end_time - start_time
print(arr)
print(time) #0.0859982967376709

# arr = numpy.random.randint(0, 1000, 100000)
# start_time = time.time()
# insertion_sort(arr)
# end_time = time.time()
# time = end_time - start_time
# print(time) #602.0025125935235