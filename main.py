from tkinter import *

#draws circle on board
def drawCircle(x, y):
    canvas_1.create_oval(x - 100, y  - 100, x + 100, y + 100, fill = "red", width = 3)

#draws non-religious cross on board
def drawNonReligiousCross(x, y):
    canvas_1.create_line(x - 100, y - 100, x + 100, y + 100, fill = "red", width = 3)
    canvas_1.create_line(x + 100, y - 100, x - 100, y + 100, fill = "red", width = 3)

def coordinateCheck(x, y):

    boardOvalX = 0
    boardOvalY = 0

    #checks x position of mouse click
    if (x == 0):                     #added to remove inital value of mouse click (error handler)
        boardOvalX = 0
    elif (x <= 250):
        boardOvalX = 1
    elif (x > 250 and x <= 500):
        boardOvalX = 2
    else:
        boardOvalX = 3

    #checks y position of mouse click
    if (y == 0):                     #added to remove inital value of mouse click (error handler)
        boardOvalY = 0
    elif (y <= 250):
        boardOvalY = 1
    elif (y > 250 and y <= 500):
        boardOvalY = 2
    else:
        boardOvalY = 3

    return str(boardOvalX) + str(boardOvalY)

#creates global variable for coordinates need to get coords from playerInput function
mouseX = 0
mouseY = 0
coordinates = '0'

#gets mouse click and sets input to global variables: mouseX and mouseY
def playerInput(event):

    global mouseX, mouseY

    mouseX, mouseY = event.x, event.y

    #converts mouse click into coordinates
    global coordinates

    #calls function that figures out which oval was clicked
    coordinates = coordinateCheck(mouseX, mouseY)

    #error handler that sees if oval clicked was previously owned
    legalMoveFlag = legalMoveCheck(coordinates)

    if legalMoveFlag == 0:
        updateBoardOval(coordinates)
        updateTurn()

    gameLogic()

#sets root to canvas funtion
root = Tk()
root2 = Tk()

#canvas size
CanWidth = 750
CanHeight = 750

#initializes canvas_1 which displays board
canvas_1 = Canvas(root, width = CanWidth, height = CanHeight)

#initializes canvas_2 which displays player information/winner condition
canvas_2 = Canvas(root2, width = 350, height = 200)

#title of canvas canvas_1 is generating
root.title('Tic Tac Toe')

#sets grid for canvas_1
canvas_1.grid(row = 0, column = 1)

#sets grid for canvas_2
canvas_2.grid(row = 0, column = 1)

#welcoime to the game!
canvas_2.create_text(175, 100, fill = "blue", font = "Times 20 italic bold", text = "Welcome! Click to begin.")

#draws the lines dividing the tic-tac-toe boxes
canvas_1.create_line(250, 0, 250, 750, fill = "blue", width = 3)
canvas_1.create_line(500, 0, 500, 750, fill = "blue", width = 3)
canvas_1.create_line(0, 250, 750, 250, fill = "blue", width = 3)
canvas_1.create_line(0, 500, 750, 500, fill = "blue", width = 3)


#gets size of screen game is being run on
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

#calculate position x and y coordinates and then sets canvas_1 location to center of screen
x = (screen_width / 2) - (CanWidth / 2)
y = (screen_height / 2) - (CanHeight / 2)
root.geometry('%dx%d+%d+%d' % (CanWidth, CanHeight, x, y))

#checks for player mouse input
canvas_1.bind("<Button-1>", playerInput)

#oval class definition
class oval():
    def __init__(self, x, y, owner):
        self.x = x
        self.y = y
        self.owner = owner

#list created to hold all of board ovals
boardOvals = [0, 1, 2, 3, 4, 5, 6, 7, 8]

#manual creation of all 9 board ovals
boardOvals[0] = oval(125, 125, 0)
boardOvals[1] = oval(375, 125, 0)
boardOvals[2] = oval(625, 125, 0)
boardOvals[3] = oval(125, 375, 0)
boardOvals[4] = oval(375, 375, 0)
boardOvals[5] = oval(625, 375, 0)
boardOvals[6] = oval(125, 625, 0)
boardOvals[7] = oval(375, 625, 0)
boardOvals[8] = oval(625, 625, 0)

