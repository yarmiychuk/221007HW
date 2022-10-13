# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

# Пример: aaaaaaabbbbbbccccccccc => 7a6b9c и 11a3b7c => aaaaaaaaaaabbbccccccc

from random import randint as r

pathCompress = 'compr.txt'
pathDecompress = 'decompr.txt'

def createRandomText():
    text = ''
    for _ in range(0, r(5, 10)):
        text += getSegment(None, None)
    return text

def getSegment(num, letter):
    segment = ''
    if num == None:
        num = r(2, 15)
        letters = 'abcdefghijklmnopqrstuvwxyz'
        letter = letters[r(0, len(letters) - 1)]
    for _ in range(0, num):
        segment += letter
    return segment

def compressText(text):
    result = ''
    letter = ''
    count = 0
    for item in text:
        if item == letter:
            count += 1
        else:
            if letter != '':
                result += str(count) + letter
            letter = item
            count = 1
    if count > 0:
        result += str(count) + letter
    return result

def decompressText(text):
    result = ''
    dig = 0
    for item in text:
        if item.isdigit():
            dig = dig * 10 + int(item)
        else:
            for i in range(0, dig):
                result += item
            dig = 0
    return result

text = createRandomText()
print(f'Сгенерированный случайный текст:\n{text}')

text1 = compressText(text)
print(f'Результат сжатия: {text1}')
with open(pathCompress, 'w') as f:
    f.write(text1)
print(f'Записан в файл {pathCompress}\n')

with open(pathCompress) as f:
    text = f.read()
text = decompressText(text)
print(f'Результат обратной декомпрессии текста:\n{text}')
with open(pathDecompress, 'w') as f:
    f.write(text)
print(f'Записан в файл {pathDecompress}')