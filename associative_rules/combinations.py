


def add_x(data):
    new_mass = []
    for item in data:
        new_mass.append(item)
    return new_mass

def print_data(data):
    print('_' * 100)
    for i in data:
        print(i)
    print('_' * 100)


if __name__ == '__main__':
    data = []
    for i in range(28):
        data.append(f'Элемент №{i + 1}')
    print(data)

    mass_group_product = []
    n = len(data)

    for count_items in range(2, 3):
        new = [0] * count_items
        for i in range(count_items - 1):
            start = 0
            for j in range(n):
                new[i] = start
                while new[i + 1] >= n:
                    print(new)
                    mass_group_product.append(add_x(new))
                    # if new[i] == new[i + 1] + 1:
                    #     new[i + 1] += 2
                    # else:
                    new[i + 1] += 1
                else:
                    start += 1
                    new[i+1] = 0
    print_data(mass_group_product)
