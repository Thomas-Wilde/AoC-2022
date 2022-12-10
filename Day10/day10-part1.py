##--------------------------------------------------------------------------##
# file = open("example.data", "r")
# file = open("example2.data", "r")
file = open("input.data", "r")
lines = file.readlines()
for idx in range(len(lines)):
    lines[idx] = lines[idx].replace("\n", "")

##--------------------------------------------------------------------------##
x = int(1)
cycles = [1]
for line in lines:
    op = line.split(" ")[0]
    # --- handle noop
    if op == "noop":
        cycles.append(int(x))
        continue
    # --- handle addx
    if op == "addx":
        add = int(line.split(" ")[1])
        cycles.append(int(x))
        cycles.append(int(x))
        x += add
cycles.append(int(x))
##--------------------------------------------------------------------------##
# for idx in range(1, len(cycles)):
#     print(str(idx) + " " + str(cycles[idx]))
# print(cycles)
result = 0
for idx in range(20, len(cycles), 40):
    print(str(idx) + " " + str(cycles[idx]) + " " + str(cycles[idx] * idx))
    result += cycles[idx] * idx
print(result)

# noop

# addx 3
# addx -5

# 1 1
# 2 1
# 3 1
# 4 4
# 5 4
# 6 -1
# 7
# 8
# 9
