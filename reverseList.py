# Python program to reverse an array
def list_reverse(arr, size):
    i = 0
    while i < size // 2:
        # swap elements from the start with elements from the end iteratively
        arr[i], arr[size - i - 1] = arr[size - i - 1], arr[i]
        i += 1
    return arr


arr = [1, 2, 3, 4, 5]
size = 5
print('Original list: ', arr)
print("Reversed list: ", list_reverse(arr, size))

# This contributed by Sushrut Thakur
