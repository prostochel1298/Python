import re
text = '''Иван Иванович! 
Нужен ответ на письмо от ivanoff@ivan-chai.ru. 
Не забудьте поставить в копию 
serge'o-lupin@mail.ru- это важно.'''
pattern = r"['-A-Z|a-z0-9]+@[A-Z|a-z-]+[.A-Z|a-z-]{2,3}"
matcs = re.findall(pattern,text)
print(matcs)