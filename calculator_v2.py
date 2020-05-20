
def adding2(a,b):
    #the a and b are arguments
    my_sum = a+b
    #make a string
    my_string = "{} + {} = {}".format(a,b, my_sum)
    print(my_string)

def subtracting(a,b):
    my_sum = a-b
    my_string = "{} - {} = {}".format(a,b, my_sum)
    print(my_string)

def diving(a,b):
    my_sum = a/b
    my_string = "{} / {} = {}".format(a,b, my_sum)
    print(my_string)

def multiplying(a,b):
    my_sum = a*b
    my_string = "{} x {} = {}".format(a,b, my_sum)
    print(my_string)

def get_integer(m):
    #the () is the info box, if you need to get something in the function)
    my_number = int(input(m))
    return my_number

def menu():
    number_one = get_integer("Please enter your first number: ->")
    number_two = get_integer("Please enter your second number: ->")
    
    my_menu = '''
    1: add
    2: subtract
    3: divide
    4: multiply
    0: quit
    '''
    print (my_menu)
    user_choice = get_integer("Please choose a option from the menu: -> ")
    if user_choice == 1:
        adding2(number_one,number_two)
    elif user_choice ==2:
        subtracting(number_one,number_two)
    elif user_choice == 3:
        diving(number_one,number_two)
    elif user_choice == 4:
        multiplying(number_one,number_two)
    elif user_choice == 0:
        print("Quitting")
    else:
        print("Unrecognised entry")

menu()



