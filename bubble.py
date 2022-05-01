input_array = []
n = int(input("enter the number of elements"))
for i in range(n):
    element = int(input())
    input_array.append(element)
print(input_array)

k = len(input_array)
for i in range(k-1):
    for j in range(0, n-i-1):
        if input_array[j] > input_array[j+1]:
            input_array[j], input_array[j+1] = input_array[j+1], input_array[j]

sort =[]
for i in range(len(input_array)):
    element1 = input_array[i]
    sort.append(element1)
print(sort)