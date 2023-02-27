# Chromatic Flow
This Python code generates a colorful and dynamic console display. It shows six colored hash marks that travel from left to right and change hues.
Just run the code in a Python3 environment to run it. To quit the code, use Ctrl-C while it is executing.

## The code uses the following modules:
1.	time: time: Gives a time delay to alter the flow's pace.
2.	sys: The exit() method is used to gracefully quit the application.
3.	bext: A custom module that allows you to color text in the terminal.

The main loop of the code controls the number of spaces before the hash marks via a variable named indent. The variable indent_increasing is used to regulate the flow direction. When True, the number of available spaces grows; when False, the number of available spaces drops.

To handle problems and quit gracefully if the user pushes Ctrl-C, the code employs a try/except block.
