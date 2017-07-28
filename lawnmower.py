# from __future__ import print_function
import time, sys, os
from reprint import output

def grow_blades():
	# writes blades to screen
	for i in range(len(blades)):
		if blades[i] != GRASS_HEIGHT:
			blades[i] += 1
			grass_top_row = blades[i] - 1
			grass_col = i*2
			screen[grass_top_row][grass_col] = '|'
			break


def build_screen():
	# this is where we reverse the order of rows 
	out_screen = [""] * LAWN_HEIGHT
	
	for row in range(len(screen)):
		row_string = ""
		for col in range(len(screen[row])):
			row_string += screen[row][col]
		out_screen[LAWN_HEIGHT - 1 - row] = row_string

	return out_screen

def print_screen():
	for i in range(LAWN_HEIGHT):
		string_screen = build_screen()
		output_list[i] = string_screen[i]
	
def move_lawnmower():
	LAWNMOWER_POS['col'] += 1
	write_lawnmower()

def write_lawnmower():
	# (row, col) is position of top of handle
	#TODO: don't draw overflow
	# draw handle
	row = LAWNMOWER_POS['row']
	col = LAWNMOWER_POS['col']
	
	if col >= -8:
		screen[row-2][col+8] = ' '
		screen[row-4][col+8] = ' '
		screen[row-3][col+8] = '|'
		screen[row-5][col+8] = ')'
	if col >= -7:
		screen[row-5][col+7] = '_'
		screen[row-3][col+7] = ' '
		screen[row-2][col+7] = '-'
		screen[row-4][col+7] = '-'
	if col >= -6:
		screen[row-5][col+6] = '('
		screen[row-3][col+6] = ' '
		screen[row-2][col+6] = '-'
		screen[row-4][col+6] = '-'
	if col >= -5:
		screen[row-5][col+5] = '_'
		screen[row-3][col+5] = ' '
		screen[row-2][col+5] = '-'
		screen[row-4][col+5] = '-'
	if col >= -4:
		screen[row-5][col+4] = ')'
		screen[row-3][col+4] = ' '
		screen[row-2][col+4] = '-'
		screen[row-4][col+4] = '-'
	if col >= -3:
		screen[row-5][col+3] = '_'
		screen[row-3][col+3] = ' '
		screen[row-2][col+3] = '-'
		screen[row-4][col+3] = '-'
	if col >= -2:
		screen[row-2][col+2] = ' '
		screen[row-4][col+2] = ' '
		screen[row-5][col+2] = '('
		screen[row-3][col+2] = '|'
	if col >= -1:
		screen[row-1][col+1] = '\\'
		screen[row-5][col+1] = '_'
		screen[row-3][col+1] = ' ' 
	if col >= 0:
		screen[row][col] = '\\'
		screen[row-1][col] = ' ' # what to do with this
	if col >= 1:
		screen[row][col-1] = ' ' # what to do with this

def init():
	# initialize globals
	global screen, blades, LAWN_WIDTH, LAWN_HEIGHT, GRASS_HEIGHT, GROUND_LINE, GRASS_TOP_LINE
	global LAWNMOWER_POS, DONE_GROWING
	TERM_HEIGHT, TERM_WIDTH = os.popen('stty size', 'r').read().split()
	LAWN_WIDTH = int(TERM_WIDTH)
	LAWN_WIDTH = LAWN_WIDTH - (LAWN_WIDTH % 2)
	LAWN_HEIGHT = 7
	GRASS_HEIGHT = 3
	GROUND_LINE = LAWN_HEIGHT - 1
	GRASS_TOP_LINE = GROUND_LINE - GRASS_HEIGHT - 1
	LAWNMOWER_POS = {'row': 5, 'col': -9}
	DONE_GROWING = False
	blades = [0] * ((LAWN_WIDTH)/2)

	# list of strings for screen chars. screen[row][column]
	# rows maintained from ground up for ease of logic
	screen = []
	for row in range(LAWN_HEIGHT):
		screen.append([' ']*LAWN_WIDTH)
	screen[0] = ['_'] * LAWN_WIDTH

	os.system("printf '\e[8;30;" + str(LAWN_WIDTH) + "t'")

def run():
	global output_list, DONE_GROWING
	with output(output_type="list", initial_len=LAWN_HEIGHT, interval=0) as output_list:
		while True:
			print_screen()

			if not DONE_GROWING:
				grow_blades()
			elif LAWNMOWER_POS['col'] < LAWN_WIDTH - 9:
				move_lawnmower()
			else:
				return

			if blades[len(blades) - 1] == GRASS_HEIGHT:
				DONE_GROWING = True

			time.sleep(0.03)

if __name__ == '__main__':
	init()
	run()

		