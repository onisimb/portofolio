# I will create a string and use .lower and .upper on each alternate character

my_string = "The Golum will be King"
alternative_string_char = ""

# Below i have the block for a loop changing each char in the string
for i in range(len(my_string)):
    if i % 2 == 0:
        alternative_string_char += my_string[i].upper()
    else:
        alternative_string_char += my_string[i].lower()

print(alternative_string_char)

# Below block will only change the words as a whole

split_list = my_string.split()
alternative_string_words = []

# Below block contains the interation and the methods amending the words
for i in range(len(split_list)):
   
    if i % 2 == 1:
        split_list[i] = split_list[i].upper()

    else:
        split_list[i] = split_list[i].lower()

print(" ".join(split_list))

# My apologies I forgot to add and use the join method