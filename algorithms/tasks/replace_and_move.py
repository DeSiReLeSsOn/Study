"""Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched."""


def pig_it(text):
    res = []
    word = text.split(' ')
    for i in word:
        if i.isalpha():
            new_words = i[1:] + i[0] + 'ay'
            res.append(new_words)
        else:
            res.append(i)
    return ' '.join(res) 