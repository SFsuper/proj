d = {'a': '.-', 'b': '- ...', 'c': '-.-.', 'd': '-..', 'e': '.', 'f': '..-.', 'g': '--.',
         'h': '....',
         'i': '..', 'j': '.---', 'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.', 'o': '---',
         'p': '.--.', 'q': '--.-', 'r': '.-.',
         's': '...', 't': '-', 'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-', 'y': '-.--',
         'z': '--..', ' ': ' '}
def encode_to_morse(text):
    text = list(text)
    trans = list()
    for i in text:
        trans.append(d[i])


    print(' '.join(trans))

encode_to_morse(input())