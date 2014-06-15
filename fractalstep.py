import pygame
import math
import time
import random
try:
	import Tkinter as tkinter  # py2.7
	import ttk  # py2.7
	import tkColorChooser  # py2.7
except ImportError:
	import tkinter  # py3.4
	import tkinter.ttk as ttk  # py3.4
	import tkinter.colorchooser as tkColorChooser  # py3.4



class turtle(object):
	"""drawing automaton"""
	angle = 0
	draw = True

	def __init__(self, window, xinit, yinit, in_color=(255, 255, 255)):
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
		print("(" + str(self.x) + ", " + str(self.y) + ")")

	def printAngle(self):
		print(str(-math.degrees(self.angle)))

	def draw_circle(self, radius):
		pygame.draw.circle(self.window, self.color, (self.x, self.y), radius)


def buffons_needle(niter,
					in_window, in_color, iter_color,
					in_needle_length, in_line_sep):
	"""buffons needle simulation"""
	window = in_window
	color = in_color
	n = niter
	initial_line_sep = 50 if not in_line_sep else int(in_line_sep)
	line_sep = initial_line_sep
	lineheights = []
	needle_length = 45 if not in_needle_length else int(in_needle_length)
	paused = False
	t = turtle(window, 0, line_sep, color)
	t.setAngle(0)
	t.setColor(color)
	while line_sep < 480:
		t.move(640)
		lineheights.append(line_sep)
		line_sep += initial_line_sep
		t.setPos(0, line_sep)
	pygame.display.flip()
	num_crossed = 0
	pifloat_str = ""
	for N in range(n):
		if iter_color:
			color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
			t.setColor(color)
		else:
			t.setColor(color)
		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					return
				elif event.type == pygame.KEYDOWN:
					if event.key == pygame.K_ESCAPE:
						pygame.quit()
						return
					elif event.key == pygame.K_SPACE:
						paused = not paused
				else:
					pass
			if paused:
				continue
			else:
				break
		xpos = random.randint(needle_length, 640-needle_length)
		ypos = random.randint(needle_length, 480-needle_length)
		needle_angle = random.randint(0, 360)
		t.setAngle(needle_angle)
		xtip = xpos - float(needle_length)/2.0*math.cos(t.angle)
		ytip = ypos - float(needle_length)/2.0*math.sin(t.angle)
		t.setPos(xtip, ytip)
		shortest_len_to_line = min([abs(ypos-l) for l in lineheights])
		if shortest_len_to_line <= abs(float(needle_length)/2.0*math.sin(t.angle)):
			num_crossed += 1
		t.move(needle_length)
		if num_crossed:
			pifloat_str = str(2*(float(N+1)*float(needle_length))/(float(num_crossed)*float(initial_line_sep)))
		pygame.display.set_caption(pifloat_str)
		pygame.display.flip()
		pygame.time.wait(50)


def pascal_sierpinski(niter, in_window, in_color, iter_color, x_start=2, y_start=2):
	"""sierpinski triangle using pascals triangle"""
	window = in_window
	n = niter
	line_height = 6
	char_width = 6
	color = in_color
	t = turtle(window, x_start, y_start, color)

	def pascal(n):
		pas = [[1], [1, 1], [1, 2, 1]]
		for y in range(n-3):
			nth = [1]
			last = pas[len(pas)-1]
			for x in range(len(last)-1):
				nth.append(last[x]+last[x+1])
			nth.append(1)
			pas.append(nth)
		return pas

	def even_odd(pascal):
		for p in pascal:
			for x, b in enumerate(p):
				if b % 2:
					p[x] = "."
		return pascal
	pastri = even_odd(pascal(n))
	irtsap = pastri[::-1]
	for x, row in enumerate(irtsap):
		irtsap[x] = row[::-1]
	pygame.display.flip()
	paused = False
	for x, row in enumerate(pastri):
		row += irtsap[x]
		for ele in row:
			if ele != ".":
				t.draw_circle(2)
			if iter_color and ele != ".":
				color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
				t.setColor(color)
			x_start += char_width
			t.setPos(x_start, y_start)
			while True:
				for event in pygame.event.get():
					if event.type == pygame.QUIT:
						pygame.quit()
						return
					elif event.type == pygame.KEYDOWN:
						if event.key == pygame.K_ESCAPE:
							pygame.quit()
							return
						elif event.key == pygame.K_SPACE:
							paused = not paused
					else:
						pass
				if paused:
					continue
				else:
					break
		pygame.display.flip()
		pygame.time.wait(100)
		y_start += line_height
		x_start = 2
		t.setPos(x_start, y_start)


