def main():
    do = ''
    while do != 'стоп1':
        do = input('Что вы ходите сделать?Кодировать или декодировать(для остановки напишите "стоп1"').lower()
        if do == 'кодировать':
            text = input('Введите текст')
            encode_to_morse(text)
        elif do == 'декодировать':
            code = input('Введите код морзе(после каждой буквы один пробел, слова - два')
            decode_from_morse(code)
