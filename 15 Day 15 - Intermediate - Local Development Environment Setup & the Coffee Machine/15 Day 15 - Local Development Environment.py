from menu import MENU
#Coffee machine program
#Makes 3 hot flavors

#The customer must be able to check current status of available ingredients using report
def report(sitRep, money):
    water = sitRep["water"]
    coffee = sitRep["coffee"]
    milk = sitRep["milk"]
    print(f"Water: {water}ml\nMilk: {milk}ml\nCoffee: {coffee}g\nMoney: {money}")
'''
def checkEnoughResources(type,ingred, menu):
        # for items in menu:
        #      if type["ingredients"][items]
        if ingred["water"] < menu[f"{type}"]["ingredients"]["water"] or ingred["coffee"] < menu[f"{type}"]["ingredients"]["coffee"]:
             print("Sorry there is Not enough resources")
        else:
             return 1
        ''' 
def is_resources_enough(order_ingredients):
     for items in order_ingredients:
          if order_ingredients[items]>= ingredients[items]:
               print(f"Sorry not enough {items}")
               return False
          else:
               return True       


def doPayment():
     print("Please insert coins: ")
     quarters = float(input("How many quarters? : ")) * 0.25
     dimes = float(input("How many dimes? : ")) * 0.1
     nickles = float(input("How many nickles? : ")) * 0.05
     pennies = float(input("How many pennies? : ")) * 0.01
     total = quarters + dimes + nickles + pennies
     return total
    #  if total == MENU[type]["cost"]:
    #       return total
    #  elif total < MENU[type]["cost"]:
    #       return 0
    #  elif total > MENU[type]["cost"]:
        
def is_transaction_Successful(money_received, drink_Cost):
     if money_received >= drink_Cost:
          change = round(money_received - drink_Cost,2)
          print(f"Here is #{change} in change.")
          global money
          money += drink_Cost
          return True
     else:
          print("Sorry not enough money. Money refunded.")
          return False
    
def makeCoffee(drinkName, order_ingredients):
     for item in order_ingredients:
          ingredients[item] -= order_ingredients[item]
    
     print(f"Here is your {drinkName} ")
#123123
money = 0
ingredients = {
    "water": 300,
    "coffee": 100,
    "milk": 200
}
#Ask the user about which coffee they would like to order
while True:
    order = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if order == "report":
        report(ingredients, money=money)
        # print(f"Money: ${money}")
    elif order == "off":
        break
    else:
         drink = MENU[order]
         if is_resources_enough(drink["ingredients"]):
         
        #  if checkEnoughResources(type=order, ingred=ingredients,menu=MENU) == 1:
            #   while True:
                    payment = doPayment()
                    if is_transaction_Successful(payment, drink["cost"]):
                         makeCoffee(order, drink["ingredients"])
                         
                    # if payment == 1:
                    #      money += payment
                    #      print("I can make coffee")
                    #     #  break
                    # elif payment == 0:
                    #      print("Sorry that's not enough money. Money refunded")
                    # else:
                    #      refund = round(payment - MENU[order]["cost"], 2)
                    #      money += MENU[order]["cost"]
                    #      print(f"Here is ${refund} in change")

#Tell user to insert coins
#Ask user about how many quarters 0.25, dimes 0.1, nickles 0.05 or pennies 0.01
#If user has given more coins then prompt should appear Here is $ in change
#If user has given less coins then prompt Sorry that's not enough money. Money refunded
#Then prompt Here is your coffeeName Enjoy!
#if user asks about coffee for which any ingredient is low then print Sorry there is not enough 
# ingredientName
