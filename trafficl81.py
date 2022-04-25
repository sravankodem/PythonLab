import tkinter as tk


class TrafficLights(Frame):

    def __init__(self):
        Frame.__init__(self)
        self.master.title("Traffic Lights")
        self.grid()
        x='white'
        y='white'
        z='green'

        self.canvas = Canvas(self, width = 300, height = 400, bg = "black")
        self.canvas.grid(row = 0, column = 0)
        self.canvas.create_rectangle(100, 50, 200, 350)

        self.canvas.create_oval(100, 50, 200, 150, fill=x)
        self.canvas.create_oval(100, 150, 200, 250, fill=y)
        self.canvas.create_oval(100, 250, 200, 350, fill=z)
def main():
    TrafficLights().mainloop()

main()
