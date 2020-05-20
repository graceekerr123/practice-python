import random
# change a value (at an index)
# for the list L at index 3 = L[3] (array index operator/access operator)
# L[3] = "Tommi"

def get_integer(m):
    my_integer=int(input(m))
    return my_integer

def get_string(m):
    my_string=input(m)
    return my_string

def print_at_index(L):
    my_index = get_integer("Please choose index")
    print(L[my_index])

def print_at_index2(L):
    my_index = get_integer("Please choose index")
    output = "The value -- {} -- is at index {} in the list".format(L[my_index], my_index)
    print(output)

def print_list(L):
    for x in L:
        print(x)

def print_list_indexes(L):
    for i in range(0,len(L)):
        print("{} : {}".format(i,L[i]))

def add_item(L):
    new_item = get_string("Please enter new item")
    # L is the placeholder for whatever is being passed
    L.append(new_item)

def find_item(L):
    item = get_string("Who do you want to find? -> ")
    if item in L:
        index_num = L.index(item)
        output = "{} has been found is at index number {}".format(L[index_num], index_num)
        print(output)
    else:
        print("{} is not the list".format(item))
    print("." * 100)

def remove_item(L):
    item = get_string("Who do you want to remove? -> ")
    if item in L:
        L.remove(item)
        output = "{} has been removed from the list".format(item)
        print(output)
    else:
        print("{} could not be found".format(item))
    print("." * 100)

def sort_list(L):
    L.sort()

def shuffle_list(L):
    random.shuffle(L)
    

# ----------------- NEW STUFF ------------------------



my_list= ["Louis", "Harry", "Liam", "Zayn", "Niall"]

# quick function design:
def change_value(L):
    # MR K: Print menu so user has index numbers
    # print the list
    print_list_indexes(L)
    # we need an index and a value
    index_num = get_integer("Please choose index number: -> ")
    new_value = get_string("Please enter new value:  ->")
    # now we have the values we need

    # to test that everything works up to this point:
    #print(index_num)
    #print(new_value)
    
    old_value = L[index_num]
    #print(old_value) - to test
    
    L[index_num] = new_value
    # need some confirmation to see this worked
    output = "The old value of {} has now been changed to {}".format(old_value, L[index_num])
    print(output)

#change_value(my_list)





# to turn off the function, make it false
# you can create 2 lists
def menu():
    my_list_one = ["Louis", "Harry", "Liam", "Zayn", "Niall"]
    my_list_two = ["Luke", "Calum", "Ashton", "Micheal"]
    my_list = my_list_one
    print("my list is currently set to the List 1 of One Direction members")
    print("if you want to change to 5SOS members, change to List 2")
    my_menu ='''
    A: print the list
    B: print the list with indices
    C: add item to list
    D: print at index number
    E: change value
    F: Choose List 1
    G: Choose List 2
    H: Find item in a list
    I: Remove item from a list
    J: Sort list
    K: Shuffle list
    Q: Quit
    '''

    # test the function
    #change_value(my_list)

    run = True
    while run == True:
        print(my_menu)
        choice = get_string("Please select your option: -> ").upper()
        print("."*60)
        if choice == "A":
            print_list(my_list)
        elif choice == "B":
            print_list_indexes(my_list)
        elif choice == "C":
            add_item(my_list)
        elif choice == "D":
            print_at_index2(my_list)
        elif choice == "E":
            change_value(my_list)
        elif choice == "F":
            my_list = my_list_one
            print("my list ONE is now selected")
        elif choice == "G":
            my_list = my_list_two
            print("my list TWO is now selected")
        elif choice == "H":
            find_item(my_list)
        elif choice == "I":
            remove_item(my_list)
        elif choice == "J":
            sort_list(my_list)
        elif choice == "K":
            shuffle_list(my_list)
        elif choice == "Q":
            print("thank you")
            run = False
menu()

#find_item(my_list)
#remove_item(my_list)
#sort_list(my_list)
#shuffle_list(my_list)
