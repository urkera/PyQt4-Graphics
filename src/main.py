from PyQt4.QtCore import *
from PyQt4.QtGui import *
from src.form import Ui_MainWindow
from src.items import PolygonItem

import sys


class Window(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.setupUi(self)

        # üzerinde oluşturduğumuz nesneleri göstereceğim QGraphicsScene'yi
        # scene değişkenine atıyor ve graphicsView'e çizim için bu
        # scene'yi kullanacağımız belirtiyoruz (setScene)
        self.scene = QGraphicsScene()
        self.graphicsView.setScene(self.scene)

        # ucgen isimli bir PolygonItem oluşturuyoruz ve bunun scene'deki
        # konumunu 50, 50 olarak tanımlıyoruz.

        red_pen = QPen(QColor(255, 0, 0))
        red_pen.setWidth(2)

        blue_pen = QPen(QColor(0, 0, 255))
        blue_pen.setWidth(3)

        red_brush = QBrush(QColor(255, 0, 0))
        blue_brush = QBrush(QColor(0, 0, 255))

        ucgen = PolygonItem(edge_count=3, radius=30)

        ucgen.pen = red_pen
        ucgen.brush = red_brush

        ucgen.setPos(QPointF(50, 50))
        self.scene.addItem(ucgen)

        # aynı şekilde istediğimiz kenar sayısına sahip çokgen oluşturup
        # ekleyebiliriz. bir tane de beşgen ekleyelim.

        besgen = PolygonItem(edge_count=5, radius=25)

        besgen.pen = blue_pen
        besgen.brush = blue_brush

        besgen.setPos(QPointF(0, 0))
        self.scene.addItem(besgen)


def main():
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
