import tkinter as tk
from PIL import ImageTk,Image

root = tk.Tk()

buttonColor = "#2596be"
headerFont = 'Arial 75 bold'
normalFont = 'Arial 25'
mediumFont = 'Arial 20'
smallFont = 'Arial 15'

root.title("SPLASH")
root.geometry("800x480")

#Drink class - used for storing values
class Drink():
    def __init__(self,name:str,colaRatio:float,rumRatio:float,vodkaRatio:float):
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

#global variables

#drink lists
drinkList = []
drinkButtonList = []

#slider variables
sliderList = []
sliderLabelList = []
sliderValueList = []

#Predefined drinks
drinkList.append(Drink("Rum and Coke",80,20,0))
drinkList.append(Drink("Vodka and Coke",80,0,20))
drinkList.append(Drink("Super Mix ", 70,15,15))
drinkList.append(Drink("Oliver Special", 40,50,10))
drinkList.append(Drink("Quad Spejlæg",20,20,60))
nameVar = tk.StringVar()

#addional variables
colaContainerEmpty = False
vodkaContainerEmpty = False
rumContainerEmpty = False
sizeSelected = "Small"
drinkSelected = drinkList[0] #default



#Default button handler
def btnPressed(btnValue): 
        if btnValue == "home":
            displayHomeMenu()
        if btnValue == "mix":
            drinkSizeMenu()
        if btnValue == "add":
            addDrinkMenu()
        if btnValue == "remove":
            removeDrinkMenu()
        if btnValue == "drinkAddedContinue":
            if updateSliderValueList() == -1:
                return
            addDrinkConfirmationMenu()
        if btnValue == "addDrinkConfirm":
            print("Drink added")
            drinkList.append(Drink(nameVar.get(),sliderValueList[0],sliderValueList[1],sliderValueList[2]))
            displayHomeMenu()
        if btnValue =="Small" or btnValue=="Medium" or btnValue=="Large":
            global sizeSelected
            sizeSelected = btnValue
            mixDrinkMenu()
        if btnValue == "pour":
            print("Pouring drink!")

#Button handler for mix drink and remove drink menues
def drinkBtnPressed(drink):
    global drinkSelected
    drinkSelected = drink
    mixDrinkConfirmationMenu()
    return

def updateDrinkButtons():
    drinkButtonList.clear()
    for drink in drinkList: #create button for every drink
        drinkButtonList.append(tk.Button(text=drink.name,bg = "#581105", fg = "white", font=smallFont,command = lambda: drinkBtnPressed(drink)))

def updateSliderValueList():
    sliderValueList.clear()
    totalpercentage = 0
    for i in range(len(sliderList)):
        sliderValueList.append(sliderList[i].get())
        totalpercentage += sliderValueList[i]
    #check if percentages add up to 100%
    if(totalpercentage == 0):
        return -1 #error
    if totalpercentage != 100:
        for i in range(len(sliderList)):
            #setting values to add up to 100%
            sliderValueList[i] /= (totalpercentage/100)

#Homescreen and menu buttons
Header = tk.Label(text="SPLASH",font=headerFont,foreground="black")
mixDrinkButton = tk.Button(text="MIX DRINK",font = smallFont,fg="black",bg=buttonColor,
command=lambda: btnPressed("mix")
)

addDrinkButton = tk.Button(text="ADD DRINK",font = smallFont,fg="black",bg=buttonColor,
command=lambda: btnPressed("add")
)

removeDrinkButton = tk.Button(text="REMOVE DRINK",font = smallFont,fg="black",bg=buttonColor,
command=lambda: btnPressed("remove")
)

#ÆNDRE STIEN HVIS DER ER COMPILER FEJL 
home_img = ImageTk.PhotoImage(Image.open(r"icons/white_homeicon_80x80.png"))
home_button = tk.Button(image=home_img,
command= lambda: btnPressed("home")
)

back_img = ImageTk.PhotoImage(Image.open(r"icons/arrow_original_80x80.png"))
back_button = tk.Button(image=back_img)


#Functions for displaying various menues
def clearScreen():
    for widget in root.winfo_children():
        widget.place_forget()

def displayMenuButtons():
    home_button.place(y=400,x = 0)
    back_button.place(y=400,x = 720)

def displayDrinkButtons():
    #mapping x and y positions for button placement
    xpos = [0.1, 0.3, 0.5, 0.7, 0.1, 0.3, 0.5, 0.7]
    ypos = [0.2, 0.2, 0.2, 0.2, 0.5, 0.5, 0.5, 0.5]
    btnLimit = 8
    for i,drinkBtn in enumerate(drinkButtonList):
        if i < btnLimit:
            drinkBtn.place(rely=ypos[i],relx = xpos[i],height = 100, width = 150)

def displayHomeMenu():
    clearScreen()
    Header.place(rely= 0.05, relx=0.26)
    mixDrinkButton.place(rely = 0.4,relx=0.075, height = 200, width = 200)
    addDrinkButton.place(rely = 0.4,relx=0.375, height = 200, width = 200)
    removeDrinkButton.place(rely = 0.4,relx=0.675, height = 200, width = 200)

def mixDrinkMenu():
    clearScreen()
    displayMenuButtons()
    updateDrinkButtons()
    displayDrinkButtons()

