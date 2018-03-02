from PyQt4.QtGui import QGraphicsItem, QPolygonF, QPen, QBrush
from PyQt4.QtCore import QPointF, Qt
from math import pi, sin, cos


class PolygonItem(QGraphicsItem):
    def __init__(self, edge_count=3, radius=20):
        super(PolygonItem, self).__init__()
        # edge_count çokgenin kaç kenarı olduğunu
        # radius ise çokgenin herhangi bir köşesinin
        # merkeze olan mesafesini belirliyor.
        # bir önceki görseldeki 'r' değeri
        self.edge_count = edge_count
        self.radius = radius
        self.polygon = self.calculate_polygon_points()

        self._pen = QPen(Qt.black)
        self._brush = QBrush(Qt.NoBrush)

    def set_pen(self, pen):
        if isinstance(pen, QPen):
            self._pen = pen

    def get_pen(self):
        return self._pen

    pen = property(fget=get_pen, fset=set_pen)

    def set_brush(self, brush):
        if isinstance(brush, QBrush):
            self._brush = brush

    def get_brush(self):
        return self._brush

    brush = property(fget=get_brush, fset=set_brush)

    def calculate_angle(self):
        # bir önceki görseldeki θ değerini hesaplıyoruz
        return (2 * pi) / self.edge_count

    def calculate_polygon_points(self):
        # QPolygonF nesnesi oluşturup tüm köşe noktalarının
        # x ve y değerlerini hesaplıyoruz. Sonrasında x,y
        # değerleriyle QPointF nesnesi oluşturup QPolygon'a
        # bu noktaları ekliyoruz.
        p = QPolygonF()
        angle = self.calculate_angle()
        for i in range(self.edge_count):
            x = cos(angle * i) * self.radius
            y = sin(angle * i) * self.radius
            p.append(QPointF(x, y))
        return p

    def boundingRect(self):
        # kendi QGraphicsItem nesnenizi oluşturduğunuzda
        # boundingRect ve paint fonksiyonlarını yeniden
        # tanımlamanız gerekiyor. bu fonksiyonda oluşturacağımız
        # nesnenin sınırlarını gösteren QRectF nesnesini
        # hesaplayıp döndürmemiz gerekiyor.
        return self.polygon.boundingRect()

    def paint(self, painter, option, widget=None):
        # bu fonksiyon ise oluşturduğumuz QGraphicsItem nesnesinin
        # ne çizeceğini belirlediğimiz fonksiyon.

        painter.setPen(self.pen)
        painter.setBrush(self.brush)

        painter.drawPolygon(self.polygon)