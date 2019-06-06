#snake game
import curses
from curses import textpad
import time
import numpy as np

#snake class
class snake:

	def __init__(self,direction='right'):
		self.snake=[[10,12],[10,11],[10,10]]
		self.direction='right'
		self.y,self.x = 0,0
		self.fy,self.fx=0,0
		self.s=0

	#whole screen display
	def display(self,screen):
		screen.clear()
		self.display_details(screen)
		textpad.rectangle(screen,5,5,self.y-5,self.x-5)
		for i,v in enumerate(self.snake):
			screen.addstr(v[0],v[1],'o')
		screen.addstr(self.fy,self.fx,'o')	
		screen.refresh()
	
	#score display
	def display_details(self,screen):
		sm='SCORE:'
		self.s=len(self.snake)-3
		screen.addstr(4,self.x-len(sm+str(self.s))-5,sm+str(self.s))

	#:( lost display will display on the current screen
	def loose_Display(self,screen):
		message='GAME OVER'
		screen.addstr(self.y//2,self.x//2-len(message)//2,message)	
		screen.refresh()
		time.sleep(2)
		message1='press left arrow to exit or press right arrow to play again'
		screen.addstr(self.y//2,self.x//2-len(message),'')
		screen.addstr(self.y//2+1,self.x//2-len(message1)//2,message1)	
		screen.refresh()
		for i in range(5,0,-1):
			screen.clear()
			screen.addstr(self.y//2,self.x//2-1,str(i))
			screen.refresh()
			time.sleep(1)
			
		
		
		
			
	def right(self,screen):
		head=self.snake[0]
		nh=[head[0],head[1]+1]
		self.snake.insert(0,nh)
		self.snake.pop()	
		

	def left(self):
		head=self.snake[0]
		nh=[head[0],head[1]-1]
		self.snake.insert(0,nh)
		self.snake.pop()

	def down(self):
		head=self.snake[0]
		nh=[head[0]+1,head[1]]
		self.snake.insert(0,nh)
		self.snake.pop()

	def up(self):
		head=self.snake[0]
		nh=[head[0]-1,head[1]]
		self.snake.insert(0,nh)
		self.snake.pop()	

	#to increment the snake size
	def food(self,screen):
		if(self.snake[0][0] == self.fy and self.snake[0][1] == self.fx):
			if self.direction == curses.KEY_RIGHT:
				self.snake.insert(0,[self.fy,self.fx+1])
			elif self.direction == curses.KEY_LEFT:
				self.snake.insert(0,[self.fy,self.fx-1])
			elif self.direction == curses.KEY_UP:
				self.snake.insert(0,[self.fy-1,self.fx])	
			elif self.direction == curses.KEY_DOWN:
				self.snake.insert(0,[self.fy+1,self.fx])		
			self.display(screen)
			self.fy,self.fx =np.random.randint(low=6, high=self.y-5),np.random.randint(low=6, high=self.y-5)
	
	#speed controller
	def speed(self):
		if self.s==10:
			screen.timeout(150)
		elif self.s==20:
			screen.timeout(125)	
		elif self.s==25:
			screen.timeout(100)
		elif self.s==30:
			screen.timeout(75)
		elif self.s==40:
			screen.timeout(50)	
			


def main(screen):
	curses.curs_set(0)
	screen.nodelay(1)
	screen.timeout(200)
	s=snake()
	s.y,s.x=screen.getmaxyx()
	s.fy,s.fx=np.random.randint(low=6, high=s.y-5),np.random.randint(low=6, high=s.y-5)
	s.direction=curses.KEY_RIGHT
	loop=True
	while(loop):
		key=screen.getch()
		s.display(screen)
		# direction navigator
		if key in [curses.KEY_RIGHT,curses.KEY_LEFT,curses.KEY_UP,curses.KEY_DOWN]:
			if (s.direction == curses.KEY_RIGHT and key == curses.KEY_LEFT):
				s.direction=curses.KEY_RIGHT
			elif (s.direction == curses.KEY_LEFT and key == curses.KEY_RIGHT):
				s.direction=curses.KEY_LEFT	
			elif(s.direction == curses.KEY_DOWN and key == curses.KEY_UP):
				s.direction=curses.KEY_DOWN
			elif(s.direction == curses.KEY_UP and key == curses.KEY_DOWN):
				s.direction=curses.KEY_UP
			else:
				s.direction=key	
		


		if s.direction==curses.KEY_RIGHT:
			#s.display(screen)
			s.food(screen)
			#s.right(screen)
			s.display(screen)
			s.right(screen)
				
		elif s.direction==curses.KEY_DOWN:
			s.food(screen)
			s.display(screen)
			s.down()
			
		elif s.direction==curses.KEY_UP:
			s.food(screen)
			s.display(screen)
			s.up()
			
		elif s.direction==curses.KEY_LEFT:
			s.food(screen)
			s.display(screen)	
			s.left()	
			
		s.speed()

		#s.display(screen)
		if s.snake[0][0] == 5 or s.snake[0][0] == s.y-5 or s.snake[0][1] == 5 or s.snake[0][1] == s.x-5 or s.snake[0] in s.snake[1:]:
			loop = s.loose_Display(screen)
	
	time.sleep(0)



curses.wrapper(main)
