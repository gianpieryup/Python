# "Usare tuplas para aprovechar lo de % por print"
# lista = [0 for x in range(10)] # lista = [0,0,0,0,0,0,0,0,0,0]
# incremento = list(range(10)) # incremento = [0,1,2,3,4,5,6,7,8,9]

# print("       0   1   2   3   4   5   6   7   8   9")
# print("---------------------------------------------")
# print('%d: %5d %3d %3d %3d %3d %3d %3d %3d %3d %3d' % tuple([0]+lista))
# for x in range(1,10):
#     for i in range(10):
#         lista[i]+=incremento[i]
#     print('%d: %5d %3d %3d %3d %3d %3d %3d %3d %3d %3d' % tuple([x]+lista))
    
    
# Se pude usar solamente prints
print('-'*44)
for x in range(10):
    print(f'{x}:  ',end='')
    for i in range(10):
        print(f'{x*i:3} ',end='')
    print()
    