def word_reverse(phrase):
    lst = []
    stringg = ""
    split = phrase.split(' ')
    for i in reversed(split):
        lst.append(i)
        
    for i in lst:
        stringg += i + ' '
        
    return (stringg.rstrip())

inp = input('What sentence would you like reversed? ')

print(word_reverse(inp))