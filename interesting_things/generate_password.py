# generate random password 

import random
from string import ascii_lowercase, ascii_uppercase


random.seed(5)


def pasw(N):
    string = ''
    chars = ascii_lowercase + ascii_uppercase + "0123456789!?@#$*"
    for j in range(N):
        string = string + chars[random.randint(0,len(chars))]
    yield string 
    string = ''
    
    
N = int(input())
for i in range(5):
    for i in pasw(N):
        print(i)