import enum

PAWN_LOCATION = None
KNIGHT_LOCATION = None


class Stack(list):
    def push(self, item):
        self.append(item)

    def isEmpty(self):
        return not self

    def peek(self):
        return self[len(self)-1]


class CoordLetters(enum.Enum):
    a = 1
    b = 2
    c = 3
    d = 4
    e = 5
    f = 6
    g = 7
    h = 8


class Pawn:
    x = None
    y = None

    def __init__(self, coords):
        x, y = [int(i) for i in str(coords)]
        self.x = x
        self.y = y

    def is_under_pawn_attack(self, coords):
        x, y = [int(i) for i in str(coords)]
        print(self.x, self.y)
        print(x, y)
        if self.y - 1 == y:
            if self.x + 1 == x or self.x - 1 == x:
                return True
        return False


class Knight:
    x = None
    y = None

    def __init__(self, coords):
        x, y = [int(i) for i in str(coords)]
        self.x = x
        self.y = y

class Cell():
    x = None
    y = None

    def __init__(self, coords):
        x, y = [int(i) for i in str(coords)]
        self.x = x
        self.y = y

def interpretate(coords):
    coords = str(coords)
    first_part = coords[:1]
    second_part = coords[1:]
    if first_part.isalpha():
        return int(str(CoordLetters[first_part].value) + second_part)
    else:
        return str(CoordLetters(int(first_part)).name + second_part)


with open("in.txt", 'r') as file:
    pawn_loc = file.read(2)
    PAWN_LOCATION = interpretate(pawn_loc)
    pawn_class = Pawn(PAWN_LOCATION)
    file.read(1)
    knight_loc = file.read()
    KNIGHT_LOCATION = interpretate(knight_loc)
    knight_class = Knight(KNIGHT_LOCATION)

stack = Stack()
stack.push(Cell(KNIGHT_LOCATION))
while stack.peek(). Cell(PAWN_LOCATION):

    break
