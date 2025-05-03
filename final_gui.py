import tkinter as tk
from lib import dataInput
from selenium import webdriver
#from datainput import create_bots

#this creates the bots when button is pressed
def do_the_thing():
    i = 0
    iterations = int(e_num.get())
    while i < iterations:
        dataInput.dataInput(webdriver.Firefox())
        i+=1


root = tk.Tk()

root.title("Bot Control Center")
root.configure(background="grey")
root.minsize(200,200)
root.maxsize(800,800)

#structuring label
tk.Label(root,text="Creation Amount: ").grid(row=0,column=0)
e_num = tk.Entry(root)
e_num.grid(row=0,column=2)

tk.Button(root,text="Create",command=do_the_thing).grid(row=0,column=3)

#entry field







root.mainloop()