nested_list = [[5, 3, 9, 7, 6],
               [2, 7, 2, 1, 9],
              [8, 5, 3, 1, 8]]

def print_list(nested_list):
    print('print out list values one at a time')
    for i in range(len(nested_list)):
        for j in range(len(nested_list[0])):
            print(nested_list[i][j])

print_list(nested_list)


def print_formatted_list(nested_list):
    # print a blank line
    print('\nprint out list values with formatting')
    # print out list values with formatting
    for i in range(len(nested_list)):
        for j in range(len(nested_list[0])):
            # if statement makes sure the last number in a row does not have a comma
            if j != len(nested_list[0]) - 1:
                print(str(nested_list[i][j]) + ", " , end="")
            else:
                print(str(nested_list[i][j]), end="")

        print()
    print()
    
print_formatted_list(nested_list)


twodlist = []
number_rows = 5

for i in range(number_rows):
    twodlist.append([5, 2, 1, 8])        

print_formatted_list(twodlist)


twodlist = []
row = []
number_rows = 5
number_columns = 6

for i in range(number_rows):
    for j in range(number_columns):
        row.append(i)
    twodlist.append(row)
    row = []

print_formatted_list(twodlist)


