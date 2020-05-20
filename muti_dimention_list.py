# test file
def double_loop(L):
    for i in range(0, len(L)):
        output = "{} : {}".format(i, L[i])
        print (output)
        for j in range(0, len(L[i])):
            output = "{} : {}".format(j, L[i][j])
            print(output)

def main():
    my_list=[["JJ", "Blond", 21],
             ["John B", "Sandy Blond", 27],
             ["Sarah Cameron", "Blond", 22],
             ["Kiara", "Dark Brown", 21],
             ["Pope", "Black", 21]
            ]
    # print(my_list)
    #print(double_loop(my_list))
    for i in range(0,len(my_list)):
        # 10 charcter space, so it will use a 10 character space for the variable and will put the variable in
        # so this repiclates a table structure
        # ^ = center alignment
        # < = left alignment
        # > = right aligment
        output = "{:<10} {:^10} {:10}".format(my_list[i[0]], my_list[i[1]], my_list[i[2]])



main()