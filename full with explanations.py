d = {'a': '.-', 'b': '- ...', 'c': '-.-.', 'd': '-..', 'e': '.', 'f': '..-.', 'g': '--.',
         'h': '....',
         'i': '..', 'j': '.---', 'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.', 'o': '---',
         'p': '.--.', 'q': '--.-', 'r': '.-.',
         's': '...', 't': '-', 'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-', 'y': '-.--',
         'z': '--..', ' ': ' ', '  ': ''}

decode = {value: key for key, value in d.items()}


def encode_to_morse(text):
    text = list(text.lower())
    trans = list()
    for i in text:
        trans.append(d[i])
    print(' '.join(trans))


def decode_from_morse(code):
    trans = list()
    code = code.replace('  ', ' ').split(' ') # Преобразовываем code в список для дальнейших преобразований
    for i in(code):
        trans.append(decode[i]) # Добавляем к списку trans преобразованные символы
    print(''.join(trans).capitalize().replace('  ',' ')) # Преобразовываем список в строку и выводим его

def main():
    do = ''
    while do != 'стоп1':
        do = input('Что вы ходите сделать? Кодировать или декодировать(для остановки напишите "стоп1"): ').lower()
        if do == 'кодировать':
            text = input('Введите предложение(без цифр и специальных знаков): ')
            encode_to_morse(text)
        elif do == 'декодировать':
            code = input('Введите код морзе(после каждой буквы один пробел, слова - два): ')
            decode_from_morse(code)


main()