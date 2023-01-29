import sys

class Game:
    def __init__(self, N, L, field, rotates):
        self.size = N
        self.snake = Snake()
        self.field = field
        self.rotates = rotates
        self.num = L
        self.check = 0
        self.turn = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        ny, nx = self.snake.move()
        if (ny >= N or nx >= N or ny < 0 or nx < 0) or (field[ny][nx] == 2):
            raise StopIteration
        if field[ny][nx] == 0:
            oy, ox = self.snake.shorten()
            field[oy][ox] = 0
        field[ny][nx] = 2
        self.turn += 1
        if self.check < self.num and (self.rotates[self.check][0] == str(self.turn)):
            self.snake.rotate(self.rotates[self.check][1])
            self.check += 1


class Snake:
    def __init__(self):
        self.loc = [(0, 0)]
        self.dx = [1, 0, -1, 0]
        self.dy = [0, 1, 0, -1]
        self.dir = 0
        
    def move(self):
        nx = self.loc[-1][1] + self.dx[self.dir]
        ny = self.loc[-1][0] + self.dy[self.dir]
        self.loc.append((ny, nx))
        return ny, nx
    
    def shorten(self):
        return self.loc.pop(0)

    def right(self):
        self.dir = (self.dir + 1) % 4
    
    def left(self):
        self.dir = (self.dir - 1) % 4

    def rotate(self, r):
        if r == 'D':
            self.right()
        elif r == 'L':
            self.left()


if __name__ == '__main__':
    input = sys.stdin.readline
    N, K = int(input()), int(input())
    field = [[0] * N for _ in range(N)]
    field[0][0] = 2
    for _ in range(K):
        x, y = input().rstrip().split()
        field[int(x)-1][int(y)-1] = 1

    L = int(input())
    rotates = [input().rstrip().split() for _ in range(L)]
    
    game = Game(N, L, field, rotates)
    for _ in game:
        pass
    
    print(game.turn + 1)