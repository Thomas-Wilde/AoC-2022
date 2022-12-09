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
        self.knots = []
        for _ in range(10):
            self.knots.append(Point(0, 0))

    def __str__(self) -> str:
        rope = "[" + str(self.head) + " " + str(self.tail) + "]"
        return rope

    def right(self) -> None:
        head = self.knots[0]
        head.move_x(1)
        self.move_tail()

    def left(self) -> None:
        head = self.knots[0]
        head.move_x(-1)
        self.move_tail()

    def up(self) -> None:
        head = self.knots[0]
        head.move_y(1)
        self.move_tail()

    def down(self) -> None:
        head = self.knots[0]
        head.move_y(-1)
        self.move_tail()

    def move_tail(self) -> None:
        for i in range(1, 10):
            self.move_knot(i)

    def is_knot_ok(self, idx: int) -> bool:
        head = self.knots[idx - 1]
        tail = self.knots[idx]
        dx = abs(tail.x - head.x)
        dy = abs(tail.y - head.y)
        if dx > 1 or dy > 1:
            return False
        return True

    def move_knot(self, idx: int) -> None:
        if self.is_knot_ok(idx):
            return
        head = self.knots[idx - 1]
        tail = self.knots[idx]
        dx = head.x - tail.x
        dy = head.y - tail.y
        total = abs(dx) + abs(dy)
        # print(str(dx) + " " + str(dy))
        if total > 2:
            sx = dx // 2 if abs(dx) == 2 else dx
            sy = dy // 2 if abs(dy) == 2 else dy
        if total == 2:
            sx = int(dx // 2)
            sy = int(dy // 2)
        self.knots[idx].x += sx
        self.knots[idx].y += sy
        # ---
        if not self.is_knot_ok(idx):
            print("something went wrong")

    def print_grid(self) -> None:
        tmp = ".................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................."
        for i in range(9, -1, -1):
            knot = self.knots[i]
            kx = knot.x
            ky = knot.y
            pos_k = ky * 26 + kx
            if pos_k == 26:
                tmp = tmp[:pos_k] + str(i)
            else:
                tmp = tmp[:pos_k] + str(i) + tmp[pos_k + 1 :]
        grid = ""
        ## col 26 rows 21
        for i in range(21):
            grid = tmp[i * 26 : i * 26 + 26] + "\n" + grid
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
        path.add(str(rope.knots[-1]))
    # rope.print_grid()

# print(path)
print(len(path))
