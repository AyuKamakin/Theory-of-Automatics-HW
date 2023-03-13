from tabulate import tabulate
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
for i in alldes.keys():
    data.append([])
    for j in alldes.keys():
        sum=binary_sum(alldes[i], alldes[j])[2:]
        if len(sum)>4:
            sum=sum[3:]
        sumR=i+j
        if sumR>=10:
            sumR=sumR-10
        sum='0'*(4-len(sum))+sum
        data[int(i)].append(alldes[sumR]+'\n'+sum)
        sum = '0' * (4 - len(sum)) + sum
        for cc in ('0011','0111','1101'):
            sumK= binary_sum(sum, cc)[2:]
            if len(sumK)>4:
                sumK=sumK[1:]
            sumK = '0' * (4 - len(sumK)) + sumK
            if alldes[sumR]==sumK:
                data[int(i)][int(j)] += '\n' + 'коррект '+cc+': '+sumK
print(tabulate(data, headers=alldes.keys(), tablefmt="fancy_grid", showindex="always"))