def dragon(x_start, y_start, in_dist, niter, in_window, in_color, iter_color):
	"""dragon curve"""
	window = in_window
	color = in_color
	t = turtle(window, x_start, y_start, color)
	angle = 90
	dist = in_dist
	t.setAngle(angle)
	steps = [-1]
	n = niter
	for i in range(n):  # iterations of fractal
		window.fill((25, 25, 25))
		if iter_color:
			color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
			t.setColor(color)
		paused = False
		t.move(dist)  # initial step before rotation
		for s in steps:  # number of step for given iteration
			t.rotateBy(s*90)
			t.move(dist)
			pygame.display.flip()
			while True:
				for event in pygame.event.get():
					if event.type == pygame.QUIT:
						pygame.quit()
						return
					elif event.type == pygame.KEYDOWN:
						if event.key == pygame.K_ESCAPE:
							pygame.quit()
							return
						elif event.key == pygame.K_SPACE:
							paused = not paused
					else:
						pass
				if paused:
					continue
				else:
					break
		t.setPos(x_start, y_start)  # move back to start
		angle = angle + 45  # rotate start angle by 45
		t.setAngle(angle)
		tmp_steps = [k*-1 for k in steps[::-1]]
		steps = steps[:] + [-1] + tmp_steps[:]  # update new steps
		dist = dist/math.sqrt(2)  # scale down by sqrt(2)
		time.sleep(0.5)


def sqrkochcurve(x_start, y_start, in_dist, niter, in_window, in_color, iter_color):
	"""square koch curve (quadratic type 1)"""
	window = in_window
	color = in_color
	t = turtle(window, x_start, y_start, in_color)
	dist = in_dist
	steps = [1, -1, -1, 1]
	pattern = steps[:]
	n = niter
	for i in range(n):
		window.fill((25, 25, 25))
		if iter_color:
			color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
			t.setColor(color)
		t.move(dist)
		paused = False
		for s in steps:
			t.rotateBy(s*90)
			t.move(dist)
			pygame.display.flip()
			while True:
				for event in pygame.event.get():
					if event.type == pygame.QUIT:
						pygame.quit()
						return
					elif event.type == pygame.KEYDOWN:
						if event.key == pygame.K_ESCAPE:
							pygame.quit()
							return
						elif event.key == pygame.K_SPACE:
							paused = not paused
					else:
						pass
				if paused:
					continue
				else:
					break

		t.setPos(x_start, y_start)
		t.setAngle(0)
		tmp_steps = []
		for p in pattern:
			tmp_steps = tmp_steps[:] + steps[:] + [p]

		tmp_steps = tmp_steps[:] + steps[:]

		steps = tmp_steps[:]
		dist = float(dist)/3.
		time.sleep(.5)


def kochcurve(x_start, y_start, in_dist, niter, in_window, in_color, iter_color):
	"""standard koch curve"""
	window = in_window
	color = in_color
	t = turtle(window, x_start, y_start, color)
	dist = in_dist
	steps = [1, -1, 1]
	pattern = steps[:]
	n = niter
	for i in range(n):
		window.fill((25, 25, 25))
		if iter_color:
			color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
			t.setColor(color)
		t.move(dist)
		paused = False
		for s in steps:
			if s == -1:
				t.rotateBy(s*120)
			elif s == 1:
				t.rotateBy(s*60)
			t.move(dist)
			pygame.display.flip()
			while True:
				for event in pygame.event.get():
					if event.type == pygame.QUIT:
						pygame.quit()
						return
					elif event.type == pygame.KEYDOWN:
						if event.key == pygame.K_ESCAPE:
							pygame.quit()
							return
						elif event.key == pygame.K_SPACE:
							paused = not paused
					else:
						pass
				if paused:
					continue
				else:
					break
		t.setPos(x_start, y_start)
		t.setAngle(0)
		tmp_steps = []
		for p in pattern:
			tmp_steps = tmp_steps[:] + steps[:] + [p]
		tmp_steps = tmp_steps[:] + steps[:]
		steps = tmp_steps[:]
		dist = float(dist)/3.
		time.sleep(.5)

global colorcho
global colorchohex
colorcho = (255, 255, 255)
colorchohex = "#ffffff"


