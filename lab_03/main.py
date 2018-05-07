from tkinter import *
from tkinter.colorchooser import askcolor
import math

root = Tk()
root.geometry('1250x700') #960
canv = Canvas(bg='white')
canv.pack(fill = BOTH, expand = 1)

def main():
    global point_list
    point_list = []
    add_line_button()
    add_circle_button()
    delete_all_button()
    color_lines_button()
    color_background_button()
    list()
    #create_lab()
    list_change_button()
    route()

def add_line_button():
    #Кнопка добавление 
    global add_x1, add_y1, add_x2, add_y2

    #Начало
    add_x1 = Entry(root)
    add_x1.pack()
    add_x1.place(x = 980, y = 130, width = 50)
    add_y1 = Entry(root)
    add_y1.pack()
    add_y1.place(x = 1050, y = 130, width = 50)

    #Конец
    add_x2 = Entry(root)
    add_x2.pack()
    add_x2.place(x = 980, y = 180, width = 50) 
    add_y2 = Entry(root)
    add_y2.pack()
    add_y2.place(x = 1050, y = 180, width = 50)
    
    button_1 = Button(root,text=u"Нарисовать линию")
    button_1.pack()
    button_1.place(x = 1100, y = 180, width = 145)
    button_1.bind("<Button-1>", get_AL)

def get_AL(root):
    global add_x1, add_y1, add_x2, add_y2, point_list, method
    x1 = add_x1.get()
    y1 = add_y1.get()
    x2 = add_x2.get()
    y2 = add_y2.get()
    x1 = int(x1)
    y1 = int(y1)
    x2 = int(x2)
    y2 = int(y2)
    #point_list.append([x1, y1, x2, y2])
    if (method == "Станадртная библиотека"):
        canv.create_line(x1, y1, x2, y2)
    elif (method == "Алгоритм Брезенхема с целочисленными"):
        brez_int(x1, y1, x2, y2)
    elif (method == "Алгоритм цифрового дифференциального анализа"):
        CDA(x1, y1, x2, y2)    
    elif (method == "Алгоритм Брезенхема с устранением ступенчатости"):
    	brez_stup(x1, y1, x2, y2)
    elif (method == "Алгоритм Брезенхема с вещественными"):
        brez_float(x1, y1, x2, y2)
    #draw_points()
    

def add_circle_button():
    #Кнопка добавление 
    global add_r, add_a
    #Начало
    add_r = Entry(root)
    add_r.pack()
    add_r.place(x = 980, y = 230, width = 50)
    add_a = Entry(root)
    add_a.pack()
    add_a.place(x = 980, y = 280, width = 50)
    
    button_2 = Button(root,text=u"Нарисовать круг")
    button_2.pack()
    button_2.place(x = 1100, y = 280, width = 145)
    button_2.bind("<Button-1>", get_AC)

def get_AC(root):
    global add_r, add_a, point_list
    radius = add_r.get()
    angle = add_a.get()
    radius = int(radius)
    angle = int(angle)
    rotate(angle, radius)
    #point_list.append([radius, angle])
    #canv.delete("all")
    #draw_points()

def rotate(angle, r):

    x_c = 500
    y_c = 500
    x1 = x_c - r 
    y1 = y_c
    x2 = x_c + r
    y2 = 0
    canv.create_line(x1 , y1, x2, y2)
    x1c = x1
    x2c = x2
    y1c = y1
    y2c = y2
    for i in range(0, 360, 10):
        angle_rotate = i * math.pi / 180
        x_1 = x_c + (x1 - x_c) * math.cos(angle_rotate) + (y1 - y_c) * math.sin(angle_rotate)
        y_1 = y_c - (x1 - x_c) * math.sin(angle_rotate) + (y1 - y_c) * math.cos(angle_rotate)
        x_2 = x_c + (x2 - x_c) * math.cos(angle_rotate) + (y2 - y_c) * math.sin(angle_rotate)
        y_2 =0
        x1 = int(x_1)
        y1 = int(y_1)
        x2 = int(x_2)
        y2 = int(x_2)
        canv.create_line(x1, y1, x2, y2)
        x1 = x1c
        x2 = x2c
        y1 = y1c
        y2 = y2c

def create_lab():
    canv.create_line(300, 300, 250, 350)
    canv.create_line(250, 350, 200, 300)
    canv.create_line(200, 300, 250, 250)
    canv.create_line(250, 250, 300, 300)
    canv.create_line(300, 300, 350, 300)
    canv.create_line(350, 300, 350, 100)
    canv.create_line(350, 100, 300, 100)
    canv.create_line(300, 100, 300, 300)
    canv.create_line(350, 300, 400, 350)
    canv.create_line(400, 350, 450, 300)
    canv.create_line(450, 300, 400, 250)
    canv.create_line(400, 250, 350, 300)

    '''
    for i in range (int(360 / angle)):
        angle_rotate = i * math.pi / 180
        #brez_int(x1, y1, x2, y2)
        canv.create_line(x1, y1, x2, y2)
        x_1 = x_c + (x1 - x_c) * math.cos(angle_rotate) + (y1 - y_c) * math.sin(angle_rotate)
        y_1 = y_c - (x1 - x_c) * math.sin(angle_rotate) + (y1 - y_c) * math.cos(angle_rotate)
        x_2 = x_c + (x2 - x_c) * math.cos(angle_rotate) + (y2 - y_c) * math.sin(angle_rotate)
        y_2 = y_c - (x2 - x_c) * math.sin(angle_rotate) + (y2 - y_c) * math.cos(angle_rotate)
        x1 = int(x_1)
        y1 = int(y_1)
        x2 = int(x_2)
        y2 = int(x_2)
    '''

