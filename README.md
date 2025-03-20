#天數
year=int(input())
d=0
y=1900
while y<year:
  if (y%100!=0 and y%4==0) or y%400==0:
    d=d+366
  else :
    d=d+365
  y=y+1

#元旦判斷    
t=d%7

#日曆

#1
print("一月")
print("一","二","三","四","五","六","日")
for i in range(t):
  print("   ",end="")
k=32
for date in range(1,k):
  if  date<10:
     print(" ",end="")
  if (date+t)%7==0:
    print(date)
  else:
    print(date,"",end="")
print()

#2

if (y%100!=0 and y%4==0) or y%400==0:
  k=30
else:
  k=29

t=((31%7)+t)%7
print("二月")
print("一","二","三","四","五","六","日")
for i in range(t):
  print("   ",end="")
for date in range(1,k):
 if  date<10:
  print(" ",end="")
 if (date+t)%7==0:
  print(date)
 else:
    print(date,"",end="")
print()

#3
t=(((k-1)%7)+t)%7
print("三月")
k=32
print("一","二","三","四","五","六","日")
for i in range(t):
  print("   ",end="")
for date in range(1,k):
 if  date<10:
  print(" ",end="")
 if (date+t)%7==0:
  print(date)
 else:
    print(date,"",end="")
print()

#4
t=(((k-1)%7)+t)%7
print("四月")
k=31
print("一","二","三","四","五","六","日")
for i in range(t):
  print("   ",end="")
for date in range(1,k):
 if  date<10:
  print(" ",end="")
 if (date+t)%7==0:
  print(date)
 else:
    print(date,"",end="")
print()

#5
t=(((k-1)%7)+t)%7
print("五月")
k=32
print("一","二","三","四","五","六","日")
for i in range(t):
  print("   ",end="")
for date in range(1,k):
 if  date<10:
  print(" ",end="")
 if (date+t)%7==0:
  print(date)
 else:
    print(date,"",end="")
print()

#6
t=(((k-1)%7)+t)%7
print("六月")
k=31
print("一","二","三","四","五","六","日")
for i in range(t):
  print("   ",end="")
for date in range(1,k):
 if  date<10:
  print(" ",end="")
 if (date+t)%7==0:
  print(date)
 else:
    print(date,"",end="")
print()

#7
t=(((k-1)%7)+t)%7
print("七月")
k=32
print("一","二","三","四","五","六","日")
for i in range(t):
  print("   ",end="")
for date in range(1,k):
 if  date<10:
  print(" ",end="")
 if (date+t)%7==0:
  print(date)
 else:
    print(date,"",end="")
print()

#8
t=(((k-1)%7)+t)%7
print("八月")
k=32
print("一","二","三","四","五","六","日")
for i in range(t):
  print("   ",end="")
for date in range(1,k):
 if  date<10:
  print(" ",end="")
 if (date+t)%7==0:
  print(date)
 else:
    print(date,"",end="")
print()

#9
t=(((k-1)%7)+t)%7
print("九月")
k=31
print("一","二","三","四","五","六","日")
for i in range(t):
  print("   ",end="")
for date in range(1,k):
 if  date<10:
  print(" ",end="")
 if (date+t)%7==0:
  print(date)
 else:
    print(date,"",end="")
print()

#10
t=(((k-1)%7)+t)%7
print("十月")
k=32
print("一","二","三","四","五","六","日")
for i in range(t):
  print("   ",end="")
for date in range(1,k):
 if  date<10:
  print(" ",end="")
 if (date+t)%7==0:
  print(date)
 else:
    print(date,"",end="")
print()

#11
t=(((k-1)%7)+t)%7
print("十一月")
k=31
print("一","二","三","四","五","六","日")
for i in range(t):
  print("   ",end="")
for date in range(1,k):
 if  date<10:
  print(" ",end="")
 if (date+t)%7==0:
  print(date)
 else:
    print(date,"",end="")
print()

#12
t=(((k-1)%7)+t)%7
print("十二月")
k=32
print("一","二","三","四","五","六","日")
for i in range(t):
  print("   ",end="")
for date in range(1,k):
 if  date<10:
  print(" ",end="")
 if (date+t)%7==0:
  print(date)
 else:
    print(date,"",end="")
print()