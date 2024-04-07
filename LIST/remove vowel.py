def novowel(s):
    if s not in 'AEIOUaeiou':
        return s
        
string = 'abcgerdfgio'
consonants = list(filter(novowel,string))
consonants_str = ''.join(consonants)
print(consonants_str)
