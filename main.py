# -*- coding: utf-8 -*-
from prettytable import PrettyTable
import math


def find(arr, element):
    for i in range(len(arr)):
        if arr[i] == element:
            return 1
    return 0


def conctostr(arr, razd):
    result = ""
    for i in range(len(arr)):
        if i != 0:
            result = result + f"{razd}{arr[i]}"
        else:
            result = arr[i]
    return result


def main():
    Sup = 0.8
    Sdown = 0.2
    Cup = 0.8
    Cdown = 0.2

    foods = []
    poolofdeals = []

    def getAssaciation(Aprint, Bprint):
        A = Aprint.split(', ')
        B = Bprint.split(', ')

        # проверим коректность
        for i in range(len(A)):
            el = A[i]
            if find(foods, el) == 0:
                print(f"отсуствует элемент {el}")
                return
        for i in range(len(B)):
            el = B[i]
            if find(foods, el) == 0:
                print(f"отсуствует элемент {el}")
                return
        ABsum = 0
        Asum = 0
        Bsum = 0
        for i in range(len(poolofdeals)):
            f = 0
            for k in range(len(A)):
                if find(poolofdeals[i], A[k]) == 0:
                    break
            else:
                Asum = Asum + 1
                f = 1
            for k in range(len(B)):
                if find(poolofdeals[i], B[k]) == 0:
                    break
            else:
                Bsum = Bsum + 1
                if f == 1:
                    ABsum = ABsum + 1
        SAB = ABsum / len(poolofdeals)
        if Asum != 0:
            CAB = ABsum / Asum
        else:
            CAB = 0
        SB = Bsum / len(poolofdeals)
        LAB = CAB / SB
        return [Aprint, Bprint, SAB, CAB, LAB]

    f = open('checs.txt')
    l = []
    for line in f:
        i = line.find('\n')
        if i != -1:
            line = line[:i]
        l.append(line.split('/'))
    for i in range(len(l)):
        num = l[i][0]
        index = -1
        for j in range(len(poolofdeals)):
            if poolofdeals[j][0] == num:
                index = j
                break
        for j in range(len(l[i])):
            if j != 0 and find(foods, l[i][j]) == 0:
                foods.append(l[i][j])
        if index == -1:
            poolofdeals.append(l[i])
            poolofdeals.sort(key=lambda x: x[0])
        else:
            for j in range(len(l[i])):
                if j != 0:
                    if find(poolofdeals[index], l[i][j]) == 0:
                        poolofdeals[index].append(l[i][j])
    foods.sort()
    print(poolofdeals)
    print(foods)
    print()
    reterntabl = PrettyTable()
    reterntablsize = 1
    reterntabl.field_names = ["номер", "правило", "следствие", "потдержка", "достоверность", "лифт"]
    workingCombinations = foods
    for i in range(len(foods)):
        print(i)
        combinations = []
        for j in range(len(workingCombinations)):
            for k in range(len(foods)):
                if find(workingCombinations[j].split(', '), foods[k]) == 0:
                    split = workingCombinations[j].split(', ')
                    split.append(foods[k])
                    split.sort()
                    split = conctostr(split, ', ')
                    result = getAssaciation(workingCombinations[j], foods[k])
                    print(result)
                    if (result[2] <= Sup and result[2] >= Sdown and result[3] <= Cup and result[3] >= Cdown):
                        reterntabl.add_row([reterntablsize, result[0], result[1], result[2], result[3], result[4]])
                        reterntablsize = reterntablsize + 1
                        if find(combinations, split) == 0:
                            combinations.append(split)
        workingCombinations = combinations
    print(reterntabl)


if __name__ == '__main__':
    main()
