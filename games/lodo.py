##
# logo game using curses
# Two main clases one is to display game board and the other is handel the user responses
##

from datetime import datetime
import curses
from curses import textpad
import time
import numpy as np

# display class for different types of screens


class DisplayScreens:

	def __init__(self, screen):
		self.screen = screen
		self.y, self.x = self.screen.getmaxyx()

	# menu display

	def menu(self, s):
		men = ['Start', 'Exit']
		y, x = self.screen.getmaxyx()
		if s == 1:
			self.screen.attron(curses.color_pair(1))
			self.screen.addstr(y//2, x//2 - len(men[0])//2, men[0])
			self.screen.attroff(curses.color_pair(1))
			self.screen.addstr(y // 2 + 2, x // 2 - len(men[1]) // 2, men[1])
		else:
			self.screen.addstr(y // 2, x // 2 - len(men[0]) // 2, men[0])
			self.screen.attron(curses.color_pair(1))
			self.screen.addstr(y // 2 + 2, x // 2 - len(men[1])//2, men[1])
			self.screen.attroff(curses.color_pair(1))
		self.screen.refresh()

	# function to display game board

	def displaygameboard(self):
		self.screen.clear()
		textpad.rectangle(self.screen, 5, 5, 35, 65)  # main
		self.screen.addstr(38, 5, 'Press E to always exit but not always...........!!')
		# self.screen.attron(curses.color_pair(1))
		for i in range(5, 16, 2):

			textpad.rectangle(self.screen, i, 29, i+2, 33)
			textpad.rectangle(self.screen, i, 33, i+2, 37)
			textpad.rectangle(self.screen, i, 37, i+2, 41)
			if i != 5:
				self.screen.attron(curses.color_pair(3))
				self.screen.addstr(i+1, 34, '   ')
				self.screen.addstr(8, 38, '   ')
				self.screen.attroff(curses.color_pair(3))

		for i in range(5, 26, 4):
			textpad.rectangle(self.screen, 19, i, 21, i + 4)
			textpad.rectangle(self.screen, 17, i, 19, i+4)
			textpad.rectangle(self.screen, 21, i, 23, i+4)
			if i != 5:
				self.screen.attron(curses.color_pair(2))
				self.screen.addstr(20, i+1, '   ')
				self.screen.addstr(18, 10, '   ')
				self.screen.attroff(curses.color_pair(2))

		for i in range(41, 62, 4):
			textpad.rectangle(self.screen, 19, i, 21, 4 + i)
			textpad.rectangle(self.screen, 17, i, 19, 4+i)
			textpad.rectangle(self.screen, 21, i, 23, 4+i)
			if i != 61:
				self.screen.attron(curses.color_pair(4))
				self.screen.addstr(20, i+1, '   ')
				self.screen.addstr(22, 58, '   ')
				self.screen.attroff(curses.color_pair(4))

		for i in range(23, 34, 2):
			textpad.rectangle(self.screen, i, 29, 2+i, 33)
			textpad.rectangle(self.screen, i, 33, 2+i, 37)
			textpad.rectangle(self.screen, i, 37, i+2, 41)
			if i != 33:
				self.screen.attron(curses.color_pair(5))
				self.screen.addstr(i+1, 34, '   ')
				self.screen.addstr(32, 30, '   ')
				self.screen.attroff(curses.color_pair(5))

		# player one positions
		textpad.rectangle(self.screen, 7, 9, 9, 13)
		textpad.rectangle(self.screen, 7, 21, 9, 25)
		textpad.rectangle(self.screen, 13, 9, 15, 13)
		textpad.rectangle(self.screen, 13, 21, 15, 25)

		# player two positions
		textpad.rectangle(self.screen, 7, 45, 9, 49)
		textpad.rectangle(self.screen, 7, 57, 9, 61)
		textpad.rectangle(self.screen, 13, 45, 15, 49)
		textpad.rectangle(self.screen, 13, 57, 15, 61)

		# player three positions
		textpad.rectangle(self.screen, 25, 9, 27, 13)
		textpad.rectangle(self.screen, 25, 21, 27, 25)
		textpad.rectangle(self.screen, 31, 9, 33, 13)
		textpad.rectangle(self.screen, 31, 21, 33, 25)

		# player four positions
		textpad.rectangle(self.screen, 25, 45, 27, 49)
		textpad.rectangle(self.screen, 25, 57, 27, 61)
		textpad.rectangle(self.screen, 31, 45, 33, 49)
		textpad.rectangle(self.screen, 31, 57, 33, 61)
		# self.screen.attroff(curses.color_pair(1))
		# players area
		self.screen.attron(curses.color_pair(3))
		textpad.rectangle(self.screen, 5, 41, 17, 65)  # p2
		self.screen.attroff(curses.color_pair(3))
		self.screen.attron(curses.color_pair(2))
		textpad.rectangle(self.screen, 5, 5, 17, 29)   # p1
		self.screen.attroff(curses.color_pair(2))
		self.screen.attron(curses.color_pair(5))
		textpad.rectangle(self.screen, 23, 5, 35, 29)  # p3
		self.screen.attroff(curses.color_pair(5))
		self.screen.attron(curses.color_pair(4))
		textpad.rectangle(self.screen, 23, 41, 35, 65)  # p4
		self.screen.attroff(curses.color_pair(4))

		# score board dice:
		textpad.rectangle(self.screen, 6, 70, 8, 100)
		textpad.rectangle(self.screen, 6, 105, 8, 110)
		textpad.rectangle(self.screen, 10, 70, 12, 100)
		textpad.rectangle(self.screen, 10, 105, 12, 110)

# this class holds all information about the players and handles the user inputs
class Player:

	def __init__(self, screen, name):
		self.name = name
		self.c = [None, None, None, None]
		self.ccurrent = [[0, 0], [0, 0], [0, 0], [0, 0]]
		self.start = None
		self.lock = [1, 1, 1, 1]
		self.intermediate = None
		self.screen = screen
		self.current = None
		self.end = None
	# moves the coin for dice score

	def move(self, steps, cn):
		currenty = self.ccurrent[cn][0]
		currentx = self.ccurrent[cn][1]
		# print(self.current)
		positionlist=[]
		if self.lock[cn] == 1 and steps == 6:
			self.screen.addstr(self.start[0], self.start[1], 'o')
			self.screen.addstr(self.c[cn][0], self.c[cn][1], ' ')
			self.lock[cn] = 0
			# print(self.start)
			self.ccurrent[cn][0], self.ccurrent[cn][1] = self.start[0], self.start[1]

			self.screen.refresh()
			time.sleep(1)
		else:
			for i in range(steps):
				if self.ccurrent[cn][0] in [18] and self.ccurrent[cn][1] in [7, 11, 15, 19, 23, 27, 43, 47, 51, 55, 59, 63]:
					self.screen.addstr(self.ccurrent[cn][0], self.ccurrent[cn][1], ' ')
					# print(self.ccurrent[cn][1])
					# print('incc 4')
					if self.ccurrent[cn][1] == 27 and self.ccurrent[cn][0] == 18:
						self.ccurrent[cn][0], self.ccurrent[cn][1] = [16, 31]
						self.screen.addstr(self.ccurrent[cn][0], self.ccurrent[cn][1], 'o')
					elif self.ccurrent[cn][1] == 27 and self.ccurrent[cn][0] == 20:
						self.ccurrent[cn][0], self.ccurrent[cn][1] = [20, 31]
						self.screen.addstr(self.ccurrent[cn][0], self.ccurrent[cn][1], 'o')
					elif self.ccurrent[cn][1] == 63:
						self.ccurrent[cn][0], self.ccurrent[cn][1] = [20, 63]
						self.screen.addstr(self.ccurrent[cn][0], self.ccurrent[cn][1], 'o')
					else:
						self.ccurrent[cn][1] += 4
						self.screen.addstr(self.ccurrent[cn][0], self.ccurrent[cn][1], 'o')
					self.screen.refresh()
					time.sleep(1)

				elif self.ccurrent[cn][0] in [20] and self.ccurrent[cn][1] in [11, 15, 19, 23, 27]:
					self.screen.attron(curses.color_pair(2))
					self.screen.addstr(self.ccurrent[cn][0], self.ccurrent[cn][1], ' ')
					self.screen.attroff(curses.color_pair(2))
					# print(self.ccurrent[cn][1])
					# print('incc 4')
					if self.ccurrent[cn][1] == 27 and self.ccurrent[cn][0] == 18:
						self.ccurrent[cn][0], self.ccurrent[cn][1] = [20, 29]
						self.screen.addstr(self.ccurrent[cn][0], self.ccurrent[cn][1], 'o')
					else:
						self.ccurrent[cn][1] += 4
						self.screen.addstr(self.ccurrent[cn][0], self.ccurrent[cn][1], 'o')
					self.screen.refresh()
					time.sleep(1)

				elif self.ccurrent[cn][0] in [16, 14, 12, 10, 8] and self.ccurrent[cn][1] == 35:
					self.screen.attron(curses.color_pair(3))
					self.screen.addstr(self.ccurrent[cn][0], self.ccurrent[cn][1], ' ')
					self.screen.attroff(curses.color_pair(3))
					# print(self.ccurrent[cn][1])
					if self.ccurrent[cn][0] == 16:
						self.ccurrent[cn][0], self.ccurrent[cn][1] = [18, 35]
						self.screen.addstr(self.ccurrent[cn][0], self.ccurrent[cn][1], 'o')
					else:
						self.ccurrent[cn][0] += 2
						self.screen.addstr(self.ccurrent[cn][0], self.ccurrent[cn][1], 'o')
					self.screen.refresh()
					time.sleep(1)

				elif self.ccurrent[cn][0] in [24, 26, 28, 30, 32] and self.ccurrent[cn][1] == 35:
					self.screen.attron(curses.color_pair(5))
					self.screen.addstr(self.ccurrent[cn][0], self.ccurrent[cn][1], ' ')
					self.screen.attroff(curses.color_pair(5))
					# print(self.ccurrent[cn][1])
					if self.ccurrent[cn][0] == 24:
						self.ccurrent[cn][0], self.ccurrent[cn][1] = [22, 35]
						self.screen.addstr(self.ccurrent[cn][0], self.ccurrent[cn][1], 'o')
					else:
						self.ccurrent[cn][0] -= 2
						self.screen.addstr(self.ccurrent[cn][0], self.ccurrent[cn][1], 'o')
					self.screen.refresh()
					time.sleep(1)

				elif self.ccurrent[cn][0] == 20 and self.ccurrent[cn][1] in [43, 47, 51, 55, 59]:
					self.screen.attron(curses.color_pair(4))
					self.screen.addstr(self.ccurrent[cn][0], self.ccurrent[cn][1], ' ')
					self.screen.attroff(curses.color_pair(4))
					# print(self.ccurrent[cn][1])
					if self.ccurrent[cn][1] == 43:
						self.ccurrent[cn][0], self.ccurrent[cn][1] = [20, 39]
						self.screen.addstr(self.ccurrent[cn][0], self.ccurrent[cn][1], 'o')
					else:
						self.ccurrent[cn][1] -= 4
						self.screen.addstr(self.ccurrent[cn][0], self.ccurrent[cn][1], 'o')
					self.screen.refresh()
					time.sleep(1)

				elif self.ccurrent[cn][0] == 22 and self.ccurrent[cn][1] in [43, 47, 51, 55, 59, 63, 7, 11, 15, 19, 23, 27]:
					self.screen.addstr(self.ccurrent[cn][0], self.ccurrent[cn][1], ' ')
					# print(self.ccurrent[cn][1])
					if self.ccurrent[cn][1] == 43:
						self.ccurrent[cn][0], self.ccurrent[cn][1] = [24, 39]
						self.screen.addstr(self.ccurrent[cn][0], self.ccurrent[cn][1], 'o')
					elif self.ccurrent[cn][1] == 7:
						self.ccurrent[cn][0], self.ccurrent[cn][1] = [20, 7]
						self.screen.addstr(self.ccurrent[cn][0], self.ccurrent[cn][1], 'o')
					else:
						self.ccurrent[cn][1] -= 4
						self.screen.addstr(self.ccurrent[cn][0], self.ccurrent[cn][1], 'o')
					self.screen.refresh()
					time.sleep(1)

				elif self.ccurrent[cn][0] in [16, 14, 12, 10, 8, 6, 24, 26, 28, 30, 32, 34] and self.ccurrent[cn][1] == 31:
					self.screen.addstr(self.ccurrent[cn][0], self.ccurrent[cn][1], ' ')
					# print(self.ccurrent[cn][1])
					if self.ccurrent[cn][0] == 6:
						self.ccurrent[cn][0], self.ccurrent[cn][1] = [6, 35]
						self.screen.addstr(self.ccurrent[cn][0], self.ccurrent[cn][1], 'o')
					elif self.ccurrent[cn][0] == 24:
						self.ccurrent[cn][0], self.ccurrent[cn][1] = [22, 27]
						self.screen.addstr(self.ccurrent[cn][0], self.ccurrent[cn][1], 'o')
					else:
						self.ccurrent[cn][0] -= 2
						self.screen.addstr(self.ccurrent[cn][0], self.ccurrent[cn][1], 'o')
					self.screen.refresh()
					time.sleep(1)

				elif self.ccurrent[cn][0] in [16, 14, 12, 10, 8, 6, 24, 26, 28, 30, 32, 34] and self.ccurrent[cn][1] == 39:
					self.screen.addstr(self.ccurrent[cn][0], self.ccurrent[cn][1], ' ')
					# print(self.ccurrent[cn][1])
					if self.ccurrent[cn][0] == 16:
						self.ccurrent[cn][0], self.ccurrent[cn][1] = [18, 43]
						self.screen.addstr(self.ccurrent[cn][0], self.ccurrent[cn][1], 'o')
					elif self.ccurrent[cn][0] == 34:
						self.ccurrent[cn][0], self.ccurrent[cn][1] = [34, 35]
						self.screen.addstr(self.ccurrent[cn][0], self.ccurrent[cn][1], 'o')
					else:
						self.ccurrent[cn][0] += 2
						self.screen.addstr(self.ccurrent[cn][0], self.ccurrent[cn][1], 'o')
					self.screen.refresh()
					time.sleep(1)

				elif self.ccurrent[cn][0] == 6 and self.ccurrent[cn][1] == 35:
					self.screen.addstr(self.ccurrent[cn][0], self.ccurrent[cn][1], ' ')
					if self.ccurrent[cn][0] == self.intermediate[0] and self.ccurrent[cn][1] == self.intermediate[1]:
						self.ccurrent[cn][0], self.ccurrent[cn][1] = [8, 35]
						self.screen.addstr(self.ccurrent[cn][0], self.ccurrent[cn][1], 'o')
					else:
						self.ccurrent[cn][0], self.ccurrent[cn][1] = [6, 39]
						self.screen.addstr(self.ccurrent[cn][0], self.ccurrent[cn][1], 'o')
					self.screen.refresh()
					time.sleep(1)

				elif self.ccurrent[cn][0] == 20 and self.ccurrent[cn][1] == 63:
					# print('right node')
					self.screen.addstr(self.ccurrent[cn][0], self.ccurrent[cn][1], ' ')
					if self.ccurrent[cn][0] == self.intermediate[0] and self.ccurrent[cn][1] == self.intermediate[1]:
						self.ccurrent[cn][0], self.ccurrent[cn][1] = [20, 59]
						self.screen.addstr(self.ccurrent[cn][0], self.ccurrent[cn][1], 'o')
					else:
						self.ccurrent[cn][0], self.ccurrent[cn][1] = [22, 63]
						self.screen.addstr(self.ccurrent[cn][0], self.ccurrent[cn][1], 'o')
					self.screen.refresh()
					time.sleep(1)

				elif self.ccurrent[cn][0] == 34 and self.ccurrent[cn][1] == 35:
					self.screen.addstr(self.ccurrent[cn][0], self.ccurrent[cn][1], ' ')
					if self.ccurrent[cn][0] == self.intermediate[0] and self.ccurrent[cn][1] == self.intermediate[1]:
						self.ccurrent[cn][0], self.ccurrent[cn][1] = [32, 35]
						self.screen.addstr(self.ccurrent[cn][0], self.ccurrent[cn][1], 'o')
					else:
						self.ccurrent[cn][0], self.ccurrent[cn][1] = [34, 31]
						self.screen.addstr(self.ccurrent[cn][0], self.ccurrent[cn][1], 'o')
					self.screen.refresh()
					time.sleep(1)

				elif self.ccurrent[cn][0] == 20 and self.ccurrent[cn][1] == 7:
					self.screen.addstr(self.ccurrent[cn][0], self.ccurrent[cn][1], ' ')
					if self.ccurrent[cn][0] == self.intermediate[0] and self.ccurrent[cn][1] == self.intermediate[1]:
						self.ccurrent[cn][0], self.ccurrent[cn][1] = [20, 11]
						self.screen.addstr(self.ccurrent[cn][0], self.ccurrent[cn][1], 'o')
					else:
						self.ccurrent[cn][0], self.ccurrent[cn][1] = [18, 7]
						self.screen.addstr(self.ccurrent[cn][0], self.ccurrent[cn][1], 'o')
					self.screen.refresh()
					time.sleep(1)

				# print(i)
				# print(self.ccurrent[cn][0], self.ccurrent[cn][1])
				positionlist.append([self.ccurrent[cn][0], self.ccurrent[cn][1]])
		if len(positionlist) >= 2:
			# print('current', positionlist)
			ls = positionlist.pop()
			lb = positionlist.pop()
			if ls[0] == lb[0] and ls[1] == lb[1]:
				self.screen.addstr(self.ccurrent[cn][0], self.ccurrent[cn][1], ' ')
				# print(currenty,currentx, 'hello')
				self.ccurrent[cn][0], self.ccurrent[cn][1] = currenty, currentx
				self.screen.addstr(self.ccurrent[cn][0], self.ccurrent[cn][1], 'o')
				self.screen.refresh()
		# print('current position ', self.ccurrent)
		# print('start position', self.start)
		# print('current',positionlist)
		# print('locks', self.lock)
		# print('end', self.end)
		if self.end[0] == self.ccurrent[cn][0] and self.end[1] == self.ccurrent[cn][1]:
			self.lock[cn] = 2
			# print('current locks', self.lock)

# holds the data fo all players


class Lodo:

	def __init__(self, screen, n1, n2, n3, n4, npy):
		self.screen = screen
		self.players = [Player(screen, n1), Player(screen, n2), Player(screen, n3), Player(screen, n4)]
		self.time = [[datetime.now().timestamp(),0], [datetime.now().timestamp(),1], [datetime.now().timestamp(),2], [datetime.now().timestamp(),3]]
		self.numplayer = npy
		self.active = None
		self.players[0].c[0] = [8, 11]
		self.players[0].c[1] = [8, 23]
		self.players[0].c[2] = [14, 11]
		self.players[0].c[3] = [14, 23]
		self.players[1].c[0] = [8, 47]
		self.players[1].c[1] = [8, 59]
		self.players[1].c[2] = [14, 47]
		self.players[1].c[3] = [14, 59]
		self.players[3].c[0] = [26, 11]
		self.players[3].c[1] = [26, 23]
		self.players[3].c[2] = [32, 11]
		self.players[3].c[3] = [32, 23]
		self.players[2].c[0] = [26, 47]
		self.players[2].c[1] = [26, 59]
		self.players[2].c[2] = [32, 47]
		self.players[2].c[3] = [32, 59]
		self.players[0].start = [18, 11]
		self.players[0].intermediate = [20, 7]
		self.players[1].start = [8, 39]
		self.players[1].intermediate = [6, 35]
		self.players[3].start = [32, 31]
		self.players[3].intermediate = [34, 35]
		self.players[2].start = [22, 59]
		self.players[2].intermediate = [20, 63]
		self.players[0].end = [20, 31]
		self.players[1].end = [18, 35]
		self.players[3].end = [22, 35]
		self.players[2].end = [20, 39]
		if self.numplayer == 2:
			#print('2wertjgfd')
			self.active = [1, 0, 1, 0]
		elif self.numplayer == 3:
			self.active = [1, 1, 1, 0]
		else:
			self.active = [1, 1, 1, 1]
		self.displaycoins()
		# self.screen.addstr(self.players[0].start[0],self.players[0].start[1], 'o')

	def displayscore(self):
		print (self.active)
		print ('fsgd')
		self.screen.clear()
		#self.time.sort()
		#self.time.reverse()
		for i, j in self.time:
			if self.active[j] >= 1:
				self.screen.attron(curses.color_pair(j+2))
				if (max(self.time)[0])==self.time[j][0] and (min(self.time)[0])!=self.time[j][0]:
					self.screen.addstr(j+5, 5, 'players'+str(j+1)+'            WINNER ')
				else:
					self.screen.addstr(j + 5, 5, 'players' + str(j + 1) +'     Yet To Complete')
				self.screen.attroff(curses.color_pair(j+2))
				self.screen.refresh()
		time.sleep(5)

	def displaycoins(self):
		self.screen.attron(curses.color_pair(2))
		self.screen.addstr(18, 11, ' ')
		self.screen.attroff(curses.color_pair(2))
		self.screen.attron(curses.color_pair(3))
		self.screen.addstr(8, 39, ' ')
		self.screen.attroff(curses.color_pair(3))
		self.screen.attron(curses.color_pair(4))
		self.screen.addstr(22, 59, ' ')
		self.screen.attroff(curses.color_pair(4))
		self.screen.attron(curses.color_pair(5))
		self.screen.addstr(32, 31, ' ')
		self.screen.attroff(curses.color_pair(5))
		self.screen.attron(curses.color_pair(1))
		self.screen.addstr(30, 38, '   ')
		self.screen.addstr(18, 54, '   ')
		self.screen.addstr(10, 30, '   ')
		self.screen.addstr(22, 14, '   ')
		self.screen.attroff(curses.color_pair(1))
		for i in range(0, 4, 1):
			if self.active[i] == 1:
				for j in range(0, 4, 1):
					if self.players[i].lock[j] == 1:
						self.screen.attron(curses.color_pair(i+2))
						self.screen.addstr(self.players[i].c[j][0], self.players[i].c[j][1], 'o')
						self.screen.attroff(curses.color_pair(i+2))

		#print(self.active)

	def displaycoinscurrent(self):
		self.screen.attron(curses.color_pair(2))
		self.screen.addstr(18, 11, ' ')
		self.screen.attroff(curses.color_pair(2))
		self.screen.attron(curses.color_pair(3))
		self.screen.addstr(8, 39, ' ')
		self.screen.attroff(curses.color_pair(3))
		self.screen.attron(curses.color_pair(4))
		self.screen.addstr(22, 59, ' ')
		self.screen.attroff(curses.color_pair(4))
		self.screen.attron(curses.color_pair(5))
		self.screen.addstr(32, 31, ' ')
		self.screen.attroff(curses.color_pair(5))
		self.screen.attron(curses.color_pair(1))
		self.screen.addstr(30, 38, '   ')
		self.screen.addstr(18, 54, '   ')
		self.screen.addstr(10, 30, '   ')
		self.screen.addstr(22, 14, '   ')
		self.screen.attroff(curses.color_pair(1))
		for i in range(0, 4, 1):
			if self.active[i] == 1:
				for j in range(0, 4, 1):
					self.screen.attron(curses.color_pair(i+2))
					self.screen.addstr(self.players[i].ccurrent[j][0], self.players[i].ccurrent[j][1], 'o')
					self.screen.attroff(curses.color_pair(i+2))



def main(screen,nply):
	curses.curs_set(0)
	screen.refresh()
	ds = DisplayScreens(screen)
	ds.displaygameboard()

	curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
	curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_GREEN)
	curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_CYAN)
	curses.init_pair(4, curses.COLOR_BLACK, curses.COLOR_BLUE)
	curses.init_pair(5, curses.COLOR_BLACK, curses.COLOR_RED)
	curses.init_pair(6, curses.COLOR_BLACK, curses.COLOR_MAGENTA)
	game = Lodo(screen, 'as', 'srgdf', 'egsdgfg', 'sggf', int(nply))
	message = 'press y key to roll dice'
	av = 'available coins to move'
	player = 0
	#print(nply.isdigit())
	# game.players[0].move(6, 1)



	end = True
	kill = 0
	while end:

		while 1:
			screen.addstr(7, 106, ' ')
			screen.addstr(11, 106, '    '[:4])
			screen.attron(curses.color_pair(player+2))
			screen.addstr(7, 71, message)

			key = screen.getch()

			screen.refresh()
			if key == ord('y') and game.active[player] == 1:
				screen.attroff(curses.color_pair(player+2))
				screen.addstr(7, 71, message)
				p = np.random.randint(low=1, high=7)

				screen.refresh()
				a = ''
				for i, j in enumerate(game.players[player].lock):
					if j == 0:
						a = a + str(i+1)
					elif p == 6 and j != 2:
						a = a + str(i+1)
				screen.addstr(7, 106, str(p))
				screen.addstr(11, 106, (a+'   ')[:4])
				screen.attron(curses.color_pair(player+2))
				screen.addstr(11, 71, av)

				screen.refresh()
				if len(a) >= 1:
					coin = str(screen.getkey())
					while coin not in a:
						coin = str(screen.getkey())

					screen.attroff(curses.color_pair(player + 2))
					screen.addstr(11, 71, av)
					screen.refresh()
					#game.players[0].lock = [2, 2, 2, 2]
					#game.players[1].lock = [2, 2, 2, 2]
					if coin in ['1', '2', '3', '4']:
						# print('coin', coin, ord(coin), int(coin))
						# wrong = game.players[player].ccurrent[int(coin) - 1]
						game.players[player].move(p, int(coin) - 1)
						if p == 6:
							kill = 1
						if game.players[player].ccurrent[int(coin)-1] not in [[8, 39], [22, 59], [32, 31], [18, 11], [30, 38], [18, 54], [10, 30], [22, 14]]:
							if game.players[player].ccurrent[int(coin) - 1] in game.players[0].ccurrent and 0 != player:
								# print(game.players[player].ccurrent[int(coin)-1],game.players[0].ccurrent)
								for di, dy in enumerate(game.players[0].ccurrent):
									if game.players[player].ccurrent[int(coin) - 1][0] == dy[0] and game.players[player].ccurrent[int(coin) - 1][1] == dy[1]:
										kill = 1
										game.players[0].ccurrent[di][0],game.players[0].ccurrent[di][1] = [0, 0]
										game.players[0].lock[di] = 1
										game.displaycoins()
										screen.refresh()
										# print(player, 'player', int(coin) - 1, 'coin', 'killed player 0 s  coin')
								# print(player, 'player', int(coin)-1, 'coin', 'killed player 0 s  coin')
								# print(game.players[player].ccurrent[int(coin) - 1], game.players[0].ccurrent)

							elif game.players[player].ccurrent[int(coin) - 1] in game.players[1].ccurrent and 1 != player:
								# print(game.players[player].ccurrent[int(coin)-1], game.players[1].ccurrent)
								for di, dy in enumerate(game.players[1].ccurrent):
									if game.players[player].ccurrent[int(coin) - 1][0] == dy[0] and \
											game.players[player].ccurrent[int(coin) - 1][1] == dy[1]:
										kill = 1
										game.players[1].ccurrent[di][0], game.players[1].ccurrent[di][1] = [0, 0]
										game.players[1].lock[di] = 1
										game.displaycoins()
										screen.refresh()
										# print(player, 'player', int(coin) - 1, 'coin', 'killed player 0 s  coin')
								# print(player, 'player', int(coin) - 1, 'coin', 'killed player 1 s  coin')
							elif game.players[player].ccurrent[int(coin) - 1] in game.players[2].ccurrent and 2 != player:
								# print(game.players[player].ccurrent[int(coin)-1], game.players[2].ccurrent)
								for di, dy in enumerate(game.players[2].ccurrent):
									if game.players[player].ccurrent[int(coin) - 1][0] == dy[0] and \
											game.players[player].ccurrent[int(coin) - 1][1] == dy[1]:
										kill = 1
										game.players[2].ccurrent[di][0], game.players[2].ccurrent[di][1] = [0, 0]
										game.players[2].lock[di] = 1
										game.displaycoins()
										screen.refresh()
										# print(player, 'player', int(coin) - 1, 'coin', 'killed player 0 s  coin')
								# print(player, 'player', int(coin)-1, 'coin', 'killed player 2 s  coin')
							elif game.players[player].ccurrent[int(coin) - 1] in game.players[3].ccurrent and 3 != player:
								# print(game.players[player].ccurrent[int(coin)-1], game.players[3].ccurrent)
								for di, dy in enumerate(game.players[3].ccurrent):
									if game.players[player].ccurrent[int(coin) - 1][0] == dy[0] and \
											game.players[player].ccurrent[int(coin) - 1][1] == dy[1]:
										kill = 1
										game.players[3].ccurrent[di][0], game.players[3].ccurrent[di][1] = [0, 0]
										game.players[3].lock[di] = 1
										game.displaycoins()
										screen.refresh()
										# print(player, 'player', int(coin) - 1, 'coin', 'killed player 0 s  coin')
								# print(player, 'player', int(coin)-1, 'coin' ,'killed player 3 s  coin')
							#game.displaycoinscurrent()

						if sum(game.players[player].lock) == 8:
							game.active[player] = 10
							game.time[player][0]=int(datetime.now().timestamp())
						#print(game.active)
						if (sum(game.active) == 31 and game.numplayer==4) or (sum(game.active) == 21 and game.numplayer==3) or (sum(game.active) == 11 and game.numplayer==2):
							key = ord('e')
							game.displayscore()
							print("end game")
							end = False
						break

				else:
					screen.attroff(curses.color_pair(player + 2))
					screen.addstr(11, 71, av)
					break
				screen.refresh()
				# code here
				if sum(game.players[player].lock) == 8:
					game.active[player] = 10
					game.time[player][0] = int(datetime.now().timestamp())
				#print(game.active)
				if (sum(game.active) == 31 and game.numplayer == 4) or (
						sum(game.active) == 21 and game.numplayer == 3) or (
						sum(game.active) == 11 and game.numplayer == 2):
					key = ord('e')
					game.displayscore()
					print("end game")
					end = False
				break

			elif key == ord('e'):
				screen.attroff(curses.color_pair(player + 2))
				game.displayscore()
				end = False
				curses.endwin()
				break
			else:
				screen.attroff(curses.color_pair(player + 2))
		game.displaycoinscurrent()
		if kill == 1:
			kill = 0
		elif int(game.numplayer) == 2:
			player += 2
		elif int(game.numplayer) == 3 and player == 2:
			player = 0
		else:
			player += 1

		if player == 4:
			player = 0
	# time.sleep(5)
	# curses.endwin()


def main2(screen):
	curses.curs_set(0)
	curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
	ds = DisplayScreens(screen)
	op = 1
	ds.menu(op)
	while 1:
		key = screen.getch()
		if key == curses.KEY_DOWN or key == curses.KEY_UP:
			if op == 1:
				op = 2
				ds.menu(op)
			else:
				op = 1

				ds.menu(op)
		elif key in [10, 13] or key == curses.KEY_ENTER:
			if op == 2:
				time.sleep(1)
				curses.endwin()
				break
			elif op == 1:
				screen.clear()
				screen.addstr(31, 5, 'Enter number of players:')

				textpad.rectangle(screen, 30, 30, 32, 35)
				nply = str(screen.getkey())
				while nply not in ['1', '2', '3', '4']:
					screen.clear()
					screen.addstr(31, 5, 'Enter number of players:')
					textpad.rectangle(screen, 30, 30, 32, 35)
					nply = str(screen.getkey())

				screen.addstr(31, 31, nply)
				screen.refresh()
				time.sleep(1)
				main(screen,nply)
				screen.clear()
				ds.menu(1)
	screen.refresh()




curses.wrapper(main2)
