def yigindi(n):
    sum=0
    for i in range(n+1):
        sum+=i
        m=f'yigindi={sum}'
    return m

n=int(input('n ni kirit: '))
print(yigindi(n))