import random
import stdio

numbers = '1234567890'
letters = 'qwertyuiopasdfghjklzxcvbnm'
letters_caps = 'QWERTYUIOPLKJHGFDSAZXCVBNM'
symbols = '!@#$%^&*()_+=~`:"<>?|\;,."`'

def create_password(leng):
    """Creates a random password.
    Arguments - leng, an integer, has to be multiple of 4.

    """
    password = ''
    lis = []
    for i in range(leng / 4):
        randnum = numbers[random.randrange(0, len(numbers))]
        lis.append(randnum)
        randletter = letters[random.randrange(0, len(letters))]
        lis.append(randletter)
        randletter_cap = letters_caps[random.randrange(0, len(letters_caps))]
        lis.append(randletter_cap)
        randsymbol = symbols[random.randrange(0, len(symbols))]
        lis.append(randsymbol)
    for items in lis:
        password += random.choice(lis)
    return password


def password(leng):
    password = ''
    lis = []
    for i in range(leng):
        mod = i % 4
        if mod == 0:
            randitem = numbers[random.randrange(0, len(numbers))]
        elif mod == 1:
            randitem = letters[random.randrange(0, len(letters))]
        elif mod == 2:
            randitem = letters_caps[random.randrange(0, len(letters_caps))]
        else:
            randitem = symbols[random.randrange(0, len(symbols))]
        lis.append(randitem)
    for item in lis:
        password += item
    return password


def write_pass_to_file(filename, leng, numofpass):
    counter = 1
    with open(filename, 'r+') as myfile:
        myfile.write("Here are your passwords!\n\n\n")
        for i in range(numofpass):
            password = create_password(leng)
            myfile.write(str(counter).rjust(4) + ". "  + password + '\n')
            counter += 1

write_pass_to_file('text.txt', 12, 100000)
