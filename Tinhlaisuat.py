tien_goc=100-000-000
lai_suat=0.07
nam=int(input("Nhập vào số năm đầu tư: "))
print("số tiền mỗi năm là :")
for i in range(1,nam+1):
    tien_goc=tien_goc*(1+lai_suat)
    print(f"năm{i}: {tien_goc}VND")