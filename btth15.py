n=int(input("Nhập số n:"))

s1=0
for i in range (1,n+1):
    s1+=1/i
    
s2=10 
for i in range(1,n+1):
    s2+=+1/(i+1)

print(f"s1={s1:.2f}")
print(f"s2={s2:.2f}")