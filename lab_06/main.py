from tkinter import *
import math
import time



root = Tk()
root.geometry('1250x700') #960
canv = Canvas(root, width = 1250, height = 700, bg="#ffffff")
canv.pack()


def main():
    global point_list, img, x_start, y_start, lines_check, n, y_pred, edges, exterm, pix_flag, pix, points_array, pix_array
    pix_array = []
    pix_flag = False
    exterm = []
    edges = []
    points_array = []
    n = 0
    x_start = False
    y_start = False
    img = PhotoImage(width = 1250, height = 700)
    canv.create_image((1250//2, 700//2), image=img, state="normal")
    point_list = []
    lines_check = []
    y_pred = -1
    add_line_button()
    route()
    delete_all_button()
    end_button()
    paint_button()
    paint_delay_button()
    add_pixel_button()

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
    global point_list, x_start, y_start, x_end, y_end, n, pix_flag, pix
    if (pix_flag == True):
        pix = []
        x = root.x
        y = root.y
        pix = [x, y]
        print(pix)
        return 1
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
    #CDA(x_start, y_start, x, y)
    x_start = x
    y_start = y

def get_AL(root):
    global add_x, add_y, point_list, x_start, y_start, x_end, y_end, n
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
    #CDA(x_start, y_start, x, y)
    x_start = x
    y_start = y

def delete_all_button():
    button_2 = Button(root, text = u"Удалить все точки")
    button_2.pack()
    button_2.place(x = 980, y = 60, width = 140)
    button_2.bind("<Button-1>", get_DA)

def add_pixel_button():
    button_5 = Button(root, text = u"Добавить точку затравки")
    button_5.pack()
    button_5.place(x = 980, y = 180, width = 140)
    button_5.bind("<Button-1>", get_PIX)

def get_PIX(root):
    global pix_flag
    pix_flag = True

def get_DA(root):
    global point_list, x_start, y_start, x_end, y_end, lines_check, n, edges, exterm
    maxi = []
    mini = []
    edges = []
    exterm = []
    n = 0
    point_list = []
    lines_check = []
    x_end = False
    y_end = False
    y_pred = -1
    x_start = False
    y_start = False
    canv.delete("all")
    delete_img()
    route()

def paint_button():
    button_3 = Button(root, text = u"Закрасить")
    button_3.pack()
    button_3.place(x = 980, y = 120, width = 140)
    button_3.bind("<Button-1>", get_P)

def paint_delay_button():
    button_4 = Button(root, text = u"Закрасить с задержкой")
    button_4.pack()
    button_4.place(x = 980, y = 150, width = 140)
    button_4.bind("<Button-1>", get_PD)

def get_P(root):
    global lines_check, edges, exterm, pix, pix_array
    for i in range(len(edges)):
        for j in range(len(edges[i]) - 1, -1, -1):
            if (j + 1 > len(edges[i]) - 1):
                y0 = edges[i][0][1]
                x0 = edges[i][0][0]
            else:
                y0 = edges[i][j + 1][1]
                x0 = edges[i][j + 1][0]
            fill_exterm(edges[i][j][0], edges[i][j][1], edges[i][j - 1][0], edges[i][j - 1][1], y0)
    for i in range(len(edges)):
        for j in range(len(edges[i]) - 1, -1, -1):
            x1 = edges[i][j][0]
            y1 = edges[i][j][1]
            x2 = edges[i][j - 1][0]
            y2 = edges[i][j - 1][1]
            if (j + 1 > len(edges[i]) - 1):
                y0 = edges[i][0][1]
                x0 = edges[i][0][0]
            else:
                y0 = edges[i][j + 1][1]
                x0 = edges[i][j + 1][0]
            CDA(x1, y1, x2, y2, y0)
    flag_end = False
    pix_array.append(pix)
    while (flag_end == False):
        x_s, x_e = full()
        find_end(x_s, x_e)
        if (pix_array == []):
            flag_end = True

def find_end(x_s, x_e):
    global lines_check, points_array, pix_array
    if (x_s == -1) or (x_e == -1):
        return -1
    for i in range(x_e[0], x_s[0], -1):
        #print("1: ", x_e[0], x_s[0])
        point = [i, x_s[1] + 1]

        if (point not in points_array) and (point not in lines_check) and (point[0] > x_s[0]) and (point[0] < x_e[0]):
            #print("kaka")
            pix = point
            pix_array.append(pix)
            break
    for i in range(x_e[0], x_s[0], -1):
        #print("2: ", x_e[0], x_s[0])
        point = [i, x_s[1] - 1]
        if (point not in points_array) and (point not in lines_check) and (point[0] > x_s[0]) and (point[0] < x_e[0]):
            #print("Yatyt")
            pix = point
            pix_array.append(pix)
            break
            
    #print(pix_array)

def full():
    global lines_check, points_array, pix_array
    pix = pix_array[0]
    pix_array.pop(0)
    #print(pix_array)
    flag = False
    point = pix
    i1 = 0
    x_s = -1
    x_e = -1
    for i in range(0, 700):
        if (flag == False):
            points_array.append(point)
            if (point in lines_check):
                canv.create_line(pix[0], pix[1], point[0], point[1])
                x_s = point
                point = pix
                i1 = 0
                flag = True
            point = [pix[0] - i1, pix[1]]
            i1 += 1
        else:
            if (point in lines_check):
                canv.create_line(pix[0], pix[1], point[0], point[1])
                x_e = point
                point = pix
                break
            point = [pix[0] + i1, pix[1]]
            points_array.append(point)
            i1 += 1
    return x_s, x_e


def get_PD(root):
    global lines_check, img
    lines_check = sort()
    for i in range(len(lines_check)):
        for j in range(0, len(lines_check[i]) - 1, 2):
            for k in range(lines_check[i][j][0], lines_check[i][j + 1][0]):

                start = lines_check[i][j][0]
                end = lines_check[i][j + 1][0]
                if (k > start and k < end):
                    canv.after(100, lambda: canv.create_image((1250//2, 700//2), image=img, state="normal"))
                    img.put("black", (k, lines_check[i][j][1]))
                    root.update()

def sort():
    global lines_check
    array = []
    lines_sort = []
    #Создание трехмерного массива точек
    for i in range(len(lines_check) - 1):
        if (lines_check[i][1] == lines_check[i + 1][1]):
            array.append(lines_check[i])
        else: 
            array.append(lines_check[i])
            lines_sort.append(array)
            array = []

    return lines_sort

def fill_exterm(x1, y1, x2, y2, y0):
    global exterm
    if (y0 < y1 and y2 < y1) or (y0 > y1 and y2 > y1):
        exterm.append([x1, y1])

def CDA(x1, y1, x2, y2, y0): # rely on DDA
    global lines_check, exterm
    if (y1 == y2):
        return -1
    if (y1 > y2):
        y1, y2 = y2, y1
        x1, x2 = x2, x1

    point = [x2, y2]
    if (point in exterm):
            lines_check.append([x2, y2])
        
    y = y1 + 1
    dx = (x2 - x1) / (y2 - y1)
    x = x1 + dx * (y - y1)

    while (y <= y2):
        lines_check.append([int(round(x)), y])
        y += 1
        x += dx 

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
    global x_start, y_start, x_end, y_end, point_list
    canv.create_line(x_start, y_start, x_end, y_end)
    #CDA(x_start, y_start, x_end, y_end)
    edges.append(point_list)
    point_list = []
    x_start = False
    y_start = False
    x_end = False
    y_end = False

if __name__ == '__main__':
    main()

root.mainloop()

