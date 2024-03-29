import tkinter as tk
from PIL import ImageTk,Image
import time
import os
from drink import Drink
from constants import buttonColor,headerFont,normalFont,mediumFont,smallFont,testmode

root = tk.Tk()
root.title("SPLASH")
root.geometry("800x430")

#img paths
glass_img1 = ImageTk.PhotoImage(Image.open(r"icons/glassIcon1.png"))
glass_img2 = ImageTk.PhotoImage(Image.open(r"icons/glassIcon2.png"))
placeGlassLabel = tk.Label(image=glass_img1) # used for animation

fillglass_img1 = ImageTk.PhotoImage(Image.open(r"icons/Glass empty.png"))
fillglass_img2 = ImageTk.PhotoImage(Image.open(r"icons/Glass third full.png"))
fillglass_img3 = ImageTk.PhotoImage(Image.open(r"icons/Glass third empty.png"))
fillglass_img4 = ImageTk.PhotoImage(Image.open(r"icons/Glass full.png"))
fillGlassLabel = tk.Label(image=fillglass_img1)

#global variables
#drink lists
drinkList = []
drinkButtonList = []

#slider variables
sliderList = []
sliderLabelList = []
sliderValueList = []
nameVar = tk.StringVar() 

#Predefined drinks
drinkList.append(Drink("Rum and Coke",80,20,0))
drinkList.append(Drink("Vodka and Coke",80,0,20))
drinkList.append(Drink("Super Mix ", 70,15,15))
drinkList.append(Drink("Oliver Special", 40,50,10))
drinkList.append(Drink("Quad Spejlæg",20,20,60))

#addional variables
colaContainerEmpty = False
vodkaContainerEmpty = False
rumContainerEmpty = False   
sizeSelected = "Small"
drinkSelected = drinkList[0] #default

#Default button handler
def btnPressed(btnValue:str): 
        if btnValue == "home":
            homeMenu()
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
            homeMenu()
        if btnValue =="Small" or btnValue=="Medium" or btnValue=="Large":
            global sizeSelected
            sizeSelected = btnValue #setDrinkSize
            mixDrinkMenu()
        if btnValue == "mixDrinkConfirm":
            pourDrink()

#Button handler for mix drink and remove drink menues
def drinkBtnPressed(drink:Drink,remove:bool,index:int):
    if(remove == 0):
        global drinkSelected
        drinkSelected = drink #setDrinkChoice
        placeGlassMenu()
    else: 
        del drinkList[index]
        time.sleep(0.5)
        homeMenu()

def updateDrinkButtons(remove:bool):
    print("Update drink buttons called")
    drinkButtonList.clear()
    for i,drink in enumerate(drinkList): #create button for every drink
        drinkButtonList.append(tk.Button(text=drink.name,bg =  "#581105", fg = "white", font=smallFont, command = lambda drink=drink,i=i: drinkBtnPressed(drink,remove,i)))
        #check for empty containers 
        if((colaContainerEmpty and drink.colaRatio > 0) or (rumContainerEmpty and drink.rumRatio > 0) or (vodkaContainerEmpty and drink.vodkaRatio > 0)):
            drinkButtonList[i].configure(command=None) 
            if(remove != 1):
                drinkButtonList[i].configure(bg = "grey")
        
def updateSliderValueList():
    print("Update slider values called")
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

home_img = ImageTk.PhotoImage(Image.open(r"icons/white_homeicon_80x80.png"))
home_button = tk.Button(image=home_img,
command= lambda: btnPressed("home")
)

#Functions for displaying various menues
def clearScreen():
    print("Clear screen called")
    for widget in root.winfo_children():
        widget.place_forget()

def displayMenuButtons():
    print("Display menu buttons called")
    home_button.place(y = 350,x = 0)
   #back_button.place(y=400,x = 720)

