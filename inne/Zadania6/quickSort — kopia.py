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
  

file = open("data.txt")
try:
    text = file.read()
except:
    print('Could not load data.txt')
finally:
    file.close()

arr = []
split = text.split(', ')

for i in range(0, len(split)):
    arr.append(int(split[i]))

print(arr)
quick_sort(arr, 0, len(arr) - 1)
print(arr)
  
