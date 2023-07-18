# By using the while loop I will create a function, that will ask the user to input a number until a specific condition will be met, and as to show their mean at the end. 
user_num_list = []
i = 1

# Using the while loop, with try and except to account for any error from user inputs.
while i != -1:
    try:
        user_input = int(input("Type a number (-1 to break loop):"))
        user_num_list.append(user_input)
        i += 1
        
        if user_input == -1:
            average_from_input = (sum(user_num_list[0:-1]) / len(user_num_list[0:-1]))     
            print(f"The average from the user input numbers is {average_from_input: .2f}.")
            break
    
    except:
        print("Invalid input. Please chose only numbers.")
          

# Reference:
# For this task I have accessed additional resources on 02/04/2023 from stackoverflow website from author 'jadjad93hehe'. Find link beloww:
# https://stackoverflow.com/questions/36962479/how-to-store-user-input-into-list-on-python


   

