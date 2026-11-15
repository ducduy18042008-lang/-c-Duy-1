#Bai 1:
a,b = map(int,input().split())
print(a+b, a*b)
#Bai 2:
r = int(input())
c = 2*3.14*r
s = 3.14*r**2
print(c,s)
#Bai 3:
a,b,c = map(int,input().split())
if a+b > c and a+c>b and b+c >a:
    p = a+b+c
    s = (p*(p-a)*(p-b)*(p-c))**(1/2)
    print (s,p)
    if a == b == c:
        print("Tam giac deu")
    elif a == b or b == c or a==c:
        print("Tam giac can")
    elif a**2 +b**2 == c**2 or a**2+c**2== b**2 or b**2 + c**2 == a**2:
        print ("Tam giac vuong")
    else:
        print("Tam giac thuong")
else:
    print("Khong la ba canh cua mot tam giac")
#Bai 4: viết giải phương trình bậc 1 y = ax+b
a,b = map(float,input().split())
if a == 0:
    if b == 0:
        print("phương trình có vô số nghiệm")
    else:
        print ("phương trình vô nghiệm")
else:
    x = -b/a
    print(x)
#Bai 5:
import math
a,b,c = map(int,input().split())
delta = b**2 -4*a*c
if delta > 0:
    x1 = (-b + math.sqrt(delta))/(2*a)
    x2 = (-b - math.sqrt(delta))/(2*a)
    print("phương trình có hai nghiệm",x1,x2)
elif delta == 0:
    x = (-b + math.sqrt(delta))/(2*a)
    print ("phương trình có nghiệm kép")
elif delta < 0:
    print("phương trình vô nghiệm")
#Bai 6:
a,b,c,d = map(int,input().split())
print(max(a,b,c,d))
#Bai 7:
a,b,c,d = map(int,input().split())
print(min(a,b,c,d))
#Bai 8:
a,b,m = map(int,input().split())
c,d,n = map(int,input().split())
D = a*d - b*c
Dx = m*d - n*b
Dy = a*n - m*c
if D != 0:
    x = Dx / D
    y = Dy / D
    print(x)
    print(y)
else:
    if a == 0 and b == 0 and c == 0 and d == 0:
        if m == 0 and n == 0:
            print ("He co vo so nghiem")
        else:
            print("He vo nghiem")
    elif a*n == c*m and b*n == d*m:
        print("He co vo so nghiem")
    else:
        print("He vo nghiem")
#Bai 9:
x = int(input())
h = 0
m = 0
s = 0
h = x //3600
m = (x-h*3600)//60
s = x -h*3600 -m*60
print(h,m,s)
#Bai 10
x,y = map(int,input().split())
x1,y1 = map(int,input().split())
d = ((x-x1)**2+(y-y1)**2)**1/2
if d == 0:
    print(f"A ({x1},{y1}) nam tren duong tron")
elif d > 0:
    print(f"A ({x1},{y1}) nam ngoai duong tron")
else:
    print(f"A ({x1},{y1}) nam trong duong tron")
#Bai 11:
x,y = float(input().split())
mu = x**y
print(mu)