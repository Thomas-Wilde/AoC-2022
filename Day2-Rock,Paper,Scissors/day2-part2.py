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
        case "X":  # lose
            me = 0
        case "Y":  # draw
            me = 3
        case "Z":  # win
            me = 6
    print(str(op) + " " + str(me))
    # 1 - rock
    # 2 - paper
    # 3 - scissors
    score += me
    if op == 1:  # rock
        match me:
            case 0:  # lose → scissors
                score += 3
            case 3:  # draw → rock
                score += 1
            case 6:  # win → paper
                score += 2
    if op == 2:  # paper
        match me:
            case 0:  # lose → rock
                score += 1
            case 3:  # draw → paper
                score += 2
            case 6:  # win → scissors
                score += 3
    if op == 3:  # scissors
        match me:
            case 0:  # lose → paper
                score += 2
            case 3:  # draw → scissors
                score += 3
            case 6:  # win → rock
                score += 1
print(score)
