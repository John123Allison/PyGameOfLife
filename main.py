from tkinter import *

master = Tk()

# declare constants
WINDOW_SIZE = 500
CELL_SIZE = 10
STEP_LENGTH = 300

# create window
window = Canvas(master, width=WINDOW_SIZE, height=WINDOW_SIZE)
window.pack()

class Cell:
	def __init__(self, x, y):
		self.alive = False
		self.x = x
		self. y = y
		window.create_rectangle(self.x, self.y, self.x + CELL_SIZE, self.y + CELL_SIZE)
	def change_state(self):
		window.create_rectangle(self.x, self.y, self.x + CELL_SIZE, self.y + CELL_SIZE)

cells = []

# test drawing cells
for x in range(0, WINDOW_SIZE, CELL_SIZE):
	for y in range(0, WINDOW_SIZE, CELL_SIZE):
		cell = Cell(x, y)
		cells.append(cell)

for cell in cells:
	print(cell.alive)

if __name__ == "__main__":
	mainloop()