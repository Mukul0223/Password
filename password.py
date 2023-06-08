import random
import string

punctuation = string.punctuation

def shuffle(string):
    templist = list(string)
    random.shuffle(templist)
    random.shuffle(templist)
    return ''.join(templist)

uppercaseLetter1 = chr(random.randint(68,90))
uppercaseLetter2 = chr(random.randint(68,90))
uppercaseLetter3 = chr(random.randint(68,90))
lowercaseLetter4 = chr(random.randint(97,122))
lowercaseLetter5 = chr(random.randint(97,122))
lowercaseLetter6 = chr(random.randint(97,122))
lowercaseLetter7 = chr(random.randint(97,122))
punctuationSign1 = random.choice(punctuation)
punctuationSign1 = random.choice(punctuation)
punctuationSign2 = random.choice(punctuation)
digit = random.randint(0,9)
digit1 = random.randint(0,9)

password = uppercaseLetter1 + uppercaseLetter2 + uppercaseLetter3 + lowercaseLetter4 + lowercaseLetter5 + lowercaseLetter6 +lowercaseLetter7 + str(digit) + str(digit1) + punctuationSign1 + punctuationSign2
password = shuffle(password)

print(f"The password is {password}")
