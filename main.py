from tabulate import tabulate
def secsum(a, b, c):
    s=str(a)+str(b)+str(c)
    meaning='0'
    perenos='0'
    if s.count('1')==2:
        perenos=1
    elif s.count('1')==3:
        perenos=1
        meaning='1'
    elif s.count('1')==1:
        meaning='1'
    return [meaning,perenos]
def goThrough(num1, num2):
    res=secsum(str(num1)[-1], str(num2)[-1],'0')[0]
    p=secsum(str(num1)[-1], str(num2)[-1],'0')[1]
    if len(str(num1))>len(str(num2)):
        num2=(len(num1)-len(num2))*'0'+num2
    elif len(num1)<len(num2):
        num1=(len(num2)-len(num1))*'0'+num1
    for i in range(-2, -len(num1)-1, -1):
        res=secsum(str(num1)[i], str(num2)[i],p)[0]+res
        p=secsum(str(num1)[i], str(num2)[i],p)[1]
    return res
a = "1101"
b = "1001"
dop='0011'
allBIN=[]
allDESCOD=[]
alldes={}
correction={}
binary_sum = lambda a, b: bin(int(a, 2) + int(b, 2))
for a1 in '0','1':
    for a2 in '0', '1':
        for a3 in '0', '1':
            for a4 in '0', '1':
                allBIN.append(a1 + a2 + a3 + a4)
                if int(a1+a2+a3+a4,2) <=9:
                    alldes[int(a1+a2+a3+a4,2)]=binary_sum(a1+a2+a3+a4, dop)[2:]
for i in alldes.keys():
    if len(alldes[i])<4:
        alldes[i]='0'*(4-len(alldes[i]))+alldes[i]
print(alldes)
print('сверху ожидаемое значение, под ним посчитанное, под подсчитанным коррекция, внизу итог')
data=[]
res={}
for i in alldes.keys():
    data.append([])
    for j in alldes.keys():
        sum=goThrough(alldes[i], alldes[j])
        sumR=i+j
        if sumR>=10:
            sumR=sumR-10
        data[int(i)].append(alldes[sumR]+'\n'+sum)
        for cc in ('0011','0111','1101'):
            sumK= goThrough(sum, cc)
            if alldes[sumR]==sumK:
                data[int(i)][int(j)] += '\n' + 'коррект '+cc+': '+sumK

print(tabulate(data, headers=alldes.keys(), tablefmt="fancy_grid", showindex="always")) #
