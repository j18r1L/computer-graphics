from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtGui import QPen, QColor, QImage, QPixmap, QPainter
from PyQt5.QtCore import Qt, QTime, QCoreApplication, QEventLoop, QPoint
import time

col_one = Qt.black
col_zero = Qt.white

dotsX = []
dotsY = []
scan_dots = []
mini = []
maxi = []

# с упорядоченным списком ребер

class Window(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        uic.loadUi("window.ui", self)
        self.scene = myScene(0, 0, 561, 581)
        self.scene.win = self
        self.view.setScene(self.scene)
        self.image = QImage(561, 581, QImage.Format_ARGB32_Premultiplied)
        self.image.fill(col_zero)
        self.lock.clicked.connect(lambda: lock(self))
        self.erase.clicked.connect(lambda: clean_all(self))
        self.paint.clicked.connect(lambda: fill_flag(self))
        self.addpoint.clicked.connect(lambda: add_point_by_btn(self))
        self.edges = []
        self.point_now = None
        self.point_lock = None
        self.pen = QPen(col_one)
        self.delay.setChecked(False)


class myScene(QtWidgets.QGraphicsScene):
    def mousePressEvent(self, event):
        add_point(event.scenePos())


def add_row(win):
    win.table.insertRow(win.table.rowCount())


def add_point(point):
    global w
    item_x = QTableWidgetItem("{0}".format(point.x()))
    item_y = QTableWidgetItem("{0}".format(point.y()))
    dotsX.append(int(round(float(item_x.text()))))
    dotsY.append(int(round(float(item_y.text()))))

    if w.point_now is None:
        w.point_now = point
        w.point_lock = point
        add_row(w)
        i = w.table.rowCount() - 1
        item_x = QTableWidgetItem("{0}".format(point.x()))
        item_y = QTableWidgetItem("{0}".format(point.y()))
        w.table.setItem(i, 0, item_x)
        w.table.setItem(i, 1, item_y)
    else:
        w.edges.append([w.point_now.x(), w.point_now.y(),
                        point.x(), point.y()])
        #print([w.point_now.x(), w.point_now.y(),
        #                point.x(), point.y()])
        w.point_now = point
        add_row(w)
        i = w.table.rowCount() - 1
        item_x = QTableWidgetItem("{0}".format(point.x()))
        item_y = QTableWidgetItem("{0}".format(point.y()))
        w.table.setItem(i, 0, item_x)
        w.table.setItem(i, 1, item_y)
        item_x = w.table.item(i-1, 0)
        item_y = w.table.item(i-1, 1)
        w.scene.addLine(point.x(), point.y(), float(item_x.text()), float(item_y.text()), w.pen)
    #print(w.edges)


def lock(win):
    win.edges.append([win.point_now.x(), win.point_now.y(), win.point_lock.x(), win.point_lock.y()])
    win.scene.addLine(win.point_now.x(), win.point_now.y(), win.point_lock.x(), win.point_lock.y(), w.pen)
    win.point_now = None


def fill_extrem(win):
    #print(win.edges[1])
    for i in range(len(win.edges) - 1):
        a = win.edges[i]
        b = win.edges[i + 1]
        if (a[3] > a[1]) and (b[1] > b[3]):
            maxi.append((a[2], a[3]))
        if (a[3] < a[1]) and (b[1] < b[3]):
            mini.append((a[2], a[3]))
    
    a = win.edges[len(win.edges) - 1]
    b = win.edges[0]
    if (a[3] > a[1]) and (b[1] > b[3]):
            maxi.append((a[2], a[3]))
    if (a[3] < a[1]) and (b[1] < b[3]):
            mini.append((a[2], a[3]))



def clean_all(win):
    win.scene.clear()
    win.table.clear()
    dotsY.clear()
    dotsX.clear()
    scan_dots.clear()
    win.edges = []
    win.point_now = None
    win.point_lock = None
    win.image.fill(col_zero)
    r = win.table.rowCount()
    for i in range(r, -1, -1):
        win.table.removeRow(i)


def delay():
    QtWidgets.QApplication.processEvents(QEventLoop.AllEvents, 10)


def FindPoints(win): # rely on DDA
    ymax = max(dotsY)
    ymin = min(dotsY)
    dbl_add = False
    #print(w.edges)
    for i in range(len(win.edges)):
        x1 = int(round(win.edges[i][0]))
        y1 = int(round(win.edges[i][1]))
        x2 = int(round(win.edges[i][2]))
        y2 = int(round(win.edges[i][3]))

        if (y1 == y2):
            continue
        
        if (y1 > y2):
            y1, y2 = y2, y1
            x1, x2 = x2, x1

        if ((x2,y2) in maxi or (x2, y2) in mini):
            scan_dots.append((x2, y2))
            print(x2, y2)
        y = y1 + 1
        dx = (x2 - x1) / (y2 - y1)
        x = x1 + dx * (y - y1)

        while (y <= y2):
            dot = (int(round(x)), y)
            scan_dots.append(dot)
            y += 1
            x += dx
    print(scan_dots)
    print("-----------------------\n")


def DotCmp(dot1, dot2):
    if(dot1[1] > dot2[1]):
        return True

    if(dot1[1] == dot2[1] and dot1[0] <= dot2[0]):
        return True

    return False
    
def fill_flag(win):
    pix = QPixmap()
    p = QPainter()
    p.begin(win.image)
    #p.setPen(QPen(col_one))

    fill_extrem(win)
    FindPoints(win)
    #Sorter()
    #print(scan_dots)

    for i in range(len(scan_dots)):
        for j in range (0, 560):
            if (j > scan_dots[i][0]):
                #p.drawLine(scan_dots[i][0], scan_dots[i][1], scan_dots[i + 1][0], scan_dots[i + 1][1])
                col = QColor(win.image.pixel(j, scan_dots[i][1]))
                if col == col_zero:
                    p.setPen(QPen(col_one))
                else:
                    p.setPen(QPen(col_zero))
                    #p.drawLine(scan_dots[i][0], scan_dots[i][1], 581, scan_dots[i][1])
                p.drawPoint(j, scan_dots[i][1])
        if win.delay.isChecked():
            delay()
            pix.convertFromImage(win.image)
            win.scene.addPixmap(pix)

    if not win.delay.isChecked():
        pix.convertFromImage(win.image)
        win.scene.addPixmap(pix)
    #pix.convertFromImage(win.image)
    #win.scene.addPixmap(pix)
    p.end()  


def add_point_by_btn(win):
    x = win.x.value()
    y = win.y.value()
    p = QPoint()
    p.setX(x)
    p.setY(y)
    add_point(p)



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    w = Window()
    w.show()
    sys.exit(app.exec_())
