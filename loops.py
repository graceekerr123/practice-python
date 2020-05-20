# loops
# loops are repeated actions (iterations)

# loop wiht a counter (will run a certain number of times)
# n will become whatever you give it,
# the function is expecting a value from anywhere, but only 1 value
# so could have loop_with_counter(5)
# or my_num = 23 n\ loop_with_counter(my_num)
def loop_with_counter(n):
    # requires a counter
    c = 0
    while c < n:
        print("hello c is now {}".format(c)   )
        # increment c
        c += 1
    return None

count = 10
def loop_with_counter2(count):
    # requires a count
    c = 0
    # counter is set on the counter value
    while c < count:
        print(   "hello c is now {}".format(c)   )
        # increment c
        c += 1
    print("all done")


# indefinite loop
def while_loop_indefinite():
    # set a condition
    run = True
    # check the condition
    while run == True:
        user_choice = input("Enter 'n' to stop loop n\or any other key to stay in the loop: ->")
        if user_choice == "n":
            print("loop will stop")
            run = False
        else:
            print("you are still in the loop")


def for_in_range_loop():
    # this has a bulit in counter
    # can be anything but we generally use i or j or k
    # can add steps (integer)
    # first number, after last number, increment number (steps)
    # if you put no step, then it's one
    for i in range(3, 20, 5):
        print(i)

# double loop
def double_loop():
    for i in range(0,5):
        for j in range(0,6):
            print( "({},{})".format(j,i) , end = "" )
        print()


def menu():
    my_menu = '''
    1: while loop with counter
    2: while loop with quit
    3: for in range
    4: double loop
    0: quit
    '''
    print (my_menu)
    choice = int(input("choose your option: -> "))
    if choice == 1:
        amount = int(input("How many would you like: ->"))
        loop_with_counter(amount)
    elif choice ==2:
        while_loop_indefinite()
    elif choice == 3:
        for_in_range_loop()
    elif choice == 4:
        double_loop()
    elif choice == 0:
        print("Thankyou")
    else:
        print("Unrecognised entry")
#menu()


# double_loop()
# for_in_range_loop()
# while_loop_indefinite() 
# loop_with_counter(6)
#loop_with_counter2(6)

# 5.00
