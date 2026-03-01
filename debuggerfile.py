import random
namesList = [
    "Ayaan", "Zara", "Hamza", "Elena",
    "Rayan", "Sophia", "Daniyal", "Maya",
    "Ibrahim", "Lina", "Arham", "Ava",
    "Saad", "Noor", "Hassan", "Amelia"
]
printList = []

for _ in range(0, len(namesList)):
    printList.append("_")
print(printList)


for names in range(0,len(printList)):
    randomName = random.choice(namesList)
    if randomName not in printList:
        printList[names] = randomName
        print(printList)
    else:
        randomName = random.choice(namesList)
        

