def insertionsort(in_list):
    for idx in range(1, len(in_list)):
        while idx > 0 and in_list[idx] < in_list[idx - 1]:
            in_list[idx], in_list[idx - 1] = in_list[idx - 1], in_list[idx]
            idx -= 1
    return in_list

if __name__ == '__main__':
    print(insertionsort([45, 3, 98, 44, 65, 89, 22, 12, 1]))
