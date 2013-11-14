import sys
import pygame
import math
import time
import Tkinter
import ttk

class turtle(object):
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

def dragon(x_start, y_start, in_dist, niter, in_window):
	window = in_window
	t = turtle(window, x_start, y_start)
	angle = 90
	dist = in_dist
	t.setAngle(angle)
	steps = [-1]
	n = niter
	for i in range(n): #iterations of fractal
	#	if i == (n-1):
	#		t.setDraw(True)

	#	T0 = time.clock()
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
	#	pygame.display.flip()
	#	T = time.clock() - T0
		time.sleep(0.5)	

def sqrkochcurve(x_start, y_start, in_dist, niter, in_window):
	window = in_window
	t = turtle(window, x_start, y_start)
	dist = in_dist
	steps = [1, -1, -1, 1]
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
		for j in range(5):
			if j == 0:
				tmp_steps = tmp_steps[:] + steps[:] + [1]
			elif j == 1:
				tmp_steps = tmp_steps[:] + steps[:] + [-1]
			elif j == 2:
				tmp_steps = tmp_steps[:] + steps[:] + [-1]
			elif j == 3:
				tmp_steps = tmp_steps[:] + steps[:] + [1]
			elif j == 4:
				tmp_steps = tmp_steps[:] + steps[:]	

		steps = tmp_steps[:]
		dist = float(dist)/3.
		#pygame.display.flip()
		time.sleep(.5)

def kochcurve(x_start, y_start, in_dist, niter, in_window):
	window = in_window
	t = turtle(window, x_start, y_start)
	dist = in_dist
	steps = [1, -1, 1]
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
		for j in range(4):
			if j < 3:
				tmp_steps = tmp_steps[:] + steps[:] + [(-1)**j]
			elif j == 3:
				tmp_steps = tmp_steps[:] + steps[:]

		steps = tmp_steps[:]
		dist = float(dist)/3.
		#pygame.display.flip()
		time.sleep(.5)

def run():
	print fracvar.get()
	if fracvar.get() == 'Dragon':
		dragon(200, 300, 200, 17, window)
	elif fracvar.get() == 'Koch':
		kochcurve(20, 400, 200, 6, window)
	elif fracvar.get() == 'Koch sqr':
		sqrkochcurve(20, 400, 200, 6, window)

pygame.init()
window = pygame.display.set_mode((640,480))

#x_start = 200
#y_start = 300

#while True:
#	dragon(200, 300, 200, 17, window)
#	sqrkochcurve(20, 400, 200, 6, window)
#	kochcurve(20, 400, 200, 6, window)
#	T = time.clock()
#	while True:
#		for event in pygame.event.get():
#				if event.type == pygame.QUIT:
#					pygame.quit()
#					sys.exit()
#				else:
#					pass

#		if (time.clock() - T) >= 5.:
#			break

root = Tkinter.Tk()
root.title("Max magiska laada")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky="n, w, e, s")
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

#ttk.Button(mainframe, text="Dragon", command=lambda: dragon(200, 300, 200, 17, window)).grid(column=1, row=1, sticky="w")
#ttk.Button(mainframe, text="Koch", command=lambda: kochcurve(20, 400, 200, 6, window)).grid(column=1, row=2, sticky="w")
#ttk.Button(mainframe, text="Koch sqr", command=lambda: sqrkochcurve(20, 400, 200, 6, window)).grid(column=1, row=3, sticky="w")
fractals = ('Dragon', 'Koch', 'Koch sqr')
fracvar = Tkinter.StringVar()
frac = ttk.Combobox(mainframe, textvariable=fracvar, values=fractals, state='readonly').grid(column=1, row=1, sticky='w')
ttk.Button(mainframe, text='Go!', command=run).grid(column=2, row=1, sticky='w')
#frac['values'] = ['Dragon', 'Koch', 'Koch sqr']
#frac['state'] = ('readonly')

for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

root.mainloop()
