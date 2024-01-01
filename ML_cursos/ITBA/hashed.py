def error(x,n):
    res = (x*10**-18 + n)**2
    return  res - int(res)
    
def retornar_num(sakura_hash):
    n = 1
    while error(sakura_hash,n) > 10**-15:
        n+=1
    res = (sakura_hash*10**-18 + n)**2
    return int(res)

num = int(input())
for i in range(num):
    h = int(input())
    print(retornar_num(h))