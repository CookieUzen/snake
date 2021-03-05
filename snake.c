#include <stdio.h>
#include <ncurses.h>

// Size of playing field
#define WIDTH 10
#define HEIGHT 10

/*	The playing field is calculated using the grid below
 *	This way, we do not have to create an array to store 
 *	the entirety of the playing field, but just where the
 *	snake occupies space.
 *
 *	For example, the index of a 4 by 4 playing field is 
 *	listed below.
 *	+-----------+
 *	|0 |1 |2 |3 |
 *	|--+--+--+--|
 *	|4 |5 |6 |7 |
 *	|--+--+--+--|
 *	|8 |9 |10|11|
 *	|--+--+--+--|
 *	|12|13|14|15|
 *	+-----------+
 *
 *	Use the coordinateToX and coordinateToY functions to
 *	find the x/y coordinates of each index.
 *
 *	The following table show the x/y coordinate of a 4 by 4
 *	playing field:
 *
 * +-------+-------+-------+-------+
 * | (0,1) | (1,1) | (2,1) | (3,1) |
 * +-------+-------+-------+-------+
 * | (0,2) | (1,2) | (2,2) | (3,2) |
 * +-------+-------+-------+-------+
 * | (0,3) | (1,3) | (2,3) | (3,3) |
 * +-------+-------+-------+-------+
 * | (0,4) | (1,4) | (2,4) | (3,4) |
 * +-------+-------+-------+-------+
 *
 */

// Array to store snake position
// snake[number on grid][time to live]
int snake[WIDTH*HEIGHT][2];	// TODO: dynamically allocated snake instead of setting hard value

void initGrid();
void initNcurses();
int coordinateToX(int input);
int coordinateToY(int input);

int	main () {
	initNcurses();
	initGrid();
	
	getch();

	endwin();
	return(0);
}



void initNcurses () {
	initscr();
	cbreak();
	noecho();
	keypad(stdscr, TRUE);
	curs_set(0);
}

// Prints screen, initialize grid
void initGrid () {
	// Enable Color
	start_color();
	init_pair(1, COLOR_BLACK, COLOR_CYAN);	// Snake color
	init_pair(2, COLOR_BLACK, COLOR_RED);	// Apple color

	// Print top and bottom bars
	move(0,0);
	printw("+");
	for (int i = 0; i < WIDTH*2; i++)
		printw("-");
	printw("+");

	move(HEIGHT,0);
	printw("+");
	for (int i = 0; i < WIDTH*2; i++)
		printw("-");
	printw("+");

	// Print sidebars
	for (int i = 1; i < HEIGHT; i++)
		mvprintw(i,0,"|");

	for (int i = 1; i < HEIGHT; i++)
		mvprintw(i,WIDTH*2+1,"|");

}

// Parse the coordinate number system to array index (x)
int coordinateToX ( int input ) {
	return input%WIDTH;
}

// Parse the coordinate number system to array index (y)
int coordinateToY ( int input ) {
	return input/HEIGHT;
}

