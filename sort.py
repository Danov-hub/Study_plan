def binary_sort(arr, key_func):
    for i in range(1, len(arr)):
        current = arr[i]
        key = key_func(current)
        left, right = 0, i
        while left < right:
            mid = (left + right) // 2
            if key_func(arr[mid]) <= key:
                left = mid + 1
            else:
                right = mid
                
        #Cдвиг элементов от i до left на одну позицию вправо
        for j in range(i, left, -1):
            arr[j] = arr[j - 1]
        arr[left] = current
    return arr
