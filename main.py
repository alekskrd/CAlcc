"""Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
"""

def del_w(text_w):
    text_w = input('Введите текст где присутствует слово АБВ: ')
    text_w = list(filter(lambda x: 'абв' not in x, text_w.split()))
    return " ".join(text_w)


text_w = del_w(text_w=0)
print(text_w)


"""Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

"""


def data():
    data = input('Введите данные: ')
    cout = 1
    for i in range(len(data) - 1):
        if i <= len(data):
            if data[i] == data[i + 1]:
                cout += 1
            else:
                a = data[i]
                print(cout, data[i])
                cout = 1
    print(cout, data[i])



