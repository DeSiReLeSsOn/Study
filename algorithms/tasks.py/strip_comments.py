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


def strip_comments(strng, markers):
    str = strng.split('\n')
    for i in range(len(str)):
        for mark in markers:
            if mark in str[i]:
                str[i] = str[i].split(mark)[0].rstrip()
    return '\n'.join(str)