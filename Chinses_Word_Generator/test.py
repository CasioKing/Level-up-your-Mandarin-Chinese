import random
import time

score = 0
total = 0

def you_Guess():
    global score
    global total
    value = random.randint(1, 11)
    print('What number am I thinking of?')
    the_Answer = input()
    time.sleep(1)
    print(value)
    if value == the_Answer:
        print('correct')
        score += 1
        total += 1
    else:
        print('wrong')
        total += 1


def the_Test():
    global score
    global total
    define = input()
    while total <= 100:
        you_Guess()
        define
        if define == 'Finish'.lower():
            break


