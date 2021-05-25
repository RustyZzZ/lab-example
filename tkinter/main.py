import tkinter as tk

window = tk.Tk()
window.title("Hello Tkinter")


def change():
    firstIntVar.set(1)
    lastIntVar.set(1)
    label = tk.Label(text=str(ints))
    label.pack()


lbl_hello = tk.Label(text="Hello label",
                     width=50,
                     height=25,
                     fg="Black",
                     bg="SkyBlue4"
                     )

btn_hello = tk.Button(
    text="Press me",
    width=10,
    height=3,
    command=change
)

txt_code = tk.Text(width=50, height=20)

boolState = tk.BooleanVar()
intState = tk.IntVar()
intState.set(0)


def first_command():
    ints[0] = firstIntVar.get()


def last_command():
    ints[1] = lastIntVar.get()


rbt_first = tk.Radiobutton(text="first", variable=intState, value=0, command=first_command)
rbt_last = tk.Radiobutton(text="last", variable=intState, value=1, command=last_command)

firstIntVar = tk.IntVar()
lastIntVar = tk.IntVar()
ints = [0, 0]


def add():
    ints.append(1)


frame1 = tk.Frame()
frame2 = tk.Frame()
frame3= tk.Frame()
frame4 = tk.Frame()


def cmd(event):
    if(event.keycode==39):
        frame2.grid_remove()
    if (event.keycode == 38):
        frame2.grid()
    else:
        print(str(event))

btn_00=tk.Button(master=frame1, text="button00", width=10, height=5)
btn_01=tk.Button(master=frame1, text="button01", width=10, height=5)
btn_10=tk.Button(master=frame1, text="button10", width=10, height=5)
btn_11=tk.Button(master=frame1, text="button11", width=10, height=5)
btn_2=tk.Button(master=frame2, text="button2", width=20, height=10, command=cmd)
btn_3=tk.Button(master=frame3, text="button3", width=20, height=10)
btn_4=tk.Button( master=frame4, text="button4", width=20, height=10)
window.bind("a", cmd)
btn_3.bind("<Shift-Up>", lambda event:print("asdasdasdasd", str(event)))

btn_00.grid(master=frame1, row=0, column=3)
btn_00.grid(row=0, column=3)
btn_00.grid(row=3, column=0)
btn_00.grid(row=3, column=1)
btn_2.pack()
btn_3.pack()
btn_4.pack()

frame1.grid(row=0, column=3, padx=5, pady=5, sticky="nsew", columnspan=2, rowspan=2)
frame2.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")
frame3.grid(row=3, column=0, padx=5, pady=5, sticky="nsew")
frame4.grid(row=3, column=3, padx=5, pady=5, sticky="nsew")


window.columnconfigure(0, weight=1, minsize=75)
window.columnconfigure(1, weight=1, minsize=75)
window.columnconfigure(2, weight=1, minsize=75)
window.rowconfigure(0, weight=1, minsize=50)
window.rowconfigure(1, weight=1, minsize=50)
window.rowconfigure(2, weight=1, minsize=50)

cbt_first = tk.Checkbutton(text="First", variable=firstIntVar, onvalue=1, offvalue=0)
cbt_last = tk.Checkbutton(text="last", variable=lastIntVar, onvalue=1, offvalue=0, command=last_command)

# cbt_first.grid(row=0, column=0)
# cbt_last.grid(row=3, column=3)

# rbt_first.pack()
# rbt_last.pack()
# txt_code.pack()
# btn_hello.pack()

window.mainloop()
