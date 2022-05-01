input_array = []
n = int(input("Enter the number of elements"))
for i in range(0, n):
    ele = int(input())
    input_array.append(ele)
print(input_array)

for k in range(1, len(input_array)):
    key = input_array[k]
    j = k - 1

    while j >= 0 and key < input_array[j]:
        input_array[j+1] = input_array[j]
        j = j-1
    input_array[j+1] = key

isort = []
for i in range(len(input_array)):
    ee = input_array[i]
    isort.append(ee)
print(isort)
