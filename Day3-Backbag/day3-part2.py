# Using readlines()
file = open("input.data", "r")
# file = open("example.data", "r")
lines = file.readlines()
sum_value = 0
for z in range(0, len(lines), 3):
    # z = 0
    line0 = lines[z]
    line1 = lines[z + 1]
    line2 = lines[z + 2]
    line0 = line0.replace("\n", "")
    line1 = line1.replace("\n", "")
    line2 = line2.replace("\n", "")
    # print(line0)
    # print(line1)
    # print(line2)
    # print("---")
    bag0 = [*line0]
    bag1 = [*line1]
    bag2 = [*line2]
    bag0.sort()
    bag1.sort()
    bag2.sort()
    # print(bag0)
    # print(bag1)
    # print(bag2)
    # ---
    found = False
    item = ""
    while not found:
        item0 = bag0[0]
        item1 = bag1[0]
        item2 = bag2[0]
        value0 = ord(item0)
        value1 = ord(item1)
        value2 = ord(item2)
        if (value0 == value1) and (value0 == value2):
            found = True
            item = item0
            # print("found common item " + item0)
            break
        minimum = min(value0, value1)
        minimum = min(minimum, value2)
        # print(chr(minimum))
        if bag0[0] == chr(minimum):
            bag0.remove(chr(minimum))
        if bag1[0] == chr(minimum):
            bag1.remove(chr(minimum))
        if bag2[0] == chr(minimum):
            bag2.remove(chr(minimum))
        # print("...")
        # print(bag0)
        # print(bag1)
        # print(bag2)
        # print("---")
    value = (ord(item) - 97 + 1) if item.islower() else (ord(item) - 65 + 27)
    sum_value += value
    # print(item)
    # print(bag0.count(item))
    # print(bag1.count(item))
    # print(bag2.count(item))
print(sum_value)
