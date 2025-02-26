import tkinter
import tkinter.messagebox


class MyGUI:
    def __init__(self):
        # Frames
        self.mainWindow = tkinter.Tk()
        self.mainWindow.title("Pizzeria")
        self.size = tkinter.Frame(self.mainWindow)
        self.toppings = tkinter.Frame(self.mainWindow)
        self.bottom = tkinter.Frame(self.mainWindow)
        # Radio Buttons
        self.S0 = tkinter.Label(self.size, text="Choose the size of your pizza:")
        self.intVar1 = tkinter.IntVar()
        self.S1 = tkinter.Radiobutton(
            self.size, text="Small", value=1, variable=self.intVar1
        )
        self.S2 = tkinter.Radiobutton(
            self.size, text="Medium", value=2, variable=self.intVar1
        )
        self.S3 = tkinter.Radiobutton(
            self.size, text="Large", value=3, variable=self.intVar1
        )
        self.intVar1.set(2)
        # Ingredients
        self.intVar0b = tkinter.IntVar()
        self.T0 = tkinter.Checkbutton(
            self.toppings, text="Pepperoni", variable=self.intVar0b
        )
        self.intVar1b = tkinter.IntVar()
        self.T1 = tkinter.Checkbutton(
            self.toppings, text="Chicken", variable=self.intVar1b
        )
        self.intVar2b = tkinter.IntVar()
        self.T2 = tkinter.Checkbutton(
            self.toppings, text="Beef", variable=self.intVar2b
        )
        self.intVar3b = tkinter.IntVar()
        self.T3 = tkinter.Checkbutton(
            self.toppings, text="Green Pepper", variable=self.intVar3b
        )
        self.intVar4b = tkinter.IntVar()
        self.T4 = tkinter.Checkbutton(
            self.toppings, text="Mushroom", variable=self.intVar4b
        )
        self.intVar5b = tkinter.IntVar()
        self.T5 = tkinter.Checkbutton(
            self.toppings, text="Spinach", variable=self.intVar5b
        )
        self.intVar6b = tkinter.IntVar()
        self.T6 = tkinter.Checkbutton(
            self.toppings, text="Tomato", variable=self.intVar6b
        )
        # Order and Destruction buttons
        self.Order = tkinter.Button(self.bottom, text="Order",
                                    command=self.costCalc)
        self.Exit = tkinter.Button(
            self.bottom, text="Exit", command=self.mainWindow.destroy
        )
        # Packing
        self.size.pack()
        self.toppings.pack()
        self.bottom.pack()
        self.S0.pack(side="left")
        self.S1.pack(side="left")
        self.S2.pack(side="left")
        self.S3.pack(side="left")
        self.T0.pack(side="top")
        self.T1.pack(side="top")
        self.T2.pack(side="top")
        self.T3.pack(side="top")
        self.T4.pack(side="top")
        self.T5.pack(side="top")
        self.T6.pack(side="top")
        self.Order.pack(side="left")
        self.Exit.pack(side="left")

        tkinter.mainloop()

    def costCalc(self):
        costCounter = 0
        if self.intVar1.get() == 1:
            costCounter += 5
        elif self.intVar1.get() == 2:
            costCounter += 10
        elif self.intVar1.get() == 3:
            costCounter += 15

        if self.intVar0b.get() == 1:
            costCounter += 3
        if self.intVar1b.get() == 1:
            costCounter += 4
        if self.intVar2b.get() == 1:
            costCounter += 4
        if self.intVar3b.get() == 1:
            costCounter += 2
        if self.intVar4b.get() == 1:
            costCounter += 2
        if self.intVar5b.get() == 1:
            costCounter += 2
        if self.intVar6b.get() == 1:
            costCounter += 2

        tkinter.messagebox.showinfo(
            "Total Cost",
            "Your total cost is: " + str(costCounter + costCounter / 100 * 7),
        )


MyGUI()
