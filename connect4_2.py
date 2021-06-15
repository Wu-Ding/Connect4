import numpy as np
import random as rd
import math
import tkinter


#Check the row in which the piece will fall to
def fall_column(column, grid):
    empty_row = -1
    
    while (grid[empty_row + 1][column] == 0):
        empty_row = empty_row + 1
        if (empty_row == r_num-1):
            break
    
    #Returns the "lowest" empty row in the chosen column 
    return empty_row



#Place a piece
def place_piece(row, column, grid, player):
    
    grid[row][column] = player
    
    if (player == 1):
        color = "red"
    elif (player == 2):
        color = "yellow"
    else:
        color = "lime"
    
    #Update the color on the board
    o = canvas_list[row][column].create_oval(4,4,70,70,fill=color)
    
    return grid



#Check if the player wins on this turn
def winner(row, column, grid, player):
    
    r_coordinates = []
    r_sweep = 0
    #Getting the rows coordinates
    for c in range(column-sweep+1, column+sweep):
        if ((c < 0) or (c >= c_num)):
            continue
        coord = (row, c)
        r_coordinates.append(coord)
    #Checking for 4 in a row
    for coord in r_coordinates:
        if (grid[coord[0]][coord[1]] == player):
            r_sweep += 1
            if (r_sweep == sweep):
                return True
        else:
            r_sweep = 0
        
    c_coordinates = []
    c_sweep = 0
    #Getting the columns coordinates
    for r in range(row-sweep+1, row+sweep):
        if ((r < 0) or (r >= r_num)):
            continue
        coord = (r, column)
        c_coordinates.append(coord)
    #Checking for 4 in a row
    for coord in c_coordinates:
        if (grid[coord[0]][coord[1]] == player):
            c_sweep += 1
            if (c_sweep == sweep):
                return True
        else:
            c_sweep = 0
    
    d1_coordinates = []
    d1_sweep = 0
    #Getting the diagonal1 coordinates
    r = row-sweep+1
    c = column-sweep+1
    for i in range(2*sweep-1):
        if ((r < 0) or (r >= r_num) or (c < 0) or (c >= c_num)):
            r += 1
            c += 1
            continue
        coord = (r, c)
        d1_coordinates.append(coord)
        r += 1
        c += 1
    #Checking for 4 in a row
    for coord in d1_coordinates:
        if (grid[coord[0]][coord[1]] == player):
            d1_sweep += 1
            if (d1_sweep == sweep):
                return True
        else:
            d1_sweep = 0    
    
    d2_coordinates = []
    d2_sweep = 0
    #Getting the diagonal2 coordinates
    r = row-sweep+1
    c = column+sweep-1
    for i in range(2*sweep-1):
        if ((r < 0) or (r >= r_num) or (c < 0) or (c >= c_num)):
            r += 1
            c -= 1
            continue
        coord = (r, c)
        d2_coordinates.append(coord)
        r += 1
        c -= 1
    #Checking for 4 in a row
    for coord in d2_coordinates:
        if (grid[coord[0]][coord[1]] == player):
            d2_sweep += 1
            if (d2_sweep == sweep):
                return True
        else:
            d2_sweep = 0
    
    #If there is no four in a row
    return False


def tie(grid):
    for c in range(c_num):
        for r in range(r_num):
            if (grid[r][c] == 0):
                return False
    return True


