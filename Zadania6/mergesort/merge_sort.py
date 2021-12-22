import numpy, time

def merge_sort(arr):
    if len(arr) > 1:
        m = len(arr) // 2
        l = arr[:m]
        r = arr[m:]
        merge_sort(l)
        merge_sort(r)
        i = j = k = 0
        while i < len(l) and j < len(r):
            if l[i] < r[j]:
                arr[k] = l[i]
                i += 1
            else:
                arr[k] = r[j]
                j += 1
            k += 1
        while i < len(l):
            arr[k] = l[i]
            i += 1
            k += 1
        while j < len(r):
            arr[k] = r[j]
            j += 1
            k += 1


# arr = numpy.random.randint(0, 1000, 1000)
# start_time = time.time()
# merge_sort(arr)
# end_time = time.time()
# time = end_time - start_time
# print(arr)
# print(time) #0.00499725341796875

arr = numpy.random.randint(0, 1000, 100000)
start_time = time.time()
merge_sort(arr)
end_time = time.time()
time = end_time - start_time
print(arr)
print(time) #0.8538455963134766