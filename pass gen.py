from tkinter import *
import random

def password_gen(length):
    
    upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lower = upper.lower()
    num = '1234567890'
    punc = ',.(){#~@'

    length_pass = length.get()
    
    all = upper + lower + num + punc

    password = ''.join(random.sample(all, int(length_pass)))
    draw_password_window(password,length_pass)

def draw_password_window(given_password,name12):
    global new_text
    new_text = Label(text = str(given_password))
    new_text.place(relx = 0.5,rely =0.45,anchor = CENTER)
    
def password_gen_Start():
    password_gen(name)

def go_again():
    new_text.cget('text')
    new_text.config(text='')
    
    name.delete(0,'end')
    

    
def window():
    global name
    screen = Tk()
    screen.title('my first graphics program')
    screen.geometry('400x200')

    welcome_text = Label(text = 'password generator')
    welcome_text.pack()

    explain_text = Label(text = 'above enter the length of the password')
    explain_text.place(relx = 0.5,rely=0.65, anchor = CENTER)
  

    press = Button(text = 'rest',height =1, command = go_again)
    press.place(relx=0.5,rely=0.75,anchor = CENTER)

    
    
    

    press_2 = Button(text = 'enter',command = password_gen_Start)
    press_2.place(relx=0.5,rely = 0.9,anchor = CENTER)
    length_pass = 0
    name = Entry(textvariable = length_pass)
    name.place(relx = 0.5,rely = 0.55,anchor = CENTER)
    
    

    

    

    screen.mainloop()
window()

##out_put(password)

