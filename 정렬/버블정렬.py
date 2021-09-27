def bubble_sort_1(array):
    for index in reversed(range(len(array))):
        for i in range(index):
            if array[i] > array[i+1]:
                x[i],x[i+1] = x[i+1],x[i]
                

def bubble_sort_2(arr):
    for i in range(len(arr)):
        for j in range(0, len(arr) - i - 1):
            if arr[j] > arr[j + 1]: 
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

arr = [64, 34, 25, 12, 57, 93, 1, 123]
bubble_sort2(arr)