import tkinter as tk
import time

t = 0

class MyApp(object):
    def __init__(self, master):
        self.text = tk.Text(master)
        self.t = time.time()        
        self.text.bind('<Key>', self.callback)
        self.text.pack()
        self.text.focus()

    def callback(self, event):
        delta = time.time() - self.t
        print('{}'.format(delta))

root = tk.Tk()
app = MyApp(root)
root.mainloop()