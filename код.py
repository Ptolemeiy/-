from tkinter import *

def add_1():
    btn.pack_forget()
    frame_1.pack()
    btn.pack()

def add_2():
    btn.pack_forget()
    btn2.pack()
    frame_2.pack()
    btn1["text"] = 'Нажмите сюда чтобы выбрать'
    if rbt.get() == 1:
        lab1["bg"] = "green"
        frame_2.pack_forget()
    if rbt.get() == 2:
        lab1["bg"] = "yellow"
        frame_2.pack_forget()
    if rbt.get() == 3:
        lab1["bg"] = "red"
        frame_2.pack_forget()



root = Tk()
root.geometry("360x750")

lab = Label(text = "Какие у Вас на сегодня планы?", anchor = CENTER, font = "device", height = 3)
lab.pack()

btn = Button(text = "Добавить действие", font = "device", command = add_1)
btn.pack()

frame_1 = Frame(height = 20, width = 90)

lab1 = Label(frame_1, text = 'Что Вы хотите сделать?', height = 3)
lab1.pack()
ent = Entry(frame_1)
ent.pack(anchor = N)
btn1 = Button(frame_1, text = 'Приоритетность', font = "device", command = add_2)
btn1.pack()

frame_2 = Frame(width = 10)

btn2 = Button(frame_1, text = "Действие добавить", font = "device")
btn2.pack()

rbt = IntVar()

rbt_1 = Radiobutton(frame_2, text = 'Очень важно', value = 1, variable = rbt)
rbt_1.pack()

rbt_2 = Radiobutton(frame_2, text = 'Особо не важно', value = 2, variable = rbt)
rbt_2.pack()

rbt_3 = Radiobutton(frame_2, text = 'Совсем не важно', value = 3, variable = rbt)
rbt_3.pack()

root.mainloop()