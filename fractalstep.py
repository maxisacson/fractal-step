import sys
import pygame
import math
import time
import Tkinter
import ttk

class turtle(object): #drawing automaton
	angle = 0
	draw = True
	def __init__(self, window, xinit, yinit):
		self.window = window
		self.x = xinit
		self.y = yinit
	
	def setDraw(self, var):
		self.draw = var	

	def setPos(self, newx, newy):
		self.x = newx
		self.y = newy

	def setAngle(self, alpha):
		self.angle = math.radians(-alpha)

	def rotateBy(self, beta):
		self.angle = self.angle + math.radians(-beta)

	def move(self, dist):
		x_new = self.x + dist*math.cos(self.angle)
		y_new = self.y + dist*math.sin(self.angle)
		if self.draw:
			pygame.draw.line(self.window, (255, 255, 255), (self.x, self.y), (x_new, y_new), 1)
		else:
			pass

		self.x = x_new
		self.y = y_new

	def printPos(self):
		print "(" + str(self.x) + ", " + str(self.y) + ")"

	def printAngle(self):
		print str(-math.degrees(self.angle))

def dragon(x_start, y_start, in_dist, niter, in_window): #dragon curve
	window = in_window
	t = turtle(window, x_start, y_start)
	angle = 90
	dist = in_dist
	t.setAngle(angle)
	steps = [-1]
	n = niter
	for i in range(n): #iterations of fractal
		window.fill((0,0,0))
		t.move(dist) #initial step before rotation
		for s in steps: #number of step for given iteration
			t.rotateBy(s*90)
			t.move(dist)
			pygame.display.flip()
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()
				else:
					pass

		t.setPos(x_start, y_start) #move back to start
		angle = angle + 45 #rotate start angle by 45
		t.setAngle(angle)
		tmp_steps = [k*-1 for k in steps[::-1]]
		steps = steps[:] + [-1] + tmp_steps[:] #update new steps
		dist = dist/math.sqrt(2) #scale down by sqrt(2)
		time.sleep(0.5)	

def sqrkochcurve(x_start, y_start, in_dist, niter, in_window): #square koch curve (quadratic type 1)
	window = in_window
	t = turtle(window, x_start, y_start)
	dist = in_dist
	steps = [1, -1, -1, 1]
	pattern = steps[:]
	n = niter
	for i in range(n):
		window.fill((0,0,0))
		t.move(dist)
		for s in steps:
			t.rotateBy(s*90)
			t.move(dist)
			pygame.display.flip()
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()
				else:
					pass

		t.setPos(x_start, y_start)
		t.setAngle(0)
		tmp_steps = []
		for p in pattern:
			tmp_steps = tmp_steps[:] + steps[:] + [p]

		tmp_steps = tmp_steps[:] + steps[:]

		steps = tmp_steps[:]
		dist = float(dist)/3.
		time.sleep(.5)

def kochcurve(x_start, y_start, in_dist, niter, in_window): #standard koch curve
	window = in_window
	t = turtle(window, x_start, y_start)
	dist = in_dist
	steps = [1, -1, 1]
	pattern = steps[:]
	n = niter
	for i in range(n):
		window.fill((0,0,0))
		t.move(dist)
		for s in steps:
			if s == -1:
				t.rotateBy(s*120)
			elif s == 1:
				t.rotateBy(s*60)

			t.move(dist)
			pygame.display.flip()
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()
				else:
					pass

		t.setPos(x_start, y_start)
		t.setAngle(0)
		tmp_steps = []
		for p in pattern:
			tmp_steps = tmp_steps[:] + steps[:] + [p]

		tmp_steps = tmp_steps[:] + steps[:]

		steps = tmp_steps[:]
		dist = float(dist)/3.
		time.sleep(.5)

def run(): #this runs the drawing methods, called from run button in gui
	pygame.init() #initialize pygame
	window = pygame.display.set_mode((640,480)) #set display window
	if fracvar.get() == 'Dragon':
		dragon(200, 300, 200, 17, window)
	elif fracvar.get() == 'Koch':
		kochcurve(20, 400, 200, 6, window)
	elif fracvar.get() == 'Koch sqr':
		sqrkochcurve(20, 400, 200, 6, window)

## Initialization and stuff ##

fractals = ('Dragon', 'Koch', 'Koch sqr') #list of fractals available

root = Tkinter.Tk()
root.title("Max magiska laada")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky="n, w, e, s")
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

fracvar = Tkinter.StringVar()
frac = ttk.Combobox(mainframe, textvariable=fracvar, values=fractals, state='readonly').grid(column=1, row=1, sticky='w')
ttk.Button(mainframe, text='Go!', command=run).grid(column=2, row=1, sticky='w')

for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

## Main stuff ##

root.mainloop()
