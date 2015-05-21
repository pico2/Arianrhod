from .QCommon import *

class QGraphicsGlowEffect(QGraphicsEffect):
    def __init__(self, *, extent = 1, strength = 2, blurRadius = 3.5, color = QColor(38, 41, 44)):
        super().__init__()

        self.extent = extent
        self.strength = strength
        self.blurRadius = blurRadius
        self.color = color

    def setColor(self, color):
        self.color = color

    def setStrength(self, strength):
        self.strength = strength

    def setBlurRadius(self, blurRadius):
        self.blurRadius = blurRadius

    def boundingRectFor(self, rect):
        return QRectF(
                    rect.left() - self.extent,
                    rect.top() - self.extent,
                    rect.width() + 2 * self.extent,
                    rect.height() + 2 * self.extent
                )

    def draw(self, painter):
        source, offset = self.sourcePixmap(Qt.LogicalCoordinates)

        colorize = QGraphicsColorizeEffect()
        colorize.setColor(self.color)
        colorize.setStrength(1)
        glow = self.applyEffectToPixmap(source, colorize, 0)

        blur = QGraphicsBlurEffect()
        blur.setBlurRadius(self.blurRadius)
        glow = self.applyEffectToPixmap(glow, blur, self.extent)

        for _ in range(self.strength):
            painter.drawPixmap(offset - QPoint(self.extent, self.extent), glow)

        self.drawSource(painter)

    @classmethod
    def applyEffectToPixmap(cls, src, effect, extent):
        if src.isNull():
            return QPixmap()

        if not effect:
            return src

        scene = QGraphicsScene()

        item = QGraphicsPixmapItem()
        item.setPixmap(src)
        item.setGraphicsEffect(effect)

        scene.addItem(item)

        size = src.size() + QSize(extent * 2, extent * 2)
        res = QPixmap(size.width(), size.height())

        res.fill(Qt.transparent)

        painter = QPainter(res)
        scene.render(painter, QRectF(), QRectF(-extent, -extent, size.width(), size.height()))

        return res
