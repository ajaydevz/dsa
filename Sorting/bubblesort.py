arr = [47,12,34,56,76,54,32,45]

def bubblesort(arr):
    
    n = len(arr)

    for i in range(n):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]

    return arr

print(bubblesort(arr))