def next_player(player, window):
    if (rando):
        #print("random")
        new_player = rd.randint(1, players)
        
        #Better odds
        if (new_player == player):
            go_again = rd.randint(1, players + 1)
            if (go_again != 1):
                new_player = rd.randint(1, players)
            
    elif (snake_draft):
        #print("snake")
        new_player = ((player + players + 1) % (2 * players + 1)) - players
        if (new_player == 0):
            new_player += 1
    else:
        #print("normal")
        new_player = (player % players) + 1
    
    tkinter.Label(window, text="                                   ", justify="center", height=2).grid(row=0, columnspan=c_num)
    tkinter.Label(window, text="Player "+str(abs(new_player))+ "'s turn", justify="center", height=2).grid(row=0, columnspan=c_num)
    
    if (abs(new_player) == 1):
        color = "red"
    elif (abs(new_player) == 2):
        color = "yellow"
    else:
        color = "lime"
    
    right_frame = tkinter.Frame(window, bg="black")
    right_frame.grid(row=0, column=c_num-1)
    right = tkinter.Label(right_frame, text="      ", bg=color, bd=0).pack(padx=1, pady=1)
    
    left_frame = tkinter.Frame(window, bg="black")
    left_frame.grid(row=0, column=0)
    left = tkinter.Label(left_frame, text="      ", bg=color, bd=0).pack(padx=1, pady=1)
    
    return new_player



def turn(column):
    global grid
    global player
    
    #Make sure the row is valid
    row = fall_column(column, grid)
    
    if (row == -1):
        label = tkinter.Label(window, text="                                                 ", justify="center", height=2).grid(row=r_num+3, columnspan=c_num)
        label = tkinter.Label(window, text="Column " + str(column + 1) + " is full. Choose again.", justify="center", height=2).grid(row=r_num+3, columnspan=c_num)
        return
    
    else:
        grid = place_piece(row, column, grid, abs(player))
        win = winner(row, column, grid, abs(player))
        
        if (win):
            label = tkinter.Label(window, text="                                   ", justify="center", height=2).grid(row=0, columnspan=c_num)
            label = tkinter.Label(window, text="Player "+str(abs(player))+ " wins!!!", justify="center", height=2).grid(row=0, columnspan=c_num)
            
            for b in button_list:
                b.destroy()
            
            return
        
        if (tie(grid)):
            label = tkinter.Label(window, text="                                   ", justify="center", height=2).grid(row=0, columnspan=c_num)
            label = tkinter.Label(window, text="Tie game. Losers.", justify="center", height=2).grid(row=0, columnspan=c_num)
            
            for b in button_list:
                b.destroy()
            
            return
       
        #Change players
        player = next_player(player, window)
        return


def turn0():
    return turn(0)
def turn1():
    return turn(1)
def turn2():
    return turn(2)
def turn3():
    return turn(3)
def turn4():
    return turn(4)
def turn5():
    return turn(5)
def turn6():
    return turn(6)
def turn7():
    return turn(7)
def turn8():
    return turn(8)
def turn9():
    return turn(9)
def turn10():
    return turn(10)



def play():
    global grid
    grid = np.zeros((r_num, c_num), int)
    
    global players
    players = int(entry.get())
    
    global rando
    global snake_draft
    global r
    global s
    rando = rando_state.get()
    snake_draft = snake_state.get()
    
    if (rando):
        snake_button.configure(bg="light gray")
        rando_button.configure(bg="pink")
        snake_button.deselect()
    elif (snake_draft):
        snake_button.configure(bg="pink")
        rando_button.configure(bg="light gray")
    else:
        snake_button.configure(bg="light gray")
        rando_button.configure(bg="light gray")
        
    
    #print(rando)
    #print(snake_draft)
    
    global player
    player = 0
    player = next_player(player, window)
    
    
    
    for r in range(r_num):
        for c in range(c_num):
            o = canvas_list[r][c].create_oval(4,4,70,70,fill="black")
            
    global button_list
    button_list = []
    
    for j in range(c_num):
        c = tkinter.Button(window, height=2, width=7, fg="grey", activeforeground="blue", activebackground="blue", text= "Place", command=turn_list[j])
        button_list.append(c)
    
    for j in range(c_num):
        button_list[j].grid(row=r_num + 1, column=j, pady=7)
        
    play_button.configure(command=reset)
    
    return



