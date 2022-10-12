# Напишите программу, удаляющую из текста все слова, содержащие "абв".

text = 'Хотел я, ириабвкк конечно, попить воылрабввабв вина, но придётся всё же квабвсить сделать эту домашнюю аквабврель работу...'
tfind = 'абв'
print(text)

tempList = text.split()
textResult = ''
for i in range(len(tempList) - 1, -1, -1):
    if not tfind in tempList[i]:
        textResult = tempList[i] + ' ' + textResult
print(f'Результат удаления "{tfind}" из текста:')
print(textResult)
