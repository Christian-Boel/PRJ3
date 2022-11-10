import tkinter as tk
from PIL import ImageTk,Image

root = tk.Tk()

buttonColor = "#2596be"
headerFont = 'Arial 75 bold'
buttonFont = 'Arial 15'

root.title("SPLASH")
root.geometry("800x480")
#root.configure(background="white")

Header = tk.Label(
    text="SPLASH",
    font=headerFont,
    foreground="black")

def homeBtnPressed(): #go home button
    homeMenu()

def btnPressed(btn): #Button pressed while on homescreen
    match btn:
        case "home":
            homeMenu()
        case "mix":
            mixDrinkMenu()
            #myLabel = tk.Label(root,text="mix drink clicked!")
            #myLabel.pack()
        case "add":
            addDrinkMenu()

        #case "remove":
            #removeDrinkMenu()


#define buttons
mixDrinkButton = tk.Button(
    text="MIX DRINK",
    font = buttonFont,
    fg="black",
    bg=buttonColor,
    command=lambda: btnPressed("mix")
)

addDrinkButton = tk.Button(
    text="ADD DRINK",
    font = buttonFont,
    fg="black",
    bg=buttonColor,
    command=lambda: btnPressed("add")
)

removeDrinkButton = tk.Button(
    text="REMOVE DRINK",
    font = buttonFont,
    fg="black",
    bg=buttonColor,
    command=lambda: btnPressed("remove")
)


#EDIT PICTURE PATH!

home_img = ImageTk.PhotoImage(Image.open(r"gui_test/icons/white_homeicon_80x80.png"))
home_button = tk.Button(
    image=home_img,
    command= lambda: btnPressed("home")
    )

back_img = ImageTk.PhotoImage(Image.open(r"gui_test/icons/arrow_original_80x80.png"))
back_button = tk.Button(image=back_img)


#homescreen

def clearScreen():
    for widget in root.winfo_children():
        widget.place_forget()

def homeMenu():
    clearScreen()
    Header.place(rely= 0.05, relx=0.3)
    mixDrinkButton.place(rely = 0.4,relx=0.075, height = 200, width = 200)
    addDrinkButton.place(rely = 0.4,relx=0.375, height = 200, width = 200)
    removeDrinkButton.place(rely = 0.4,relx=0.675, height = 200, width = 200)

def mixDrinkMenu():
    clearScreen()
    home_button.place(y = 400,x = 0)
    back_button.place(y=400,x = 720)

# class Slider:
#     def __init__(self,relX,relY,name,nameX,nameY):
#         self.name = name
#         self.scale = tk.Scale(from_=0, to=100,tickinterval=10, orient="horizontal" ).set(0)
#         self.label = tk.Label(root, text = name, font=(24)).place(relx=0.1, rely=0.14)
    
#     def printSlider(relx, rely):
        
#     def printName(relX,relY):



def addDrinkMenu():
    clearScreen()
    home_button.place(y = 400,x = 0)
    back_button.place(y=400,x = 720)

    sliderCount = 4
    sliderList = []
    sliderLabelList = []
    sliderValueList = []
    sliderXvalue = 0.15
    sliderYvalues = [0.1, 0.25, 0.4 0.55]
    sliderLabelNames = ["Cola", "Rom", "Juice","Vodka"]
    fontSize = 24
    sliderWidth = 600
    nameXvalue = 0.1    
    nameYvalues = [0.14,0.29, 0.44, 0.59]

    for i in range(sliderCount):
        sliderList.append(tk.Scale(root,from_=0, to=100,tickinterval=10, orient="horizontal" ))
        sliderList[i].set(0)
        sliderList[i].place(relx = sliderXvalue, rely = sliderYvalues[i], width = sliderWidth)
        sliderLabelList.append(tk.Label(root,text = sliderLabelNames[i],font=(fontSize)))
        sliderLabelList[i].place(relx = nameXvalue, rely = nameYvalues[i])
    

#run program - start in home menu
homeMenu()
root.mainloop()