def displayDrinkButtons():
    print("Display drink buttons called")
    #mapping x and y positions for button placement
    xpos = [0.1, 0.3, 0.5, 0.7, 0.1, 0.3, 0.5, 0.7]
    ypos = [0.2, 0.2, 0.2, 0.2, 0.5, 0.5, 0.5, 0.5]
    btnLimit = 8
    for i,drinkBtn in enumerate(drinkButtonList):
        if i < btnLimit:
            drinkBtn.place(rely=ypos[i],relx = xpos[i],height = 100, width = 150)

def homeMenu():
    #Homescreen and menu buttons
    Header = tk.Label(text="SPLASH",font=headerFont,foreground="black")
    mixDrinkButton = tk.Button(text="MIX DRINK",font = smallFont,bg=buttonColor,
    command=lambda: btnPressed("mix"))
    addDrinkButton = tk.Button(text="ADD DRINK",font = smallFont,bg=buttonColor,
    command=lambda: btnPressed("add"))
    removeDrinkButton = tk.Button(text="REMOVE DRINK",font = smallFont,bg=buttonColor,
    command=lambda: btnPressed("remove"))

    print("Entering home menu")
    clearScreen()
    Header.place(rely = 0.2, relx=0.5, anchor = "center")
    mixDrinkButton.place(rely = 0.4,relx=0.075, height = 200, width = 200)
    addDrinkButton.place(rely = 0.4,relx=0.375, height = 200, width = 200)
    removeDrinkButton.place(rely = 0.4,relx=0.675, height = 200, width = 200)

def removeDrinkMenu():
    print("Entering remove drink menu")
    clearScreen()
    displayMenuButtons()
    updateDrinkButtons(True)
    displayDrinkButtons()
    label = tk.Label(text = "Remove a drink: ", font = "arial 30 bold")
    label.place(rely = 0.1, relx =0.5,anchor= "center")

