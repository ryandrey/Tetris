from tkinter import*
import random


class Segment:
    def __init__(self, x, y, color):
        self.instance = cnv.create_rectangle(x, y, x + CELL_SIZE, y + CELL_SIZE, fill = color, width = 2)


class J_tet():
    def __init__(self):
        self.color = 'cyan'
        self.round = 'N'
        self.segments = [Segment(5 * CELL_SIZE, -CELL_SIZE, self.color), Segment(5 * CELL_SIZE, -2 * CELL_SIZE, self.color), Segment(5 * CELL_SIZE, -3 * CELL_SIZE, self.color), Segment(4 * CELL_SIZE, -CELL_SIZE, self.color)]

    def move(self):
        for segment in self.segments:
            cnv.move(segment.instance, 0, CELL_SIZE)

    def turn(self):
        if self.round == 'N':
            x, y = cnv.coords(self.segments[0].instance)[:2]
            x = int(x // CELL_SIZE)
            y = int(y // CELL_SIZE)
            if x - 2 >= 0 and y + 1 < HEIGHT // CELL_SIZE and FIELD[y][x - 2] == 0 and FIELD[y + 1][x] == 0:
                self.round = 'W'
                cnv.move(self.segments[1].instance, -CELL_SIZE, CELL_SIZE)
                cnv.move(self.segments[2].instance, -2 * CELL_SIZE, 2 * CELL_SIZE)
                cnv.move(self.segments[3].instance, CELL_SIZE, CELL_SIZE)
        elif self.round == 'W':
            x, y = cnv.coords(self.segments[0].instance)[:2]
            x = int(x // CELL_SIZE)
            y = int(y // CELL_SIZE)
            if x + 1 < WIDTH // CELL_SIZE and y + 2 < HEIGHT // CELL_SIZE and FIELD[y + 2][x] == 0 and FIELD[y][x + 1] == 0:
                self.round = 'S'
                cnv.move(self.segments[1].instance, CELL_SIZE, CELL_SIZE)
                cnv.move(self.segments[2].instance, 2 * CELL_SIZE, 2 * CELL_SIZE)
                cnv.move(self.segments[3].instance, CELL_SIZE, -CELL_SIZE)
        elif self.round == 'S':
            x, y = cnv.coords(self.segments[0].instance)[:2]
            x = int(x // CELL_SIZE)
            y = int(y // CELL_SIZE)
            if x + 2 < WIDTH // CELL_SIZE and FIELD[y][x + 2] == 0 and FIELD[y + 1][x] == 0:
                self.round = 'E'
                cnv.move(self.segments[1].instance, CELL_SIZE, -CELL_SIZE)
                cnv.move(self.segments[2].instance, 2 * CELL_SIZE, -2 * CELL_SIZE)
                cnv.move(self.segments[3].instance, -CELL_SIZE, -CELL_SIZE)
        elif self.round == 'E':
            x, y = cnv.coords(self.segments[0].instance)[:2]
            x = int(x // CELL_SIZE)
            y = int(y // CELL_SIZE)
            if x - 1 >= 0 and FIELD[y][x - 1] == 0 and FIELD[y + 2][x] == 0:
                self.round = 'N'
                cnv.move(self.segments[1].instance, -CELL_SIZE, -CELL_SIZE)
                cnv.move(self.segments[2].instance, -2 * CELL_SIZE, -2 * CELL_SIZE)
                cnv.move(self.segments[3].instance, -CELL_SIZE, CELL_SIZE)


class L_tet:
    def __init__(self):
        self.color = 'violet'
        self.segments = [Segment(4 * CELL_SIZE, -CELL_SIZE, self.color), Segment(4 * CELL_SIZE, -2 * CELL_SIZE, self.color), Segment(4 * CELL_SIZE, -3 * CELL_SIZE, self.color), Segment(5 * CELL_SIZE, -CELL_SIZE, self.color)]
        self.round = 'N'

    def move(self):
        for segment in self.segments:
            cnv.move(segment.instance, 0, CELL_SIZE)

    def turn(self):
        if self.round == 'N':
            x, y = cnv.coords(self.segments[0].instance)[:2]
            x = int(x // CELL_SIZE)
            y = int(y // CELL_SIZE)
            if x - 2 >= 0 and FIELD[y][x - 1] == 0 and FIELD[y][x - 2] == 0:
                self.round = 'W'
                cnv.move(self.segments[1].instance, -CELL_SIZE, CELL_SIZE)
                cnv.move(self.segments[2].instance, -2 * CELL_SIZE, 2 * CELL_SIZE)
                cnv.move(self.segments[3].instance, -CELL_SIZE, -CELL_SIZE)
        elif self.round == 'W':
            x, y = cnv.coords(self.segments[0].instance)[:2]
            x = int(x // CELL_SIZE)
            y = int(y // CELL_SIZE)
            if y + 2 < HEIGHT // CELL_SIZE and FIELD[y + 1][x] == 0 and FIELD[y + 2][x] == 0:
                self.round = 'S'
                cnv.move(self.segments[1].instance, CELL_SIZE, CELL_SIZE)
                cnv.move(self.segments[2].instance, 2 * CELL_SIZE, 2 * CELL_SIZE)
                cnv.move(self.segments[3].instance, -CELL_SIZE, CELL_SIZE)
        elif self.round == 'S':
            x, y = cnv.coords(self.segments[0].instance)[:2]
            x = int(x // CELL_SIZE)
            y = int(y // CELL_SIZE)
            if x + 2 < WIDTH // CELL_SIZE and FIELD[y][x + 1] == 0 and FIELD[y][x + 2] == 0:
                self.round = 'E'
                cnv.move(self.segments[1].instance, CELL_SIZE, -CELL_SIZE)
                cnv.move(self.segments[2].instance, 2 * CELL_SIZE, -2 * CELL_SIZE)
                cnv.move(self.segments[3].instance, CELL_SIZE, CELL_SIZE)
        elif self.round == 'E':
            x, y = cnv.coords(self.segments[0].instance)[:2]
            x = int(x // CELL_SIZE)
            y = int(y // CELL_SIZE)
            if FIELD[y + 1][x] == 0 and FIELD[y + 2][x] == 0:
                self.round = 'N'
                cnv.move(self.segments[1].instance, -CELL_SIZE, -CELL_SIZE)
                cnv.move(self.segments[2].instance, -2 * CELL_SIZE, -2 * CELL_SIZE)
                cnv.move(self.segments[3].instance, CELL_SIZE, -CELL_SIZE)


class S_tet:
    def __init__(self):
        self.color = 'lightgreen'
        self.segments = [Segment(4 * CELL_SIZE, -CELL_SIZE, self.color), Segment(5 * CELL_SIZE, -CELL_SIZE, self.color), Segment(5 * CELL_SIZE, -2 * CELL_SIZE, self.color), Segment(6 * CELL_SIZE, -2 * CELL_SIZE, self.color)]
        self.round = 'N'

    def move(self):
        for segment in self.segments:
            cnv.move(segment.instance, 0, CELL_SIZE)

    def turn(self):
        if self.round == 'N':
            x, y = cnv.coords(self.segments[2].instance)[:2]
            x = int(x // CELL_SIZE)
            y = int(y // CELL_SIZE)
            if FIELD[y + 1][x + 1] == 0 and FIELD[y - 1][x] == 0:
                self.round = 'E'
                cnv.move(self.segments[0].instance, 2 * CELL_SIZE, 0)
                cnv.move(self.segments[1].instance, 0, -2 * CELL_SIZE)
        elif self.round == 'E':
            x, y = cnv.coords(self.segments[2].instance)[:2]
            x = int(x // CELL_SIZE)
            y = int(y // CELL_SIZE)
            if x > 0 and FIELD[y + 1][x] == 0 and FIELD[y + 1][x - 1] == 0:
                self.round = 'N'
                cnv.move(self.segments[0].instance, -2 * CELL_SIZE, 0)
                cnv.move(self.segments[1].instance, 0, 2 * CELL_SIZE)
                

class Z_tet:
    def __init__(self):
        self.color = 'green'
        self.segments = [Segment(4 * CELL_SIZE, -2 * CELL_SIZE, self.color), Segment(5 * CELL_SIZE, -2 * CELL_SIZE, self.color), Segment(5 * CELL_SIZE, -CELL_SIZE, self.color), Segment(6 * CELL_SIZE, -CELL_SIZE, self.color)]
        self.round = 'N'

    def move(self):
        for segment in self.segments:
            cnv.move(segment.instance, 0, CELL_SIZE)

    def turn(self):
        if self.round == 'N':
            x, y = cnv.coords(self.segments[1].instance)[:2]
            x = int(x // CELL_SIZE)
            y = int(y // CELL_SIZE)
            if y + 1 < HEIGHT // CELL_SIZE and FIELD[y + 1][x] == 0 and FIELD[y][x + 1] == 0 and FIELD[y - 1][x + 1] == 0:
                self.round = 'E'
                cnv.move(self.segments[0].instance, CELL_SIZE, CELL_SIZE)
                cnv.move(self.segments[2].instance, CELL_SIZE, -CELL_SIZE)
                cnv.move(self.segments[3].instance, 0, -2 * CELL_SIZE)
        elif self.round == 'E':
            x, y = cnv.coords(self.segments[1].instance)[:2]
            x = int(x // CELL_SIZE)
            y = int(y // CELL_SIZE)
            if x > 0 and FIELD[y][x - 1] == 0 and FIELD[y + 1][x] == 0 and FIELD[y + 1][x + 1] == 0:
                self.round = 'N'
                cnv.move(self.segments[0].instance, -CELL_SIZE, -CELL_SIZE)
                cnv.move(self.segments[2].instance, -CELL_SIZE, CELL_SIZE)
                cnv.move(self.segments[3].instance, 0, 2 * CELL_SIZE)
            

class T_tet:
    def __init__(self):
        self.color = 'orange'
        self.segments = [Segment(5 * CELL_SIZE, -2 * CELL_SIZE, self.color), Segment(4 * CELL_SIZE, -2 * CELL_SIZE, self.color), Segment(5 * CELL_SIZE, -CELL_SIZE, self.color), Segment(6 * CELL_SIZE, -2 * CELL_SIZE, self.color)]
        self.round = 'S'

    def move(self):
        for segment in self.segments:
            cnv.move(segment.instance, 0, CELL_SIZE)

    def turn(self):
        if self.round == 'S':
            x, y = cnv.coords(self.segments[0].instance)[:2]
            x = int(x // CELL_SIZE)
            y = int(y // CELL_SIZE)
            if FIELD[y - 1][x] == 0:
                self.round = 'E'
                cnv.move(self.segments[1].instance, CELL_SIZE, CELL_SIZE)
                cnv.move(self.segments[2].instance, CELL_SIZE, -CELL_SIZE)
                cnv.move(self.segments[3].instance, -CELL_SIZE, -CELL_SIZE)
        elif self.round == 'E':
            x, y = cnv.coords(self.segments[0].instance)[:2]
            x = int(x // CELL_SIZE)
            y = int(y // CELL_SIZE)
            if x > 0 and FIELD[y][x - 1] == 0:
                self.round = 'N'
                cnv.move(self.segments[1].instance, CELL_SIZE, -CELL_SIZE)
                cnv.move(self.segments[2].instance, -CELL_SIZE, -CELL_SIZE)
                cnv.move(self.segments[3].instance, -CELL_SIZE, CELL_SIZE)
        elif self.round == 'N':
            x, y = cnv.coords(self.segments[0].instance)[:2]
            x = int(x // CELL_SIZE)
            y = int(y // CELL_SIZE)
            if y + 1 < HEIGHT // CELL_SIZE and FIELD[y + 1][x] == 0:
                self.round = 'W'
                cnv.move(self.segments[1].instance, -CELL_SIZE, -CELL_SIZE)
                cnv.move(self.segments[2].instance, -CELL_SIZE, CELL_SIZE)
                cnv.move(self.segments[3].instance, CELL_SIZE, CELL_SIZE)
        elif self.round == 'W':
            x, y = cnv.coords(self.segments[0].instance)[:2]
            x = int(x // CELL_SIZE)
            y = int(y // CELL_SIZE)
            if x + 1 < WIDTH // CELL_SIZE and FIELD[y][x + 1] == 0:
                self.round = 'S'
                cnv.move(self.segments[1].instance, -CELL_SIZE, CELL_SIZE)
                cnv.move(self.segments[2].instance, CELL_SIZE, CELL_SIZE)
                cnv.move(self.segments[3].instance, CELL_SIZE, -CELL_SIZE)


class I_tet:
    def __init__(self):
        self.round = 'N'
        self.color = 'blue'
        self.segments = [Segment(4 * CELL_SIZE, -CELL_SIZE, self.color), Segment(4 * CELL_SIZE, -2 * CELL_SIZE, self.color), Segment(4 * CELL_SIZE, -3 * CELL_SIZE, self.color), Segment(4 * CELL_SIZE, -4 * CELL_SIZE, self.color)]

    def move(self):
        for segment in self.segments:
            cnv.move(segment.instance, 0, CELL_SIZE)

    def turn(self):
        if self.round == 'N':
            place = True
            for i in range(1, 4):
                x, y = cnv.coords(self.segments[i].instance)[:2]
                x = int(x // CELL_SIZE)
                y = int(y // CELL_SIZE)
                if not (0 <= x + i < WIDTH // CELL_SIZE and y + i < HEIGHT // CELL_SIZE) or FIELD[y + i][x + i] != 0:
                    place = False
                    break
            if place:
                self.round = 'E'
                for i in range(4):
                    cnv.move(self.segments[i].instance, i * CELL_SIZE, i * CELL_SIZE)
        else:
            place = True
            for i in range(1, 4):
                x, y = cnv.coords(self.segments[i].instance)[:2]
                x = int(x // CELL_SIZE)
                y = int(y // CELL_SIZE)
                if not (0 <= x - i < WIDTH // CELL_SIZE and y - i < HEIGHT // CELL_SIZE) or FIELD[y - i][x - i] != 0:
                    place = False
                    break
            if place:
                self.round = 'N'
                for i in range(4):
                    cnv.move(self.segments[i].instance, -i * CELL_SIZE, -i * CELL_SIZE)
            

    

class O_tet:
    def __init__(self):
        self.color = 'red'
        self.segments = [Segment(4 * CELL_SIZE, -CELL_SIZE, self.color), Segment(4 * CELL_SIZE, -2 * CELL_SIZE, self.color), Segment(5 * CELL_SIZE, -CELL_SIZE, self.color), Segment(5 * CELL_SIZE, -2 * CELL_SIZE, self.color)]

    def move(self):
        for segment in self.segments:
            cnv.move(segment.instance, 0, CELL_SIZE)

    def turn(self):
        return


def event(event):
    global tet, pause, PAUSE
    if event.keysym == 'Escape':
        pause = not pause
        if pause:
            PAUSE = cnv.create_text(WIDTH // 2, HEIGHT // 2, text = 'PAUSE', fill = 'red', font = 'Arial 30')
        else:
            cnv.delete(PAUSE)
    if not pause:
        if event.keysym == 'Right':
            for segment in tet.segments:
                x = int(cnv.coords(segment.instance)[0] // CELL_SIZE)
                y = int(cnv.coords(segment.instance)[1] // CELL_SIZE)
                if cnv.coords(segment.instance)[0] == WIDTH - CELL_SIZE or FIELD[y][x + 1] != 0:
                    break
            else:
                for segment in tet.segments:
                    cnv.move(segment.instance, CELL_SIZE, 0)
        elif event.keysym == 'Left':
            for segment in tet.segments:
                x = int(cnv.coords(segment.instance)[0] // CELL_SIZE)
                y = int(cnv.coords(segment.instance)[1] // CELL_SIZE)
                if cnv.coords(segment.instance)[0] == 0 or FIELD[y][x - 1] != 0:
                    break
            else:
                for segment in tet.segments:
                    cnv.move(segment.instance, -CELL_SIZE, 0)
        elif event.keysym == 'space':
            tet.turn()
        elif event.keysym == 'Down' and tet != 0:
            place = True
            for segment in tet.segments:
                x, y = cnv.coords(segment.instance)[0], cnv.coords(segment.instance)[1]
                x = int(x // CELL_SIZE)
                y = int(y // CELL_SIZE)
                if y + 1 >= 0 and (y == HEIGHT // CELL_SIZE - 1 or FIELD[y + 1][x] != 0):
                    place = False
                    break
            if place:
                tet.move()
            

def new_tet():
    global tet
    i = random.randint(0, 6)
    if i == 0:
        tet = O_tet()
    if i == 1:
        tet = I_tet()
    if i == 2:
        tet = T_tet()
    if i == 3:
        tet = Z_tet()
    if i == 4:
        tet = S_tet()
    if i == 5:
        tet = L_tet()
    if i == 6:
        tet = J_tet()



def delete():
    global scores
    lines = 0
    for i in range(HEIGHT // CELL_SIZE - 1, -1, -1):
        if FIELD[i].count(0) == 0:
            lines += 1
            for segment in FIELD[i]:
                cnv.delete(segment.instance)
            FIELD[i] = [-1] * (WIDTH // CELL_SIZE)
    i = HEIGHT // CELL_SIZE - 1
    while i != -1:
        if FIELD[i].count(-1) == WIDTH // CELL_SIZE:
            for j in range(i - 1, -1, -1):
                for segment in FIELD[j]:
                    if segment != 0 and segment != -1:
                        cnv.move(segment.instance, 0, CELL_SIZE)
                FIELD[j + 1] = FIELD[j][:]
            FIELD[0] = [0] * (WIDTH // CELL_SIZE)
        else:
            i -= 1
    scores += (2 ** lines - 1) * 10 + 4
    cnv2.itemconfig(SCORES, text = str(scores))


            
def main():
    global IN_GAME, tet, TETS, pause
    if IN_GAME and not pause:
        place = True
        for segment in tet.segments:
            x, y = cnv.coords(segment.instance)[0], cnv.coords(segment.instance)[1]
            x = int(x // CELL_SIZE)
            y = int(y // CELL_SIZE)
            if y + 1 >= 0 and (y == HEIGHT // CELL_SIZE - 1 or FIELD[y + 1][x] != 0):
                place = False
                break
        if place:
            tet.move()
            cnv.after(300, main)
        else:
            for segment in tet.segments:
                x, y = cnv.coords(segment.instance)[0], cnv.coords(segment.instance)[1]
                x = int(x // CELL_SIZE)
                y = int(y // CELL_SIZE)
                if y < 0:
                    IN_GAME = False
                    break
                else:
                    FIELD[y][x] = segment
            tet = 0
            delete()
            new_tet()
            cnv.after(300, main)
    elif pause:
        cnv.after(500, main)
            
    
  

root = Tk()
root.geometry('800x500+100+100')
root.title('Tetris')

WIDTH = 200
HEIGHT = 400
CELL_SIZE = 20
IN_GAME = True
pause = False
scores = 0

cnv2 = Canvas(root, height = 100, width = 200)
SCORES = cnv2.create_text(50, 50, text = str(scores), font = 'Verdana 25')
cnv = Canvas(root, width = WIDTH, height = HEIGHT, bg = '#EEEEEE')
cnv.focus_set()
for i in range(WIDTH // CELL_SIZE):
    cnv.create_line(CELL_SIZE * i, 0, CELL_SIZE * i, HEIGHT, fill = '#4444AA')
for i in range(HEIGHT // CELL_SIZE):
    cnv.create_line(0, CELL_SIZE * i, WIDTH, CELL_SIZE * i, fill = '#4444AA')
cnv.bind('<KeyPress>', event)
FIELD = [[0] * (WIDTH // CELL_SIZE) for i in range(HEIGHT // CELL_SIZE)]
new_tet()
main()

cnv.pack()
cnv2.pack()
root.mainloop()
