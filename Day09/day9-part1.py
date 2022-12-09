import math

# Point
# [x] save position
# [ ] compute distance

# Rope
# [x] member: head, tail
# [x] move
# [x] checks distance between head and tail
# [x] moves tail, if necessary

##--------------------------------------------------------------------------##
def test_point_class() -> None:
    pos = Point(0, 0)
    print(pos)
    pos.move_x(3)
    print(pos)
    pos.move_y(3)
    print(pos)
    pos.move_x(-5)
    print(pos)
    pos.move_y(-5)
    print(pos)


##--------------------------------------------------------------------------##
def test_head_move_I() -> None:
    rope = Rope()
    print(rope)
    rope.right()
    print(rope)
    rope.right()
    print(rope)
    rope.up()
    rope.up()
    print(rope)
    rope.down()
    rope.down()
    rope.down()
    print(rope)
    rope.left()
    print(rope)


##--------------------------------------------------------------------------##
def test_head_move_II() -> None:
    rope = Rope()
    rope.right()
    rope.right()
    print("check_move")
    rope.left()
    rope.up()
    rope.up()
    print("check_move")


##--------------------------------------------------------------------------##
def test_head_move_III() -> None:
    rope = Rope()
    print(rope)
    rope.right()
    print(rope)
    rope.right()
    print(rope)
    rope.up()
    print(rope)
    rope.up()
    print(rope)
    rope.down()
    print(rope)
    rope.down()
    print(rope)
    rope.down()
    print(rope)
    rope.left()
    print(rope)


##--------------------------------------------------------------------------##
class Point:
    def __init__(self, x_val: int, y_val: int):
        self.x = x_val
        self.y = y_val

    def move_x(self, dist: int) -> None:
        self.x += dist

    def move_y(self, dist: int) -> None:
        self.y += dist

    def __str__(self) -> str:
        point = "(" + str(self.x) + ", " + str(self.y) + ")"
        return point


##--------------------------------------------------------------------------##
class Rope:
    def __init__(self):
        self.head = Point(0, 0)
        self.tail = Point(0, 0)

    def __str__(self) -> str:
        rope = "[" + str(self.head) + " " + str(self.tail) + "]"
        return rope

    def right(self) -> None:
        self.head.move_x(1)
        self.move_tail()

    def left(self) -> None:
        self.head.move_x(-1)
        self.move_tail()

    def up(self) -> None:
        self.head.move_y(1)
        self.move_tail()

    def down(self) -> None:
        self.head.move_y(-1)
        self.move_tail()

    def is_tail_ok(self) -> bool:
        dx = abs(self.tail.x - self.head.x)
        dy = abs(self.tail.y - self.head.y)
        if dx > 1 or dy > 1:
            return False
        return True

    def move_tail(self) -> None:
        if self.is_tail_ok():
            return
        dx = self.head.x - self.tail.x
        dy = self.head.y - self.tail.y
        total = abs(dx) + abs(dy)
        if total == 3:
            sx = dx // 2 if abs(dx) == 2 else dx
            sy = dy // 2 if abs(dy) == 2 else dy
        if total == 2:
            sx = int(dx // 2)
            sy = int(dy // 2)
        self.tail.x += sx
        self.tail.y += sy
        # ---
        if not self.is_tail_ok():
            print("something went wrong")

    def print_grid(self) -> None:
        tmp = ".............................."
        hx = self.head.x
        hy = self.head.y
        pos_h = hy * 5 + hx
        tx = self.tail.x
        ty = self.tail.y
        pos_t = ty * 5 + tx
        tmp = tmp[:pos_h] + "H" + tmp[pos_h + 1 :]
        tmp = tmp[:pos_t] + "T" + tmp[pos_t + 1 :]
        grid = ""
        for i in range(5):
            grid = tmp[i * 5 : i * 5 + 6] + "\n" + grid
        grid += "\n"
        print(grid)


##--------------------------------------------------------------------------##
# file = open("example.data", "r")
file = open("input.data", "r")
lines = file.readlines()

rope = Rope()
path = set()
for line in lines:
    line = line.replace("\n", "")
    data = line.split(" ")
    dir = data[0]
    steps = int(data[1])
    # ---
    # print(line)
    for i in range(steps):
        match dir:
            case "R":
                rope.right()
            case "L":
                rope.left()
            case "U":
                rope.up()
            case "D":
                rope.down()
        path.add(str(rope.tail))
        # rope.print_grid()

# print(path)
print(len(path))
