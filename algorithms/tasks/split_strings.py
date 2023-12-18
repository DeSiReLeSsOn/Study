"""Complete the solution so that it splits the string into pairs of two characters. 
If the string contains an odd number of characters then it should replace the missing second character of the final pair with an underscore ('_').

Examples:

* 'abc' =>  ['ab', 'c_']
* 'abcdef' => ['ab', 'cd', 'ef']"""


def split_string(s):
    res = []
    if len(s) % 2 != 0:
        s += '_'
    for i in range(0, len(s), 2):
        res.append(s[i:i+2]) 
    return res


s = 'abc' 
print(split_string(s))