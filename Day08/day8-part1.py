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
for y_tree in range(1, (height - 1)):
    for x_tree in range(1, (width - 1)):
        # ----------------------------------------
        # --- extract lines to border
        tree = field[x_tree][y_tree]
        up = field[x_tree][0:y_tree]
        up.sort(reverse=True)
        down = field[x_tree][y_tree + 1 : height]
        down.sort(reverse=True)
        # --- read left part
        cols = field[0:x_tree]
        left = []
        for col in cols:
            left.append(col[y_tree])
        left.sort(reverse=True)
        # --- read right part
        cols = field[(x_tree + 1) :]
        right = []
        for col in cols:
            right.append(col[y_tree])
        right.sort(reverse=True)
        # ----------------------------------------
        # check visibilty from border
        if (up[0] < tree) or (down[0] < tree) or (left[0] < tree) or (right[0] < tree):
            visible += 1
            print("(" + str(x_tree) + "," + str(y_tree) + ") is visible")
        else:
            print("(" + str(x_tree) + "," + str(y_tree) + ") is NOT visible")
# ----
# add border
visible += 2 * height
visible += (2 * width) - 4

print("a total of " + str(visible) + " trees are visible")
# print(left)

# # 30373
# # 25512
# # 65332
# # 33549
# # 35390
