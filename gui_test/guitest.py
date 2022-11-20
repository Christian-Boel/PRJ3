import tkinter as tk
from PIL import ImageTk,Image

root = tk.Tk()

buttonColor = "#2596be"
headerFont = 'Arial 75 bold'
normalFont = 'Arial 25'
buttonFont = 'Arial 15'

root.title("SPLASH")
root.geometry("800x480")
#root.configure(background="white")

sliderList = []
sliderLabelList = []
sliderValueList = []

class Drink():
    def __init__(self,name = "Default",colaRatio = 100,rumRatio = 0,vodkaRatio = 0):
        self.name = name
        self.colaRatio = colaRatio
        self.rumRatio = rumRatio
        self.vodkaRatio = vodkaRatio
    def setRatio(self,colaRatio,rumRatio,vodkaRatio):
        self.colaRatio = colaRatio
        self.rumRatio = rumRatio
        self.vodkaRatio = vodkaRatio
    def setName(self,name):
        self.name = name

drinkList = []

rumCoke = Drink("rumCoke",80,20,0)
vodkaCoke = Drink("vodkaCoke",80,0,20)

Header = tk.Label(text="SPLASH",font=headerFont,foreground="black")

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
        case "drinkAddedContinue":
            updateSliderValueList()
            addDrinkConfirmationMenu()
        case "addDrinkConfirm":
            print("Drink added")
            

def updateSliderValueList():
    sliderValueList.clear()
    for i in range(3):
        sliderValueList.append(sliderList[i].get())
    
#define buttons
mixDrinkButton = tk.Button(text="MIX DRINK",font = buttonFont,fg="black",bg=buttonColor,
command=lambda: btnPressed("mix")
)

addDrinkButton = tk.Button(text="ADD DRINK",font = buttonFont,fg="black",bg=buttonColor,
command=lambda: btnPressed("add")
)

removeDrinkButton = tk.Button(text="REMOVE DRINK",font = buttonFont,fg="black",bg=buttonColor,
command=lambda: btnPressed("remove")
)

#EDIT PICTURE PATH!

home_img = ImageTk.PhotoImage(Image.open(r"gui_test/icons/white_homeicon_80x80.png"))
home_button = tk.Button(image=home_img,
command= lambda: btnPressed("home")
)

back_img = ImageTk.PhotoImage(Image.open(r"gui_test/icons/arrow_original_80x80.png"))
back_button = tk.Button(image=back_img)

#homescreen

def clearScreen():
    for widget in root.winfo_children():
        widget.place_forget()

def addMenuButtons():
    home_button.place(y = 400,x = 0)
    back_button.place(y=400,x = 720)

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

    addDrinkContinuedButton = tk.Button(text="CONFIRM" ,font=buttonFont,fg="black", bg=buttonColor,
    command=lambda: btnPressed("drinkAddedContinue"))

    label = tk.Label(text="Choose drink content",font=buttonFont)
    label.place(relx = 0.4, rely = 0.1)
    sliderCount = 3
    sliderLabelList = []
    sliderXvalue = 0.15
    sliderYvalues = [0.2, 0.35, 0.5]
    sliderLabelNames = ["Cola", "Rom", "Vodka"]
    fontSize = 24
    sliderWidth = 600
    nameXvalue = 0.1

    global sliderList
    global sliderValueList
    sliderList.clear()
    sliderValueList.clear()

    clearScreen()
    addMenuButtons()

    for i in range(sliderCount):
        sliderList.append(tk.Scale(root,from_=0, to=100,tickinterval=20, orient="horizontal" ))
        sliderList[i].set(0)
        sliderList[i].place(relx = sliderXvalue, rely = sliderYvalues[i], width = sliderWidth)
        sliderLabelList.append(tk.Label(root,text = sliderLabelNames[i],font=(fontSize)))
        sliderLabelList[i].place(relx = nameXvalue, rely = sliderYvalues[i]+0.04)

    addDrinkContinuedButton.place(relx = 0.3, rely = 0.65, height=100, width= 200)

def addDrinkConfirmationMenu():
    clearScreen()
    confirmButton = tk.Button(text="CONFIRM",font = buttonFont)
    addMenuButtons()
    label = tk.Label(text = "You selected these ingredients:", font = "arial 35 bold")
    label1 = tk.Label(text = "Cola: " + str(sliderValueList[0]) + " %",font = normalFont)
    label2 = tk.Label(text = "Rom: " + str(sliderValueList[1]) + " %", font = normalFont)
    label3 = tk.Label(text = "Vodka: " + str(sliderValueList[2]) + " %", font = normalFont)

    label.place(relx = 0.2,rely = 0.1)
    label1.place(relx = 0.4, rely = 0.25)
    label2.place(relx = 0.4, rely = 0.40)
    label3.place(relx = 0.4, rely = 0.55)
    confirmButton.place(relx = 0.35,rely = 0.65, height=100, width=200,
    command = lambda: btnPressed("addDrinkConfirm"))

#run program - start in home menu
homeMenu()
root.mainloop()
