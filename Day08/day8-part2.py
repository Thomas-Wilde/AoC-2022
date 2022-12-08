##--------------------------------------------------------------------------##
# file = open("example.data", "r")
file = open("input.data", "r")
lines = file.readlines()
# --- remove linebreak
for idx in range(len(lines)):
    lines[idx] = lines[idx].replace("\n", "")

##--------------------------------------------------------------------------##
## --- define array of correct size
height = len(lines)
width = len(lines[0])
field = [[]]
for x in range(width):
    for y in range(height):
        field[x].append(int(0))
    field.append([])
# print(str(width) + " " + str(height))
field.pop()
# print(field)
## --- transfer data to field
y = 0
for line in lines:
    for x in range(len(line)):
        number = int(line[x])
        # print(str(x) + " " + str(y) + " " + str(number))
        field[x][y] = number
    y += 1
# print(field)
## --- print field
# for y in range(height):
#     for x in range(width):
#         number = field[x][y]
#         print(number, end="")
#     # print()
##--------------------------------------------------------------------------##
visible = int(0)
max_score = int(-1)
for y_tree in range(0, height):
    for x_tree in range(0, width):
        # ----------------------------------------
        # --- extract lines to border
        tree = field[x_tree][y_tree]
        up = field[x_tree][0:y_tree]
        up.reverse()
        down = field[x_tree][y_tree + 1 : height]
        # --- read left part
        cols = field[0:x_tree]
        left = []
        for col in cols:
            left.append(col[y_tree])
        left.reverse()
        # --- read right part
        cols = field[(x_tree + 1) :]
        right = []
        for col in cols:
            right.append(col[y_tree])
        # ----------------------------------------
        # check visibility to next taller tree
        # ---
        lists = [left, up, right, down]
        trees = []
        for list in lists:
            count = int(0)
            while len(list) > 0:
                if list[0] < tree:
                    count += 1
                    list.pop(0)
                else:
                    count += 1
                    break
            trees.append(int(count))
        # print(trees)
        scenic_score = int(1)
        for val in trees:
            scenic_score *= val
        # print("(" + str(x_tree) + "," + str(y_tree) + ") has " + str(trees) + " visible trees")
        if scenic_score > max_score:
            max_score = scenic_score
            print(
                "("
                + str(x_tree)
                + ","
                + str(y_tree)
                + ") has "
                + str(scenic_score)
                + " score"
            )
# print(left)
# print(right)
# print(down)
print("maximum score was " + str(max_score))

# # 30373
# # 25512
# # 65332
# # 33549
# # 35390
