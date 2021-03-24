any_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
print(id(any_list))  # первоначальный ID списка
message = ''
message_5 = ''
message_6 = ''
for s in any_list.copy():
    idx_s = any_list.index(s)

    if s[-1::].isnumeric() and s.isalnum():  # условие  ищет числа в списке строк

        any_list[idx_s] = s.zfill(2)
        any_list.insert(idx_s, ' "')  # если находит число, добавляет в список кавычки до и после
        any_list.insert(idx_s + 2, '" ')  # ----//-------
        # ниже условие необходимо, чтобы соединить элементы списка в строку с правильной последовательностью
        if idx_s < 4:
            message_1 = ' '.join(any_list[:idx_s]) + ''.join(any_list[idx_s:idx_s + 3])

        else:
            message_1 = ' '.join(any_list[4:idx_s]) + ''.join(any_list[idx_s:idx_s + 3]) + ' '.join(
                any_list[idx_s + 3:idx_s + 7])
        message_5 += message_1

    # это условие ищет в списке строк числа со знаком и добавляет кавычки в список до числа и после, а за тем
    # объединяет в строку
    elif s[0] == '+' or s[0] == '-':
        any_list[idx_s] = str('+' + str(s[1:].zfill(2)))
        any_list.insert(idx_s, ' "')
        any_list.insert(idx_s + 2, '" ')
        message_1 = ''.join(any_list[idx_s:idx_s + 3]) + ''.join(any_list[idx_s + 3:])

        message_6 += message_1
        message = message_5 + message_6  # итоговая строка

print(any_list)  # выводит список
print(message)  # выводит итоговое сообщение
print(id(any_list))  # выводит ID списка для подтверждения, что он не изменился
