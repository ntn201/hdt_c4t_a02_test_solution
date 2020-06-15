def sum(arr):
    total = 0
    for i in arr:
        total += i
    return total

def min(arr):
    min_elem = arr[0]
    for i in arr:
        if i < min_elem:
            min_elem = i
    return min_elem

def max(arr):
    min_elem = arr[0]
    for i in arr:
        if i > min_elem:
            min_elem = i
    return min_elem

def count(arr,x):
    count = 0
    for i in arr:
        if i == x:
            count += 1
    return count

n = int(input("Nhap vao so N: "))
arr = [0 for i in range(n)]
for i in range(n):
    arr[i] = int(input("Nhap vao phan tu thu " + str(i+1) + " : "))

print("Tong cua mang la:",sum(arr))
print("Phan tu nho nhat cua mang la:",min(arr))
print("Phan tu lon nhat cua mang la:",max(arr))
x = int(input("Nhap vao x: "))
print(x,"xuat hien",count(arr,x),"lan")