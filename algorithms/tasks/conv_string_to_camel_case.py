"""Complete the method/function so that it converts dash/underscore delimited words into camel casing. 
The first word within the output should be capitalized only if the original word was capitalized (known as Upper Camel Case, also often referred to as Pascal case). The next words should be always capitalized.

Examples
"the-stealth-warrior" gets converted to "theStealthWarrior"

"The_Stealth_Warrior" gets converted to "TheStealthWarrior"

"The_Stealth-Warrior" gets converted to "TheStealthWarrior" """ 


def to_camel_case(text):
    string = text.replace('-', ' ').replace('_', ' ') 
    string = string.split()
    if len(string) == 0:
        return text
    return string[0] + ''.join([x.capitalize() for x in string[1:]]) 

s = "The_Stealth-Warrior"
print(to_camel_case(s))