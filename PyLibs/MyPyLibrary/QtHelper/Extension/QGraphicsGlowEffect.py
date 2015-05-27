from .QCommon import *

class QGraphicsGlowEffect(QGraphicsEffect):
    def __init__(self, *, extent = 1, strength = 2, blurRadius = 3.5, color = QColor(38, 41, 44)):
        super().__init__()

        self._extent     = extent
        self._strength   = strength
        self._blurRadius = blurRadius
        self._color      = color
        self._opacity    = 0.0

    @pyqtProperty(int)
    def extent(self):
        return self._extent

    @extent.setter
    def extent(self, extent):
        self._extent = extent
        self.update()

    @pyqtProperty(float)
    def opacity(self):
        return self._opacity

    @opacity.setter
    def opacity(self, opacity):
        self._opacity = opacity
        self.update()

    @pyqtProperty(int)
    def color(self):
        return self._color

    @color.setter
    def color(self, color):
        self._color = color
        self.update()

    @pyqtProperty(int)
    def strength(self):
        return self._strength

    @strength.setter
    def strength(self, strength):
        self._strength = strength
        self.update()

    @pyqtProperty(float)
    def blurRadius(self):
        return self._blurRadius

    @blurRadius.setter
    def blurRadius(self, blurRadius):
        self._blurRadius = blurRadius
        self.update()

    def boundingRectFor(self, rect):
        return QRectF(
                    rect.left() - self.extent,
                    rect.top() - self.extent,
                    rect.width() + 2 * self.extent,
                    rect.height() + 2 * self.extent
                )

    def sourceChanged(self, flags):
        # self.update()
        pass

    def draw(self, painter):
        source, offset = self.sourcePixmap(Qt.LogicalCoordinates)

        colorize = QGraphicsColorizeEffect()
        colorize.setColor(self._color)
        colorize.setStrength(1)
        glow = self.applyEffectToPixmap(source, colorize, 0)

        blurEffect = QGraphicsBlurEffect()
        blurEffect.setBlurRadius(self._blurRadius)
        glow = self.applyEffectToPixmap(glow, blurEffect, self._extent)

        opacityEffect = QGraphicsOpacityEffect()
        opacityEffect.setOpacity(self._opacity)
        glow = self.applyEffectToPixmap(glow, opacityEffect, self._extent)

        for _ in range(self.strength):
            painter.drawPixmap(offset - QPoint(self._extent, self._extent), glow)

        self.drawSource(painter)

    @classmethod
    def applyEffectToPixmap(cls, src, effect, extent = 0):
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
