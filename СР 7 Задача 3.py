m = int(input("Введите максимальную массу, которую может выдержать лодка"))
n = int(input("Введите количество рыбаков"))
b=[]
s=0
for i in range(n):
    a=int(input())
    s+=a
s=s//m
print(s+1)
