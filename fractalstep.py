import sys
import pygame
import math
import time
import Tkinter
import ttk

class turtle(object): #drawing automaton
	angle = 0
	draw = True
	def __init__(self, window, xinit, yinit, in_color = (255, 255, 255)):
		self.window = window
		self.x = xinit
		self.y = yinit
		self.color = in_color
	
	def setDraw(self, var):
		self.draw = var	

	def setPos(self, newx, newy):
		self.x = newx
		self.y = newy

	def setAngle(self, alpha):
		self.angle = math.radians(-alpha)

	def rotateBy(self, beta):
		self.angle = self.angle + math.radians(-beta)

	def setColor(self, in_color):
		self.color = in_color

	def move(self, dist):
		x_new = self.x + dist*math.cos(self.angle)
		y_new = self.y + dist*math.sin(self.angle)
		if self.draw:
			pygame.draw.line(self.window, self.color, (self.x, self.y), (x_new, y_new), 1)
		else:
			pass

		self.x = x_new
		self.y = y_new

	def printPos(self):
		print "(" + str(self.x) + ", " + str(self.y) + ")"

	def printAngle(self):
		print str(-math.degrees(self.angle))

def dragon(x_start, y_start, in_dist, niter, in_window, in_color): #dragon curve
	window = in_window
	color = in_color
	t = turtle(window, x_start, y_start, color)
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
					return
				else:
					pass

		t.setPos(x_start, y_start) #move back to start
		angle = angle + 45 #rotate start angle by 45
		t.setAngle(angle)
		tmp_steps = [k*-1 for k in steps[::-1]]
		steps = steps[:] + [-1] + tmp_steps[:] #update new steps
		dist = dist/math.sqrt(2) #scale down by sqrt(2)
		time.sleep(0.5)	

def sqrkochcurve(x_start, y_start, in_dist, niter, in_window, in_color): #square koch curve (quadratic type 1)
	window = in_window
	color = in_color
	t = turtle(window, x_start, y_start, in_color)
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
					return
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

def kochcurve(x_start, y_start, in_dist, niter, in_window, in_color): #standard koch curve
	window = in_window
	color = in_color
	t = turtle(window, x_start, y_start, color)
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
					return
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

def run(*args): #this runs the drawing methods, called from run button in gui
	pygame.init() #initialize pygame
	window = pygame.display.set_mode((640,480)) #set display window

	# Set options #
	if (red.get() != '' and green.get() != '' and blue.get() != ''):
		if (int(red.get()) < 256 and int(green.get()) < 256 and int(blue.get()) < 256):
			if (int(red.get()) > -1 and int(green.get()) > -1 and int(blue.get()) > -1):
				global color
				color = (int(red.get()), int(green.get()), int(blue.get()))

	if fracvar.get() == 'Dragon':
		dragon(200, 300, 200, 17, window, color)
	elif fracvar.get() == 'Koch':
		kochcurve(20, 400, 200, 6, window, color)
	elif fracvar.get() == 'Koch sqr':
		sqrkochcurve(20, 400, 200, 6, window, color)

def options(*args): #set fractal specific options
	s = fracvar.get()
	if s == 'Dragon':
		pass
	elif s == 'Koch':
		pass
	elif s == 'Koch sqr':
		pass



## Initialization and stuff ##

root = Tkinter.Tk()
fractals = ('Dragon', 'Koch', 'Koch sqr') #list of fractals available

# Fractal independent options, such as color #
color = (255, 255, 255) #default color
red = Tkinter.StringVar()
blue = Tkinter.StringVar()
green = Tkinter.StringVar()

## GUI ##
root.title("Max magiska laada")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky="n, w, e, s")
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

# Options section #
optframe = ttk.Frame(mainframe, padding="3 3 12 12")
optframe.grid(column=0, row=1, sticky="n, w")
optframe.columnconfigure(0, weight=1)
optframe.rowconfigure(0, weight=1)

red_entry = ttk.Entry(optframe, textvariable=red, width=3)
red_entry.grid(column=1, row=0, sticky='w')
red_label = ttk.Label(optframe, text='R:').grid(column=0, row=0, sticky='w')

green_entry = ttk.Entry(optframe, textvariable=green, width=3)
green_entry.grid(column=3, row=0, sticky='w')
green_label = ttk.Label(optframe, text='G:').grid(column=2, row=0, sticky='w')

blue_entry = ttk.Entry(optframe, textvariable=blue, width=3)
blue_entry.grid(column=5, row=0, sticky='w')
blue_label = ttk.Label(optframe, text='B:').grid(column=4, row=0, sticky='w')


# Run section #
fracvar = Tkinter.StringVar()
frac = ttk.Combobox(mainframe, textvariable=fracvar)
frac.grid(column=0, row=0, sticky='w')
frac['values'] = fractals
frac['state'] = 'readonly'
frac.bind('<<ComboboxSelected>>', options)
frac.current(0)
ttk.Button(mainframe, text='Go!', command=run).grid(column=1, row=0, sticky='w')

for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

## Main stuff ##

root.mainloop()
