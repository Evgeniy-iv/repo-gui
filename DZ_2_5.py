price_list = [50.21, 245.81, 386.1, 101.87, 55.0, 316.69, 864.72, 862.47, 323.66, 684.51, 663.6, 253.19, 941.1, 787.13,
              629.71, 193.85, 880.57, 784.24, 203.49, 934.77]
print('ID списка:')
print(id(price_list))

price_list = ['{:.2f}'.format(n) for n in price_list]
string = ' '.join(price_list)
string = string.replace(' ', ' коп, ')
string = string.replace('.', ' руб ')

price_list = [float(n) for n in price_list]
price_list.sort()
print('Строка с ценами в формате XX руб, YY коп:\n' + string)

print('Отсортированный по возрастанию список:')
print(price_list)

print('Убеждаемся что ID списка не изменился:')
print(id(price_list))

price_list_reversed = []  # создаем список
price_list.sort(reverse=True)
price_list_reversed.extend(price_list)  # помещаем в него инвертированный список price_list
print(price_list_reversed)  # выводим на экран
print('Убеждаемся что список отсортированый по убыванию - является объектом отличным от price_list:')
print(id(price_list_reversed))
price_five_max = []
price_five_max.extend(price_list_reversed[:5])
price_five_max.sort()
print('Выводим список самых высоких цен по возрастанию:')
print(price_five_max)
