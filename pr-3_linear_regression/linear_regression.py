import matplotlib.pyplot as plt
import math

mass = [[1, 13, 1000, 1323.4, 0],
        [2, 20, 600, 305.6, 1],
        [3, 17, 500, 741.8, 0],
        [4, 15, 1200, 1032.6, 1],
        [5, 16, 1000, 887.2, 1],
        [6, 12, 1500, 1468.8, 1],
        [7, 16, 500, 887.2, 0],
        [8, 14, 1200, 1178.0, 1],
        [9, 10, 1700, 1759.6, 0],
        [10, 11, 2000, 1614.2, 1]]


fig = plt.figure(figsize=(10, 7))
axis = fig.add_subplot()
axis.grid()
for i in mass:
    if i[-1] == 0:
        axis.scatter(i[1], i[2], s=50, c='green')
    else:
        axis.scatter(i[1], i[2], s=50, c='r')
plt.xlim(0,25)
plt.ylim(0,2500)
plt.show()

n = len(mass)
summ_x = 0
summ_y = 0
summ_x2 = 0
summ_xy = 0
for i in mass:
    summ_x += i[1]
for i in mass:
    summ_x2 += i[1] ** 2
for i in mass:
    summ_y += i[2]
for i in mass:
    summ_xy += i[1] * i[2]

print('n =', n)
print('summ x =', summ_x)
print('summ x**2 =', summ_x2)
print('summ y =', summ_y)
print('summ xy =', summ_xy)

print(f'b0 * {n} + b1 * {summ_x} = {summ_y}')
print(f'{summ_x} · b0 + {summ_x2} · b1 = {summ_xy} |==| 149300')
print(f'b0 = {summ_y}/{n} - {summ_x}·b1 = {summ_y/n} - {summ_x/n}*b1 ')
print(f'{summ_x} * ({summ_y/n} - {summ_x/n}·b1) + {summ_x**2}·b1 = {mass[0][1]*summ_y}')
b1 = round((-(summ_x * (summ_y/n)) + (summ_xy)) / (summ_x*(-summ_x/n) + (summ_x2)), 3)
print(f'{(-(summ_x * (summ_y/n)) + (summ_xy))} / {(summ_x*(-summ_x/n) + (summ_x2))}')
print(b1)
b0 = round(summ_y/n - summ_x/n*b1, 3)
print(f'{b0} = {summ_y/n} - {summ_x/n} * b1')
print(f'b0 = {b0}')
print(f'b1 = {b1}')
print(f'y^ = {b0} + {b1} * x')
dy = round(b0+b1 * mass[0][1], 3)
print(f'{dy} = {b0} + {b1} * x')
print()

n = len(mass)
summ_x = 0
summ_y = 0
summ_x2 = 0
summ_xy = 0
for i in mass:
    summ_x += i[1]
for i in mass:
    summ_x2 += i[1] ** 2
for i in mass:
    summ_y += i[2]
for i in mass:
    summ_xy += i[1] * i[2]

print('n =', n)
print('summ x =', summ_x)
print('summ x**2 =', summ_x2)
print('summ y =', summ_y)
print('summ xy =', summ_xy)
for i in range(len(mass)):
    b1 = round((-(summ_x * (summ_y/n)) + (summ_xy)) / (summ_x*(-summ_x/n) + (summ_x2)), 3)
    mass[i].append(b1)
    b0 = round(summ_y / n - summ_x / n * b1, 3)
    mass[i].append(b0)
    dy = round(b0 + b1 * mass[i][1], 3)
    mass[i].append(dy)
print()
for i in range(len(mass)):
    print(f'для x = {mass[i][1]} и y = {mass[i][2]}')
    print('b0 =', mass[i][-3])
    print('b1 =', mass[i][-2])
    print('dy =',mass[i][-1])
    print()
Q = 0
for i in mass:
    Q+= i[-1]
print('Q =', Q)
summ_y2 = 0
for i in mass:
    summ_y2 += i[2] **2

summ_for_Ecko = 0
for i in range(len(mass)):
    summ_for_Ecko += (round((mass[i][-1]-mass[i][2])**2, 3))
print('summ_for_Ecko =',summ_for_Ecko)
#%%
m = 1
Ecko = round(summ_for_Ecko/(n-m-1), 3)
print("Ecko =", Ecko)
Ect = round(math.sqrt(Ecko), 3)
print('Ect = ', Ect)

r = (summ_xy - (summ_x * summ_y)/n) / (math.sqrt (summ_x2-(summ_x**2)/n) * math.sqrt(summ_y2 - (summ_y**2) /10))
r = math.sqrt(r**2)
print(f"r = {r}")