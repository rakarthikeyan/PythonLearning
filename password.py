import random
import string

# generate random password of length 8-15
# mandatory - 1 lower, 1 upper, 1 digit, 1 special
# Dash {-}; this character is not supported as the first character in the user ID
# Period {.}; this character is not supported as the first character in the user ID

passLen = random.randint(8, 15)
lcase = string.ascii_lowercase
Ucase = string.ascii_uppercase
digit = string.digits
special = string.punctuation
complete = lcase+Ucase+digit+special

# generate mandatory password string
mandatoryPass = random.choice(
    lcase)+random.choice(Ucase)+random.choice(digit)+random.choice(special)
password = ""

for x in range(passLen-4):
    password = password+random.choice(complete)

MyPassword = password+mandatoryPass

if MyPassword[0] == "-" or MyPassword[0] == ".":
    l = list(MyPassword)
    random.shuffle(l)
    MyPassword = ''.join(l)


print("Random Password Generated : ", MyPassword)
