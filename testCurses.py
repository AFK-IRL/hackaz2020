import curses

stdscr = curses.initscr()

curses.noecho()
curses.cbreak()
stdscr.keypad(True)

stdscr.addstr(5, 10, "hello")
stdscr.refresh()

for i in range(10):
    stdscr.getch()

curses.echo()
curses.nocbreak()
stdscr.keypad(False)

curses.endwin()
