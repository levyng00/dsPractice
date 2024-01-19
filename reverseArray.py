def reverseArr(arr, n):
    i = 0
    while i < n:
        arr[i], arr[n-1] = arr[n-1], arr[i]
        i += 1
        n -= 1

arr = [1, 2, 3, 4, 5, 6, 7, 89]
n = len(arr) 
reverseArr(arr, n)
print(arr)
