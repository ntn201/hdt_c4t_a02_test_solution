def gcd(a,b):
    if a%b == 0:
        return b
    return gcd(b,a%b)

a = int(input("Nhap vao so a: "))
b = int(input("Nhap vao so b: "))


print("Uoc chung lon nhat cua 2 so la:",gcd(a,b))

print(int(a/gcd(a,b)),"/",int(b/gcd(a,b)),sep="")