import curses

def game_loop(window):
    window.addstr(f'Aperte alguma tecla.')
    while True:
        window.timout(1000)
        char = window.getch()
        window.clear()

        if char != -1:
            window.addstr(f'Tecla apertada: {char}\n')
        else:
            window.addstr(f'Nenhuma tecla apertada\n')


if __name__ == '__main__':
    curses.wrapper(game_loop)