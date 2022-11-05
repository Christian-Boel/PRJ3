import tkinter as tk
from PIL import ImageTk,Image

window = tk.Tk()


defaultcolor = "#2596be"

window.title("SPLASH")
window.geometry("800x540")



my_img = ImageTk.PhotoImage(Image.open("PRJ3\gui_test\icons\drinkicon.png"))
my_label = tk.Label(image=my_img)
#my_label.pack()


Header = tk.Label(
    text="SPLASH",
    font=('Arial',75),
    foreground="black")

def mixDrinkButtonClicked():
    myLabel = tk.Label(window,text="Mix drink clicked!")
    myLabel.pack()

mixDrinkButton = tk.Button(
    text="MIX DRINK",
    fg="black",
    bg=defaultcolor,
    width = 25,
    height = 25,
    padx = 10,
    command=mixDrinkButtonClicked
)

def addDrinkButtonClicked():
    myLabel = tk.Label(window,text="Add drink clicked!")
    myLabel.pack()

removeDrinkButton = tk.Button(
    text="ADD DRINK",
    fg="black",
    bg=defaultcolor,
    width = 25,
    height = 25,
    command=addDrinkButtonClicked
)

def removeDrinkButtonClicked():
    myLabel = tk.Label(window,text="Remove drink clicked!")
    myLabel.pack()

addDrinkButton = tk.Button(
    text="REMOVE DRINK",
    fg="black",
    bg=defaultcolor,
    width = 25,
    height = 25,
    command=removeDrinkButtonClicked
)




# entry = tk.Entry(
#     fg = "black",
#     bg = "white",
#     width=30
# )



#homescreen

def homescreen():
    Header.place(relheight= 0.1, relwidth=0.5)
    mixDrinkButton.place(relheight = 0.5,relwidth=0.1)
    addDrinkButton.place(relheight = 0.5,relwidth=0.5)
    removeDrinkButton.place(relheight = 0.5,relwidth=0.8)
    

homescreen()
window.mainloop()
