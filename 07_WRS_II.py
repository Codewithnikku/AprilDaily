class Robot:

    def __init__(self, width, height):
        self.w, self.h = width, height
        self.x = self.y = 0
        self.dir = 0
        self.d = ["East", "North", "West", "South"]

    def step(self, num: int) -> None:
        cycle = 2 * (self.w + self.h) - 4
        num %= cycle

        if num == 0:
            if self.x == 0 and self.y == 0:
                self.dir = 3
            return

        while num > 0:
            if self.dir == 0:
                move = min(num, self.w - 1 - self.x)
                self.x += move; num -= move
                if move == 0: self.dir = 1
            elif self.dir == 1:
                move = min(num, self.h - 1 - self.y)
                self.y += move; num -= move
                if move == 0: self.dir = 2
            elif self.dir == 2:
                move = min(num, self.x)
                self.x -= move; num -= move
                if move == 0: self.dir = 3
            else:
                move = min(num, self.y)
                self.y -= move; num -= move
                if move == 0: self.dir = 0

    def getPos(self):
        return [self.x, self.y]

    def getDir(self):
        return self.d[self.dir]