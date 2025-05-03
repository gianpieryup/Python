size_array = int(input())

string = " 1 2 3" #input() # "1 2 3"
string_splt = string.strip().split(" ")
original=[]
for s in string_splt:
    e = int(s)
    original.append(e)

res = [] # creo que no es necesario
for i in range(size_array):
    n = original[i-1] + original[(i+1) % size_array]
    print(n, end=" ")
    res.append(n)

