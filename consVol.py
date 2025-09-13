# To find the character is vowel or consonant


def isVowel(c):

    c=c.upper()
    return c == 'A' or c == 'E' or c == 'I' or c == 'O' or c == 'U'


c = 'f'

if not c.isalpha():
    print("Non alphabet")
elif isVowel(c):
    print(c, "is a Vowel")
else:
    print(c, "is a consonant")