import random

print('Сколько паролей хотите?')
num = int(input())
abc = 'a b c d e f g h i j k l m n o p q r s t u v w x y z'.split()
abcupper = 'a b c d e f g h i j k l m n o p q r s t u v w x y z'.upper().split()
password = ''
allabc = []
allabc.extend(abc)
allabc.extend(abcupper)
passworditems = ['1','2','3','4','5','6','7','8','9','0']
passworditems.extend(allabc)
passwords = []
for i in range(num):
    for j in range(random.randint(8,13)):
        stop = 0
        letter = random.choice(passworditems)
        password = password+letter
        while stop == 0:
            if password[j].isdigit() == True and password[j-1].isdigit() == True and int(password[j-1])+1 == password[j]:
                del password[j]
                letter = random.choice(passworditems)
                password = password + letter
            elif password[j].isdigit() == False:
                stop = 1
            else:
                stop = 1
    passwords.append(password)
    password = ''
print('Вот пароли:',*passwords)