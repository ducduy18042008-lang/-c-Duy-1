#Bài 1:
a = int(input())
cv = a*4
dt = a*a
print (cv, dt)
#Bài 2:
r = int(input())
cv = r*2*3.14
dt = r*r*3.14
print(cv, dt)
#Bài 3:
a,b = map(int,input().split())
if a > b: 
    cv = (a+b)*2
    dt = a*b
    print(cv, dt)
else:
    print(False)
#Bai 4:
a, b = map(int,input().split())
print( a+b,a*b)
#Bai 5
a,b,c = map(int,input().split())
TBC = (a+b+c)/3
print (f"{TBC:.1f}")
#Bai 6
import math
a,b,c = map(int,input().split())
cv = a+b+c
p = (a+b+c)/2
s = math.sqrt(p*(p-a)*(p-b)*(p-c))
print (f"{cv:.1f}", f"{s:.3f}")
#Bai 7
a,h = map(int,input().split())
s = a*h/2
print (f"{s:.2f}")
#Bai 8
import math
a,b,c = map(int,input().split())
p = (a+b+c)/2
S = math.sqrt(p*(p-a)*(p-b)*(p-c))
R = (a*b*c)/(4*S)
print(f"{R:.3f}")
#Bai 9
a,b,c = map(float,input().split())
TBC = (a*2 + b*2 + c)/5
print(f"{TBC:.1f}")
#Bai 10
T, HS = map(int,input().split())
print(T//HS, T%HS)
#Bai 11
n = int(input())
a = n//3600
b = (n - a*3600)//60
c = (n - a*3600 - b*60)
print(a,":",b,":",c)
#Bai 12:
n = int(input())
a = n%100 
b = n//10
print("%d %02d" % (b,a))
#%d: in số nguyên 
#%2d:độ rộng tối thiểu 2 kí tự 
#%02d: độ rộng 2 ký tự, nếu thiếu thì thêm số 0 ở trước
#Bai 13
a,b,c = map(int,input().split())
if a == b == c: 
    print("=")
else:
    print(max(a,b,c))
#Bai 14
t = int(input())
if 0<t<=11:
    print("Thieu nhi")
elif 11<t<=25:
    print("Thieu nien")
elif 25<t<=50:
    print("Trung nien")
else:
    print("Lao nien")
#Bai 15:
import math
a,b,c = map(float,input().split())
if a + b> c and  a+c>b and b+c>a:
    cv = a + b + c
    p = cv/2 
    s = math.sqrt(p*(p-a)*(p-b)*(p-c))
    print("Day la 3 canh cua 1 tam giac")
    print(cv,s)
else: 
    print("Day khong phai la 3 canh cua mot tam giac")
#Bai 16
TBHKI, TBHKII = map(float,input().split())
TBCN = ((TBHKI+TBHKII*2))/3
if TBCN >= 8: 
    print("%.1f" % TBCN)
    print("Gioi")
elif 6.5 <= TBCN < 8:
    print("%.1f" % TBCN)
    print("Kha")
elif 5 <=   TBCN <6.5:
    print("%.1f" % TBCN)
    print("Trung binh")
elif 3.5 <= TBCN < 5:
    print("%.1f" % TBCN)
    print("Yeu")
else: 
    print("%.1f" % TBCN)
    print("Kem")
#Bai 17
t = int(input())
if  1 <= t <= 12:
    if t == 2 or t == 3 or t == 4:
        print("Mua Xuan")
    elif t == 5 or t == 6 or t == 7:
        print("Mua Ha")
    elif t == 8 or t == 9 or t == 10:
        print("Mua Thu")
    else:
        print ("Mua Dong")
#Bai 18
month, year = map(int,input().split())
A = [1,3,5,7,8,10,12]
B = [4,6,9,11]
if year % 4 == 0 and year % 100 != 0 and month == 2: # Nam nhuan
    print ("29") 
if year % 4 == 1 or year %4 == 2 or year % 4 == 3 and month == 2: # Nam khong nhuan
    print("28")    
for x in A:
    if month == x:
        print(31)
for y in B:
    if month == y:
        print("30")
if month > 12 or month < 1:
    print("Thang khong hop le")
#Bai 19
x = list(map(int,input())) #map dùng để áp dụng một hàm lên từng phần tử của một dãy dữ liệu (đối tượng map, thực hiện biến đổi khi được duyệt)
n = 0
for i in x :
    n += i
if n % 10 == 9:
    print(n%10)
    print("may man")
else:
    print(n%10)
    print("chua may man")
#Bai 20
N = int(input())
a = 1000
b = 2000
c = 5000
if N % 1000 == 0 and N <= 1000000:
    x = N // c 
    y = (N-c*x)//b
    z = (N-c*x-b*y)//a
    print(x,y,z)
#Bai 21
km = int(input())
Tien = 0
if km <= 1:
    Tien = 12000
    print(Tien)
elif 2<= km<= 30:
    Tien =  12000+ (km-1)*10000
    print(Tien)
else:
    Tien = 12000 + 29*10000 +(km-30)*9000
    print(Tien)
#Bai 22
t = int(input())
if t <= 50:
    Tien = 600*t
    print(Tien)
elif 50<t<=100:
    Tien = 600*50 + 800*(t -50) 
    print(Tien)
elif 100<t<=200:
    Tien = 600*50 + 800*50 +(t - 100)*1100
    print(Tien)
else:
    Tien = 600*50 + 800*50 +1100*100+ (t-200)*1500
    print(Tien)
#Bai 23
n = int(input())
for i in range(1,n+1):
   
    if i % 3 == 0:
        print(i,end=(" "))
if 0< n <3:
    print("-")
#Bai 24
n = int(input())
cnt = 0
for i in range (1,n+1):
    if i % 3 == 0 : 
        cnt += 1
print(cnt)
#Bai 25
n = int(input())
cnt = 0
for i in range(1,n+1):
    if i%2 == 0:
        cnt += i
print ( cnt)
#Bai 26
n = int(input())
T = 0
for i in range(1,n+1):
    if i % 3 == 0 and i%5 == 0:
        T += i
print(T)
#Bai 27
n =int(input())
T = 0
for i in range(1,n+1):
    if i % 3 == 0 or i%5 == 0:
        T += i
print (T)
#Bai 28
import math
n = int(input())
cnt = 0 
for i in range (1,math.isqrt(n)+1):
    if n%i ==0: 
        cnt += 2
        if i == n/i:
            cnt -= 1
print (cnt)
#Bai 29
import math
n = int(input())
cnt = 0
for i in range (2,math.isqrt(n)+1):
    if n % i == 0:
        cnt += 1
    else:
        cnt += 0
if cnt >= 1 :
    print("No")
else:
    print("Yes")
#Bai 30
m,n = map(int,input().split())
T = 0
for i in range (m,n+1):
    if m < n:
        T +=i
print (T)
#Bai 31
m,n = map(int,input().split())
cnt = 0
for i in range (m,n+1):
    if i % 3 == 0:
        cnt += 1
print (cnt)
#Bai 32
m,n = map(int,input().split())
cnt = 0
T = 0
for i in range (m,n+1):
    if i % 3 == 0 or i % 5 == 0:
        cnt += 1
    if i % 2 ==0:
        T += i
print(cnt,T)
#Bai 33
m,n = map(int,input().split())
dem = 0
for i in range (m,n+1):
    dem_uoc = 0
    for j in range(1,i+1):
        if i % j == 0:
            dem_uoc += 1
    if dem_uoc == 2:
        dem += 1 
print(dem)
#Bai 34
m,n = map(int,input().split())
dem = 0
for i in range (m,n+1):
    dem_uoc = 0
    for j in range (1,i+1):
        if i % j == 0:
            dem_uoc += 1
    if dem_uoc == 2:
        print(i,end=(" "))
#Bai 35
m,n = map(int,input().split())
dem = 0
so= 0 
for i in range (m,n+1):
    dem_uoc = 0
    for j in range (1,i+1):
        if i % j == 0:
            dem_uoc += 1
    if dem_uoc == 2:
        dem += i
        so += 1
ketqua = dem/so
print("%.2f"%ketqua)
#Bài 36
import math
m,n = map(int,input().split())
A=[]
m < n == True
for i in range (1,n):
    if m % i == 0 and n % i == 0:
        A.append(i)
print(max(A))
#Bai 37
import math
m,n = map(int,input().split())
g = math.gcd(m,n)
m //= g
n //=g
print (f"{m}/{n}")    
#Bai 38
def prime(n):
    if n < 2:
        return False
    for j in range (2,n):
        if n %  j == 0:
            return False
    return True
k=int(input())
i = 2
count = 0
while count < k:
    if prime(i):
        print (i,end=" ")
        count += 1
    i += 1 
#Bai 39 
import math
def square(n):
    can = math.sqrt(n)
    if can * can == n:
        return True
    else:
        return False
n =int(input())
if square(n):
    print("Yes")
else:
    print("No")
#Bai 40
import math
def square(n):
    can = math.sqrt(n)
    if can * can == n:
        return True
    else:
        return False
k =int(input())
i = 0
count = 0
while count < k:
    if square(i):
        print (i,end=(" "))
        count +=1
    i += 1
#Bai 41
n = int(input())
a = list(map(int,input().split()))
print(sum(a))
#Bai 42
n = int(input())
a = list(map(int,input().split()))
count = 0
for i in range (n):
    if a[i] > 0:
        count += 1
print(count)       
#Bai 43
n = int(input())
a = list(map(int,input().split()))
count=0
for i in range (n):
    if a[i] % 2 == 0:
        count += 1
print(count)
#Bai 44
n = int(input())
a = list(map(int,input().split()))
S=0
for i in range (n):
    if i % 2 == 0:
        S += a[i]
print(S)
#Bai 45
n = int(input())
a = list(map(int,input().split()))
S=0
for i in range (n):
    if a[i]%2==0:
        S +=a[i]
print(S)
#Bai 46
n,x = map(int,input().split())
a = list(map(int,input().split()))
for i in range (n):
    if x == a[i]:
        True
if True:
    print("Yes")
else: 
    print("No")
#Bai 47
n = int(input())
a = list(map(int,input().split()))
A = []
B =[]
duong = 0
am = 0
for i in range (n):
    if a[i] > 0:
        A.append(a[i])
        duong +=1
    else:
        B.append(a[i])
        am += 1
print(duong,am)
print(A)
print(B)
#Bai 48
n = int(input())
a = list(map(int,input().split()))
S = 0
for i in range (n):
    if a[i]%5==0:
        print(a[i],end=(" "))
        S += a[i]
print("")
print (S)
#Bai 49
n = int(input())
a = list(map(int,input().split()))
for i in range (n):
    if a[i] == max(a):
        print(a[i],i)
#Bai 50
n = int(input())
a = list(map(int,input().split()))
a.sort()
print(*a)
#print(*a) in từng phần tử, cách nhau bằng dấu cách 
#Bai 51
import math
a = list(map(int,input().split()))
S = 0
def prime (n):
    count = 0
    if n<2:
        return False
    for i in range (1,math.isqrt(n)+1):
        if n % i == 0:
            count +=1
            if i != n//i:
                count += 1
    if count == 2:
       return True
    else:
       return False
for x in a:
    if prime(x):
        S += x
        print(x,end=" ")
print("")
print (S)
#Bai 52
import math
a = list(map(int,input().split()))
S = 0
so = 0
def prime (n):
    count = 0
    if n<2:
        return False
    for i in range (1,math.isqrt(n)+1):
        if n % i == 0:
            count +=1
            if i != n//i:
                count += 1
    if count == 2:
       return True
    else:
       return False
for x in a:
    if prime(x):
        so += 1
        S += x
if so == 0: 
    print("-")
else:
    print (f"{S/so:.2f}") #:.2f hiển thị số thực với đúng 2 chữ số sau dấu thập phân
#Bai 53
import math
a = list(map(int,input().split()))
A = []
so = 0
def prime (n):
    count = 0
    if n<2:
        return False
    for i in range (1,math.isqrt(n)+1):
        if n % i == 0:
            count +=1
            if i != n//i:
                count += 1
    if count == 2:
       so += 1
       return True
    else:
       return False
for x in a:
    if prime(x):
        A.append(x)
if so == 0:
    print("-")
else:
    print(max(A))
#Bai 54
a = list(map(int,input().split()))
A = []
so = 0
for x in a:
    if x < 0:
        A.append(x)
        so += 1
if so == 0:
    print("-")
else:
    print(max(A))
#Bai 55
a = list(map(int,input().split()))
max1 = max(a)
max2 = None #None nghĩa là không có giá trị.Ý nói, hiện tại chưa tìm được số lớn thứ nhì, nên chưa gán giá trị cho max2
for x in a:
    if x < max1:
        if max2 == None or x > max2: #max2 == none tính trường hợp lần chạy đầu còn các lần sau x > max2 là điều kiện tất yếu
            max2 = x 
if max2 is None:
    print ("-")
else:
    print(max2)
#Bai 56
n = int(input())
a = [int(input()) for i in range(n)]
min1 = min(a)
min2 = None
min3 = None
for x in a:
    if x > min1:
        if min2 == None or x <min2:
            min2 = x
for y in a:
    if y > x:
        if min3 == None or y < min3:
            min3 = y
if min3 is None:
    print("-")
else:
    print(min3)
#Bai 57
n = int(input())
a = [int(input()) for i in range(n)]
b = set (a) #set() tạo tập hợp tự động loại bỏ phần tử trùng
print (len(b)) #đếm số phần tử trong tập hợp (độ dài tập hợp)
#Bai 58
n = int(input())
a = [int(input()) for i in range(n)]
dict = {} #tạo từ điển
for x in a:
    if x not in dict:
        dict[x]=1
    else:
        dict[x] +=1
for x in dict:
    if x in dict:
        print(x,dict[x]) #x ứng với KEY, d[x] ứng với value
#Bai 59
n = int(input())
a = [int(input()) for i in range(n)]
dict = {} #tạo từ điển
for x in a:
    if x not in dict:
        dict[x]=1
    else:
        dict[x] +=1
max_count = max(dict.values()) #dict.values() : lấy tất cả các giá trị max trong từ điển
for x in dict:
    if dict[x] == max_count:
        print(x,dict[x]) #x ứng với KEY, d[x] ứng với value
#Bai 60
import math
a = list(map(int,input().split()))
def square (n):
    can = math.isqrt(n)
    if can * can == n:
        return True
    else:
        return False
so =0
S = 0
for i in range (len(a)):
    if a[i] > 0:
        True
        if square(a[i]):
            S += a[i]
            so += 1
print(f"{S/so:.1f}")
#Bai 61
name = input()
print("Chao "+name)
#Bai 62
n = input()
a = len(n)
for i in range(len(n)):
    print(n[a-1-i],end="")
#Bai 63
n = input()
a = len(n)
for i in range(len(n)):
    print(n[i])
    print("")
#Bai 64
n = input().split()
a = len(n)
for i in range(len(n)):
    print(n[i],end="")
#Bai 65
    n = list(input())
    a = len(n)
    S = []
    for i in range(len(n)):
        S.append(n[a-1-i])
    if S == n:
        print ("Yes")
    else:
        print("No")
#Bai 66
n = input().split()
a = len(n)
for i in range(len(n)):
    print(n[i],end=" ")
#Bai 67
n = input()
a = len(n)
while n[a] == " ":
    n = n[:-1]
print (n)
#Bai 68
s = input()
s = " ".join(s.spilt())  #Nối các phần tử thành xâu, cách nhau bởi một dấu cách
print (s)
#Bai 69
n = input().split()
print (len(n))
#Bai 70
s = input()
s = s.title() #viết hoa chữ cái đầu tiên của mỗi từ
print(s)
#Bai 71
s = input()
x = input()
y = input()
s = s.replace(x,y) #thay y vào x có trong s
print(s)
#Bai 72
s = input()
s = s.upper() #viết chữ in hoa
print(s)
#Bai 73
s = input()
s = s.lower() #viết chữ thường
print(s)
#Bai 74 trùng
#Bai 75
s = input().split()
a = len(s)
for x in s:
    for i in range(len(x)):
        b = len(x)
        print(x[b-1-i],end="")
    print(end=" ")
#Bai 76 
s = list(input())
x = input()
count = 0
for y in s:
    if x == y:
        count += 1
print(count)
#Bai 77
a = input()
b =set(a)
count = 0
for x in b:
    count +=1
print(count)
#Bai 78
a = list(input())
d = {}
for x in a:
    if x not in d:
        d[x] =  1
    else:
        d[x] += 1
for x in d:
        print(x,d[x],end=" ")
#Bai 79
a = list(input())
d = {}
for x in a:
    if x not in d:
        d[x] =  1
    else:
        d[x] += 1
max_count == max(d.values())
for x in d:
        if d[x] == max_count:
            print(x,d[x],end=" ")
#Bai 80
a = list(input())
x = input()
check = False
for i in range (len(a)):
    if a[i] == x:
        check = True
        break
if check:
    print(i)
else:
    print("-1")
#Bai 81
a = list(input())
x = input()
check = False
b = len(a)
for i in range (1,len(a)+1):
    if a[-i] == x:
        check = True
        break
if check:
    print(b-i)
else:
    print("-1")
#Bai 82
a = list(input())
count = 0
for i in range(len(a)):
    if a[i].isupper():
        count +=1
print(count)
#Bai 83
a = list(input())
count = 0
for i in range(len(a)):
    if a[i].islower():
        count +=1
print(count)
#Bai 84
a = input().split()
b = len(a)
print(a[b-1])
#Bai 85
a = input().split()
b = len(a)
for i in range (len(a)-1):
    print(a[i],end=" ")
#Bai 86
import math
a,b,c = map(int,input().split())
def C(a,b,c):
    return a+b+c
def S(a,b,c):
    p = C(a,b,c)/2
    s = math.sqrt(p*(p-a)*(p-b)*(p-c))
    return s
if a+b>c and a+c>b and b+c>a:
    print (f"{C(a,b,c):.1f}" ,f"{S(a,b,c):.3f}",end=" " )
#Bai 87
n = int(input())
def check(x):
    if x % 5 == 0:
        return True
    else:
        return False
if check(n):
    print("Yes")
else:
    print("No")
#Bai 88
import math
m,n = map(int,input().split())
def ucln(m,n):
    s = math.gcd(m,n)
    return s 
if ucln(m,n):
    a = m//ucln(m,n)
    b = n//ucln(m,n)
    print(f"{a}/{b}")
#Bai 89
import math
a = int(input())
S = 0
for i in range(a):
    m,n = map(int,input().split())
    S += math.comb(m,n) #math.comb(n,k) dùng để tính nCk
print(S)
#Bai 90
k,x  = map(int,input().split())
def P(x,n):
    return x **n
F = 0
for i in range(k):
    a,n = map(int,input().split())
    F += a*P(x,n)
print(F)
#Bai 91
m,n = map(int,input().split())
for i in range (n):
    for j in range (m):
        if 0 < i < n-1 and 0 < j < m-1:
            print(" ",end=(""))
        else:
            print("*",end = (""))
    print("")
#Bai 92
a,b,c = map(int,input().split())
def cong (a,b):
    d = a + b + c
    return d
def nhan (a,b):
     return a/b
print (cong(a,b),f"{nhan(a,b)+c:.2f}", f"{a/(b+c):.3f}" )
#Bai 93
def find_min(a,b):
    return min(a,b)
a,b,c = map(int,input().split())
d = find_min(find_min(a,b),c)
print(d)
#Bai 94
from fractions import Fraction
a,b = map(int,input().split())
c,d = map(int,input().split())
m = Fraction(a,b)
n = Fraction(c,d)
tong = m + n
hon_so1 = 0
tich = m*n
hon_so2 = 0
while tong > 1:
    hon_so1 += 1
    tong -= 1
while tich > 1:
    hon_so2 +=1 
    tich -= 1
print (f"{hon_so1},{m+n}")
print (m - n)
print (m*n)
print (f"{hon_so2},{m/n}")
#Bai 95
n = int(input())
a = list(map(int,input().split()))
b = sum(a)
print (f"{b / n:.1f}" )
#Bai 96
n = int(input())
a = list(map(int,input().split()))
tong = 0
for x in a:
    if x % 2 ==0:
        tong += x
print(f"{tong:.2f}")
#Bai 97
import math
a = list(map(int,input().split()))
def check(a):
    dem = 0
    for x in a:
        if x < 2:
            continue
        for i in range (2,math.isqrt(x)+1):
            if x % i == 0:
                break
        else:
                dem += 1 
    return dem
print(check(a))
#Bai 98
import math
a = list(map(int,input().split()))
def check(a):
    tong = 0
    dem = 0
    for x in a:
        if x < 2:
            continue
        for i in range (2,math.isqrt(x)+1):
            if x % i == 0:
                break
        else:
                dem += 1
                tong += x
    return (f"{tong/dem:.2f}")
print(check(a))
#Bai 99
import math
a = list(map(int,input().split()))
tong =0
dem = 0 
for x in a:
    if x > 0:
        can = math.isqrt(x)
        if can*can == x:
            tong += x 
            dem +=1
if dem == 0:
    print("-")
print(f"{tong/dem:.1f}")
#Bai 100
import math
n = int(input())
a = list(map(int,input().split()))
for i in range (n):
    if a[i] == max(a):
        print(max(a), i)
for i in range (n):
    if a[i] == min(a):
        print(min(a), i)