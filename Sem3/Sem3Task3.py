#Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
#Каждый кортеж хранит информацию об отдельном товаре.
#В кортеже должно быть два элемента — номер товара и словарь с параметрами
#(характеристиками товара: название, цена, количество, единица измерения).
#Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.

def dict_complet():
    name = input('Введите название товара: ')
    price = int(input('Введите цену товара: '))
    count = int(input('Введите количество товара: '))
    unit = input('Введите единицу измерения товара: ')
    my_dict = {"название": name, "цена": price, "количество": count, "eд": unit}
    return my_dict

def create_structure(n):
    my_list = []
    for i in range(n):
        my_tuple = (i + 1, dict_complet())
        my_list.append(my_tuple)
    return my_list

def product_analytics(my_list):
    name_list = list()
    price_list = list()
    count_list = list()
    unit_list = list()
    for i in range(len(my_list)):
        my_dict = my_list[i]
        val = list(my_dict[1].values())
        name_list.append(val[0])
        price_list.append(val[1])
        count_list.append(val[2])
        unit_list.append(val[3])
    my_dict_res = {"Названия": name_list, "Цены": price_list,
                   "Количества": count_list, "Ед": list(set(unit_list))}
    return my_dict_res

number_of_goods = int(input('Введите количество товаров в базе данных: '))
res = create_structure(number_of_goods)
print()
print('База данных "Товары"')
for i in range(len(res)):
    print(res[i], sep="\n")
print()
print("Аналитика о товарах:")
result = product_analytics(res)
for key, value in result.items():
    print(key, ':', value)
