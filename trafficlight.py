from tkinter import * # Import tkinter

class Trafficlight:
    def __init__(self):
        window = Tk() # Create a window
        window.title("Traffic Light") # Set a title

# Add three radio buttons to frame1
frame1 = Frame(window) # Create and add a frame to window
frame1.pack()
self.v1 = IntVar()
self.v2 = IntVar()
rbRed = Radiobutton(frame1, text = "Red", bg = "red",
variable = self.v2,
value = 1,
command = self.processRadiobutton)
rbYellow = Radiobutton(frame1, text = "Yellow", bg = "yellow",
variable = self.v2, value = 2,
command = self.processRadiobutton)
rbGreen = Radiobutton(frame1, text = "Green", bg = "green",
variable = self.v2, value = 3,
command = self.processRadiobutton)

rbRed.grid(row = 10, column = 1)
rbYellow.grid(row = 10, column = 2)
rbGreen.grid(row = 10, column = 3)

# Add Radio Button process below once I figure that out

# Place canvas in the window

self.canvas = Canvas(window, width = 480, height = 480, bg =
"white")
self.canvas.pack()

# Display a rectangle

def displayRect(self):
self.canvas.create_rectangle(10, 10, 190, tages = "rect")

# Display a Oval for the top light

def displayOval(self):
self.canvas.create_oval(10, 10, 10, 10)

# Display an Oval for the middle light

def displayOval(self):
self.canvas.create_oval(20, 20, 20, 20)

# Display an Oval for the bottom light

def displayOval(self):
self.canvas.create_oval(30, 30, 30, 30)

# Create an event loop

Trafficlight()
