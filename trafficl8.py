import tkinter as tk
# py2
#import Tkinter as tk

class Fun(tk.Tk):
    def __init__(self):
        tk.Frame.__init__(self)
        self.master.title("I say things")

        self.count = 0
        self.count_str = tk.StringVar()
        self.count_str.set(str(self.count))

        tk.Entry(self.master, textvariable=self.count_str).pack()

    def more_count(self):
        self.after(2000, self.more_count)
        self.count += 1
        self.count_str.set(str(self.count))


f = Fun()
f.more_count()
f.mainloop()
