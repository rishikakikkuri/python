in_array = []
n = int(input("enter the number of elements"))
for i in range(n):
    ele = int(input())
    in_array.append(ele)
print(in_array)

x = int(input("enter the value to find"))
for i in range(len(in_array)):
    if in_array[i] == x:
        print(i)

        break;
print("element not found")