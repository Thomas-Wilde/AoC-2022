print("Day 1 - Calories")

# Using readlines()
# file = open("input.data", "r")
file = open("example.data", "r")
lines = file.readlines()

linebreaks = 0
elf_idx = 0
sum_elf = 0
maximum = -1
max_elf_index = -1
# read lines
for line in lines:
    # found new elf
    if line == ("\n"):
        print("found new elf (line break)")
        # current elf has the most calories
        if sum_elf > maximum:
            maximum = sum_elf
            max_elf_index = elf_idx
        # prepare stuff for next elf
        linebreaks += 1
        sum_elf = 0
        elf_idx += 1
        continue
    # add calories of current elf
    number = int(line)
    sum_elf += number
    print(number)

print("--- result ---")
print("found " + str(linebreaks + 1) + " elves")
print("elf " + str(max_elf_index) + " has the most calories:")
print(maximum)

# 254 elves expected
