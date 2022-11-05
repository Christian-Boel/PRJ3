import tkinter as tk

window = tk.Tk()


window.title("test")
window.geometry("500x300")
greeting = tk.Label(
    text="Hello world",
    foreground="white",
    background="black")

button = tk.Button(
    text="Click me!",
    fg="blue",
    bg="yellow",
    width = 25,
    height = 5
)
    
entry = tk.Entry(
    fg = "black",
    bg = "white",
    width=30
)




#greeting.pack()
#button.pack()
entry.pack()

window.mainloop()
