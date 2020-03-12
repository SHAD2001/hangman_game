import random
import sys



#List of the arguments
fruits = ['apple','pineapple','orange']
sports = ['football', 'cricket','volleyball']


#I HAVE ADDED ALL THE ARGUMENTS IN A DICTIONARY THROUGH LIST
# YOU CAN ADD MORE ARGUMENTS HERE!
arguments = {'fruits':['apple','pineapple','orange'],'sports':['football', 'cricket','volleyball']}


#choose an argument
while True:
    the_choice = input(f'choose one of the following argument; {arguments.keys()} --> ')

# This is more OPTIMIZE than block of code down below
    if the_choice not in arguments.keys():
        print('opps')
        continue
    else:
        word = random.choice(arguments[the_choice])
        break
# ///////////////////////////////////////////////////

    # if the_choice.lower()[0] == 'f':
    #     word = random.choice(fruits)
    #     break
    # elif the_choice.lower()[0] == 's':
    #     word = random.choice(sports)
    #     break
    # else:
    #     print(f'Please one of the following arguments;  Fruits or Sports.')
    #     continue

# /////////////////////////////////////////////

print('The word contains', len(word), 'letters.')


#func spliting the word.
def split_word(word):
    return [lett for lett in word]

# Choosing the random lett from 'word'
word_stg = split_word(word)
random_choice = random.choice(word_stg)

print('Hint latter is -->',random_choice)
print('Position of the letter is', word_stg.index(random_choice) + 1)


body_parts = ['left leg','right leg','body','right arm','left arm','head']



# The main loop for the game!
while len(word_stg) > 0:

    try:
        ask_let = input('Insert a letter: ')
        if ask_let.lower()[0] in word_stg:
            word_stg.remove(ask_let.lower()[0])
            print('Yes good remains; ', len(word_stg)+1, 'letters')
        else:
            if len(body_parts) > 0:
                print(body_parts[0])
                body_parts.pop(0)
                print('[+ WARNING]',len(body_parts)+1,'more attempts remaining!')
                continue
            else:
                if len(body_parts) < 1:
                    print('GAME OVER! MAN HANGED (or women hanged whatever)')
                    break


    # If you exit from the game it will print the following
    except KeyboardInterrupt:
        print('CTRL-C Quitting the game....')
        print('Gome closed!')
        sys.exit()
