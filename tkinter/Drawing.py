import tkinter as tk
from PIL import Image, ImageTk
window = tk.Tk()
window.title("Drawing")

canvas = tk.Canvas(width=400, height=400)
# canvas.create_line(0, 0, 100, 100)
# canvas.create_line(100, 100, 200, 215, dash=(10, 2))
# canvas.create_line(100, 100, 0, 200, 110, 215, 11, 25, width=10, fill="#ff0000")
#
# canvas.create_oval(10, 10, 80, 80, width=10)
# canvas.create_oval(108, 108, 80, 180, width=3, outline="#ff0000", fill="#00ff00")
# canvas.create_rectangle(200, 300, 10,10, width=4)
# points = [150, 100, 200, 120, 240,180, 200, 300]
# canvas.create_polygon(points, outline="#aa12bb")
image_open = Image.open("index.jpg")
image = ImageTk.PhotoImage(image_open)
canvas.create_image(100,100, image=image)

# canvas.create_arc(100,100, 50,50, start=0, extent=210, fill="#1f1")
# canvas.create_text(300, 100, font="Arial", text="Hello I like python")
# canvas.create_text(300, 200, font=("Times New Roman", 25), text="Hello I like python")
# canvas.create_text(300, 300, font=("JetBrains Mono", 25), text="Hello I like python")


canvas.pack()
tk.mainloop()
