import numpy, time

def partition(arr, low, high):
    index = (low - 1) 
    pivot = arr[high]     
  
    for j in range(low, high):
        if arr[j] <= pivot:
            index += 1
            arr[index], arr[j] = arr[j], arr[index]
  
    arr[index + 1], arr[high] = arr[high], arr[index + 1]
    return (index + 1)
  

def quick_sort(arr, low, high):
    if len(arr) == 1:
        return arr

    if low < high:
        index = partition(arr, low, high)
        quick_sort(arr, low, index - 1)
        quick_sort(arr, index + 1, high)
  

# arr = numpy.random.randint(0, 1000, 1000)
# start_time = time.time()
# quick_sort(arr, 0, len(arr) - 1)
# end_time = time.time()
# time = end_time - start_time
# print(arr)
# print(time) #0.003997325897216797

arr = numpy.random.randint(0, 1000, 100000)
start_time = time.time()
quick_sort(arr, 0, len(arr) - 1)
end_time = time.time()
time = end_time - start_time
print(arr)
print(time) #3.019979953765869