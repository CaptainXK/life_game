from draw_map import *
from tkinter import messagebox

X=30
Y=30
tk = Tk()

def global_stop():
    global global_quit
    tkinter.messagebox.showinfo("warning","stop running")
    global_quit = 1

global_quit=0

def _main_():
    canvas = Canvas(tk, width = 5 * (X + 1), height = 5 * (Y + 1), bg='red')
    label = Label(tk, width = 20, bg = 'black', fg = 'white')
    stop_button = Button(tk, text='stop', command = global_stop)

    label.pack()#.pack() is used to control the presentation of component
    stop_button.pack()
    canvas.pack()

    cur_map = Area(X, Y)

    init_draw(tk, canvas, label, X, Y)

    # init_pos = [[50,51], [50,52], [51,51], [52, 52], [51, 53]]    

    # cur_map.init_map(init_pos)

    cur_map.init_map_random()

    scan_and_draw(tk, canvas, label, cur_map, 0)

    # do_end_draw(tk)

    global global_quit

    idx = 0

    while global_quit == 0:
        go_life_game(tk, canvas, label, cur_map, idx+1)
        idx += 1        

    do_end_draw(tk)

_main_()





