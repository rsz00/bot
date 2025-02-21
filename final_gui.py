import tkinter as tk

root = tk.Tk()

root.title("Bot Control Center")
root.configure(background="grey")
root.minsize(200,200)
root.maxsize(800,800)

#struzcturing label
tk.Label(root,text="Creation Amount: ").grid(row=0,column=0)
e1 = tk.Entry(root).grid(row=0,column=1)


#entry field







root.mainloop()