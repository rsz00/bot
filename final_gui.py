import tkinter as tk
#from datainput import create_bots

#this creates the bots when button is pressed
def do_the_thing():
    

root = tk.Tk()

root.title("Bot Control Center")
root.configure(background="grey")
root.minsize(200,200)
root.maxsize(800,800)

#struzcturing label
tk.Label(root,text="Creation Amount: ").grid(row=0,column=0)
e_num = tk.Entry(root)
e_num.grid(row=0,column=2)

tk.Button(root,text="Create",command=get_value).grid(row=0,column=3)

#entry field







root.mainloop()