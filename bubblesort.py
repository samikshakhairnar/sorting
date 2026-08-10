n = int(input("Enter number of employees: "))

arr = []


for i in range(n):
    salary = float(input("Enter salary: "))
    arr.append(salary)

for i in range(0,n-1):
    
    for j in range(0,n - 1):
        if(arr[j]>arr[j+1]):
            temp = arr[j]
            arr[j] = arr[j + 1]
            arr[j + 1] = temp


print("Salaries in ascending order:")

for i in range(n):
    print(arr[i])

