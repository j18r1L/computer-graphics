from tkinter import *
from math import *
#x_k_zoom = 1/x_k_zoom

def grapth(figures):
    
    #Функция зумирования
    def zoom(figures, x_k_zoom, point_list1, point_list2, point_list3, point_list4, point_list5, y_k_zoom):
        global flag_zoom, flag_move, flag_rotate, angle_rotate, x_c_z, y_c_z
        #Зумируем овалы
        def zoom_ovals(point_list, x_c_z, y_c_z):
            for i in range (0, len(point_list), 2):
                point_list[i] = x_k_zoom * point_list[i] + (1 - x_k_zoom) * x_c_z
                point_list[i + 1] = y_k_zoom * point_list[i + 1] + (1 - y_k_zoom) * y_c_z
            return point_list
    
        flag_zoom = True 
        flag_move = False
        flag_rotate = False
        #Зумируем фигуру
        for i in range(len(figures)):
            figures[i][0] = x_k_zoom * figures[i][0] + (1 - x_k_zoom) * x_c_z
            figures[i][1] = y_k_zoom * figures[i][1] + (1 - y_k_zoom) * y_c_z
            figures[i][2] = x_k_zoom * figures[i][2] + (1 - x_k_zoom) * x_c_z
            figures[i][3] = y_k_zoom * figures[i][3] + (1 - y_k_zoom) * y_c_z
    
        point_list1 = zoom_ovals(point_list1, x_c_z, y_c_z)
        point_list2 = zoom_ovals(point_list2, x_c_z, y_c_z)
        point_list3 = zoom_ovals(point_list3, x_c_z, y_c_z)
        point_list4 = zoom_ovals(point_list4, x_c_z, y_c_z)
        point_list5 = zoom_ovals(point_list5, x_c_z, y_c_z)
        #Создаем новый лист
        canv.delete("all")
        lines_ovals(figures, point_list1, point_list2, point_list3, point_list4, point_list5)
        route()
        root.update()

    #Вызываем кнопкой функцию зумирования
    def get_Z(root):
        global x_k_zoom, y_c_z, x_c_z, y_k_zoom
        x_k_zoom = scale_zoom_xz.get()
        x_k_zoom = float(x_k_zoom)
        y_k_zoom = scale_zoom_yz.get()
        y_k_zoom = float(y_k_zoom)
        x_c_z = scale_zoom_x.get()
        x_c_z = float(x_c_z)
        y_c_z = scale_zoom_y.get()
        y_c_z = float(y_c_z)
        
        zoom(figures, x_k_zoom, point_list1, point_list2, point_list3, point_list4, point_list5, y_k_zoom)
    
    #Функция шага назад
    def back(figures, x_k_zoom, point_list1, point_list2, point_list3, point_list4, x_c, y_c, x_c_z, y_c_z, point_list5, y_k_zoom):
        global flag_zoom, x_move, y_move, flag_move, angle_rotate, flag_rotate
        
        ##Модуль шага назад при зумировании
        #Шаг назад овалов
        x_k_zoom = 1.0 / x_k_zoom
        y_k_zoom = 1.0 / y_k_zoom
        def bacx_k_zoom_ovals(point_list, x_c_z, y_c_z):
            for i in range (0, len(point_list), 2):
                point_list[i] = x_k_zoom * point_list[i] + (1 - x_k_zoom) * x_c_z
                point_list[i + 1] = y_k_zoom * point_list[i + 1] + (1 - y_k_zoom) * y_c_z
            return point_list
        #Шаг назад фигуры
        if flag_zoom == True:
            for i in range(len(figures)):
                figures[i][0] = x_k_zoom * figures[i][0] + (1 - x_k_zoom) * x_c_z
                figures[i][1] = y_k_zoom * figures[i][1] + (1 - y_k_zoom) * y_c_z
                figures[i][2] = x_k_zoom * figures[i][2] + (1 - x_k_zoom) * x_c_z
                figures[i][3] = y_k_zoom * figures[i][3] + (1 - y_k_zoom) * y_c_z
        
            point_list1 = bacx_k_zoom_ovals(point_list1, x_c_z, y_c_z)
            point_list2 = bacx_k_zoom_ovals(point_list2, x_c_z, y_c_z)
            point_list3 = bacx_k_zoom_ovals(point_list3, x_c_z, y_c_z)
            point_list4 = bacx_k_zoom_ovals(point_list4, x_c_z, y_c_z)
            point_list5 = bacx_k_zoom_ovals(point_list5, x_c_z, y_c_z)
            flag_zoom = False
        ##Модуль шага назад при перемещении
        if flag_move == True:
            move(figures, -x_move, -y_move, point_list1, point_list2, point_list3, point_list4,point_list5)
            flag_move = False
        ##Модуль шага назад при повороте
        if flag_rotate == True:
            rotate(figures, -angle_rotate, x_c, y_c, point_list1, point_list2, point_list3, point_list4,point_list5)
            flag_rotate = False
        ##Пересоздаем лист
        canv.delete("all")
        lines_ovals(figures, point_list1, point_list2, point_list3, point_list4, point_list5)
        route()
        root.update()
    #Вызываем кнопкой функцию шага назад
    def get_B(root):
        global x_k_zoom, y_k_zoom
        back(figures, x_k_zoom, point_list1, point_list2, point_list3, point_list4, x_c, y_c, x_c_z, y_c_z, point_list5, y_k_zoom)

    #Функция перемещения
    def move(figures, x, y, point_list1, point_list2, point_list3, point_list4, point_list5):
        global flag_move, flag_zoom, flag_rotate, angle_rotate
        #перемещение овалов
        def move_ovals(point_list):
            for i in range (0, len(point_list), 2):
                point_list[i] += x
                point_list[i + 1] += y
            return point_list
        
        flag_move = True
        flag_zoom = False
        flag_rotate = False
        #Перемещение фугуры
        for i in range(len(figures)):
            for j in range(1, 4, 2):
                figures[i][j] = figures[i][j] + y
            for j in range(0, 4, 2):
                figures[i][j] = figures[i][j] + x
    
        point_list1 = move_ovals(point_list1)
        point_list2 = move_ovals(point_list2)
        point_list3 = move_ovals(point_list3)
        point_list4 = move_ovals(point_list4)
        point_list5 = move_ovals(point_list5)
        
        
        #Пересоздаем лист
        canv.delete("all")
        lines_ovals(figures, point_list1, point_list2, point_list3, point_list4, point_list5)
        route()
        root.update()
            
    #Вызываем кнопкой функцию перемещения
    def get_M(root):
        global x_move, y_move
        x_move = scale_move_x.get()
        y_move = scale_move_y.get()
        x_move = int(x_move)
        y_move = int(y_move)
        move(figures, x_move, y_move, point_list1, point_list2, point_list3, point_list4, point_list5)

    #Функция вращения
    def rotate(figures, angle_rotate, x_c, y_c, point_list1, point_list2, point_list3, point_list4, point_list5):
        global flag_move, flag_zoom, flag_rotate
        #Вращаем овалы
        def rotate_ovals(point_list):
            for i in range(0, len(point_list), 2):
                x_1 = x_c + (point_list[i] - x_c) * cos(angle_rotate) + (point_list[i + 1] - y_c) * sin(angle_rotate)
                y_1  = y_c - (point_list[i] - x_c) * sin(angle_rotate) + (point_list[i + 1] - y_c) * cos(angle_rotate)
                point_list[i] = x_1
                point_list[i + 1] = y_1

            return point_list
        
        flag_rotate = True
        flag_move = False
        flag_zoom = False
        #Вращаем фигуру
        for i in range(4 ,len(figures)):
            #x_1 = x_c + (x - x_c) * cos(angle_rotate) + (y - y_c) * sin(angle_rotate)
            #y_1 = y_c - (x - x_c) * sin(angle_rotate) + (y - y_c) * cos(angle_rotate)
            #x = x_1
            #y = y_1
            x_1  = x_c + (figures[i][0] - x_c) * cos(angle_rotate) + (figures[i][1] - y_c) * sin(angle_rotate)
            y_1  = y_c - (figures[i][0] - x_c) * sin(angle_rotate) + (figures[i][1] - y_c) * cos(angle_rotate)
            x_2  = x_c + (figures[i][2] - x_c) * cos(angle_rotate) + (figures[i][3] - y_c) * sin(angle_rotate)
            y_2  = y_c - (figures[i][2] - x_c) * sin(angle_rotate) + (figures[i][3] - y_c) * cos(angle_rotate)
            figures[i][0] = x_1
            figures[i][1] = y_1
            figures[i][2] = x_2
            figures[i][3] = y_2


        point_list1 = rotate_ovals(point_list1)
        point_list2 = rotate_ovals(point_list2)
        point_list3 = rotate_ovals(point_list3)
        point_list4 = rotate_ovals(point_list4)
        point_list5 = rotate_ovals(point_list5)

        canv.delete("all")
        lines_ovals(figures, point_list1, point_list2, point_list3, point_list4, point_list5)
        route()
        root.update()
    
    #Вызываем кнопкой функцию вращения
    def get_R(root):
        global angle_rotate, x_c, y_c
        angle_rotate = scale_rotate.get()
        angle_rotate = float(angle_rotate)
        x_c = scale_rotate_x.get()
        x_c = float(x_c)
        y_c = scale_rotate_y.get()
        y_c = float(y_c)
        angle_rotate = angle_rotate * pi / 180.0
        rotate(figures, angle_rotate, x_c, y_c, point_list1, point_list2, point_list3, point_list4, point_list5)

    #Создание системы координат
    def route():
        canv.create_line(480, 0, 480, 700, width = 1, fill = 'red', arrow = LAST)
        canv.create_line(0, 350, 960, 350, width = 1, fill = 'red', arrow = LAST)
        for i in range (480, 960, 100):
            canv.create_text(i, 360, text = i)
            canv.create_oval(i - 1, 349, i + 1, 351, width = 2)
        for i in range (480, 0, -100):
            canv.create_text(i, 360, text = i)
            canv.create_oval(i - 1, 349, i + 1, 351, width = 2)
        for i in range (350, 700, 100):
            canv.create_text(495, i, text = i)
            canv.create_oval(479, i - 1, 481, i + 1, width = 2)
        for i in range (350, 0, -100):
            canv.create_text(495, i, text = i)
            canv.create_oval(479, i - 1, 481, i + 1, width = 2)

    #Создание овала точками
    def poly_oval(x0,y0, x1,y1, steps=20, rotation=0):
        rotation = rotation * pi / 180.0
        a = (x1 - x0) / 2.0
        b = (y1 - y0) / 2.0
        xc = x0 + a
        yc = y0 + b
        point_list = []
        for i in range(steps):
            theta = (pi * 2) * (float(i) / steps)
            x1 = a * cos(theta)
            y1 = b * sin(theta)
            x = (x1 * cos(rotation)) + (y1 * sin(rotation))
            y = (y1 * cos(rotation)) - (x1 * sin(rotation))
            point_list.append(round(x + xc))
            point_list.append(round(y + yc))
        return point_list

    #Создание фигуры
    def lines_ovals(figures, point_list1, point_list2, point_list3, point_list4 ,point_list5):
        canv.create_polygon((point_list1), fill = 'white', outline = 'black', smooth = 'true')
        canv.create_polygon((point_list2), fill = 'white', outline = 'black', smooth = 'true')
        canv.create_polygon((point_list3), fill = 'white', outline = 'black', smooth = 'true')
        canv.create_polygon((point_list4), fill = 'white', outline = 'black', smooth = 'true')
        canv.create_line(figures[4][0], figures[4][1], figures[4][2], figures[4][3])
        canv.create_line(figures[5][0], figures[5][1], figures[5][2], figures[5][3])
        canv.create_line(figures[6][0], figures[6][1], figures[6][2], figures[6][3])
        canv.create_line(figures[7][0], figures[7][1], figures[7][2], figures[7][3])
        canv.create_line(figures[8][0], figures[8][1], figures[8][2], figures[8][3])
        canv.create_line(figures[9][0], figures[9][1], figures[9][2], figures[9][3])
        canv.create_line(figures[10][0], figures[10][1], figures[10][2], figures[10][3])
        canv.create_line(figures[11][0], figures[11][1], figures[11][2], figures[11][3])
        canv.create_line(figures[12][0], figures[12][1], figures[12][2], figures[12][3])
        canv.create_line(figures[13][0], figures[13][1], figures[13][2], figures[13][3])
        canv.create_line(figures[14][0], figures[14][1], figures[14][2], figures[14][3])
        canv.create_line(figures[15][0], figures[15][1], figures[15][2], figures[15][3])
        canv.create_polygon((point_list5), fill = 'white', outline = 'black', smooth = 'true')

    def diagonal(x, y, x_c, y_c, angle, steps):
    	points = []
    	angle = angle * pi / 180.0
    	for i in range(steps):
    		x_1 = x_c + (x - x_c) * cos(angle) + (y - y_c) * sin(angle)
    		y_1 = y_c - (x - x_c) * sin(angle) + (y - y_c) * cos(angle)
    		x = x_1
    		y = y_1
    		points.append(x)
    		points.append(y)
    	return points


    #Объявление переменных
    def start():
        global x_move, y_move, flag_move, x_k_zoom, flag_zoom, flag_rotate, angle_rotate, point_list1, x_c, y_c, x_c_z, y_c_z, y_k_zoom
        x_move = 0           #Перемещение по x
        y_move = 0           #Перемещение по y
        flag_move = False    #Флаг наличия передвижения
        flag_rotate = False  #Флаг наличия вращения
        x_k_zoom = 1           #Коэффициент зумирования
        y_k_zoom = 1
        angle_rotate = 0     #Угол вращения
        flag_zoom = False    #Флаг наличия зумирования
        x_c = 0              #Центр при вращении по x
        y_c = 0              #Центр при вращении по y
        x_c_z = 0            #Центр при зумировании по x
        y_c_z = 0            #ЦЕнтр при зумировании по y
    
    
    #Создаем лист
    root = Tk()
    root.geometry('960x700') #960
    canv = Canvas(bg='white')
    canv.pack(fill = BOTH, expand = 1)
    ##Создание фигуры
    #Создание тела
    figures.append([555, 600, 405, 350])
    figures.append([555, 350, 405, 200])
    #Создание глаз
    figures.append([500, 250, 525, 275])
    figures.append([435, 250, 460, 275])   
    #Создание усов
    figures.append([480, 250, 455, 150])
    figures.append([480, 250, 505, 150])
    figures.append([455, 150, 430, 150])
    figures.append([505, 150, 530, 150])
    #Создание ног
    figures.append([505, 592, 505, 625])
    figures.append([455, 592, 455, 625])
    figures.append([505, 625, 555, 625])
    figures.append([455, 625, 405, 625])
    #Создание рук
    figures.append([530, 425, 605, 350])
    figures.append([605, 350, 530, 475])
    figures.append([430, 425, 355, 350])
    figures.append([355, 350, 430, 475])
    #Создание улыбки

    #Объявление переменных
    start()
    #Создание массивов точек овалов
    point_list1 = poly_oval(figures[0][0],figures[0][1], figures[0][2], figures[0][3], 400, rotation = 0)
    point_list2 = poly_oval(figures[1][0],figures[1][1], figures[1][2], figures[1][3], 400, rotation = 0)
    point_list3 = poly_oval(figures[2][0],figures[2][1], figures[2][2], figures[2][3], 400, rotation = 0)
    point_list4 = poly_oval(figures[3][0],figures[3][1], figures[3][2], figures[3][3], 400, rotation = 0)
    point_list5 = diagonal(460, 300, 480, 300, 1, 180)
    lines_ovals(figures, point_list1, point_list2, point_list3, point_list4, point_list5)

    #Вызов функции создания системы координат
    route()
    ##Создаем кнопки меню
    #Кнопка масштабирования
    canv.create_text(20, 56, text = 'x: ')
    scale_zoom_x = Entry(root)
    scale_zoom_x.pack()
    scale_zoom_x.place(x = 30, y = 43, width = 50)
    
    canv.create_text(95, 56, text = 'y: ')
    scale_zoom_y = Entry(root)
    scale_zoom_y.pack()
    scale_zoom_y.place(x = 100, y = 43, width = 50)

    canv.create_text(165, 56, text = 'k_x: ')
    scale_zoom_xz = Entry(root)
    scale_zoom_xz.pack()
    scale_zoom_xz.place(x = 175, y = 43, width = 50)
    
    canv.create_text(240, 56, text = 'k_y: ')
    scale_zoom_yz = Entry(root)
    scale_zoom_yz.pack()
    scale_zoom_yz.place(x = 250, y = 43, width = 50)

    button_1 = Button(root,text=u"Масштабировать изображение")
    button_1.pack()
    button_1.place(x = 10, y = 10,width = 230)
    button_1.bind("<Button-1>", get_Z)

    

    #Кнопка поворота
    canv.create_text(20, 112, text = 'x: ')
    scale_rotate_x = Entry(root)
    scale_rotate_x.pack()
    scale_rotate_x.place(x = 30, y = 100, width = 50)
    
    canv.create_text(95, 112, text = 'y: ')
    scale_rotate_y = Entry(root)
    scale_rotate_y.pack()
    scale_rotate_y.place(x = 100, y = 100, width = 50)

    canv.create_text(165, 112, text = 'k: ')
    scale_rotate = Entry(root)
    scale_rotate.pack()
    scale_rotate.place(x = 170, y = 100, width = 50)
    
    button_3 = Button(root,text=u"Повернуть изображение")
    button_3.pack()
    button_3.place(x = 10, y = 70,width = 200)
    button_3.bind("<Button-1>", get_R)

    #Кнопка переноса
    canv.create_text(20, 173, text = 'x: ')
    scale_move_x = Entry(root)
    scale_move_x.pack()
    scale_move_x.place(x = 30, y = 160, width = 50)
    
    canv.create_text(95, 173, text = 'y: ')
    scale_move_y = Entry(root)
    scale_move_y.pack()
    scale_move_y.place(x = 100, y = 160, width = 50)
    
    button_4 = Button(root,text=u"Передвинуть изображение")
    button_4.pack()
    button_4.place(x = 10, y = 130,width = 200)
    button_4.bind("<Button-1>", get_M)

    #Кнопка шага назад
    button_2 = Button(root,text=u"Шаг назад")
    button_2.pack()
    button_2.place(x = 10, y = 190,width = 100)
    button_2.bind("<Button-1>", get_B)

    Button(root, text = 'Выход', command = exit).place(x = 10, y = 220, width = 70)

    root.mainloop()
    return figures

def main():
    figures = []
    grapth(figures)
    
    
    
if __name__ == '__main__':
    main()