def reset():
    global grid
    grid = np.zeros((r_num, c_num), int)
    
    global players
    players = int(entry.get())
    
    global rando
    global snake_draft
    global r
    global s
    rando = rando_state.get()
    snake_draft = snake_state.get()
    
    if (rando):
        snake_button.configure(bg="light gray")
        rando_button.configure(bg="pink")
        snake_button.deselect()
    elif (snake_draft):
        snake_button.configure(bg="pink")
        rando_button.configure(bg="light gray")
    else:
        snake_button.configure(bg="light gray")
        rando_button.configure(bg="light gray")
        
    
    #print(rando)
    #print(snake_draft)
    
    global player
    player = 0
    player = next_player(player, window)
    
    
    
    for r in range(r_num):
        for c in range(c_num):
            o = canvas_list[r][c].create_oval(4,4,70,70,fill="black")
            
    global button_list
    
    if (len(button_list) != 0):
        for b in button_list:
            b.destroy()
            
    button_list = []
    
    for j in range(c_num):
        c = tkinter.Button(window, height=2, width=7, fg="grey", activeforeground="blue", activebackground="blue", text= "Place", command=turn_list[j])
        button_list.append(c)
    
    for j in range(c_num):
        button_list[j].grid(row=r_num + 1, column=j, pady=7)
    
    return
    
    
    







"""=================================================RUNNING==================================================="""
"""=================================================RUNNING==================================================="""
"""=================================================RUNNING==================================================="""


#Rules/Grid size
r_num = 6
c_num = 7
sweep = 4
grid = np.zeros((r_num, c_num), int)

"""player = 0
players = 2
rando = False
snake_draft = True"""

# Let's create the Tkinter window
window = tkinter.Tk()
window.title("Grid")
window.geometry(str(76*c_num)+"x"+str(100*(r_num + 1) - 20))

canvas_list = []

label = tkinter.Label(window, text="Welcome to connect "+str(sweep), justify="center", height=2).grid(row=0, columnspan=c_num)


#Making the board
for r in range(1,r_num+1):
    empty = []
    canvas_list.append(empty)
    for c in range(c_num):
        can = tkinter.Canvas(window, height=70, width=70, bg="light blue", bd=0)
        oval = can.create_oval(4,4,70,70,fill="black")
        canvas_list[r-1].append(can)
        can.grid(row=r, column=c, sticky="NESW")
    
#Adding the play button
play_button = tkinter.Button(window, height=2, width=10, fg="grey", activeforeground="blue", activebackground="blue", text="Play/Reset", padx=15, command=play)
play_button.grid(row=r_num+2, column=c_num//2 - 1, columnspan=3, pady=10)

#Adding the entry where we put the number of players
entry = tkinter.Entry(window, width=7, )
entry.grid(row=r_num+3, column=c_num-1)
entry.insert(0, "2")
p_label = tkinter.Label(window, text="Players").grid(row=r_num+3, column=c_num-2, sticky="E")

#adding the checkbutton to decide if the turns are snake_draft based
snake_state = tkinter.BooleanVar()
snake_button = tkinter.Checkbutton(window, bg="light gray", text="Snake", variable=snake_state, width=8, justify="left")
snake_button.grid(row=r_num+4, column=c_num-2, columnspan=2, sticky="E")

#adding the checkbutton to decide if the turns are random
rando_state = tkinter.BooleanVar()
rando_button = tkinter.Checkbutton(window, bg="light gray", text="Random", variable=rando_state, width=8, justify="left")
rando_button.grid(row=r_num+5, column=c_num-2, columnspan=2, sticky="E")

#Adding a label to indicate how many in a row is needed to win
frame = tkinter.Frame(window, bg="black")
frame.grid(row=r_num+3, column=0, columnspan=2, sticky="W")
tkinter.Label(frame, text=str(sweep)+" in a row to win").pack(padx=1, pady=1)

#Creating a list of functions that will add a piece to the column "i"
turn_list = []
turn_list.append(turn0)
turn_list.append(turn1)
turn_list.append(turn2)
turn_list.append(turn3)
turn_list.append(turn4)
turn_list.append(turn5)
turn_list.append(turn6)
turn_list.append(turn7)
turn_list.append(turn8)
turn_list.append(turn9)
turn_list.append(turn10)

#Running the tkinter
window.mainloop()
