from tkinter import *
import time

def my_watch():
    x = time.strftime("Current date and time : \n%Y-%m-%d %H:%M:%S")
    clock.config(text=x)
    clock.after(200,my_watch)

root = Tk()
root.geometry("700x200")
clock = Label(root, font = ("times", 50, "bold"), bg="white")
clock.grid(row=0, column=1)

Label_1=Label(root, bg='white', text="</Developed By:-Shailendra kumar/> \n DM me for further querry:www.facebook/shailendrakr007", width=180, font=("bold",8))
Label_1.place(x=5,y=155)
my_watch()
root.mainloop()