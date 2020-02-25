#enter marks of 5 subjects and find total, average, & percentage

a=float(input("science marks:"))
b=float(input("maths marks:"))
c=float(input("soial marks:"))
d=float(input("english marks:"))
e=float(input("hindi marks:"))
t=(a+b+c+d+e)
avg=t/5
p=(t/500)*100
print("total=",t,"average=",avg,"percentage=",p)