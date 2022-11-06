import tkinter as tk
from PIL import ImageTk,Image

root = tk.Tk()

buttonColor = "#2596be"
headerFont = 'Arial 75 bold'
buttonFont = 'Arial 15'

root.title("SPLASH")
root.geometry("800x480")
#root.configure(background="white")


#EDIT PICTURE PATH!

home_img = ImageTk.PhotoImage(Image.open(r"C:\Users\boel\PRJ3\PRJ3\gui_test\icons\white_homeicon_80x80.png"))
home_button = tk.Button(image=home_img)

back_img = ImageTk.PhotoImage(Image.open(r"C:\Users\boel\PRJ3\PRJ3\gui_test\icons\arrow_original_80x80.png"))
back_button = tk.Button(image=back_img)

Header = tk.Label(
    text="SPLASH",
    font=headerFont,
    foreground="black")


def homescreenBtnPressed(btn): #Button pressed while on homescreen
    match btn:
        case "mix":
            mixDrinkMenu()
            #myLabel = tk.Label(root,text="mix drink clicked!")
            #myLabel.pack()
        case "add":
            #addDrinkMenu()
            myLabel = tk.Label(root,text="Add drink clicked!")
            myLabel.pack()

        case "remove":
            #removeDrinkMenu()
            myLabel = tk.Label(root,text="Remove drink clicked!")
            myLabel.pack()


#define buttons
mixDrinkButton = tk.Button(
    text="MIX DRINK",
    font = buttonFont,
    fg="black",
    bg=buttonColor,
    command=lambda: homescreenBtnPressed("mix")
)

addDrinkButton = tk.Button(
    text="REMOVE DRINK",
    font = buttonFont,
    fg="black",
    bg=buttonColor,
    command=lambda: homescreenBtnPressed("add")
)

removeDrinkButton = tk.Button(
    text="ADD DRINK",
    font = buttonFont,
    fg="black",
    bg=buttonColor,
    command=lambda: homescreenBtnPressed("remove")
)

# entry = tk.Entry(
#     fg = "black",
#     bg = "white",
#     width=30
# )

#homescreen


def clearScreen():
    for widget in root.winfo_children():
        widget.place_forget()

def homeMenu():
    clearScreen()
    Header.place(rely= 0.05, relx=0.25)
    mixDrinkButton.place(rely = 0.4,relx=0.075, height = 200, width = 200)
    addDrinkButton.place(rely = 0.4,relx=0.375, height = 200, width = 200)
    removeDrinkButton.place(rely = 0.4,relx=0.675, height = 200, width = 200)

def mixDrinkMenu():
    clearScreen()
    home_button.place(y = 400,x = 0)
    back_button.place(y=400,x = 720)

#run program - start in home menu
homeMenu()
root.mainloop()
