import tkinter
from tkinter import *
import random

LIVE=0
DEAD=1
KEEP=2

COLOR = ['black', 'white']

BASE_X=BASE_Y=4

class Area:
    _x=0
    _y=0
    _map_=[[]]    

    def __init__(self, X, Y):
        self._map_ = [ [DEAD for i in range(X)] for i in range(Y)]
        self._x = X
        self._y = Y
    
    def get_stat(self, _x, _y):
        return self._map_[_x][_y]
    
    def set_stat(self, _x, _y, val):
        self._map_[_x][_y] = val
    
    def set_stats(self, pos_list, val):
        for pos in pos_list:
            self._map_[pos[0]][pos[1]] = val

    def init_map(self, init_pos):
        for pos in init_pos:
            self._map_[pos[0]][pos[1]] = LIVE

    def init_map_random(self):
        for i in range(1, self._x - 1, 1):
            for j in range(1, self._y - 1, 1):
                self._map_[i][j] = random.randint(LIVE, DEAD)

    def show(self):
        i=0
        j=0
        for i in range(X):
            for j in range(Y):
                print( "%d"%(self.get_stat(i,j)), end='')    
            print("\n")
    
    def live_check(self, _x, _y):
        cnt = 0
        #do not check current centre point itself
        for i in range(- 1, 2, 1):
            for j in range(-1, 2, 1):
                if not (i == 0 and j == 0):
                    if self._map_[i + _x][j + _y] == LIVE:
                        cnt += 1
        
        if cnt < 2 and self._map_[_x][_y] == LIVE:
            return DEAD
        elif (cnt == 2 or cnt == 3) and self._map_[_x][_y] == LIVE:
            return KEEP
        elif cnt > 3 and self._map_[_x][_y] == LIVE:
            return DEAD
        elif cnt == 3 and self._map_[_x][_y] == DEAD:
            return LIVE
        else:
            return KEEP

def init_draw(tk, canvas, label, X, Y):
    print("Draw %d:%d map"%(X, Y))
    label.config(text=str(0))

    for i in range(0, X, 1):
        for j in range(0, Y, 1):
            x_lu = i * 5 + BASE_X
            y_lu = j * 5 + BASE_Y
            canvas.create_rectangle(x_lu, y_lu, x_lu + 5, y_lu + 5, fill=COLOR[DEAD])

    tk.update()    

def scan_and_draw(tk, canvas, label, _map, step):
    for i in range(_map._x - 1):
        for j in range(_map._y - 1):
            x_lu = i*5 + BASE_X
            y_lu = j*5 + BASE_Y
            fill_color = COLOR[DEAD]
            if _map.get_stat(i, j) == LIVE:
                fill_color = COLOR[LIVE]
            canvas.create_rectangle(x_lu, y_lu, x_lu+5, y_lu+5, fill=fill_color)

def do_life_switch(tk, canvas, _map, pos_list, life_stat):
    for pos in pos_list:
        fill_color = COLOR[LIVE]
        x_lu = pos[0] * 5 + BASE_X
        y_lu = pos[1] * 5 + BASE_Y 
        if(life_stat == DEAD):
            fill_color = COLOR[DEAD]
        canvas.create_rectangle(x_lu, y_lu, x_lu+5, y_lu+5, fill = fill_color)

def go_life_game(tk, canvas, label, _map, _step):
    die_pos = []
    born_pos = []

    for i in range(1, _map._x - 1, 1):
        for j in range(1, _map._y - 1, 1):
            ret = _map.live_check(i, j)
            if ret == DEAD:
                die_pos.append([i, j])
            elif ret == LIVE:
                born_pos.append([i, j])
            else:
                pass
    
    #update map data
    _map.set_stats(die_pos, DEAD)
    _map.set_stats(born_pos, LIVE)

    #update map canvas
    do_life_switch(tk, canvas, _map, die_pos, DEAD)
    do_life_switch(tk, canvas, _map, born_pos, LIVE)

    label.config(text = str(_step))

    tk.update()

def do_end_draw(tk):
    tk.mainloop()
    

    

