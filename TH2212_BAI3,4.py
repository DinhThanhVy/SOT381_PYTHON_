m=float(input("nhập giá trị : "))
n=float(input("nhập giá trị : "))
k=float(input("nhập giá trị : "))
def soln(m,n,k):
    max=m
    if n>max:
        max=n
    if k>max:
        max=k
    return max
solonnhat=soln(m,n,k)
print(f"số lớn nhất là: {solonnhat}")
def sonn(m,n,k):
    min=m
    if n<min:
        min=n
    if k<min:
        min=k
    return min
sonhonhat=sonn(m,n,k)
print(f"số nhỏ nhất là : {sonhonhat}")
    
