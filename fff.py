def take_large_banknotes(banknotes):
    a = list()
    a.append(banknotes)
    for i in a:
        if i > 10:
            return i
