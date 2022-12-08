# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.


def dublicate_filter (list_num = [1, 1, 2, 3, 4, 2, 1] ):

    result = list(filter(lambda x: list_num.count(x) < 2 , list_num))
    print (result)


if __name__ == '__main__':
    
    list_num = [int(x) for x in input("введите последовательность: ").split()]
    dublicate_filter(list_num) if (not list_num == []) else dublicate_filter()
