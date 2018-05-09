import enum

Pawn_coords = None
Knight_coords = None
visited = []


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

    def isEmpty(self):
        return not self

    def peek(self):
        return self[len(self)-1]


knight_deltas = \
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
        return (CoordLetters[first_part].value, int(second_part))
        #return int(str(CoordLetters[first_part].value) + second_part)
    else:
        return str(CoordLetters(int(first_part)).name + second_part)


with open("in.txt", "r") as file:
    knight_loc = file.read(2)
    file.read(1)
    pawn_loc = file.read(2)
    x1, y1 = interpretate(pawn_loc)
    Pawn_coords = Cell(x1, y1)
    x2, y2 = interpretate(knight_loc)
    Knight_coords = Cell(x2, y2)

knight_deltas_reversed = list(reversed(knight_deltas))
stack = Stack()
stack.push(Knight_coords)
while stack.peek() != Pawn_coords:
    cur_cell = stack.pop()
    if cur_cell in visited:
        continue
    visited.append(cur_cell)
    for delta in knight_deltas_reversed:
        future_move = cur_cell + delta
        if future_move is not None:
            stack.push(future_move)

result = ""
for cell in visited:
    result += str(cell) + "\n"
print(result[:-1] + "\n" + pawn_loc)

with open("out.txt", "w") as file:
    file.write(result)
