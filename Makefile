CC=gcc
FILES=snake.c
EXE=snake
INSTALL=/usr/local/bin/

build:
	$(CC) $(FILES) -o $(EXE) -lncurses

run:
	$(CC) $(FILES) -o $(EXE) -lncurses && ./$(EXE)

clean:
	rm -rf $(EXE)

install:
	sudo mv $(EXE) $(INSTALL)

uninstall:
	sudo rm $(INSTALL)$(EXE)
