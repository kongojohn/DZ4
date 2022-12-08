# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.

#--------проверка на доступность модуля
f = 0
try:
    f = open ('HWork_4_4_Polynomial_Gen.py')
    from HWork_4_4_Polynomial_Gen import polynomial_gen
    from HWork_4_4_Polynomial_Gen import string_gen
    f.close()
except FileNotFoundError:
    print ()

file1 = 'file1.txt'
file2 = 'file2.txt'


if f == 0:
    print ("модуль генерации не доступен")
else:
    f = input("Будем использовать генератор? (y - да): ")
    if f == 'y':
        polynomial_gen(file1)
        polynomial_gen(file2)

file1 = open (file1)
file2 = open (file2)

def strig_filter (file_in):
    list_file = file_in.read()
    print (list_file, ' <-- строка из файла')

    simbol = False
    temp_list = ''
    for i in list_file:
        if i.isdigit():
            temp_list = temp_list + i
            simbol = False
        elif not simbol:
                temp_list = temp_list + ' '
                simbol = True

    return [int(x) for x in temp_list.split(' ')]

file1_num_list = strig_filter (file1)
file1_num_list.reverse()
file2_num_list = strig_filter (file2)
file2_num_list.reverse()


result = list(zip(file1_num_list,file2_num_list)) 

for i in range(0,len(result),2): 
    result[i] = sum(result[i])

result = [result[x] for x in range(0,len(result),2)]

print (file1_num_list)
print (file2_num_list)
print (result)
print ()

if not f == 0: 
    print (string_gen(result), " <-- почти получилось ")





file1.close()
file2.close()