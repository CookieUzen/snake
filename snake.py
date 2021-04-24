import curses
import random

WIDTH = 4
HEIGHT = 4

# The playing field is calculated using the grid below
# This way, we do not have to create an array to store 
# the entirety of the playing field, but just where the
# snake occupies space.
#
# For example, the index of a 4 by 4 playing field is 
# listed below.
# +-----------+
# |0 |1 |2 |3 |
# |--+--+--+--|
# |4 |5 |6 |7 |
# |--+--+--+--|
# |8 |9 |10|11|
# |--+--+--+--|
# |12|13|14|15|
# +-----------+
#
# Use the gridToX and gridToY functions to
# find the x/y grids of each index.
#
# The following table show the x/y grid of a 4 by 4
# playing field:
#
# +-------+-------+-------+-------+
# | (0,0) | (1,0) | (2,0) | (3,0) |
# +-------+-------+-------+-------+
# | (0,1) | (1,1) | (2,1) | (3,1) |
# +-------+-------+-------+-------+
# | (0,2) | (1,2) | (2,2) | (3,2) |
# +-------+-------+-------+-------+
# | (0,3) | (1,3) | (2,3) | (3,3) |
# +-------+-------+-------+-------+

# Define main snake list
# snake[length][position/ttl]
snake = []
snakeLength = 5

# Define cursor for controlling snake
cursorX = 0
cursorY = 0
cursorRotation = 0

# Define array for storing apples
apple = []

# If game is over
gameEnd = False


def gridToX(gridInput):
    """Return x grid from grid grids"""
    return gridInput % WIDTH


def gridToY(gridInput):
    """Return x grid from grid grids"""
    return gridInput // HEIGHT


def coordinateToGrid(x, y):
    """Return grid from x y coordinates"""
    return y*WIDTH + x


def addLength(x, y):
    """Add new head of snake"""

    gridInput = coordinateToGrid(x, y)

    # Append to snake
    snake.insert(0, [gridInput, snakeLength])

    # Remove tail of snake
    for i in range(len(snake)):
        snake[i][1] -= 1

        if snake[i][1] < 0:
            snake.pop(i)


def printGrid():
    """print the playing field"""

    # Print top and bottom bars
    screen.clear()
    screen.addstr(0, 0, "+"+"-"*(WIDTH*2)+"+")
    screen.addstr(HEIGHT+1, 0, "+"+"-"*(WIDTH*2)+"+")

    for i in range(1, HEIGHT+1):
        screen.addstr(i, 0, "|")

    for i in range(1, HEIGHT+1):
        screen.addstr(i, WIDTH*2+1, "|")


def initCurses():
    """start curses"""
    global screen
    screen = curses.initscr()
    curses.noecho()
    curses.cbreak()
    curses.curs_set(0)
    screen.keypad(True)

    # start color
    curses.start_color()
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_CYAN)
    curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_GREEN)
    curses.init_pair(3, curses.COLOR_RED, curses.COLOR_BLACK)


def endCurses():
    """ends curses"""
    curses.curs_set(1)
    curses.endwin()


def printSnake():
    """print the snake on the playing field"""

    # print snake head
    screen.addstr(gridToY(snake[0][0])+1, gridToX(snake[0][0])*2+1, "[]", curses.color_pair(1))

    # print snake tail
    for i in range(1, len(snake)):
        screen.addstr(gridToY(snake[i][0])+1, gridToX(snake[i][0])*2+1, "  ", curses.color_pair(2))


# have to use x/y input, as gridInput is always in the playing field
def checkEdge(x, y):
    """check if snake hits edge of screen"""
    if x < 0 or x > WIDTH-1 or y < 0 or y > HEIGHT-1:
        return True

    return False


def checkSnake(gridInput):
    """check if the snake hits itself"""
    for i in range(len(snake)):
        if snake[i][0] == gridInput:
            return True

    return False


def generateApple():
    """generate an apple in the grid"""
    output = random.randint(0, HEIGHT*HEIGHT-1)
    if checkSnake(output):
        generateApple()
        return

    apple.append(output)


def printApple():
    """print location of Apple"""
    for i in range(len(apple)):
        screen.addstr(gridToY(apple[i])+1, gridToX(apple[i])*2+1, "()", curses.color_pair(3))


def moveSnake(x, y):
    """moves the snake"""
    global cursorX
    global cursorY
    cursorX += x
    cursorY += y

    global error
    global gameEnd

    if checkSnake(coordinateToGrid(cursorX, cursorY)):
        error = "checkSnake"
        gameEnd = True
    elif checkEdge(cursorX, cursorY):
        error = "checkEdge"
        gameEnd = True

    addLength(cursorX, cursorY)


def printScr():
    """Update Screen"""
    screen.clear()
    printGrid()
    printSnake()
    printApple()


def eatApple():
    """Check if apple has been eaten by snake"""
    global cursorX 
    global cursorY
    global snakeLength
    for i in range(len(apple)):
        if apple[i] == coordinateToGrid(cursorX, cursorY):
            apple.pop(i)
            snakeLength += 1


# Start curses
initCurses()

addLength(cursorX, cursorY)
generateApple()

printScr()

while gameEnd is False:
    ch = chr(screen.getch())

    if ch == 'w':
        moveSnake(0, -1)
    elif ch == 's':
        moveSnake(0, 1)
    elif ch == 'a':
        moveSnake(-1, 0)
    elif ch == 'd':
        moveSnake(1, 0)
    elif ch == 'q':
        break

    eatApple()

    printScr()

# End curses
endCurses()

print(str(cursorX) + " " + str(cursorY))
print(coordinateToGrid(cursorX, cursorY))
print(snake)
print(error)
