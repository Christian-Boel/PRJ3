import tkinter as tk
from PIL import ImageTk,Image

window = tk.Tk()


defaultcolor = "#2596be"

window.title("SPLASH")
window.geometry("800x540")
#window.configure(background="white")


#EDIT PICTURE PATH!
my_img = ImageTk.PhotoImage(Image.open("/Users/christian/PRJ3/gui_test/icons/drinkicon.png"))
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
    # width = 25,
    # height = 25,
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
    # width = 25,
    # height = 25,
    command=addDrinkButtonClicked
)

def removeDrinkButtonClicked():
    myLabel = tk.Label(window,text="Remove drink clicked!")
    myLabel.pack()

addDrinkButton = tk.Button(
    text="REMOVE DRINK",
    fg="black",
    bg=defaultcolor,
    # width = 25,
    # height = 25,
    command=removeDrinkButtonClicked
)

# entry = tk.Entry(
#     fg = "black",
#     bg = "white",
#     width=30
# )

#homescreen

def homescreen():
    Header.place(rely= 0.1, relx=0.3)
    mixDrinkButton.place(rely = 0.4,relx=0.075, height = 200, width = 200)
    addDrinkButton.place(rely = 0.4,relx=0.375, height = 200, width = 200)
    removeDrinkButton.place(rely = 0.4,relx=0.675, height = 200, width = 200)
    

homescreen()
window.mainloop()
