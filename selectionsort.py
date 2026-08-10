n = int(input("Enter number of employees: "))


arr = []

for i in range(n):
    salary = int(input("Enter salary: "))
    arr.append(salary)


for i in range(n - 1):
    min_index = i

    for j in range(i + 1, n):
        if arr[j] < arr[min_index]:
            min_index = j

    
    temp = arr[i]
    arr[i] = arr[min_index]
    arr[min_index] = temp


print("Salaries in ascending order:")

for i in range(n):
    print(arr[i])
