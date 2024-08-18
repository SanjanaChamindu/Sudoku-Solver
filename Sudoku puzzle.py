from tkinter import *
import Sudoku_solver

wn=Tk()

colors=['#8B8B83','#7F7FFF','#FFA500','#EEEE3B','#FFFFD3','#646495','#00FF00','#0000FF','#FFFF14',]
for i in range (9):
    for j in range (3):
        for k in range (3):
            row_= i//3*3+j
            column_= i%3*3+k

            globals()[f'enter{i}{j}{k}']=Entry(wn,width=5,border=1,bg=colors[i])
            globals()[f'enter{i}{j}{k}'].grid(row=row_,column_=column_)

def print_puzzle(puzzle):
    for i in range (9):
        for j in range (3):
            for k in range (3):
                globals()[f'enter{i}{j}{k}'].delete(0,END)
                globals()[f'enter{i}{j}{k}'].insert(0,f'{puzzle[i][j][k]}')

def get_values():
    puzzle=[]
    for i in range(9):
        square_items=[]
        for j in range (3):
            row_items=[]
            for k in range (3):
                n=globals()[f'enter{i}{j}{k}'].get()
                if n=='':
                    n=0
                else:
                    try:
                        n=int(n)
                        if  not n>0 and n<10:
                            return 1
                    except:
                        return 0
                row_items.append(n)
            square_items.append(row_items)
        puzzle.append(square_items)
    
    right_puzzle=Sudoku_solver.solve_(puzzle)
    print_puzzle(right_puzzle)
    


def clear_board():
    for i in range (9):
        for j in range (3):
            for k in range (3):
                globals()[f'enter{i}{j}{k}'].delete(0,END)

Label(wn,width=45,height=1).grid(row=9,column=0,columnspan=9)

solve_button=Button(wn,text='Solve',width=5,command=get_values)
solve_button.grid(row=10,column=1,columnspan=3)

clear_button=Button(wn,text='Clear',width=5,command=clear_board)
clear_button.grid(row=10,column=5,columnspan=3)


wn.mainloop()