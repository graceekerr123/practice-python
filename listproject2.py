def get_integer(m):
    my_integer=int(input(m))
    return my_integer

def get_string(m):
    my_string=input(m)
    return my_string

def add_name_age(N, A):
    count = get_integer("How many names and ages would you like to add: ->")
    for i in range(0,count):
        name = get_string("Please enter name: ->")
        age = get_integer("Please enter age: ->")
        N.append(name)
        A.append(age)
        output = "{} aged {} has been added".format(N[i],A[i])
        print(output)
    if count > 1:
        print("all names have been added")

def review(N,A):
    # number of elements in the list
    if len(N) == len(A):
        for i in range(0,len(N)):
        # N, A beause the function cannot access the variable,
        # so these arguments then get told it's name and age in the menu function
        # menu funtion is the control function and holds all of the data
        # without the (i) it will just print out the whole list
            output = "{} is {} years old".format(N[i],A[i])
            print(output)


def menu():
    # start with empty lists
    name=[]
    age=[]
    my_menu='''
    A: Add names and ages
    R: Review
    Q: Quit
    '''
    
    run = True
    while run == True:
        print(my_menu)
        choice = get_string("Please enter choice: ->")
        print("."*60)
        if choice == "A":
            add_name_age(name, age)
            print("."*60)
        elif choice == "R":
            review(name, age)
            print("."*60)
        elif choice == "Q":
            print("Thank you")
            run = False                         
    
    # print(name)
    # print(age)

menu()
