import re
text = '''Он --- серо-буро-малиновая редиска!! 
>>>:-> 
А не кот. 
www.kot.ru'''
print(len(re.findall(r'[А-Я|а-я]\w+',text)))