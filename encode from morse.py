d = {'a': '.-', 'b': '- ...', 'c': '-.-.', 'd': '-..', 'e': '.', 'f': '..-.', 'g': '--.',
         'h': '....',
         'i': '..', 'j': '.---', 'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.', 'o': '---',
         'p': '.--.', 'q': '--.-', 'r': '.-.',
         's': '...', 't': '-', 'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-', 'y': '-.--',
         'z': '--..', ' ': ''}

decode = {value: key for key, value in d.items()}

def decode_from_morse(code):
    trans = list()
    word = list()
    code = code.replace('  ', ' ').split(' ')
    for i in(code):
        trans.append(decode[i])
    print(''.join(trans).capitalize())