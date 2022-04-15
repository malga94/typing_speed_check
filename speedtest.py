import curses
import time
import string
import random
import os
from collections import deque

def get_last_word(sentence, cont):

    word = []

    for x in sentence[cont-1::-1]:
        if x == ' ':
            word.reverse()
            return ''.join(word)
        word.append(x)

    #If we hit the beginning of sentence
    word.reverse()
    return ''.join(word)

def c_main(stdscr):

    path_to_dictionary = os.environ['DICTIONARY_PATH']
    with open(path_to_dictionary, 'r') as f:
        words = f.read().splitlines()

    words = [w for w in words if len(w)>1]

    #In order to color text, you must first define a color pair, consisting of an ID, a foreground color and a background color
    #You then specify the ID of the color pair you want in addstr
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_GREEN)
    curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_RED)

    COLOR_RIGHT = curses.color_pair(1)
    COLOR_WRONG = curses.color_pair(2)

    sentence_list = random.choices(words, k=100)
    sentence = ' '.join(sentence_list)
    cont = 0

    rows, cols = stdscr.getmaxyx()
    wpm, complete_words = 0, 0

    stdscr.clear()
    stdscr.addstr(sentence + '\n')

    og_time = time.perf_counter()

    wrong_pos = []

    while True:

        if sentence[cont] == ' ':
            lastword = get_last_word(sentence, cont)
            if all([t < cont - len(lastword) for t in wrong_pos]) and lastword in sentence_list:
                sentence_list.remove(lastword)
                complete_words += 1

        time_elapsed = time.perf_counter() - og_time
        wpm = complete_words / time_elapsed * 60

        stdscr.addstr(len(sentence)//cols + 3, 0, f"Your speed is {wpm:.2f}wpm. You completed {complete_words} words.")

        char = stdscr.getch()

        if chr(char) == '\t':
            return 0

        elif char == 127:
            cont -= 1
            stdscr.addstr(cont//cols, cont%cols, sentence[cont], curses.color_pair(0))

        else:
            if chr(char) == sentence[cont]:
            #addstr is basically print, and you can specify the position (row, column) as the first two args
                stdscr.addstr(cont//cols, cont%cols, chr(char), COLOR_RIGHT)
                #User corrected spelling mistake
                if cont in wrong_pos:
                    wrong_pos.remove(cont)
            else:
                stdscr.addstr(cont//cols, cont%cols, chr(char), COLOR_WRONG)
                #User made spelling mistake
                wrong_pos.append(cont)

            cont += 1

    return 0

def main():

    curses.wrapper(c_main)

if __name__ == '__main__':
    main()
