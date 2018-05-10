import enum

PAWN_CELL = None
KNIGHT_CELL = None


class CoordLetters(enum.Enum):
    a = 1
    b = 2
    c = 3
    d = 4
    e = 5
    f = 6
    g = 7
    h = 8


class Cell:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, cell):
        if 0 < self.x + cell.x < 9 and 0 < self.y + cell.y < 9:
            return Cell(self.x + cell.x, self.y + cell.y)
        else:
            return None

    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            return True
        return False

    def __str__(self):
        return str(CoordLetters(self.x).name) + str(self.y)


class Stack(list):
    def push(self, item):
        self.append(item)

    def peek(self):
        if len(self) != 0:
            return self[len(self) - 1]
        return None


KNIGHT_DELTAS = \
    [
        Cell(1, 2),
        Cell(-1, 2),
        Cell(-2, 1),
        Cell(-2, -1),
        Cell(-1, -2),
        Cell(1, -2),
        Cell(2, -1),
        Cell(2, 1)
    ]


def interpretate(coords):
    coords = str(coords)
    first_part = coords[:1]
    second_part = coords[1:]
    if first_part.isalpha():
        return CoordLetters[first_part].value, int(second_part)
    else:
        return str(CoordLetters(int(first_part)).name + second_part)


with open("in.txt", "r") as file:
    knight_loc = file.read(2)
    file.read(1)
    pawn_loc = file.read(2)
    x1, y1 = interpretate(knight_loc)
    KNIGHT_CELL = Cell(x1, y1)
    x2, y2 = interpretate(pawn_loc)
    PAWN_CELL = Cell(x2, y2)


stack = Stack()
visited = []
stack.push(KNIGHT_CELL)
while stack.peek() != PAWN_CELL:
    cur_cell = stack.peek()
    for delta in KNIGHT_DELTAS:
        future_move = cur_cell + delta
        if future_move is not None and future_move not in visited:
            stack.push(future_move)
            visited.append(future_move)
            break
    if stack.peek() == cur_cell:
        stack.pop()


result = ""
for cell in stack:
    result += str(cell) + "\n"
print(result[:-1])

with open("out.txt", "w") as file:
    file.write(result)
