
#Dictionaries
myDict = {
    "Name": "Adil",
    "Surname": "Nawaz",
    "Age":  34,
    "City": "Gujrat"
}
print(myDict["Name"]) #Retrieving item from dictionary
print(len(myDict))
#Adding new item into dictionary
myDict["Profession"] = "Govt. Employee"
print(len(myDict))
#looping through a dictionary
for key in myDict:
    print(key)
    print(myDict[key])

#Creating a grading program
student_Scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco" : 74,
    "Neville": 62
}
student_Grades = {}
for scores in student_Scores:
    if student_Scores[scores] >= 91 and student_Scores[scores]<=100:
        student_Grades[scores] = "Outstanding"
    elif student_Scores[scores] >= 81 and student_Scores[scores]<=90:
        student_Grades[scores] = "Exceeds expectations"
    elif student_Scores[scores] >= 71 and student_Scores[scores]<=80:
        student_Grades[scores] = "Acceptable"
    else:
        student_Grades[scores] = "Fail"
for grades in student_Grades:
    print(grades)
    print(student_Grades[grades])
    
#Nesting lists and dictionaries
# dictionary = {
# "key": [List],
# "Key2": {dictionary},
# }

capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}

#Dictionary in list exercise
travelLog= [
    {
        "Country": "France",
        "cities_Visited":["Paris", "Lille", "Dijon"], 
        "totalVisits": 12,
        },
    {
        "Country": "Germany",
        "cities_Visited":["Germany", "Hamburg", "Stuttgart"],
        "totalvisits": 10,
        }
]
# def add_new_country(countryName, visits, listOfCities):
#     newCountry =[
#         {
#             "Country": countryName,
#             "cities_Visited":[listOfCities],
#             "totalVisits": visits
#         }
#     ]
#     travelLog.append(newCountry)
#     print(travelLog)

# add_new_country("Russia", 2, ["Moscow", "Saint Peterson", "Kremlin"])
# 2nd method for same work
def add_new_country(countryName, visits, listOfCities):
        newCountry ={}
        newCountry["Country"] = countryName,
        newCountry["cities_Visited"] = listOfCities,
        newCountry["totalVisits"] =  visits
        travelLog.append(newCountry)
        print(travelLog)

add_new_country("Russia", 2, ["Moscow", "Saint Peterson", "Kremlin"])

#Blind Auction Program
import asciiart
import os
print(asciiart.logo)
print("Welcome to secret Auction program.")
bids = {}
def highestBidder(bids):
    maxValue = max(bids.values())
    for key, value in bids.items():
        if value == maxValue:
            name = key
            break
    print(f"The Winner is {name} with the highest bid of ${maxValue}")

# def findHighestBidder(bidding_record):
#     highest_bid = 0
#     winner = ""
#     for bidder in bidding_record:
#         bid_amount = bidding_record[bidder]
#         if bid_amount> highest_bid:
#             highest_bid = bid_amount
#             winner = bidder
#     print(f"The winner is {winner} with a bid of ${highest_bid}")
    
while True:
    name = input("What is your name? ")
    bid  = int(input("What's your bid? $"))
    bids [name]= bid
    anyOther = input("Are there any other bidders? (y/n)").lower()
    if anyOther!="y":
        break
    else:
        os.system("cls")

highestBidder(bids=bids)