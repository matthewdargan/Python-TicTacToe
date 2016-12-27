from tkinter import * #Imports tkinter library

#Draws circle on board
def drawCircle(x, y):
    canvas_1.create_oval(x - 100, y  - 100, x + 100, y + 100, fill = "red", width = 3)

#Draws non-religious cross on board
def drawNonReligiousCross(x, y):
    canvas_1.create_line(x - 100, y - 100, x + 100, y + 100, fill = "red", width = 3)
    canvas_1.create_line(x + 100, y - 100, x - 100, y + 100, fill = "red", width = 3)

#Sets root to canvas funtion
root = Tk()

#Canvas size
CanWidth = 750
CanHeight = 750

#Title of canvas canvas_1 is generating
root.title('Tic Tac Toe')

#Initializes canvas_1
canvas_1 = Canvas(root, width = CanWidth, height = CanHeight)

#Sets grid for canvas_1
canvas_1.grid(row = 0, column = 1)

#Draws the lines dividing the tic-tac-toe boxes
canvas_1.create_line(250, 0, 250, 750, fill = "blue", width = 3)
canvas_1.create_line(500, 0, 500, 750, fill = "blue", width = 3)
canvas_1.create_line(0, 250, 750, 250, fill = "blue", width = 3)
canvas_1.create_line(0, 500, 750, 500, fill = "blue", width = 3)

#Oval class definition
class oval():
    def __init__(self, x, y, owner):
        self.x = x
        self.y = y
        self.owner = owner

#List created to hold all of board ovals
boardOvals = [0, 1, 2, 3, 4, 5, 6, 7, 8]

#Manual creation of all 9 board ovals
boardOvals[0] = oval(125, 125, 0)
boardOvals[1] = oval(375, 125, 0)
boardOvals[2] = oval(625, 125, 0)
boardOvals[3] = oval(125, 375, 0)
boardOvals[4] = oval(375, 375, 0)
boardOvals[5] = oval(625, 375, 0)
boardOvals[6] = oval(125, 625, 0)
boardOvals[7] = oval(375, 625, 0)
boardOvals[8] = oval(625, 625, 0)


drawCircle(boardOvals[0].x, boardOvals[0].y)
drawNonReligiousCross(boardOvals[1].x, boardOvals[1].y)
