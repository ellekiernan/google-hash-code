# f = open("a_example.in", "r")
# f = open("b_small.in", "r")
# f = open("c_medium.in", "r")
f = open("a_example.in", "r")
isFirst = True

#order of number to meaning
#Rows, Columns, Minimum number of each ingredient cells in a slice, Maximum total number of cells of a slice

rows, cols, minIngredients, maxCells = None, None, None, None
slice_list = []
total_cells = 0

#tCount, mCount = 0, 0
pizza = []

#makes an array of data, with just 'T's and 'M's
for row in f:
    if isFirst:
        # Open the file and want to take the first 4 numbers into memory
        rows, cols, minIngredients, maxCells = list(map(int, row.split()))
        isFirst = False
    else:
        ingredient_list = []
        for i in range(len(row)-1):
            ingredient_list.append(row[i])
        pizza.append(ingredient_list)
      
#generic count function for a given pizza slice; default values count entire pizza; returns 'T's, 'M's, and total
def count(slice = (0, 0, len(pizza), len(pizza[0]))):
    row1, col1, row2, col2 = slice
    tCount = 0
    mCount = 0
    total = 0
    for i in range(row1, row2 + 1):
        for j in range(col1, col2 + 1):
            if pizza[i][j] == 'T':
                tCount += 1
            elif pizza[i][j] == 'M':
                mCount += 1
    return tCount, mCount, tCount + mCount

#checks a called slice and returns True if slice is a valid slice and false if not
def isValid(slice):
    row1, col1, row2, col2 = slice
    print(slice)
    tCount, mCount, total = count(slice)
    if tCount < minIngredients:
        return False
    elif mCount < minIngredients:
        return False
    elif total > maxCells:
        return False
    else:
        # everytime a slice is marked as valid, returns True and keeps a running total of cells used in slices
        # total_cells += total
        return True


# primitive slice maker that just cuts in half everytime
def makeSlices(slice):

    # defines a variable deciding whether to cut vertically or horizontally for next slice checking, next_slice = 0 means next slice will be horizontal
    next_slice = 0

    row1, col1, row2, col2 = slice
    t, m, total = count(slice)
        
    if total < 2 * minIngredients:
        print("SAD")


    if isValid(slice):
        slice_list.append(slice)
   
    elif isValid(slice) == False:
        new_slice_top = (row1, col1, (row1+row2)//2, col2)
        new_slice_bottom = ((row1+row2)//2 + 1, col1, row2, col2)
        new_slice_left = (row1, col1, row2, (col1+col2)//2)
        new_slice_right = (row1, (col1+col2)//2 + 1, row2, col2)

        if isValid(new_slice_top) or isValid(new_slice_bottom):
            makeSlices(new_slice_top)
            makeSlices(new_slice_bottom)

        elif isValid(new_slice_left) or isValid(new_slice_right):
            makeSlices(new_slice_left)
            makeSlices(new_slice_right)
            

first_slice = (0, 0, len(pizza) - 1, len(pizza[0]) - 1)
print("First_slice: ", first_slice)
makeSlices(first_slice)

# slice1 = (0, 0, 2, 1)
# print('is slice valid? : {}'.format(isValid(slice1)))
# print(pizza)
