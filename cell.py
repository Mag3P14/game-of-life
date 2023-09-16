from utils import *

class Cell:
    def __init__(self, x, y, size = 20, alive = False, alive_next_gen = False):
        self.x = x
        self.y = y
        self.alive = alive
        self.alive_next_gen = alive_next_gen
        self.size = size
        self.draw(screen, self.x, self.y, self.alive)

    def draw(self, screen ,x ,y ,alive):
        if self.alive:
            pygame.draw.rect(screen, white, (x, y, self.size, self.size))
        else:
            pygame.draw.rect(screen, black, (x, y, self.size, self.size))

    def clicked(self,pos):
        if pos[0] > self.x and pos[0] < self.x + self.size:
            if pos[1] > self.y and pos[1] < self.y + self.size:
                self.alive = not self.alive
                self.draw(screen,self.x,self.y,self.alive)
                return True
        return False

def init_cells(cells):
    size = 20
    x = 0
    y = 0
    i = 0
    while y < screen_h:
        while x < screen_w: 
            cells[i].append(Cell(x,y,size))
            x += size 
        y += size 
        x = 0
        i += 1
        cells.append([])

    cells.pop(-1)

