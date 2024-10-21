# Слушатель курса Junior Python-разработчик
# Рыжаков Андрей Николаевич, anryzhakov@yandex.ru
# Домашнее задание по теме "Позиционирование в файле"

def custom_write(file_name, strings):
    n = 0
    keys = []
    items = []
    file = open(file_name, "w", encoding='utf-8')
    for item_strings in strings:
        n += 1
        position = (n, file.tell())
        keys.append(position)
        items.append(item_strings)
        file.write(f"{item_strings}\n")
    file.close()
    string = zip(keys, items)
    zipped_dictionary = dict(string)
    return zipped_dictionary



info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)

for elem in result.items():
     print(elem)

# with open(r"myfile.txt", 'r') as fp:
#     lines = len(fp.readlines())
#     print('Total Number of lines:', lines)