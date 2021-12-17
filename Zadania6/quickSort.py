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
  

arr = [43, -1, -43, 16, 12, -4, 2, 0, -5]
print(arr)
quick_sort(arr, 0, len(arr) - 1)
print(arr)
  
