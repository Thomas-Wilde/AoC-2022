##--------------------------------------------------------------------------##
### read arrangement
# file = open("example_arrange.data", "r")
file = open("input_arrange.data", "r")
lines = file.readlines()
stacks = []
# --- read crates
for line in lines:
    line = line.replace("\n", "")
    crates = line.split(" ")
    crates.reverse()
    stacks.append(crates)
print(stacks)

##--------------------------------------------------------------------------##
# --- read and performs moves
# file = open("example.data", "r")
file = open("input.data", "r")
lines = file.readlines()
# --- move crates
for line in lines:
    line = line.replace("\n", "")
    moves = line.split(" ")
    count = int(moves[0])
    fr = int(moves[1]) - 1  # -1 because of 0-based indexes
    to = int(moves[2]) - 1  # -1 because of 0-based indexes
    # ---
    for i in range(count):
        crate = stacks[fr].pop()
        stacks[to].append(crate)
print(stacks)
##--------------------------------------------------------------------------##
# --- read top crates
result = ""
for stack in stacks:
    crate = stack[-1]
    result += crate
print(result)
