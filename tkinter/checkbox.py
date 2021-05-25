import tkinter as tk

window = tk.Tk()
window.title("Hello Tkinter")

checks = []


def add():
    get = ent1.get()

    if len(list(filter(lambda c: c["text"] == get, checks))):
        print("already exist")
    else:
        variable = tk.BooleanVar()
        variable.set(0)
        checkbutton = tk.Checkbutton(text=get, variable=variable)
        checkbutton.pack()
        checks.append(checkbutton)


ent1 = tk.Entry()
btn = tk.Button(text="add", height=5, width=10, command=add)
ent1.pack()
btn.pack()
tk.mainloop()
