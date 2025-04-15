#2.1
twenty_list = list(range(21))

#2.2
def squareList(input_list):
    squared_list = []
    for num in input_list:
        squared_list.append(num * num)
    return squared_list

#2.3
def first_fifteen_elements(input_list):
    return input_list[:15]

#2.4
def every_fifth_element(input_list):
    return input_list[4::5]

#2.5
def fancy_function(input_list):
    #last_three = input_list[-3:] only needed if wanting to slice last 3 elements, but then doesn't match example output
    #return last_three[::-3]
    return input_list[::-3]

#to test the functions
#squared = squareList(twenty_list)
#print(first_fifteen_elements(squared))  # First 15 elements
#print(every_fifth_element(squared))     # Every 5th element
#print(fancy_function(squared))

#3.1
def create_2d_list():
    matrix = []
    count = 1
    for i in range(5):
        row = []
        for j in range(5):
            row.append(count)
            count += 1
        matrix.append(row)
    return matrix

#3.2
def modified_2d_list(matrix):
    new_matrix = []
    for row in matrix:
        new_row = []
        for num in row:
            if num % 3 == 0:
                new_row.append('?')
            else:
                new_row.append(num)
        new_matrix.append(new_row)
    return new_matrix

#3.3
def sum_non_question_elements(matrix):
    total = 0
    for row in matrix:
        for element in row:
            if element != '?':
                total += element
    return total

#to test functions
#matrix = create_2d_list()
#print(matrix)  # Shows the 5x5 matrix with numbers 1-25

#new_matrix = modified_2d_list(matrix)
#print(new_matrix)  # Shows matrix with '?' replacing multiples of 3

#total = sum_non_question_elements(new_matrix)
#print(total)  # Prints 217