def removeDrinkMenu():
    clearScreen()
    displayMenuButtons()
    updateDrinkButtons()
    displayDrinkButtons()

def addDrinkMenu():
    clearScreen()
    displayMenuButtons()

    addDrinkContinuedButton = tk.Button(text="Continue" ,font=smallFont,fg="black", bg=buttonColor,
    command=lambda: btnPressed("drinkAddedContinue"))
    label1 = tk.Label(text="Add drink",font="arial 25 bold")
    nameLabel = tk.Label(text="Name:",font="arial 15")
    nameEntry = tk.Entry(textvariable = nameVar, font = "arial 15")
    
    sliderCount = 3
    sliderLabelList = []
    sliderXvalue = 0.15
    sliderYvalues = [0.25, 0.4, 0.55]
    sliderLabelNames = ["Cola", "Rom", "Vodka"]
    fontSize = 24
    sliderWidth = 600
    nameXvalue = 0.1

    global sliderList
    global sliderValueList
    sliderList.clear()
    sliderValueList.clear()
    nameVar.set("")

    for i in range(sliderCount):
        sliderList.append(tk.Scale(root,from_=0, to=100,tickinterval=20, orient="horizontal" ))
        sliderList[i].set(0)
        sliderList[i].place(relx = sliderXvalue, rely = sliderYvalues[i], width = sliderWidth)
        sliderLabelList.append(tk.Label(root,text = sliderLabelNames[i],font=fontSize))
        sliderLabelList[i].place(relx = nameXvalue, rely = sliderYvalues[i]+0.04)

    addDrinkContinuedButton.place(relx = 0.35, rely = 0.7, height=100, width= 200)
    label1.place(relx = 0.4, rely = 0.05)
    nameLabel.place(relx = 0.3, rely = 0.2)
    nameEntry.place(relx = 0.4, rely = 0.2)

def addDrinkConfirmationMenu():
    clearScreen()
    confirmButton = tk.Button(text="CONFIRM",font = smallFont,bg = "green",
    command = lambda: btnPressed("addDrinkConfirm"))
    displayMenuButtons()
    label = tk.Label(text = "Ingredients selected:", font = "arial 20 bold")
    label1 = tk.Label(text = "Cola: " + str(round(sliderValueList[0],1)) + " %",font = mediumFont)
    label2 = tk.Label(text = "Rom: " + str(round(sliderValueList[1],1)) + " %", font = mediumFont)
    label3 = tk.Label(text = "Vodka: " + str(round(sliderValueList[2],1)) + " %", font = mediumFont)
    nameLabel = tk.Label(text = "Name: " + nameVar.get() , font = normalFont)

    nameLabel.place(relx = 0.32, rely = 0.1)
    label.place(relx = 0.32,rely = 0.28)
    label1.place(relx = 0.4, rely = 0.38)
    label2.place(relx = 0.4, rely = 0.48)
    label3.place(relx = 0.4, rely = 0.58)
    confirmButton.place(relx = 0.4,rely = 0.72, height=75, width=150)

def drinkSizeMenu():
    clearScreen()
    displayMenuButtons()
    label = tk.Label(text="Choose a drink size",font="arial 30 bold")
    label.place(relx = 0.30,rely = 0.1)
    button1 = tk.Button(text="Small",font=mediumFont,bg="red",command=lambda: btnPressed("Small"))
    button2 = tk.Button(text="Medium",font=mediumFont,bg="red",command=lambda: btnPressed("Medium"))
    button3 = tk.Button(text="Large",font=mediumFont,bg="red",command=lambda: btnPressed("Large"))

    button1.place(rely = 0.4,relx=0.1, height = 175, width = 175)
    button2.place(rely = 0.4,relx=0.4, height = 175, width = 175)
    button3.place(rely = 0.4,relx=0.7, height = 175, width = 175)
    
def mixDrinkConfirmationMenu():
    global drinkSelected
    clearScreen()
    displayMenuButtons()
    label0 = tk.Label(text = "Size: " + sizeSelected, font = mediumFont)
    label = tk.Label(text = "Ingredients: ", font = "arial 20 bold")
    label1 = tk.Label(text = "Cola: " + str(round(drinkSelected.colaRatio,1)) + " %",font = mediumFont)
    label2 = tk.Label(text = "Rom: " + str(round(drinkSelected.rumRatio,1)) + " %", font = mediumFont)
    label3 = tk.Label(text = "Vodka: " + str(round(drinkSelected.vodkaRatio,1)) + " %", font = mediumFont)
    nameLabel = tk.Label(text=drinkSelected.name , font = normalFont)
    confirmButton = tk.Button(text="MIX!",font = smallFont,bg = "green",command=lambda:btnPressed("pour"))

    nameLabel.place(relx = 0.4, rely = 0.01)
    label0.place(relx = 0.4,rely = 0.15)
    label.place(relx = 0.4,rely = 0.28)
    label1.place(relx = 0.4, rely = 0.38)
    label2.place(relx = 0.4, rely = 0.48)
    label3.place(relx = 0.4, rely = 0.58)
    confirmButton.place(relx = 0.4,rely = 0.72, height=75, width=150)

#run program - start in home menu
displayHomeMenu()
root.mainloop()
