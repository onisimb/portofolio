# A menu has been created for the restaurant with traditional foods 
char = " ******* "
print(f"{char}Welcome to your cafe stock management.{char}")

cafe_menu = ['Bobgulas', 'Mamaliga', 'Babe fara lapte', 'Puiut de malai']

# Below we have the manu with the current stock 
cafe_stock = {'Bobgulas': 5 , 'Mamaliga': 2, 'Babe fara lapte': 7, 'Puiut de malai': 5}

# Below we have the value for each item the cafe is selling
cafe_menu_price = {'Bobgulas': 15 , 'Mamaliga': 5, 'Babe fara lapte': 13, 'Puiut de malai': 10}

# An empty variable has been created to store the total stock value
cafe_total_stock_value = 0

# On the below loop I created the mathematical equation to find the stock value and also printed each menu item individualy 
# showing the price and how many portions are available
for item in cafe_menu:
    item_total_value = cafe_stock[item] * cafe_menu_price[item]
    cafe_total_stock_value += item_total_value
    print(f"Stock value for {item} is: £{item_total_value} ({cafe_stock[item]} portions)")

print(f"Total value of cafe stock is: £{cafe_total_stock_value}")

# References:
# PDF provided by HyperionDev for the task 
# Previous Hyperion Dev lectures


# I have added some extra bits and I hope this is fine with the marking. Thx