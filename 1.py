words = []

with open('text.txt', 'r', encoding='utf-8') as f:
    old_text = f.read()
    text = old_text.split()
for word in text:
    if 'абв' in word:
        if not word.isalpha():  # проверка на знаки препинания
            if not word[-1].isalpha():  # проверка, что это не дефис
                words[-1] = words[-1] + word[-1]


    else:
        words.append(word)
print('Старый текст:\n')
print(old_text)
print('Старый текст:\n')
print(' '.join(words))
