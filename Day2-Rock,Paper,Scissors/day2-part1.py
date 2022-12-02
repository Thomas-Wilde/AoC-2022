print("Day 2 - Rock, Paper, Scissors")

# Using readlines()
file = open("input.data", "r")
# file = open("example.data", "r")
lines = file.readlines()

# 1 - rock
# 2 - paper
# 3 - scissors
score = 0
for line in lines:
    select = line.split(" ")
    select[1] = select[1].replace("\n", "")
    # value for opponent
    op = -1
    match select[0]:
        case "A":  # rock
            op = 1
        case "B":  # paper
            op = 2
        case "C":  # scissors
            op = 3
    # value for me
    me = -1
    match select[1]:
        case "X":  # rock
            me = 1
        case "Y":  # paper
            me = 2
        case "Z":  # scissors
            me = 3
    print(str(op) + " " + str(me))
    # 1 2
    # 2 1
    # 3 3
    score += me
    if op == 1:  # rock
        match me:
            case 1:  # rock
                score += 3
            case 2:  # paper
                score += 6
            case 3:  # scissors
                score += 0
    if op == 2:  # paper
        match me:
            case 1:  # rock
                score += 0
            case 2:  # paper
                score += 3
            case 3:  # scissors
                score += 6
    if op == 3:  # scissors
        match me:
            case 1:  # rock
                score += 6
            case 2:  # paper
                score += 0
            case 3:  # scissors
                score += 3
print(score)
