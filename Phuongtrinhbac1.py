a=int(float(input("Nhập số a: ")))
b=int(float(input("Nhập số b: ")))
if a==0:
    if b==0:
        print("Phương trình vô số nghiệm")
    else:
        print("phương trình vô nghiệm")
else:
    x=-b/a
    print("phương trình có nghiệm kép là:",x)