def color_lines_button():
    button_4 = Button(root, text = u"Изменить цвет линии")
    button_4.pack()
    button_4.place(x = 980, y = 310, width = 170)
    button_4.bind("<Button-1>", get_CL)

def get_CL(root):
    global color_lines
    color_lines = askcolor()

def delete_all_button():
    button_3 = Button(root, text = u"Удалить все точки")
    button_3.pack()
    button_3.place(x = 980, y = 370, width = 140)
    button_3.bind("<Button-1>", get_DA)

def get_DA(root):
    global point_list
    point_list = []
    canv.delete("all")
    route()

def color_background_button():
    button_4 = Button(root, text = u"Изменить цвет фона")
    button_4.pack()
    button_4.place(x = 980, y = 340, width = 170)
    button_4.bind("<Button-1>", get_CB)

def get_CB(root):
    global color_background
    color_background = askcolor()

def route():
    #Текст к кнопкам
    canv.create_text(1010, 117, text = 'Начало: ')
    canv.create_text(970, 142, text = 'x: ')
    canv.create_text(1045, 142, text = 'y: ')
    canv.create_text(1005, 167, text = 'Конец: ')
    canv.create_text(970, 194, text = 'x: ')
    canv.create_text(1045, 194, text = 'y: ')
    canv.create_text(1010, 217, text = "Радиус: ")
    canv.create_text(1000, 267, text = "Угол: ")
    #Линии меню
    canv.create_line(1000, 207.5, 1200, 207.5)
    canv.create_line(1000, 309, 1200, 309)
    #Линии
    #canv.create_line(50, 0, 50, 700)
    #canv.create_line(100, 0, 100, 700)
    #canv.create_line(150, 0, 150, 700)
    #canv.create_line(200, 0, 200, 700)

    #canv.create_line(0, 200, 960, 200)
    #canv.create_line(0, 50, 960, 50)
    #canv.create_line(0, 100, 960, 100)
    #canv.create_line(0, 150, 960, 150)

def list_change_button():
    button_5 = Button(root, text = u"Изменить способ")
    button_5.pack()
    button_5.place(x = 980, y = 400, width = 140)
    button_5.bind("<Button-1>", get_L)

def get_L(root):
	global method, listbox
	method = listbox.get(ACTIVE)
	print(method)

def list():
    global listbox
    listbox = Listbox(root)
    listbox.pack()
    listbox.place(x = 875, y = 10, width = 365, height = 90)
    listbox.insert(END, "Станадртная библиотека")
    listbox.insert(END, "Алгоритм Брезенхема с целочисленными")
    listbox.insert(END, "Алгоритм Брезенхема с вещественными")
    listbox.insert(END, "Алгоритм Брезенхема с устранением ступенчатости")
    listbox.insert(END, "Алгоритм цифрового дифференциального анализа")

def brez_int(x1, y1, x2, y2):
    dx = math.fabs(x2 - x1)
    dy = math.fabs(y2 - y1)
    error = 0
    der = dy
    y = y1
    diry = y2 - y1
    if (diry > 0):
        diry = 1
    elif (diry < 0):
        diry = -1
    for i in range (x1, x2):
        canv.create_line(i, y, i, y + 1)
        canv.create_line(i, y + 1, i, y + 2, fill = "white")
        error += der
        if (error * 2 >= dx):
            y += diry
            error -= dx

def brez_float(x1, y1, x2, y2):
    dx = math.fabs(x2 - x1)
    dy = math.fabs(y2 - y1)
    error = 0
    der = dy / dx
    y = y1
    diry = y2 - y1
    if (diry > 0):
        diry = 1
    elif (diry < 0):
        diry = -1
    for i in range(x1, x2):
        canv.create_line(i, y, i, y + 1)
        canv.create_line(i, y + 1, i, y + 2, fill = "white")
        error += der
        if (error >= 0.5):
            y += diry
            error -= 1

def CDA(x1, y1, x2, y2):
    e = x2 / y2
    d_a = x2 / y2
    x = x1
    y = y1
    while (x < x2):
        canv.create_line(x, y, x, y + 1)
        canv.create_line(x, y + 1, x, y + 2, fill = "white")
        if (e > 0.5):
            x += 1
            y += 1
            e += d_a - 1
        else:
            x += 1
            e += d_a

def brez_stup(x1, y1, x2, y2):
    I = 1
    x = x1
    y = y1
    dx = x2 - x1
    dy = y2 - y1
    m = (I * dy) / dx
    w = I - m
    e = 0.5
    canv.create_line(x, y, x, y + 1)
    canv.create_line(x, y + 1, x, y + 2, fill = "white")
    while (x < x2):
        if (e < w):
            x += 1
            e += m
        else:
            x += 1
            y += 1
            e -= m
        canv.create_line(x, y, x, y + 1)
        canv.create_line(x, y + 1, x, y + 2, fill = "white")

#def brez_float(x1, y1, x2, y2):


if __name__ == '__main__':
    main()

root.mainloop()
