def pig_it(text):
    words = []
    for w in text.split():
        if w == '!' or w == '.' or w == '?':
            words.append(w)
        else:
            words.append(w[1:] + w[0] + 'ay')

    return ' '.join(words)


print(pig_it('Pig latin is cool'))  # 'igPay atinlay siay oolcay'
print(pig_it('This is my string'))  # 'hisTay siay ymay tringsay'
print(pig_it('Hello world !'))  # elloHay orldway !
print(pig_it('Quis custodiet ipsos custodes ?'))  # 'uisQay ustodietcay psosiay ustodescay ?
