#our main dictionary composes of :
#model,plate number,year released,number of times rented and colour
# create 5 cars in main dictionary

main_col = {'car1':{'model': 'minivan', 'color':'red', 'num': 2222, 'year':2018 , 'rented': 0},
            'car2':{'model': 'benz', 'color': 'brown', 'num': 3333, 'year': 2016, 'rented': 0},
            'car3':{'model':'truck', 'color': 'white','num': 4444, 'year':2017, 'rented':0},
            'car4':{'model':'tesla', 'color':'pink', 'num':9999, 'year': 2013, 'rented': 0},
            'car5' :{'model': 'wagon', 'color':'black', 'num': 3232, 'year':2015, 'rented':0}}

#functions that we will use
#function to add car to dictionary
# ask user for all car info

def addCar():
    model = input("Enter the name of new car to collection ")
    car_color = input("Enter the colour ")
    car_num = input("Enter plate number ")
    year_re = int(input("Enter year in which model was released "))
    times_rented = 0

    car6 = {"model": model, "color": car_color, "num": car_num, "year": year_re, "rented": times_rented }
    main_col["car6"] = car6
    print(main_col)

#function to rent out car
def rentCar():
    carRent = input("Car name : ")
    for k in main_col.keys():
        if k == carRent:
            main_col[carRent]['rented'] += 1
            print("Rented times : " + str(main_col[carRent]['rented']))

#function to remove car
def removeCar():
    carRemove = input("Car name : ")
    del main_col[carRemove]
    print("Deleted " + carRemove)

#function to find profit
def eachProfit():
    for k, v in main_col.items():
        profit = v['rented'] * 2000
        print(k + " profit was " + str(profit))

#function to print out the menu
def print_menu():
    print("1) add, 2) rent 3) remove 4) profit")
    usr_str = input('Type your option from menu : ')
    return usr_str

while True:

    choice = print_menu()
    if choice == '1':
        addCar()

    elif choice == '2':
        rentCar()

    elif choice == '3':
        removeCar()

    elif choice == '4':
        eachProfit()
    else:
        print("Invalid choice")

    perform = input("Do you want to operation other operations? yes or no?")
    if perform == 'yes':
        continue
    else:
        print('The program ends here! Bye!')
        break

