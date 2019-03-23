#!/usr/local/bin/python3

from sys import stdout
from numpy import ndarray
from time import sleep

import sys, pygame, random


class bend:
    def __init__(self, pos, dire):
        self.pos = pos;
        self.dire = (dire[0], dire[1]);

class snake:
    def __init__(self, _head, _len, _dire, _bends):
        self.head = _head;
        self.len = _len;
        self.dire = _dire;
        self.bends = _bends;

    def addBend(self, dire):
        if dire[0] == self.dire[0] or dire[1] == self.dire[1]:
            print (self.dire);
            print (dire);
        else:
            self.bends.insert(0, bend(0, self.dire));
            self.dire = dire;
class game:
    def __init__(self, gr, gc):
        self.r = gr;
        self.c = gc;
        self.grid = ndarray(shape=(self.r, self.r), dtype=int);
        self.prize = (20, 30);

    def clearGrid(self):
        for i in range(0, self.r):
            for j in range (0, self.c):
                self.grid[i][j] = 0;

    def addSnake(self, s):
        self.clearGrid();

        cpix = (s.head[0], s.head[1]);
        cdir = (-1*s.dire[0], -1*s.dire[1]);
        cben = 0;
        #stdout.write(self.grid);
        for i in range(0, s.len):
            self.grid[cpix[0]][cpix[1]] = 1
            if bends and cben < len(bends):
                if bends[cben].pos == i:
                    stdout.write(str(bends[cben].pos));
                    stdout.write(str(cdir));
                    cdir = (-1 * bends[cben].dire[0], -1 * bends[cben].dire[1]);
                    stdout.write(str(cdir));
                    cben += 1;
            cpix = (cpix[0] + cdir[0], cpix[1] + cdir[1]);
        self.grid[self.prize[0]][self.prize[1]] = 2;
            #stdout.write(cpix);

    def moveSnake(self, s):
        s.head = (s.head[0]+s.dire[0], s.head[1]+s.dire[1]);
        if s.bends:
            for bend in s.bends:
                bend.pos += 1;
                if bend.pos >= s.len:
                    del(bend);
        if s.head[0] >= self.r or s.head[0] < 0 or s.head[1] >= self.c or s.head[1] < 0:
            return False;
        elif self.grid[s.head[0]][s.head[1]] == 1:
            return False;
        elif self.grid[s.head[0]][s.head[1]] == 2:
            s.len += 1;
            self.prize = (random.randint(0, self.r-1),
                          random.randint(0, self.c-1));
            return True;
        return True;

    def draw(self, screen):
        print("Drawing");
        for i in range(self.r):
            for j in range(self.c):
                if (self.grid[i][j] == 1):
                    stdout.write(str(i) + ',' + str(j) + '\n')
                    screen.set_at((i, j), white)
        screen.set_at((self.prize), red);



g = game(100, 100);
bends = [];
head = (40, 40)
dire = (0, 1)
bends.append(bend(pos=2, dire=(1, 0)));
s = snake(head, 10, dire, bends);

pygame.init()
screen = pygame.display.set_mode((100, 100));
black = 0, 0, 0
red = 255, 0, 0
white = 255, 255, 255;

cont = True;
while cont:
    nokey = True;
    for event in pygame.event.get(): 
        # This is extremely important
        if event.type == pygame.QUIT: 
            sys.exit();
        elif event.type == pygame.KEYDOWN:
            # Dafuq?
            if (nokey):
                if event.key == pygame.K_UP:
                    print("UP")
                    nokey = False;
                    s.addBend((0, -1));
                elif event.key == pygame.K_DOWN:
                    print("DOWN")
                    nokey = False;
                    s.addBend((0, 1));
                elif event.key == pygame.K_LEFT:
                    print("L")
                    nokey = False;
                    s.addBend((-1, 0));
                elif event.key == pygame.K_RIGHT:
                    print("R")
                    nokey = False;
                    s.addBend((1, 0));
    screen.fill(black)
    g.addSnake(s);
    cont = g.moveSnake(s);
    g.draw(screen);
    pygame.display.flip();
    pygame.time.wait(500);
