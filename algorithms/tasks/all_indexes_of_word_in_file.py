

def find_word_indexes(text:str, word:str) -> list:
    start = 0 
    res = []
    while True:
        index = text.find(word, start)
        if index == -1:
            break 
        res.append(index)
        start = index + len(word)
    return res 



text = 'alright word and word so word in the world' 
    
print(find_word_indexes(text, 'word'))