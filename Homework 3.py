#Bai 1:
for i in range(50): 
    a = 2*i+1
    print(a,end=(" "))
#Bai 2
for i in range (1,17):
    a = 6*i
    print(a,end=(" "))
#Bai 3
a = int(input())
for i in range(1,11):
    print(f"{a} * {i} =",a*i)
#Bai 4
h = int(input())
for i in range (1,h):
    if i == 1:
        print(" "*(h-1)+"*")
    else:
        print((h-i)*" "+"*"+(2*i-3)*" "+"*")
print((2*h-1)*"*")
#Bai 5
n =int(input())
tong  = 0 
for i in range (1,n+1):
    tong += i
print(tong)
#Bai 6
import math
a =int(input())
A = []
for i in range(1,math.isqrt(a)+1):
    if a % i ==0:
        A.append(i)
        if i != a//i:
            A.append(a//i)
A.sort()
print(A)
#Bai 7 
import math
a =int(input())
count = 0
for i in range(1,math.isqrt(a)+1):
    if a % i ==0:
        count +=1 
        if i != a//i:
            count +=1
print(count)
#Bai 8
import math
a,b = map(int,input().split())
c = math.gcd(a,b)
D = []
for i in range(1,math.isqrt(c)+1):
    if c % i ==0:
        D.append(i)
        if i != c//i:
            D.append(c//i)
D.sort()
print(D)
#Bai 9
import math
a = int(input())
can = math.sqrt(a)
if can * can == a:
    print("a là số chính phương")
else:
    print("a không phải là số chính phương")
#Bai 10
import math
a = int(input())
tong = 1
for i in range (2,math.isqrt(a)+1):
    if a % i == 0:
        tong += i
        if i != a//i:
            tong += a//i
if tong == a:
    print(f"{a} là số hoàn hảo")
else:
    print(f"{a} không phải là số hoàn hảo")
#Bai 11
a = int(input())
while a <0:
    a = int(input())
if a > 0: 
    print("Bạn nhập đúng quy tắc")
#Bai 12
import math
n = int(input())
k = (-1 +(1+8*n)**(1/2))/2
if k == k//1:
    k -= 1
else:
    k = math.floor(k)
#cach 2
import math
n = int(input())
k = 0 
S = 0
while S + k + 1 < n:
    k = k + 1 
    S += k 
print(k)
print(S)
print(k)
#Bai 13
A = int(input())
S = 0
k = 0
while S + 1/(k +1) < A:
    k += 1
    S += 1/k 
print(k)
#Bai 14
a = int(input())
if a == -1:
    print("Chua nhap so nao")
else:
    max = a
    min = a
    while a != -1:
        if a > max :
            max = a
        if a < min:
            min = a
        a = int(input())
print(max)
print(min)
#Bai 15
n = input()
print(len(n))
#cach 2
n = int(input())
dem = 0 
while n > 0:
    dem +=1 
    n //=10
print (dem)
#Bai 16
n = list(input())
chan = 0
le = 0
for i in range(len(n)):
    if int(n[i]) % 2==0:
        chan +=1 
    else:
        le +=1 
print(chan) 
print(le)
#cach 2
n = int(input())
chan = 0
le = 0 
while n > 0:
    a = n % 10
    if a % 2 == 0:
        chan += 1
    else:
        le += 1
    n //= 10
print(chan)
print (le)
#Bai 17
n = int(input())
tong = 0
while n >0:
    tong += n % 10
    n //=10
print(tong)
#Bai 18
n = int(input())
ha = round(n**(1/3))
if ha*ha*ha == n:
    print (True)
else:
    print (False)
#Bai 19

    A = int(input())
fn1 = 0 
fn2 = 1
while fn1 + fn2 < A:
    fn3 = fn1+fn2
    fn1 = fn2
    fn2 = fn3
print(fn3)
#Bai 20
n = int(input())
prime_count = 0
while n >0:
    a = n%10
    if a == 2 or a == 3 or a ==5 or a == 7:
        prime_count +=1 
    n //=10
print(prime_count)


    