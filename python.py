def yigindi(n):
    sum=0
    count=1
    for i in range(1,n+1):
        sum+=i
        count*=i
    m=f'yigindi={sum} & kopaytma={count}'
    return m

n=int(input('n ni kirit: '))
print(yigindi(n))