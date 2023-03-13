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
        #print(f'a={alldes[i]}={i}, b={alldes[j]}={j}\nright sum in 8421+3={alldes[i+j]}, calculated sum in 8421+3={sum}\n')
        if sum!=alldes[sumR]:
           # if i+j<10:
            #    sum=binary_sum(sum,'1101')[3:]
             #   sum = '0' * (4 - len(sum)) + sum
              #  data[int(i)][int(j)]+='\n'+'1101'+'\n' + sum
            if ('0'*(4-len(binary_sum(sum, '0011')[2:])) + binary_sum(sum, '0011')[2:]) == alldes[sumR]:
                sum = '0' * (4 - len(binary_sum(sum, '0111')[2:])) + binary_sum(sum, '0111')[2:]
                data[int(i)][int(j)] += '\n' + '0011' + '\n' + sum
            elif ('0'*(4-len(binary_sum(sum, '0111')[2:])) + binary_sum(sum, '0111')[2:]) == alldes[sumR]:
                sum = '0' * (4 - len(binary_sum(sum, '0111')[2:])) + binary_sum(sum, '0111')[2:]
                data[int(i)][int(j)] += '\n' + '0111' + '\n' + sum
            elif ('0'*(4-len(binary_sum(sum, '1011')[2:])) + binary_sum(sum, '1011')[2:]) == alldes[sumR]:
                sum = '0' * (4 - len(binary_sum(sum, '1011')[2:])) + binary_sum(sum, '1011')[2:]
                data[int(i)][int(j)] += '\n' + '1011' + '\n' + sum
            elif ('0'*(4-len(binary_sum(sum, '1011')[3:])) + binary_sum(sum, '1011')[3:]) == alldes[sumR]:
                sum = '0' * (4 - len(binary_sum(sum, '1011')[3:])) + binary_sum(sum, '1011')[3:]
                data[int(i)][int(j)] += '\n' + '1011' + '\n' + sum
            #if alldes[i+j]==sum:
                #print(f'a={a}={i}\nb={b}={j}\nright sum in 8421+3={alldes[i+j]}\ncalculated sum in 8421+3={sum}')
#print(f'{a} = {int(a,2)} \n{b} = {int(b,2)} \n{binary_sum(a, b)[2:]}, {int(binary_sum(a, b)[2:],2)}')
print(tabulate(data, headers=alldes.keys(), tablefmt="fancy_grid", showindex="always"))
