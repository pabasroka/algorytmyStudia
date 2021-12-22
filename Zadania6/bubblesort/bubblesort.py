import numpy, time

def bubbleSort(tab):
    for i in range(1, len(tab)):
        for j in range(len(tab) - 1, i - 1, -1):
            if tab[j] < tab[j-1]:
                tab[j - 1], tab[j] = tab[j], tab[j - 1]

arr = numpy.random.randint(0, 1000, 1000)
start_time = time.time()
bubbleSort(arr)
end_time = time.time()
time = end_time - start_time
print(arr)
print(time) #0.20999598503112793

# arr = numpy.random.randint(0, 1000, 100000)
# start_time = time.time()
# bubbleSort(arr)
# end_time = time.time()
# time = end_time - start_time
# print(arr)
# print(time) #1054.07859849999999824