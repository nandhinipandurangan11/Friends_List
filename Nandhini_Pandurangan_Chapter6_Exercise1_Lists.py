# CIS40: Summer 2020: Chapter 6 Exercise1: Nandhini Pandurangan
# This program uses lists to represent friends made in 2017 and 2018
# It allows the user to check the existence of a friend and add friends

# Creating two lists of friends that were found in 2017 and 2018.
list_2017 = ["Viaan Padilla", "Lilith Moss", "Amin Morrow", "Aneeka Lewis"]
list_2018 = ["Fay Garrison", "Madeleine Odom", "Abel Marquez", "Rosemary Ewing", "Walter Legge"]

# Concatenating the two lists and showing it to the user.
print("--My friends--")
separator = " \n"
print(separator.join(list_2018 + list_2017))

# making the friend lists lowercase so it is
# easily comparable to the input
lower_list2017 = []
lower_list2018 = []

for i in list_2017:
    lower_list2017.append(i.lower())
for i in list_2018:
    lower_list2018.append(i.lower())

# Prompting the user to enter a name of a friend
name = input("\nEnter the name of one of my friends: ").strip()
name = name.lower()  # making the name lowercase

# checking if the friend was found in 2017 or 2018
# and printing the appropriate result
if name in lower_list2017:
    print("This friend was found in 2017!")
elif name in lower_list2018:
    print("This friend was found in 2018!")
else:
    print("Sorry, no such friend exists")

# Asking the user what year they want to add the friend name.
flag = True
while flag:
    year = int(input("\nWould you like to add a friend to 2017 or 2018 list? "
                 "Enter 2017 or 2018: "))
    if year == 2017 or year == 2018:
        flag = False
    else:
        print("Error! Please enter 2017 or 2018")

# Ask the user to enter a new friend name to be added to the 2017 or 2018 list
name2 = input("\nEnter the name of the friend to be added to the {0} list: ".format(year))

# appending the name to the correct list
if year == 2017:
    list_2017.append(name2)
else:
    list_2018.append(name2)

# Print both 2017 and 2018 friends' lists on the screen.
separator = ", "
print("\n2017 friends:", separator.join([name for name in list_2017]))
print("2018 friends:", separator.join([name for name in list_2018]))


"""
Output: 

--My friends--
Viaan Padilla 
Lilith Moss 
Amin Morrow 
Aneeka Lewis 
Fay Garrison 
Madeleine Odom 
Abel Marquez 
Rosemary Ewing 
Walter Legge

Enter the name of one of my friends: Lilith Moss
This friend was found in 2017!

Would you like to add a friend to 2017 or 2018 list? Enter 2017 or 2018: 2018

Enter the name of the friend to be added to the 2018 list: Barack Obama

2017 friends: Viaan Padilla, Lilith Moss, Amin Morrow, Aneeka Lewis
2018 friends: Fay Garrison, Madeleine Odom, Abel Marquez, Rosemary Ewing, Walter Legge, Barack Obama
------------------------------------------------------------------------------------------------------
Output2:

--My friends--
Viaan Padilla 
Lilith Moss 
Amin Morrow 
Aneeka Lewis 
Fay Garrison 
Madeleine Odom 
Abel Marquez 
Rosemary Ewing 
Walter Legge

Enter the name of one of my friends: aNEEka leWis
This friend was found in 2017!

Would you like to add a friend to 2017 or 2018 list? Enter 2017 or 2018: 1029
Error! Please enter 2017 or 2018

Would you like to add a friend to 2017 or 2018 list? Enter 2017 or 2018: 2017

Enter the name of the friend to be added to the 2017 list: Mickey Mouse

2017 friends: Viaan Padilla, Lilith Moss, Amin Morrow, Aneeka Lewis, Mickey Mouse
2018 friends: Fay Garrison, Madeleine Odom, Abel Marquez, Rosemary Ewing, Walter Legge
"""