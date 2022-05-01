Input_array=[]
n=int(input("Enter the number of elements:"))
for i in range(0, n):
    element = int(input())
    Input_array.append(element)
print(Input_array)
for k in range(len(Input_array)):

    min_index = k
    for j in range(k+1, n):
        if Input_array[k] > Input_array[j]:
            min_index = j

    Input_array[k], Input_array[min_index] = Input_array[min_index], Input_array[k]
sort=[]
print ("Sorted array")
for i in range(len(Input_array)):
    element1 = Input_array[i]
    sort.append(element1)
print(sort)



