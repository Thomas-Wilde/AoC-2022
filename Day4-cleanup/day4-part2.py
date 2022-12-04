# Using readlines()
file = open("input.data", "r")
# file = open("example.data", "r")
lines = file.readlines()
sum_value = 0
overlap = 0

for line in lines:
    # line = lines[0]
    line = line.replace("\n", "")
    elf0 = line.split(",")[0]
    elf1 = line.split(",")[1]
    # print(elf0 + " " + elf1)

    ### get sections
    s0_begin = int(elf0.split("-")[0])
    s0_end = int(elf0.split("-")[1])
    s1_begin = int(elf1.split("-")[0])
    s1_end = int(elf1.split("-")[1])
    # print(str(s0_begin) + "-" + str(s0_end) + "  " + str(s1_begin) + "-" + str(s1_end))

    ### two cases
    # 35-95,7-34
    if (s0_begin <= s1_begin) and (s0_end >= s1_begin):
        overlap += 1
        print(line)
        continue
    if (s1_begin <= s0_begin) and (s1_end >= s0_begin):
        overlap += 1
        print(line)
print(overlap)
