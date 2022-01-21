def even_num():
    even_list = []

    for i in range(1, 51):
        if i % 2 == 0:
            even_list.append(i)

    return even_list


print(even_num())