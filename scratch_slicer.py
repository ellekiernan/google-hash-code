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


class Node:
    def __init__(self, 
                    row1, 
                    col1, 
                    row2, 
                    col2, 
                    root = False, 
                    valid = False, 
                    leaf = False, 
                    split = None
                ):

        self.row1 = row1
        self.col1 = col1
        self.row2 = row2
        self.col2 = col2
        self.slice = (self.row1, self.col1, self.row2, self.col2)

        self.t_count, self.m_count, self.total_count = self.Count()

        self.is_root = root
        self.is_valid = self.isValid()
        self.is_leaf = self.isLeaf()

        self.split = split

        self.children = []
        #make children for each corner?
        
        self.highestcellcount = 0

        # if self.is_leaf == False:
        #     self.createAllChildren()


    #from the parent node, create child node of the same size but with a split attribute for every possible split. Append that new node to the child list of the parent.
    def makeSplitChildren(self, slice):
        row1, col1, row2, col2 = slice
        for row in range(row2+1):
            for col in range(col2+1):
                new_child = Node(row1, col1, row2, col2, split = (row, col))
                self.children.append(new_child)


    def addChild(self, row1, col1, row2, col2):
        area = (self.row2+1-self.row1) * (self.col2+1-self.col1)
        if self.is_leaf == False:
            if area > 2 * minIngredients:
                new_child = Node(row1, col1, row2, col2)
                self.children.append(new_child)
                print(row1, col1, row2, col2)

    def createAllChildren(self):
        for row in range(self.row2 + 1):
            for col in range(self.col2 + 1):
                print(row, col)
                print(self.is_leaf)
                if self.is_leaf == False:
                    #topleft
                    self.addChild(self.row1, self.col1, row, col)
                    #topright
                    if col + 1 < self.col2:
                        self.addChild(self.row1, col + 1, row, self.col2)
                    #bottomleft
                    if row+1 < self.row2:
                        self.addChild(row + 1, self.col1, self.row2, col)
                    #bottomright
                    if row + 1 < self.row2 and col+1 < self.col2:
                        self.addChild(row + 1, col + 1, self.row2, self.col2)
                else:
                    continue


    def pruneNode(self):
        pass
    
    def isLeaf(self):
        area = (self.row2+1-self.row1) * (self.col2+1-self.col1)
        if self.is_valid == True:
            return True
        elif area <= 2*minIngredients:
            return True
        else:
            return False

    def isValid(self):
        if self.t_count < minIngredients:
            return False
        elif self.m_count < minIngredients:
            return False
        elif self.total_count > maxCells:
            return False
        else:
            # everytime a slice is marked as valid, returns True and keeps a running total of cells used in slices
            # total_cells += total
            return True

    def Count(self):
        tCount = 0
        mCount = 0
        for i in range(self.row1, self.row2 + 1):
            for j in range(self.col1, self.col2 + 1):
                if pizza[i][j] == 'T':
                    tCount += 1
                elif pizza[i][j] == 'M':
                    mCount += 1
        return tCount, mCount, tCount + mCount

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
      
#Count function moved into Node class and is automatically called to determine the counts for a slice

#isValid function moved into Node class and is automatically called to determine if a node is valid when it is initialized


# primitive slice maker that just cuts in half everytime
def makeSlices(slice):

    # defines a variable deciding whether to cut vertically or horizontally for next slice checking, next_slice = 0 means next slice will be horizontal
    next_slice = 0

    row1, col1, row2, col2 = slice
    cells = (row2 + 1) * (col2 + 1)
    if isValid(slice):
        slice_list.append(slice)

    elif isValid(slice) == False:
        greatest_valid_boxes = 0
        g_v_b_coords = []
        solution_dict = {}

    for i in range(row2 + 1):
        valid_boxes = 0
        for j in range(col2 + 1):
            print(i, j)
            if i == 0 and j == 0:
                break
            else:
                slice_top_left = (row1, col1, i, j)
                makeSlices(slice_top_left)
                if j < col2:
                    slice_top_right = (row1, j+1, i, col2)
                    makeSlices(slice_top_right)
                if i < row2:
                    slice_bot_left = (i+1, col1, row2, j)
                    makeSlices(slice_bot_left)
                if i < row2 and j < col2:
                    slice_bot_right = (i+1, j+1, row2, col2)
                    makeSlices(slice_bot_right)
                if total < 2 * minIngredients:
                    break
        
            

root_pizza = Node(0, 0, rows - 1, cols -1, root = True)
root_pizza.makeSplitChildren()
for i in range(len(root_pizza.children)):
    print(root_pizza.children[i].row2)