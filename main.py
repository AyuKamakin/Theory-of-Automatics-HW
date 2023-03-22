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
correction={'1101':[], '0011':[]}
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
                if sum not in correction[cc]:
                    correction[cc].append(sum)

print(tabulate(data, headers=alldes.keys(), tablefmt="fancy_grid", showindex="always")) #
print(alldes)
a=input()
while a!='E':
    word1=''
    sum=[]
    sum2=[]
    word2=''
    corr=[]
    rsum=''
    sumR=int(a.split()[0])+int(a.split()[1])
    sumR=str(sumR)
    for i in sumR:
        rsum=rsum+alldes[int(i)]
    for i in range(0, len(a.split()[0])):
        word1+=alldes[int(a.split()[0][i])]
        word2+=alldes[int(a.split()[1][i])]
        sum.append(goThrough(alldes[int(a.split()[0][i])],alldes[int(a.split()[1][i])]))
        if int(a.split()[0][i])+int(a.split()[1][i])<10:
            sum2.append(goThrough(sum[-1], '1101'))
            corr.append('1101')
        else:
            sum2.append(goThrough(sum[-1], '0011'))
            corr.append('0011')

    print(" "+word1)
    print("+")
    print(" "+word2)
    print(' ------------')
    print(" ", end='')
    for i in reversed(sum):
        print(i, end='')
    print("\n+\n ", end='')
    for i in reversed(corr):
        print(i, end='')
    print("\n ------------\n ", end='')
    for i in reversed(sum2):
        print(i, end='')
    print("\n ------------\n ", end='')
    print('верная сумма: '+rsum)
    a=input()
a=input()
while a!='E':
    for j in correction.keys():
        for i in correction[j]:
            if i==a:
                print(j)
    a = input()
