#Hangman Project
import random
print(
    '''
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/ 
''')
stages = [

'''
+---+
|   |
O   |
/|\ |
/ \ |
    |
======
'''
,'''
+---+
|   |
O   |
/|\ |
/   |
    |
======
'''
,'''
+---+
|   |
O   |
/|\ |
    |
    |
======

'''    
,'''
+---+
|   |
O   |
/|  |
    |
    |
======
'''
,'''
+---+
|   |
O   |
|   |
    |
    |
======
''' 
    ,'''
+--+ 
 |  |
 O  |
    |
    | 
    |
=====
''',
'''
+--+     
 |  |
    |
    |
    |
    |       
===== 
''']
word_list = ["monkey", "lion", "donkey", "tiger", "deer"]
#TODO-07
lives = 6

# TODO-1 Randomly choose a word from the word list and assign it to a variable called chosen_word
random.shuffle(word_list)
# chosen_word = random.choice(word_list) this can be used as well
chosen_word = word_list[random.randint(0,len(word_list)-1)]
# TODO-4 Create an empty list called display. for each letter in chosen word add a "_" to display
display = []
for char in chosen_word:
    display.append('_')
    # display+= "_"  this can also be used
print(chosen_word)
print(display)
# TODO-2 Ask the user to guess a letter and assign their answer to a variable called guess. make guess lowercase
# TODO-6 user a while loop to let the user guess again. the loop should only stop once the user has guessed all the
# letters in the chosen_word and display has no more blanks then you can tell user they have won
end_of_game = False
while not end_of_game == True:
    guess = input("Guess a letter: ").lower()
    # print(guess)
    if guess in display:
        print(f"You have already guessed the letter {guess}. Guess another one!")
    else:   
        # TODO-3 Check if the letter the user guessed (guess) is one of the letters in the chosen word
        for ans in range(0, len(chosen_word)):
            if guess in chosen_word[ans]:      #if guess == chosen_word[ans] this can be used as well
        # TODO-5 Loop through each position in chosen_word if the letter at position matches guess then reveal that letter in
        # the display at that position
                display[ans] = chosen_word[ans]
                # print("Right")
    
            #TODO-08
        if guess not in chosen_word:
            print(stages[lives])
            lives = lives-1
            print(f"The letter {guess} is not in the word. You lost a life.")
            if lives < 0:
                end_of_game = True
                print("You Lose!")
        print(display)
        # for ans in chosen_word:
            # if guess == ans:
            #     print("Right")
            # else:
            #     print("Wrong")
    # TODO-6 user a while loop to let the user guess again. the loop should only stop once the user has guessed all the
    # letters in the chosen_word and display has no more blanks then you can tell user they have won
        if "_" not in display:
            end_of_game = True
            print("You Win!")
            print("".join(display).upper())
        