#draw shape on board based on user input
def updateBoardOval(string):

    global player

    if string == '11':
        boardOvals[0].owner = player
        if boardOvals[0].owner == 1:
            drawCircle(boardOvals[0].x, boardOvals[0].y)
        elif boardOvals[0].owner == 2:
            drawNonReligiousCross(boardOvals[0].x, boardOvals[0].y)
    elif string == '21':
        boardOvals[1].owner = player
        if boardOvals[1].owner == 1:
            drawCircle(boardOvals[1].x, boardOvals[1].y)
        elif boardOvals[1].owner == 2:
            drawNonReligiousCross(boardOvals[1].x, boardOvals[1].y)
    elif string == '31':
        boardOvals[2].owner = player
        if boardOvals[2].owner == 1:
            drawCircle(boardOvals[2].x, boardOvals[2].y)
        elif boardOvals[2].owner == 2:
            drawNonReligiousCross(boardOvals[2].x, boardOvals[2].y)
    elif string == '12':
        boardOvals[3].owner = player
        if boardOvals[3].owner == 1:
            drawCircle(boardOvals[3].x, boardOvals[3].y)
        elif boardOvals[3].owner == 2:
            drawNonReligiousCross(boardOvals[3].x, boardOvals[3].y)
    elif string == '22':
        boardOvals[4].owner = player
        if boardOvals[4].owner == 1:
            drawCircle(boardOvals[4].x, boardOvals[4].y)
        elif boardOvals[4].owner == 2:
            drawNonReligiousCross(boardOvals[4].x, boardOvals[4].y)
    elif string == '32':
        boardOvals[5].owner = player
        if boardOvals[5].owner == 1:
            drawCircle(boardOvals[5].x, boardOvals[5].y)
        elif boardOvals[5].owner == 2:
            drawNonReligiousCross(boardOvals[5].x, boardOvals[5].y)
    elif string == '13':
        boardOvals[6].owner = player
        if boardOvals[6].owner == 1:
            drawCircle(boardOvals[6].x, boardOvals[6].y)
        elif boardOvals[6].owner == 2:
            drawNonReligiousCross(boardOvals[6].x, boardOvals[6].y)
    elif string == '23':
        boardOvals[7].owner = player
        if boardOvals[7].owner == 1:
            drawCircle(boardOvals[7].x, boardOvals[7].y)
        elif boardOvals[7].owner == 2:
            drawNonReligiousCross(boardOvals[7].x, boardOvals[7].y)
    else:
        boardOvals[8].owner = player
        if boardOvals[8].owner == 1:
            drawCircle(boardOvals[8].x, boardOvals[8].y)
        elif boardOvals[8].owner == 2:
            drawNonReligiousCross(boardOvals[8].x, boardOvals[8].y)

def legalMoveCheck(string):
    if string == '11':
        if boardOvals[0].owner == 0:
            return 0
    elif string == '21':
        if boardOvals[1].owner == 0:
            return 0
    elif string == '31':
        if boardOvals[2].owner == 0:
            return 0
    elif string == '12':
        if boardOvals[3].owner == 0:
            return 0
    elif string == '22':
        if boardOvals[4].owner == 0:
            return 0
    elif string == '32':
        if boardOvals[5].owner == 0:
            return 0
    elif string == '13':
        if boardOvals[6].owner == 0:
            return 0
    elif string == '23':
        if boardOvals[7].owner == 0:
            return 0
    elif string == '33':
        if boardOvals[8].owner == 0:
            return 0
    else:
        return 1

#global variable to keep track of turn
turn = 0
player = 0
def updateTurn():

    global turn
    global player

    turn = turn + 1

    #player 2
    if (turn % 2 == 0):
        player = 2
        canvas_2.delete("all")
        canvas_2.create_text(175, 100, fill = "blue", font = "Times 20 italic bold", text = "Player 2's turn!")

    #player 1
    else:
        player = 1
        canvas_2.delete("all")
        canvas_2.create_text(175, 100, fill = "blue", font = "Times 20 italic bold", text = "Player 1's turn!")

def gameLogic():
    gameWinner = 0

    if (boardOvals[0].owner == boardOvals[1].owner and boardOvals[1].owner == boardOvals[2].owner) and boardOvals[0].owner != 0:
        gameWinner = boardOvals[0].owner
        canvas_1.create_line(10, 125, 740, 125, fill = "black", width = 3)
    elif (boardOvals[3].owner == boardOvals[4].owner and boardOvals[4].owner == boardOvals[5].owner) and boardOvals[3].owner != 0:
        gameWinner = boardOvals[3].owner
        canvas_1.create_line(10, 375, 740, 375, fill = "black", width = 3)
    elif (boardOvals[6].owner == boardOvals[7].owner and boardOvals[7].owner == boardOvals[8].owner) and boardOvals[6].owner != 0:
        gameWinner = boardOvals[6].owner
        canvas_1.create_line(10, 625, 740, 625, fill = "black", width = 3)
    elif (boardOvals[0].owner == boardOvals[4].owner and boardOvals[4].owner == boardOvals[8].owner) and boardOvals[0].owner != 0:
        gameWinner = boardOvals[0].owner
        canvas_1.create_line(10, 10, 740, 740, fill = "black", width = 3)
    elif (boardOvals[2].owner == boardOvals[4].owner and boardOvals[4].owner == boardOvals[6].owner) and boardOvals[2].owner != 0:
        gameWinner = boardOvals[2].owner
        canvas_1.create_line(740, 10, 10, 740, fill = "black", width = 3)
    elif (boardOvals[0].owner == boardOvals[3].owner and boardOvals[3].owner == boardOvals[6].owner) and boardOvals[0].owner != 0:
        gameWinner = boardOvals[0].owner
        canvas_1.create_line(125, 10, 125, 740, fill = "black", width = 3)
    elif (boardOvals[1].owner == boardOvals[4].owner and boardOvals[4].owner == boardOvals[7].owner) and boardOvals[1].owner != 0:
        gameWinner = boardOvals[1].owner
        canvas_1.create_line(375, 10, 375, 740, fill = "black", width = 3)
    elif (boardOvals[2].owner == boardOvals[5].owner and boardOvals[5].owner == boardOvals[8].owner) and boardOvals[2].owner != 0:
        gameWinner = boardOvals[2].owner
        canvas_1.create_line(625, 10, 625, 740, fill = "black", width = 3)


    if gameWinner == 1:
        canvas_2.delete("all")
        canvas_2.create_text(175, 100, fill = "blue", font = "Times 20 italic bold", text = "Player 1 Wins!")
    elif gameWinner == 2:
        canvas_2.delete("all")
        canvas_2.create_text(175, 100, fill = "blue", font = "Times 20 italic bold", text = "Player 2 Wins!")
