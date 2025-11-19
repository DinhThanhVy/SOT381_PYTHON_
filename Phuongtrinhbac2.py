a=int(float(input("nhập a: ")))
b=int(float(input("nhập b: ")))
c=int(float(input("nhập c: ")))
if a==0:
    if b == 0:
        if c == 0:
           print("phương trình có vô số nghiệm")
        else:
           print("phương trình vô nghiệm")
    else:
        x=-c/b
        print("phương trình có 1 nghiệm duy nhất x= ",x)
else:
    delta=b*b-4*a*c
    if delta<0:
        print("phương trình vô nghiệm")
    elif delta==0:
       x=-b/2*a
       print("phương trình có nghiệm kép x=",x)
    else:
        sqrt_delta=delta**0.5
        x1=(-b+sqrt_delta)/(2*a)
        x2=(-b-sqrt_delta)/(2*a)
        print("phương trình có 2 nghiệm phân biệt là: ")
        print("x1= ",round(x1,2))
        print("x2= ",round(x2,2))
        
    