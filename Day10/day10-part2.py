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
pp = 0
for idx in range(6 * 40):
    # --- handle line break
    if idx % 40 == 0:
        pp = 0
        print("")
    # --- define sign
    sgn = " "
    spr = cycles[idx + 1]
    if pp == spr or pp == (spr - 1) or pp == (spr + 1):
        sgn = "#"
    print(sgn, end="")
    # --- handle pixel pos
    pp += 1


print("\n")
