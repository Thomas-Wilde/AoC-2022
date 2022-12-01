from audioop import reverse


print("Day 1 - Calories")

# Using readlines()
file = open("input.data", "r")
# file = open("example.data", "r")
lines = file.readlines()

sum_elf = 0
# read lines
elves_list = []
for line in lines:
    # found new elf
    if line == ("\n"):
        print("found new elf (line break)")
        # prepare stuff for next elf
        elves_list.append(int(sum_elf))
        sum_elf = 0
        continue
    # add calories of current elf
    number = int(line)
    sum_elf += number
    print(number)

print("--- result ---")
elves_list.sort(reverse=True)
print(elves_list)

# 254 elves expected
print(73211 + 71575 + 69172)
