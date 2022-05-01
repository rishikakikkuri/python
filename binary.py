input_array = []
n = int(input("enter the number of elements"))
for i in range(n):
    ele = int(input())
    input_array.append(ele)
print(input_array)
x = int(input("Enter the element to be found"))

k = len(input_array)
for i in range(k-1):
    for j in range(0, n-i-1):
        if input_array[j] > input_array[j+1]:
            input_array[j], input_array[j+1] = input_array[j+1], input_array[j]

def binary_search(input_array, low, high, x):
    if high >= low:
        mid = (high+low)//2

        if input_array[mid] == x:
            return mid
        elif input_array[mid] > x:
            return binary_search(input_array, low, mid-1, x)
        else:
            return binary_search(input_array, mid+1, high, x)
    else:
        return -1


result = binary_search(input_array, 0, len(input_array) - 1, x)

if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")
