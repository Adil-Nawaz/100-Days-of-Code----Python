#Day 1 no need
#Day 2 String Manipulation
#Adding a 2 digit number 
''' 
number = input("Enter a 2 digit number to add: ")
digit1 = int(number[0])
digit2 = int(number[1])
print(f"Sum of 2 digit number {number} is: {digit1+ digit2}") 

'''
import random
names = [
    "Ayaan", "Zara", "Hamza", "Elena",
    "Rayan", "Sophia", "Daniyal", "Maya",
    "Ibrahim", "Lina", "Arham", "Ava",
    "Saad", "Noor", "Hassan", "Amelia"
]
printList = []
randomName = random.choice(names)
for _ in range(0, len(names)):
    printList.append("_")
print(printList)
for names in printList:
    if randomName != printList[names]:
        printList[names] = randomName
        print(printList)