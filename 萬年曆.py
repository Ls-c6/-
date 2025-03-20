Month=["一月","二月","三月","四月","五月","六月","七月","八月","九月","十月","十一月","十二月"]
#天數
year=int(input("請輸入年分: "))
print()
d=0
y=1900
while y<year:
  if (y%100!=0 and y%4==0) or y%400==0:
    d+=366
  else :
    d+=365
  y+=1
    
#元旦判斷    
t=d%7

#日曆
for month in range(1,13):
    print(Month[month-1])
    print("一","二","三","四","五","六","日")
    #本月天數
    if month%2!=0 or month==8:
        day=32
    elif month==2:
        if (y%100!=0 and y%4==0) or y%400==0:
            day=30
        else:
            day=29
    else:
        day=31
    #月初排版
    if month==1:
        pass
    elif month==2:
        t=((31%7)+t)%7
    else:
        t=(((d-1)%7)+t)%7
    for i in range(t):
        print("   ",end="")
    #日期排版
    for date in range(1,day):
        if date<10:
            print(" ",end="")
        if (date+t)%7==0:
            print(date)
        else:
            print(date,"",end="")
    print()
    print()