def addDrinkMenu():
    print("Entering add drink menu")
    clearScreen()
    displayMenuButtons()

    addDrinkContinuedButton = tk.Button(text="Continue" ,font=smallFont, bg=buttonColor,
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
    print("Entering add drink confirmation menu")
    clearScreen()
    confirmButton = tk.Button(text="CONFIRM",font = smallFont,bg = "green",command = lambda: btnPressed("addDrinkConfirm"))
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
    print("Entering drink size menu")
    clearScreen()
    displayMenuButtons()
    label = tk.Label(text="Choose a drink size",font="arial 30 bold")
    label.place(relx = 0.30,rely = 0.1)
    button1 = tk.Button(text="Small",font=mediumFont,bg="green",command=lambda: btnPressed("Small"))
    button2 = tk.Button(text="Medium",font=mediumFont,bg="green",command=lambda: btnPressed("Medium"))
    button3 = tk.Button(text="Large",font=mediumFont,bg="green",command=lambda: btnPressed("Large"))

    button1.place(rely = 0.4,relx=0.1, height = 175, width = 175)
    button2.place(rely = 0.4,relx=0.4, height = 175, width = 175)
    button3.place(rely = 0.4,relx=0.7, height = 175, width = 175)
    
def mixDrinkMenu():
    print("Entering mix drink menu")
    clearScreen()
    displayMenuButtons()
    updateDrinkButtons(False)
    displayDrinkButtons()
    label = tk.Label(text = "Select a drink: ", font = "arial 30 bold")
    label.place(rely = 0.1, relx =0.5,anchor= "center")

def mixDrinkDisplaySelectionMenu():
    print("Entering mix drink diplay selection menu")
    global drinkSelected
    clearScreen()
    displayMenuButtons()
    label0 = tk.Label(text = "Size: " + sizeSelected, font = mediumFont)
    label = tk.Label(text = "Ingredients: ", font = "arial 20 bold")
    label1 = tk.Label(text = "Cola: " + str(round(drinkSelected.colaRatio,1)) + " %",font = mediumFont)
    label2 = tk.Label(text = "Rom: " + str(round(drinkSelected.rumRatio,1)) + " %", font = mediumFont)
    label3 = tk.Label(text = "Vodka: " + str(round(drinkSelected.vodkaRatio,1)) + " %", font = mediumFont)
    nameLabel = tk.Label(text=drinkSelected.name , font = normalFont)
    confirmButton = tk.Button(text="Confirm",font = smallFont,bg = "green",command=lambda:btnPressed("mixDrinkConfirm"))

    nameLabel.place(relx = 0.4, rely = 0.01)
    label0.place(relx = 0.4,rely = 0.15)
    label.place(relx = 0.4,rely = 0.28)
    label1.place(relx = 0.4, rely = 0.38)
    label2.place(relx = 0.4, rely = 0.48)
    label3.place(relx = 0.4, rely = 0.58)
    confirmButton.place(relx = 0.4,rely = 0.72, height=75, width=150)

def placeGlassMenu():
    print("Entering placeglass menu")
    clearScreen()
    displayMenuButtons()
    label = tk.Label(text = "Placer glas på vægten",font = "arial 30 bold")
    label.place(rely = 0.1, relx = 0.3)
    placeGlassLabel.place(rely = 0.5, relx = 0.5, anchor="center")
    placeGlassAnimation()

def placeGlassAnimation():
    print("Starting place glass animation") 
    global placeGlassLabel
    def placeGlassAnimation1():
        placeGlassLabel.configure(image = glass_img1)
        root.after(1000,mixDrinkDisplaySelectionMenu if glassRegistered() else placeGlassAnimation2)
    def placeGlassAnimation2():
        placeGlassLabel.configure(image = glass_img2)
        root.after(1000,mixDrinkDisplaySelectionMenu if glassRegistered() else placeGlassAnimation1)
    placeGlassAnimation1()


def glassRegistered() -> bool:
    if testmode:
        return True
    SPI_Decoded = 0 #read spi
    SPI_int = 0
    try:
        file = os.open("/dev/spi_drv0", os.O_RDWR)
        SPI_Status = (os.read(file,16))
        SPI_Decoded = SPI_Status.decode()
        SPI_int = int.from_bytes(SPI_Status,byteorder='big')
        print("SPI: status read:" , SPI_Decoded)
    except:
        print("Failed to read from SPI")
    if SPI_Decoded == "255" or SPI_Decoded == " 255" or SPI_int == 255: 
        return True
    else:
        return False

def pourDrink():
    print("Pouring drink!")
    clearScreen()
    displayMenuButtons()
    label = tk.Label(text="Pouring drink",font="arial 30 bold")
    label.place(relx = 0.5, rely = 0.1, anchor = "center")
    SPI_Write()
    fillGlassLabel.place(rely = 0.5, relx = 0.5, anchor = "center")
    fillGlassAnimation()
    root.after(10000,homeMenu)

def SPI_Write():
    try:
        file = os.open("/dev/spi_drv0", os.O_RDWR)
        sizeVal = 1 if "Small" else 2 if "Medium" else 3
        #convert to string then to byte
        byteList = [str.encode(str(sizeVal| 128)), str.encode(str(drinkSelected.colaRatio|128)),
        str.encode(str(drinkSelected.rumRatio|128)),str.encode(str((drinkSelected.vodkaRatio|128)))]
        for byte in byteList:
            os.write(file,byte)
            print("Sending with SPI: ", byte.decode())
    except: 
        print("Failed to write to SPI")

x
def fillGlassAnimation():
    print("Starting fill glass animation")
    global fillGlassLabel
    def fillGlassAnimation1():
        fillGlassLabel.configure(image = fillglass_img1)
        root.after(600,fillGlassAnimation2)
    def fillGlassAnimation2():
        fillGlassLabel.configure(image = fillglass_img2)
        root.after(600,fillGlassAnimation3)
    def fillGlassAnimation3():
        fillGlassLabel.configure(image = fillglass_img3)
        root.after(600,fillGlassAnimation4)
    def fillGlassAnimation4():
        fillGlassLabel.configure(image = fillglass_img4)
        root.after(600,fillGlassAnimation1)
    fillGlassAnimation1()

#run program - start in home menu
homeMenu()
root.mainloop()
