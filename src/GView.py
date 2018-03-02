from PyQt4.QtGui import QGraphicsView
from PyQt4.QtCore import QRectF, Qt


class MyView(QGraphicsView):
    def __init__(self, parent=None):
        super(MyView, self).__init__(parent)

        # Yatay ve düşey kaydırma çubuklarını daima görünmez
        # hale getiriyoruz.
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

    # Mouse topuyla yakınlaştırma ve uzaklaştırma yapabilmek için
    # QGraphicsViewde tanımlı olan wheelEvent'i tekrar tanımlıyoruz.
    def wheelEvent(self, event):
        # zoom_factor değişkenine atanan değeri PyQt4 yüklemesiyle
        # gelen examples/graphicsview/elasticnodes.pyw dosyasında
        # kullanılan değeri seçiyoruz.
        zoom_factor = 2.0 ** (event.delta() / 240.0)

        # yakınlaştırma/uzaklaştırma yaparken daha hassas hareket
        # edebilmek için aşağıdaki fonkiyonları kullanıyoruz.
        # Bu iki satırı kaldırıp aradaki farkı görebilirsiniz.
        self.setTransformationAnchor(QGraphicsView.NoAnchor)
        self.setResizeAnchor(QGraphicsView.NoAnchor)

        # mapToScene fonksiyonu ile mouse'nin QGraphicsScene'deki konumunu
        # old_pos değişkenine atıyoruz.
        old_pos = self.mapToScene(event.pos())

        # factor değişkeninin belirlenmesinde yine examples/graphicsview/elasticnodes.pyw
        # dosyasına bakabilirsiniz.
        factor = self.matrix().scale(zoom_factor, zoom_factor).mapRect(QRectF(0, 0, 1, 1)).width()

        if factor < 0.0007 or factor > 1000:
            return

        self.scale(zoom_factor, zoom_factor)

        # mapToScene fonksiyonu ile mouse'nin yakınlaştırma/uzaklaştırma işlemi
        # sonrasındaki konumu new_pos değişkenine atıyoruz.
        new_pos = self.mapToScene(event.pos())

        # old_pos ve new_pos konumları arasındaki farkı delta değişkenine atıyoruz.
        delta = new_pos - old_pos
        # translate fonksiyonu ile QGraphicsView'i delta değeri kadar öteliyoruz.
        self.translate(delta.x(), delta.y())
