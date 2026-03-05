import random
lettersList = [
'a','b','c','d','e','f','g','h','i','j','k','l','m',
'n','o','p','q','r','s','t','u','v','w','x','y','z',
'A','B','C','D','E','F','G','H','I','J','K','L','M',
'N','O','P','Q','R','S','T','U','V','W','X','Y','Z'
]
numbersList = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbolsList = [
'!', '@', '#', '$', '%', '^', '&', '*', '(', ')',
'-', '_', '=', '+', '[', ']', '{', '}', ';', ':',
"'", '"', ',', '.', '<', '>', '/', '?', '\\', '|',
'`', '~'
]
letters = int(input("How many letters would you like in your password? "))
symbols = int(input("How many symbols would you like in your password? "))
numbers = int(input("How many numbers would you like in your password? "))

generatedPass = []
random.shuffle(lettersList)
random.shuffle(numbersList)
random.shuffle(symbolsList)
for letter in range(0,letters):
    generatedPass.append(lettersList[letter])
for symbol in range(0,symbols):
    generatedPass.append(symbolsList[symbol])
for number in range(0, numbers):
    generatedPass.append(numbersList[number])
random.shuffle(generatedPass)
finalPass = ""
finalPass.join(generatedPass)
print(finalPass)