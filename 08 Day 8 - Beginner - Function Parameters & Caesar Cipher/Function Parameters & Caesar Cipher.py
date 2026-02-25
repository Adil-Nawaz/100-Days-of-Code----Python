#Simple function
def greet():
    print("Hello World")
    print("Hello Adil")
    print("Hello Nawaz")
greet()

#Function that allows for input
def greet_with_Name(name):
    print(f"Hello {name}")
    print(f"How do you do {name}")

greet_with_Name("Adil")

#Functions with more than 1 inputs
def greetMore(name,city, age):
    print(f"Hello {name}")
    print(f"Do you live in {city}?")
    print(f"Are you {age} years of age?")

greetMore("adil","gujrat", 30) #calling with positional arguments
greetMore(name = "umar", age = 46, city="Lahore")

#paint area calculator
def paint_Calc(height, width, cover):
    print(f"You will need {round((height*width)/cover)} cans of paint")

wallHeight = int(input("Height of Wall: "))
wallWidth = int(input("Width of wall: "))
coverage = 5
paint_Calc(height=wallHeight, width=wallWidth, cover=coverage)

#Prime number checker
def primeNumber(num):
    if num <= 1:
        print(f"{num} is not prime")
    else: 
        for i in range(2, num):
            if num %i == 0:
                print(f"{num} is not prime")
                break
        else:
            print(f"{num} is prime")
while True:
    number = int(input("Enter the number to check: "))
    primeNumber(num=number)
    checkAgain = input("Want to check again? (y/n) ")
    if checkAgain != "y":
        break

#Ceaser Cipher
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m',
'n','o','p','q','r','s','t','u','v','w','x','y','z', 'a','b','c','d','e','f','g','h','i','j','k','l','m',
'n','o','p','q','r','s','t','u','v','w','x','y','z'] #we have copied alphabets again so that if z comes in word then index dont get out of range
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: ").lower()
text = input("Type your message: ").lower()
shift = int(input("Type the shift number: "))

# def encrypt(plain_text, shift_amount):
#     cipher_text = ""
#     for letter in plain_text:
#         position = alphabet.index(letter)
#         newPosition = position + shift_amount
#         newLetter = alphabet[newPosition]
#         cipher_text+=newLetter             #.join() not works here because newLetter isn't a sequence
#     print(f"The Encoded text is {cipher_text}")

# def decrypt(encoded_text, rshift_amount):
#     cipher_text = ""
#     for letter in encoded_text:
#         position = alphabet.index(letter)
#         newPosition = position - rshift_amount
#         newLetter = alphabet[newPosition]
#         cipher_text+=newLetter             #.join() not works here because newLetter isn't a sequence
#     print(f"The Decoded text is {cipher_text}")
# if direction == "encode":
#     encrypt(plain_text=text, shift_amount=shift)
# elif direction =="decode":
#     decrypt(encoded_text=text, rshift_amount=shift)
# else:
#     print("Please enter the correct command!")

# def caeser(text, shift, direction):
#     plain_text = ""
#     if direction == "encode":
#         for letter in text:
#             position = alphabet.index(letter)
#             newPosition = position + shift
#             newLetter = alphabet[newPosition]
#             plain_text+=newLetter
#     elif direction == "decode":
#         for letter in text:
#             position = alphabet.index(letter)
#             newPosition = position - shift
#             newLetter = alphabet[newPosition]
#             plain_text+=newLetter
#     else:
#         print("please enter the correct command ")
#     print(f"The {direction}ed text is {plain_text}")


#cipher

# caeser(text=text, shift=shift, direction=direction)

def caeser(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
            shift_amount *= -1
    for letter in start_text:
        position = alphabet.index(letter)
        newposition = position + shift_amount
        end_text += alphabet[newposition]
    print(f"The {direction}ed text is {end_text}")

caeser(start_text=text, shift_amount=shift, cipher_direction=direction)