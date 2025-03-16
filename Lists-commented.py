# I will start by creating an empty list.
my_list = []

# Now I add (append) some numbers to my list. Each number is added to the end of the list.
my_list.append(10)  # I add the number 10 to my list
my_list.append(20)  # I add the number 20 to my list
my_list.append(30)  # I add the number 30 to my list
my_list.append(40)  # I add the number 40 to my list
print("After appending:", my_list)  # I print my list to see what's in it

# I want to add the number 15 at the second position (index 1).
# Remember, positions start counting at 0, so the second position is index 1.
my_list.insert(1, 15)  # I insert 15 at position 1 (between 10 and 20)
print("After inserting 15:", my_list)  # I print my list again to see the change

# I want to add multiple numbers at once to the end of my list.
# I can use extend() to add all items from another list to my list.
my_list.extend([50, 60, 70])  # I add these three numbers to the end of my list
print("After extending:", my_list)  # I print my list to see the new numbers

# I want to remove the last number from my list.
# I can use pop() to remove and return the last item.
removed_element = my_list.pop()  # I remove the last number (70) from my list
print("Removed element:", removed_element)  # I print the removed number
print("After removing last element:", my_list)  # I print my list without the last number

# I want to arrange my list in order from smallest to largest.
my_list.sort()  # I sort my list in ascending order
print("After sorting:", my_list)  # I print my sorted list

# I want to find where the number 30 is in my list.
# The index() method tells me the position of a value.
index_of_30 = my_list.index(30)  # I find the position of 30 in my list
print("Index of 30:", index_of_30)  # I print the position of 30
