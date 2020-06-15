def merge(left,right):
    res = [0 for i in range(len(left)+len(right))]
    i = 0
    j = 0
    k = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            res[k] = left[i]
            i += 1
        else:
            res[k] = right[j]
            j += 1
        k += 1
    while i < len(left):
        res[k] = left[i]
        i += 1
        k += 1
    while j < len(right):
        res[k] = right[j]
        j += 1
        k += 1
    return res

def sort(arr):
    if len(arr) == 1:
        return arr
    mid = len(arr)//2
    left = sort(arr[0:mid])
    right = sort(arr[mid:])
    return merge(left,right)

n = int(input("Nhap vao so N: "))
arr = [0 for i in range(n)]
for i in range(n):
    arr[i] = int(input("Nhap vao phan tu thu " + str(i+1) + " : "))
print("Mang sau khi sap xep:",sort(arr))