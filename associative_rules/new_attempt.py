import itertools


def generate_data():
    data = []
    for i in range(10):
        data.append(i)
    return data


def out_data(data):
    print('-' * 50)
    for i in range(len(data)):
        print(f'Элемент {i} = {data[i]}')
    print('-' * 50)


def generate_combinations(data, count_comb):
    all_comb = []
    for count_item in range(1, count_comb + 1):
        permutation = itertools.permutations(data, count_item)
        comb_not_sort = []
        for comb in permutation:
            print(list(comb))
            comb_not_sort.append(list(comb))
        all_comb.append(comb_not_sort)
    print('=' * 50)
    comb_to_item = []
    permutation = itertools.permutations([0, 1, 2, 3], 2)
    for i in permutation:
        comb_to_item.append(list(i))
    return comb_to_item, all_comb


def generate_data_to_sort(comb_indexes, all_comb):
    all_data_comb = []
    for mass_comb_item in comb_indexes:
        mass_index_1 = mass_comb_item[0]
        mass_index_2 = mass_comb_item[1]
        for mass_1 in range(len(all_comb[mass_index_1])):
            for mass_2 in range(len(all_comb[mass_index_2])):
                all_data_comb.append([all_comb[mass_index_1][mass_1], all_comb[mass_index_2][mass_2]])
    print(len(all_data_comb))
    print(all_data_comb)


if __name__ == '__main__':
    unique_product = generate_data()
    out_data(unique_product)
    combination_indexes, all_combinations = generate_combinations(unique_product, 3)
    generate_data_to_sort(combination_indexes, all_combinations)
