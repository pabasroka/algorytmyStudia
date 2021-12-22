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

array1 = [4, 41, 5, 7, -8, -12, 3, 1, 2]
merge_sort(array1)
print(array1)
