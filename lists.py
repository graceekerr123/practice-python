# standard functions every programme needs
def get_integer(m):
    my_integer=int(input(m))
    return my_integer

def get_string(m):
    my_string=input(m)
    return my_string

# a list is a collection of data
# there is 5 pieces of data in this list, 5 strings of peoples names
# lists are also called arrays
# lists use index numbers, and start counting from 0
# what can you do with lists?:
# access an item, print the list (lots of ways to do this),
# add/remove to/from the list (at the end, or in a particular place),
# update an item (change it), sort the lot
my_list=["May", "Patsy", "Jean", "Constantine", "Pierre"]

#print(len(my_list))

# access an item: at an index
#print(my_list[2])

# using index
# you need a place holder so you can insert the lists(L)
def print_at_index(L):
    my_index = get_integer("Please choose index")
    print(L[my_index])
#Mr k way
def print_at_index2(L):
    my_index = get_integer("Please choose index")
    output = "The value -- {} -- is at index {} in the list".format(L[my_index], my_index)
    print(output)


# to print out whole list
# bad way to print out list
def print_list_other(L):
    print(L)

# use a loop
def print_list2(L):
    # going through each item in the list.
    # so it will loop through and x will take the value of each item in the list
    for x in L:
        print(x)

# using a list with menu structures
# when the index number is used for the menu options
def print_list_indexes(L):
    # this counter will loop through 0 - 4
    for i in range(0,len(L)):
        print("{} : {}".format(i,L[i]))

# adding to the list
# use the word 'append' (my_list append ("Damian")
def add_item(L):
    new_item = get_string("Please enter new item")
    # L is the placeholder for whatever is being passed
    L.append(new_item)

def menu():
    my_list = ["May", "Patsy", "Jean", "Constantine", "Pierre"]
    my_menu ='''
    A: print the list
    B: print the list with indices
    C: add item to list
    D: print at index number
    Q: Quit
    '''


    run = False
    while run == True:
        print(my_menu)
        choice = get_string("Please select your option: -> ")
        print("."*60)
        if choice == "A":
            print_list(my_list)
        elif choice == "B":
            print_list_indexes(my_list)
        elif choice == "C":
            add_item(my_list)
        elif choice == "D":
            print_at_index2(my_list)
        elif choice == "Q":
            print("thank you")
            run = False
#menu()


#print_list(my_list) 
#add_item(my_list)


# print_list_indexes(my_list)
# print_list2(my_list)
# print_list_other(my_list)
# print_at_index2(my_list)
# print_at_index(my_list)

    

