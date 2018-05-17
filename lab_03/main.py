from tkinter import *
from tkinter.colorchooser import askcolor
import math


root = Tk()
root.geometry('1250x700') #960
canv = Canvas(root, width = 1250, height = 700, bg="#ffffff")
canv.pack()


def main():
    global point_list, img, color_lines
    color_lines = ["1", "#000000"]
    img = PhotoImage(width = 1250, height = 700)
    canv.create_image((1250//2, 700//2), image=img, state="normal")
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
    
    print(point_list)
    #point_list.append([x1, y1, x2, y2])
    if (method == "Станадртная библиотека"):
        canv.create_line(x1, y1, x2, y2, fill = color_lines[1])
        point_list.append([x1, y1, x2, y2, 0])
    elif (method == "Алгоритм Брезенхема с целочисленными"):
        brez_int(x1, y1, x2, y2)
        point_list.append([x1, y1, x2, y2, 1])
    elif (method == "Алгоритм цифрового дифференциального анализа"):
        CDA(x1, y1, x2, y2)  
        point_list.append([x1, y1, x2, y2, 2])  
    elif (method == "Алгоритм Брезенхема с устранением ступенчатости"):
        brez_stup(x1, y1, x2, y2)
        point_list.append([x1, y1, x2, y2, 3])
    elif (method == "Алгоритм Брезенхема с вещественными"):
        brez_float(x1, y1, x2, y2)
        point_list.append([x1, y1, x2, y2, 4])
    
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

def draw_point():
    global point_list, color_lines
    for i in range(len(point_list)):
        if point_list[i][4] == 0:
            canv.create_line(point_list[i][0], point_list[i][1], point_list[i][2], point_list[i][3], fill = color_lines[i][1])
        elif point_list[i][4] == 1:
            brez_int(point_list[i][0], point_list[i][1], point_list[i][2], point_list[i][3])
        elif point_list[i][4] == 2:
            CDA(point_list[i][0], point_list[i][1], point_list[i][2], point_list[i][3])
        elif point_list[i][4] == 3:
            brez_stup(point_list[i][0], point_list[i][1], point_list[i][2], point_list[i][3])
        elif point_list[i][4] == 4:
            brez_float(point_list[i][0], point_list[i][1], point_list[i][2], point_list[i][3])

def get_AC(root):
    global add_r, add_a, point_list
    radius = add_r.get()
    angle = add_a.get()
    radius = int(radius)
    angle = int(angle)
    rotate(angle, radius)

def rotate(angle, r):
    global method, color_lines
    x_c = 500
    y_c = 500
    x1 = x_c - r 
    y1 = y_c
    x2 = x_c + r
    y2 = y_c
    #canv.create_line(x1 , y1, x2, y2)
    x1c = x1
    x2c = x2
    y1c = y1
    y2c = y2
    for i in range(0, 360, angle):
        print(i/angle)
        print(i)
        angle_rotate = i * math.pi / 180
        x_1 = x_c + (x1 - x_c) * math.cos(angle_rotate) + (y1 - y_c) * math.sin(angle_rotate)
        y_1 = y_c - (x1 - x_c) * math.sin(angle_rotate) + (y1 - y_c) * math.cos(angle_rotate)
        x_2 = x_c + (x2 - x_c) * math.cos(angle_rotate) + (y2 - y_c) * math.sin(angle_rotate)
        y_2 = x_c - (x2 - x_c) * math.sin(angle_rotate) + (y2 - y_c) * math.cos(angle_rotate)
        
        x1 = round(x_1, 0)
        y1 = round(y_1, 0)
        x2 = round(x_2, 0)
        y2 = round(y_2, 0)
        x1 = int(x1)
        y1 = int(y1)
        x2 = int(x2)
        y2 = int(y2)
        #print(x1, y1, x2, y2)
        if (method == "Станадртная библиотека"):
            canv.create_line(x1, y1, x2, y2, fill = color_lines[1])
        elif (method == "Алгоритм Брезенхема с целочисленными"):
            brez_int(x1, y1, x2, y2)
        elif (method == "Алгоритм цифрового дифференциального анализа"):
            CDA(x1, y1, x2, y2)    
        elif (method == "Алгоритм Брезенхема с устранением ступенчатости"):
            brez_stup(x1, y1, x2, y2)
        elif (method == "Алгоритм Брезенхема с вещественными"):
            brez_float(x1, y1, x2, y2)
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
    delete_img()
    route()

def color_background_button():
    button_4 = Button(root, text = u"Изменить цвет фона")
    button_4.pack()
    button_4.place(x = 980, y = 340, width = 170)
    button_4.bind("<Button-1>", get_CB)

def get_CB(root):
    global color_background
    color_background = askcolor()
    canv.create_rectangle(0, 0, 850, 700, fill = color_background[1])
    route()
    draw_point()

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
    global color_lines, img
    #init
    p1 = [x1, y1]
    p2 = [x2, y2]
    if p1 == p2:
        canv.create_image((1250//2, 700//2), image=img, state="normal")
        img.put(color_lines[1], (int(p1[0]), int(p1[1])))
        return
    dx = p2[0] - p1[0]
    dy = p2[1] - p1[1]
    sx = sign(dx)
    sy = sign(dy)
    dx = math.fabs(dx)
    dy = math.fabs(dy)
    x = p1[0]
    y = p1[1]

    change = False
    
    if dy > dx:
        temp = dx
        dx = dy
        dy = temp
        change = True

    #alg
    e = 2 * dy - dx
    i = 1
    while i <= dx:
        canv.create_image((1250//2, 700//2), image=img, state="normal")
        img.put(color_lines[1], (int(x), int(y)))
        if e >= 0:
            if change == 0:
                y += sy
            else:
                x += sx
            e -= 2 * dx
        
        if e < 0:
            if change == 0:
                x += sx
            else:
                y += sy
            e += (2 * dy)
        i += 1
    
def delete_img():
    global img
    img = PhotoImage(width = 1250, height = 700)
    canv.create_image((1250//2, 700//2), image=img, state="normal")

def brez_float(x1, y1, x2, y2):
    global img, color_lines
    #init
    p1 = [x1, y1]
    p2 = [x2, y2]
    if p1 == p2:
        canv.create_image((1250//2, 700//2), image=img, state="normal")
        img.put(color_lines[1], (int(p1[0]), int(p1[1])))
        return

    dx = p2[0] - p1[0]
    dy = p2[1] - p1[1]
    sx = sign(dx)
    sy = sign(dy)
    dx = math.fabs(dx)
    dy = math.fabs(dy)
    x = p1[0]
    y = p1[1]

    change = False
    
    if dy > dx:
        dx, dy = dy, dx
        change = True

    h = dy / dx
    
    e = h - 0.5
    i = 1
    while i <= dx:
        canv.create_image((1250//2, 700//2), image=img, state="normal")
        img.put(color_lines[1], (int(x), int(y)))
        if e >= 0:
            if change is False:
                y += sy
            else:
                x += sx
            e -= 1
        
        if e < 0:
            if change is False:
                x += sx
            else:
                y += sy
            e += h
        i+=1

def CDA(x1, y1, x2, y2):
    global img, color_lines
    p1 = [x1, y1]
    p2 = [x2, y2]

    delta_x = p2[0] - p1[0]
    delta_y = p2[1] - p1[1]

    length = max(abs(delta_x), math.fabs(delta_y))

    if round(length, 0) == 0:
        canv.create_image((1250//2, 700//2), image=img, state="normal")
        img.put(color_lines[1], (int(p1[0]), int(p1[1])))
    
    dx = delta_x/length
    dy = delta_y/length
    
    x = round(p1[0], 0)
    y = round(p1[1], 0)
    
    points = []
    
    while length > 0:
        canv.create_image((1250//2, 700//2), image=img, state="normal")
        img.put(color_lines[1], (int(round(x, 0)), int(round(y))))
        x += dx
        y += dy
        length -= 1
######
def brez_stup(x1, y1, x2, y2):
    p1 = [x1, y1]
    p2 = [x2, y2]

    delta_x = p2[0] - p1[0]
    delta_y = p2[1] - p1[1]

    max_intens = 8

    if round(max(abs(delta_x), abs(delta_y)), 0) == 0:
        canv.create_image((1250//2, 700//2), image=img, state="normal")
        img.put(color_lines[1], (int(p1[0]), int(p1[1])))

    sx, sy = sign(delta_x), sign(delta_y)
    delta_x, delta_y = abs(delta_x), abs(delta_y)

    x, y = p1
    change = False

    if delta_y > delta_x:
        delta_x, delta_y = delta_y, delta_x
        change = True

    h = max_intens*delta_y/delta_x
    w = max_intens - h
    e = max_intens/2

    points = []
    i = 1
    while i <= delta_x:
        new = change_lightness(color_lines[1], int(e), max_intens)
        canv.create_image((1250//2, 700//2), image=img, state="normal")
        img.put(new, (int(x), int(y)))
        if e <= w:
            if change:
                y += sy
            else:
                x += sx
            e += h
        else:
            x += sx
            y += sy
            e -= w
        i = i + 1

def change_lightness(color, lvl, max_levels):
    if (color == 'black'):
        color = '#000000'
    rrggbb = color[1:3], color[3:5], color[5:7]
    print(rrggbb)
    rrggbb = [int(i, 16) for i in rrggbb]
    step = int(255/max_levels-1)
    for i in range(3):
        rrggbb[i] += lvl*step
        if rrggbb[i] > 255: rrggbb[i] = 255
        rrggbb[i] = hex(rrggbb[i])[2:]
    return "#" + "".join([str(i) if len(i)==2 else "0"+str(i) for i in rrggbb])
######
def sign(x):
    if x == 0:
        return 0
    else:
        return x/math.fabs(x)

'''
def CDA(x1, y1, x2, y2):
    global img, color_lines
    e = x2 / y2
    d_a = x2 / y2
    x = x1
    y = y1
    while (x < x2):
        canv.create_image((1250//2, 700//2), image=img, state="normal")
        img.put(color_lines[1], (x, y))
        if (e > 0.5):
            x += 1
            y += 1
            e += d_a - 1
        else:
            x += 1
            e += d_a
def brez_stup(x1, y1, x2, y2):
    global img, color_lines
    I = 1
    x = x1
    y = y1
    dx = x2 - x1
    dy = y2 - y1
    m = (I * dy) / dx
    w = I - m
    e = 0.5
    canv.create_image((1250//2, 700//2), image=img, state="normal")
    img.put(color_lines[1], (x, y))
    while (x < x2):
        if (e < w):
            x += 1
            e += m
        else:
            x += 1
            y += 1
            e -= m
        canv.create_image((1250//2, 700//2), image=img, state="normal")
        img.put(color_lines[1], (x, y))
def brez_int(x1, y1, x2, y2):
    global img, color_lines
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
    canv.delete("all")
    route()
    for i in range (x1, x2):
        #canv.create_line(i, y, i, y + 1)
        #canv.create_line(i, y + 1, i, y + 2, fill = "white")
        canv.create_image((1250//2, 700//2), image=img, state="normal")
        img.put(color_lines[1], (i, y))
        error += der
        if (error * 2 >= dx):
            y += diry
            error -= dx
def brez_float(x1, y1, x2, y2):
    global img, color_lines
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
        canv.create_image((1250//2, 700//2), image=img, state="normal")
        img.put(color_lines[1], (i, y))
        error += der
        if (error >= 0.5):
            y += diry
            error -= 1
'''

if __name__ == '__main__':
    main()

root.mainloop()
