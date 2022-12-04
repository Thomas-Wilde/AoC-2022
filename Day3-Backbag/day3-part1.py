# Using readlines()
file = open("input.data", "r")
# file = open("example.data", "r")
lines = file.readlines()
sum_value = 0

for line in lines:
    # line = lines[0]
    # print(line)
    # split into compartments → single items and sort them
    line = line.replace("\n", "")
    l2 = int(len(line) / 2)
    comp0 = [*line[0:l2]]
    comp1 = [*line[l2:]]
    comp0.sort()
    comp1.sort()
    # print(comp0)
    # print(comp1)
    # search doubled entry
    i = int(0)
    j = int(0)
    item = ""
    while i < l2:
        if comp0[i] == comp1[j]:
            # print("found " + comp0[i] + comp1[j])
            item = comp0[i]
            break
        if comp0[i] < comp1[j]:
            i += 1
            continue
        if comp0[i] > comp1[j]:
            j += 1
            continue
        print("something went wrong")
    # convert to priority value
    value = int(-1)
    value = (ord(item) - 97 + 1) if item.islower() else (ord(item) - 65 + 27)
    sum_value += value
    # print(item + " " + str(value))
    # print("---")
print(sum_value)
