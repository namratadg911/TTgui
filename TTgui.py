from tkinter import *  #import package
from tkinter import messagebox # to show who won

active_player = 'X'
stop_game = False

def clicked(r,c):
    
    # active_player = "X"
    global active_player
    # global stop_game

    if active_player == "X" and states[r][c] == 0 and stop_game == False:
        b[r][c].configure(text = "X")
        states[r][c] = 'X'
        active_player='O'

    
    if active_player == 'O' and states[r][c] == 0 and stop_game == False:
        b[r][c].configure(text = 'O')
        states[r][c] = "O"
        active_player = "X"

    check_if_win()
    # check_if_tie()
    # if check_if_win() == False:
    #     tie = messagebox.showinfo("tie","its tie")
    #     return tie
def check_if_win():
    global stop_game
    # count = 0

    for i in range(3):
        if states[i][0] == states[i][1] == states[i][2] !=0:
            stop_game = True

            winner = messagebox.showinfo("Winner", states[i][0] + " Won")
            # disableAllButton()
            break

    # for j in range(3):
        elif states [0][i] == states[1][i] == states[2][i] != 0:
            stop_game = True

            winner = messagebox.showinfo("Winner", states[0][i]+ " Won!")
            break

        elif states[0][0] == states[1][1] == states[2][2] !=0:
            stop_game = True

            winner = messagebox.showinfo("Winner", states[0][0]+ " Won!")
            break

        elif states[0][2] == states[1][1] == states[2][0] !=0:
            stop_game = True

            winner = messagebox.showinfo("Winner" , states[0][2]+ " Won!")
            break

        elif states[0][0] and states[0][1] and states[0][2] and states[1][0] and states[1][1] and states[1][2] and states[2][0] and states[2][1] and states[2][2] != 0:
            stop_game = True

            winner = messagebox.showinfo("tie", "Tie")

# Design window
root = Tk()             #to create a window
root.title("Tic Tac Toe")  # Title of the window
root.resizable(0,0)

#buttons
b = [
     [0,0,0],
     [0,0,0],
     [0,0,0]]

#text for buttons
states = [
     [0,0,0],
     [0,0,0],
     [0,0,0]]

for i in range(3):
    for j in range(3): 
                                            #command = clicked means u need to write that function
        b[i][j] = Button(
                        height = 4, width = 8, 
                        font = ("Helvetica","20"), 
                        command = lambda r = i, c = j : clicked(r,c))
        b[i][j].grid(row = i, column = j)

# b[i][j].pack()
mainloop()             #To make sure the window stays and does not disappear

























# x = Label(root, text = "Player 1 : X")
# o = Label(root, text = "Player 2 : O")
 
# def clicked(r,c):
    # btn_text.set("X")
    # button.configure(text=Text.get())
    
    # if(button["text"] == "X"):
    #     button.configure(text="O")
    # else:
    #     button.configure(text="X")


