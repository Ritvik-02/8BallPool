from tkinter import *
from PIL import ImageTk, Image

def callback(event):
    global dx
    global dy
    dx = 5
    dy = 5

def move_ball():
    global dx
    global dy

    (left, top, right, bot) = canvas.coords(ball)

    if top <= 55 or bot >= 485:
        dy = -dy
    if left <= 55 or right >= 937:
        dx = -dx

    canvas.move(ball, dx, dy)

    if dx > 0:
        dx -= 0.01
    elif dx < 0:
        dx += 0.01

    if dy > 0:
        dy -= 0.01
    elif dy < 0:
        dy += 0.01

    tk.after(20, move_ball)


if __name__ == "__main__" :
    
    tk = Tk()
    tk.title("8-Ball Pool")
    tk.resizable(False, False)
    HEIGHT = 540
    WIDTH = 992

    canvas = Canvas(tk, width=WIDTH, height=HEIGHT)
    img = ImageTk.PhotoImage(Image.open("./tablepic.png"))
    canvas.create_image(496,0, anchor=N, image=img)
    canvas.pack()

    ball = canvas.create_oval(100,100,125,125,fill="black")
    dx = 5
    dy = 5

    canvas.bind("<Button-1>", callback)

    tk.after(20, move_ball)

    tk.mainloop()
