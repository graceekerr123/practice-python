def square_num1():
    for i in range(0,100):
        my_square = i * i
        my_output = "{} squared = {}".format(i, my_square)
        print(my_output)


def square_num(n):
    for i in range(0,n):
        my_square = i * i
        my_output = "{} squared = {}".format(i, my_square)
        print(my_output)
    print()

def cube_num(n):
    for i in range(0,n):
        my_cube = i * i * i
        my_output = "{} cubed = {}".format(i, my_cube)
        print(my_output)
    print()

# menu with number of calculations already choosen
def menu1():
    my_menu = '''
    A : Square Numbers
    B : Cubed Numbers
    Q : Quit
    '''
    print(my_menu)
    choice = input("Please choose option: ->")
    if choice == "A":
        square_num(6)
    elif choice == "B":
        cube_num(5)
    elif choice == "Q":
        print("Thanks for square or cubing")
    else:
        print("This was not an option")

# menu that goes in a loop but number of calculations are already chooson
def menu2():
    run = True
    while run == True:
        my_menu = '''
A : Square Numbers
B : Cubed Numbers
Q : Quit
                    '''
        print(my_menu)
        choice = input("Please choose option: ->")
        if choice == "A":
            square_num(6)
        elif choice == "B":
            cube_num(5)
        elif choice == "Q":
            run = False
            print("Thanks for square or cubing")
        else:
            print("This was not an option")

def get_integer(m):
    #the () is the info box, if you need to get something in the function)
    num = int(input(m))
    return num

# menu that asks how many calculation the user wants
def menu3():
    run = True
    while run == True:
        my_menu = '''
A : Square Numbers
B : Cubed Numbers
Q : Quit
                    '''
        print(my_menu)
        choice = input("Please choose option: ->")
        if choice == "A":
            num = get_integer("Please enter how many calculations you want: ")
            square_num(num)
        elif choice == "B":
            num = get_integer("Please enter how many calculations you want: ")
            cube_num(num)
        elif choice == "Q":
            run = False
            print("Thanks for square or cubing")
        else:
            print("This was not an option")


#menu1()
#menu2()
menu3()


#square_num1()
#square_num(20)
#cube_num(10)

