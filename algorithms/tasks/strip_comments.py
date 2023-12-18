"""Complete the solution so that it strips all text that follows any of a set of comment markers passed in. 
Any whitespace at the end of the line should also be stripped out.

Example:

Given an input string of:

apples, pears # and bananas
grapes
bananas !apples
The output expected would be:

apples, pears
grapes
bananas""" 


"""def strip_comments(strng, markers):
    str = strng.split('\n')
    for i in range(len(str)):
        for mark in markers:
            if mark in str[i]:
                str[i] = str[i].split(mark)[0].rstrip()
    return '\n'.join(str)""" 

def domain_name(url):
    if url[:7] == 'http://':
        url = url[7:]
    elif url[:8] == 'https://':
        url = url[8:] 
    if url[:4] == 'www.':
        url = url[4:]
    url_domain = url.split('/')[0:]
    res1 = url_domain[0]
    res = ''
    for i in res1:
        res += i
        if i == '.':
            break
    return res.replace('.', '')


print(domain_name("http://www.codewars.com/kata/"))