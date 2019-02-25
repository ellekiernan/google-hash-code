# f = open("a_example.in", "r")
# f = open("b_small.in", "r")
# f = open("c_medium.in", "r")
f = open("a_example.in", "r")
isFirst = True

#order of number to meaning
#Rows, Columns, Minimum number of each ingredient cells in a slice, Maximum total number of cells of a slice

rows, cols, minIngredients, maxSlices = None, None, None, None
#tCount, mCount = 0, 0
pizza = []

for row in f:
    if isFirst:
        # Open the file and want to take the first 4 numbers into memory
        rows, cols, minIngredients, maxSlices = list(map(int, row.split()))
        isFirst = False

    else:
        ingredient_list = []
        for i in range(len(row)-1):
            ingredient_list.append(row[i])
        pizza.append(ingredient_list)
      
print(pizza)
#generic count function for a given pizza slice, default values of only pizza array passed count the entire input array
def count(row1 = 0, col1 = 0, row2 = len(pizza), col2 = len(pizza[0]), pizza = pizza):
    tCount = 0
    mCount = 0
    for i in range(row1, row2):
        for j in range(col1, col2):
            if pizza[i][j] == 'T':
                tCount += 1
            elif pizza[i][j] == 'M':
                mCount += 1
    return tCount, mCount
tCount, mCount = count(pizza = pizza)
print('tCount is: {}, mCount is: {}'.format(tCount, mCount))
print(pizza)
