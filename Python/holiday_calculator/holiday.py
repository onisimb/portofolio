# On this ocassion I will create a holiday cost calculator which will take into account a few variables. 

# A simple welcome print
char = "*********"
print(f"{char} Welcome to your holiday cost prediction. {char}")

# A dictionary holding the cities available for travel and their flight costs for ease of access and minimise coding
city_flight_cost = {'transilvania': 350,
                    'cluj napoca': 450,
                    'brasov': 280}

# Below I have created the sections with all the functions used
def city_options():
    '''Available holiday destinations'''
    print("We can offer a holiday to the following 3 cities: \n\t Transilvania \n\t Cluj Napoca \n\t Brasov")

def hotel_cost(num_nights):
    '''Will calculate the hotel cost'''
    return num_nights * 150

def plane_cost(city_flight): 
    '''Will calculate the plane cost depending on the choosen city by accesing the dictionary.''' 
    if city_flight in city_flight_cost:
        return city_flight_cost[city_flight]

def car_rental(rental_days):
    '''Will calculate the car rental'''
    return rental_days * 85

def holiday_cost(hotel_cost, plane_cost, car_rental):
    '''Will calculate the total cost of the holiday taking in account all available options'''
    total_to_pay = hotel_cost + plane_cost + car_rental
    return total_to_pay

def individual_cost(hotel_total_cost, plane_total_cost, car_total_rental):
    '''Will display a breakdown after the total'''
    print(f"Your hotel total is: £{hotel_total_cost}")
    print(f"Your plane total is: £{plane_total_cost}")
    print(f"Your car rental total is: £{car_total_rental}")

city_options()

# A loop to account for eventual user input errors

while True:
    try:
        city_flight = str(input("Choose your destination from the above list: ")).lower()
        
        # This block accounts for errors besides int input from user
        if city_flight not in city_flight_cost:
            print("Your input is invalid. Try again.")
            city_options()
            continue
        
        num_nights = int(input("Choose for how many nights do you wish to book a hotel: "))
        rental_days = int(input("Choose for how many days do you wish to hire a vehicle: "))
        
        # Bellow variables have been created to hold the int calculations performed by the functions after user inputs, and to be printed later. 
        hotel_total_cost = hotel_cost(num_nights)
        plane_total_cost = plane_cost(city_flight)
        car_total_rental = car_rental(rental_days)
        total_cost = holiday_cost(hotel_total_cost, plane_total_cost, car_total_rental)

        print(f"Your total cost for the holiday choosen is £{total_cost}.")
        print("See below cost breakdown of your holiday:")
        individual_cost(hotel_total_cost, plane_total_cost, car_total_rental)
        city_options()

    except ValueError:
        print("Your input is invalid. Try again.")
        city_options()


# Reference:
# 1 - I have used all the example files provided with the task (very helpfull)
# 2 - I have also used code from the previous tasks I have submitted. Expecially task 5.
# 3 - I have also rewatched some lectures from HyperionDev     
# 4 - The comments for the def I have seen them a long time ago somewhere online but I do not recall anymore where. 