import numpy, time, heapq

def heap_sort(tab):
    heap = []
    for value in tab:
        heapq.heappush(heap, value)
    return [heapq.heappop(heap) for i in range(len(heap))]


# arr = numpy.random.randint(0, 1000, 1000)
# start_time = time.time()
# heap_sort(arr)
# end_time = time.time()
# time = end_time - start_time
# print(arr)
# print(time) #0.0009996891021728516

arr = numpy.random.randint(0, 1000, 100000)
start_time = time.time()
heap_sort(arr)
end_time = time.time()
time = end_time - start_time
print(arr)
print(time) #0.10101032257080078