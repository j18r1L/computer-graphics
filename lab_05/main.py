from tkinter import *
import math


root = Tk()
root.geometry('1250x700') #960
canv = Canvas(root, width = 1250, height = 700, bg="#ffffff")
canv.pack()


def main():
    global point_list, img, x_start, y_start
    x_start = False
    y_start = False
    img = PhotoImage(width = 1250, height = 700)
    canv.create_image((1250//2, 700//2), image=img, state="normal")
    point_list = []
    add_line_button()
    route()
    delete_all_button()
    end_button()


def add_line_button():
    global add_x, add_y
    #Начало
    add_x = Entry(root)
    add_x.pack()
    add_x.place(x = 980, y = 30, width = 50)
    add_y = Entry(root)
    add_y.pack()
    add_y.place(x = 1050, y = 30, width = 50)
    
    button_1 = Button(root,text=u"Добавить точку")
    button_1.pack()
    button_1.place(x = 1100, y = 30, width = 145)
    button_1.bind("<Button-1>", get_AL)
    canv.bind('<1>', get_C)

def get_C(root):
    global point_list, x_start, y_start, x_end, y_end
    x = root.x
    y = root.y
    if (x_start == False) and (y_start == False):
        x_start = x
        y_start = y
        x_end = x
        y_end = y
    point_list.append([x, y])
    print('| {:2s} | {:7s} | {:7.2s} |'.format('N', 'X', 'Y'))
    for i in range(len(point_list)):
        print('| {:2.0f} | {:7.0f} | {:7.0f} |'.format(i, point_list[i][0], point_list[i][1]))
    print('_______________________________\n')
    canv.create_line(x_start, y_start, x, y)
    x_start = x
    y_start = y
    lines_check()




def get_AL(root):
    global add_x, add_y, point_list, x_start, y_start, x_end, y_end
    x = add_x.get()
    y = add_y.get()
    x = int(x)
    y = int(y)
    if (x_start == False) and (y_start == False):
    	x_start = x
    	y_start = y
    	x_end = x
    	y_end = y
    point_list.append([x, y])
    print('| {:2.0s} | {:7s} | {:7.2s} |'.format('N', 'X', 'Y'))
    for i in range(len(point_list)):
        print('| {:2.0f} | {:7.0f} | {:7.0f} |'.format(i, point_list[i][0], point_list[i][1]))
    print('_______________________________\n')
    canv.create_line(x_start, y_start, x, y)
    x_start = x
    y_start = y
    lines_check()

def delete_all_button():
    button_2 = Button(root, text = u"Удалить все точки")
    button_2.pack()
    button_2.place(x = 980, y = 60, width = 140)
    button_2.bind("<Button-1>", get_DA)

def get_DA(root):
    global point_list, x_start, y_start, x_end, y_end
    point_list = []
    x_end = False
    y_end = False
    x_start = False
    y_start = False
    canv.delete("all")
    delete_img()
    route()

def delete_img():
    global img
    img = PhotoImage(width = 1250, height = 700)
    canv.create_image((1250//2, 700//2), image=img, state="normal")

def route():
    #Текст к кнопкам
    canv.create_text(970, 42, text = 'x: ')
    canv.create_text(1045, 42, text = 'y: ')

def end_button():
    button_3 = Button(root, text = u"Замкунть")
    button_3.pack()
    button_3.place(x = 980, y = 90, width = 140)
    button_3.bind("<Button-1>", get_E)

def get_E(root):
    global x_start, y_start, x_end, y_end
    canv.create_line(x_start, y_start, x_end, y_end)
    x_start = False
    y_start = False
    x_end = False
    y_end = False

def lines_check():
    global point_list, cross_list
    y_max = point_list[0][1]
    y_min = point_list[0][1]
    cross_list = []
    for i in range(len(point_list)):
        if (point_list[i][1] > y_max):
            y_max = point_list[i][1]
        elif (point_list[i][1] < y_min):
            y_min = point_list[i][1]
    for i in range(y_max, y_min, -50):
        canv.create_line(0, i, 960, i)
        for j in range(len(point_list) - 1):
            x, y = transection(0, i, 960, i, point_list[j][0], point_list[j][1], point_list[j + 1][0], point_list[j + 1][1])
            x = round(x, 0)
            y = round(y, 0)
            x = int(x)
            y = int(x)
            cross_list.append([x, y])
    print('cross_line: ', cross_list)
        
    #print('a: ', a)

def transection(ax1, ay1, ax2, ay2, bx1, by1, bx2, by2):
    v1 = (bx2 - bx1) * (ay1 - by1) - (by2 - by1) * (ax1 - bx1)
    v2 = (bx2 - bx1) * (ay2 - by1) - (by2 - by1) * (ax2 - bx1)
    v3 = (ax2 - ax1) * (by1 - ay1) - (ay2 - ay1) * (bx1 - ax1)
    v4 = (ax2 - ax1) * (by2 - ay1) - (ay2 - ay1) * (bx2 - ax1)
    if ((v1 * v2 <= 0) and (v3 * v4 <= 0)):
        flag = True
        x, y = cross_line(ax1, ay1, ax2, ay2, bx1, by1, bx2, by2)
        return x, y
    else:
        return -1, -1

def cross_line(x1, y1, x2, y2, x3, y3, x4, y4):
    dx1 = x2 - x1
    dy1 = y2 - y1
    dx2 = x4 - x3
    dy2 = y4 - y3
    x = dy1 * dx2 - dy2 * dx1

    y = x3 * y4 - y3 * x4
    x = ((x1 * y2 - y1 * x2) * dx2 - y * dx1) / x
    y = (dy2 * x - y) / dx2
    #return ((x1 <= x && x2 >= x) || (x2 <= x && x1 >= x)) && ((x3 <= x && x4 >= x) || (x4 <= x && x3 >= x))
    return x, y

if __name__ == '__main__':
    main()

root.mainloop()
