import tkinter as tk



def get_value():
    e = en.get()
    print(e)

root = tk.Tk()

root.title("Bot Control Center")
root.configure(background="grey")
root.minsize(200,200)
root.maxsize(800,800)

#struzcturing label
tk.Label(root,text="Creation Amount: ").grid(row=0,column=0)
en = tk.Entry(root)
en.grid(row=0,column=2)

tk.Button(root,text="Create",command=get_value).grid(row=0,column=3)

#entry field







root.mainloop()