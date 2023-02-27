# Chromatic Flow

import time
import sys
import bext

print('Press Ctrl-C to exit')
time.sleep(3)

indent = 0
indent_increasing = True

try:
    while True:
        print(' ' * indent, end='')
        bext.fg('red')
        print('##', end='')
        bext.fg('yellow')
        print('##', end='')
        bext.fg('green')
        print('##', end='')
        bext.fg('blue')
        print('##', end='')
        bext.fg('cyan')
        print('##', end='')
        bext.fg('purple')
        print('##', end='')

        if indent_increasing:
            # Increase the number of spaces
            indent = indent + 1
            if indent == 30:
                # Change direction
                indent_increasing = True

        else:
            # Decrease the number of spaces
            indent = indent - 1
            if indent == 0:
                # Change direction
                indent_increasing = False

        time.sleep(0.03)
except:
    sys.exit()