def run(*args):
	"""this runs the drawing methods, called from run button in gui"""
	pygame.init()  # initialize pygame
	window = pygame.display.set_mode((640, 480))  # set display window

	# Set options #
	if not iter_rand_color.get():
		if rand_color.get():
			color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
		else:
			color = colorcho

	elif iter_rand_color.get():
		color = (255, 255, 255)

	if fracvar.get() == 'Dragon':
		dragon(200, 300, 200, 17, window, color, iter_rand_color.get())
	elif fracvar.get() == 'Koch':
		kochcurve(20, 400, 200, 6, window, color, iter_rand_color.get())
	elif fracvar.get() == 'Koch sqr':
		sqrkochcurve(20, 400, 200, 6, window, color, iter_rand_color.get())
	elif fracvar.get() == "Sierpinski (Pascals triangle)":
		pascal_sierpinski(96, pygame.display.set_mode((580, 480)),
							color, iter_rand_color.get())
	elif fracvar.get() == "Buffons needle":
		buffons_needle(1000, pygame.display.set_mode((640, 480)),
							color, iter_rand_color.get(), nl.get(), ls.get())


def options(*args):
	"""set fractal specific options"""
	s = fracvar.get()
	if s == 'Dragon':
		pass
	elif s == 'Koch':
		pass
	elif s == 'Koch sqr':
		pass
	elif s == "Sierpinski (Pascals triangle)":
		pass
	elif s == "Buffons needle":
		global nl
		global ls
		ttk.Label(mainframe, text="Needle length: ").grid(column=1, row=0, sticky="w")
		ttk.Entry(mainframe, textvariable=nl, width=3).grid(column=2, row=0, sticky="w")
		ttk.Label(mainframe, text="Line sep: ").grid(column=3, row=0, sticky="w")
		ttk.Entry(mainframe, textvariable=ls, width=3).grid(column=4, row=0, sticky="w")


def quit():
	root.quit()


def color1():
	global colorcho
	global colorchohex
	global collab
	fetched = tkColorChooser.askcolor()
	colorcho = fetched[0]
	colorchohex = fetched[1]
	collab.configure(bg=colorchohex)
	collab.grid(column=1, row=0, sticky="w")

## Initialization and stuff ##
root = tkinter.Tk()
fractals = ('Dragon', 'Koch', 'Koch sqr', "Sierpinski (Pascals triangle)", "Buffons needle")  # list of fractals available

# Fractal independent options, such as color #
global nl
global ls
nl = tkinter.StringVar()
ls = tkinter.StringVar()
global rand_color
rand_color = tkinter.BooleanVar()

global iter_rand_color
iter_rand_color = tkinter.BooleanVar()

## GUI ##
root.title("Fractal Step")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky="n, w, e, s")
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

# Options section #
optframe = ttk.Frame(mainframe, padding="3 3 12 12")
optframe.grid(column=0, row=1, sticky="n, w", columnspan=5)
optframe.columnconfigure(0, weight=1)
optframe.rowconfigure(0, weight=1)

# Color preview frame #
global collab
collab = tkinter.Label(optframe, bg=colorchohex, width=5)
collab.grid(column=1, row=0, sticky="w")


#choose random color
random_color_checkbox = ttk.Checkbutton(optframe, text="Choose random color", variable=rand_color, onvalue=True, offvalue=False)
random_color_checkbox.grid(column=2, row=0, sticky='w')

#choose random color each iteration
iter_random_color_checkbox = ttk.Checkbutton(optframe, text="Change each iteration?", variable=iter_rand_color, onvalue=True, offvalue=False)
iter_random_color_checkbox.grid(column=3, row=0, sticky='w')


# Run section #
fracvar = tkinter.StringVar()
frac = ttk.Combobox(mainframe, textvariable=fracvar)
frac.grid(column=0, row=0, sticky='w')
frac['values'] = fractals
frac['state'] = 'readonly'
frac.bind('<<ComboboxSelected>>', options)
frac.current(0)
ttk.Button(mainframe, text='Go!', command=run).grid(column=5, row=0, sticky='w')
ttk.Button(mainframe, text='Exit', command=quit).grid(column=5, row=1, sticky='w')
ttk.Button(optframe, text="Choose color", command=color1).grid(column=0, row=0, sticky="w")


for child in mainframe.winfo_children():
	child.grid_configure(padx=5, pady=5)

## Main stuff ##
root.mainloop()
