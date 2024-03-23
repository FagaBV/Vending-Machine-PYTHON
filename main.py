##  Python 0- Beginner Vending Machine System -0
## Assisted with a salary system in order to check the user balance
## Project 02/23324 ##

##Generating user info
user_name = input("Enter your name: ")
user_age = input("Enter your age: ")
user_email = input("Enter your email: ")

##Creating another variable to include everything, so you don't have to call each function
print_info = user_name, user_age, user_email

##Generating salary info
salary_value = int(input("Enter your salary without taxes: "))
salary_tax = int(input("Enter your country TAX RATE: "))
salary_currency = input("Enter your currency: ")
tax_calculation = salary_tax / 100 * salary_value

#Creating another variable to show the salary without taxes
final_salary = salary_value - tax_calculation

print("Your user info is: ")
print(print_info)

print("Your salary without taxes is: ")
print(final_salary, salary_currency)

##Generating lists with the : Currency Info, Location Selection & Machine Name
machine_names = ["Pepsi&Coke Romania Machine", "Blue Rizz Machine", "Luxury Keys Machine"]
selection_details = ["Brasov, Romania", "New York, USA", "Dubai, UAE"]
currency = ["RON", "USD", "DIRHAM"]
booleans = ["Yes", "No"]

##Generating the variables using the indexes of the lists created above
coke_machine = machine_names[0]
liquor_machine = machine_names[1]
tapes_machine = machine_names[2]
coke_location = selection_details[0]
liquor_location = selection_details[1]
tapes_location = selection_details[2]

##Generating menu & prices for the machines itself

coke_menu = ["Pepsi", "Cola", "Fanta", "Sprite", "7UP"]
coke_prices = [7, 6.50, 6.50, 6, 5.50]
liquor_menu = ["Jack Daniels", "J&B", "Captain Morgan", "Absolut Vodka", "Strongbow"]
liquor_prices = [65, 70, 85, 45]
keys_menu = ["Lamborghini", "Ferrari", "Rolls Royce", "Audi", "Range Rover"]
keys_prices = [124500, 129990, 358000, 120000, 85000]

##Defining functions in order to create the menus

def coke():
    print(coke_menu)

def liquor():
    print(liquor_menu)

def keys():
    print(keys_menu)
    
##Asking the user to input his location in order to check for machines
print(selection_details)
selection = input("Enter your location in order to check for machines: ")

##Checks the selection from the list, and shows up the coke machine & location
##& the item prices
if selection == coke_location:
    print("You choosed the coke machine :")
    print(coke_location, " - ", coke_machine)
    coke()
    select = input("Choose one of the items in order to buy it: ")
    
    
    if select == coke_menu[0]:
        print("Item costs: ", coke_prices[0], currency[0])
        buy = input("Continue buying? :")
    if buy == booleans[0]:
        update = salary_value - coke_prices[0]
        print("Money remaining:")
        print(update, salary_currency)
    else:
        print("Thanks for showing interest into buying! Maybe next time!")
        
if selection == liquor_location:
    print("You choosed the soda machine :")
    print(liquor_location, " - ", liquor_machine)
    liquor()
    select = input("Choose one of the items in order to buy it: ")
    
    if select == liquor_menu[0]:
        print("Item costs: ", liquor_prices[0], currency[1])
    if select == liquor_menu[1]:
        print("Item costs: ", liquor_prices[1], currency[1])
    if select == liquor_menu[2]:
        print("Item costs: ", liquor_prices[2], currency[1])
    if select == liquor_menu[3]:
        print("Item costs: ", liquor_prices[3], currency[1])
    if select == liquor_menu[4]:
        print("Item costs: ", liquor_prices[4], currency[1])
    
if selection == tapes_location:
    print("You choosed the luxury cars machine :")
    print(tapes_location, " - ", tapes_machine)
    keys()
    select = input("Choose one of the items in order to buy it: ")
    
    if select == keys_menu[0]:
        print("Item costs: ", keys_prices[0], currency[2])
    if select == keys_menu[1]:
        print("Item costs: ", keys_prices[1], currency[2])
    if select == keys_menu[2]:
        print("Item costs: ", keys_prices[2], currency[2])
    if select == keys_menu[3]:
        print("Item costs: ", keys_prices[3], currency[2])
    if select == keys_menu[4]:
        print("Item costs: ", keys_prices[4], currency[2])
        
