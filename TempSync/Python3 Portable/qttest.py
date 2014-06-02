from mlqt import *

class QuitButton(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Quit button')

        quit = QtWidgets.QPushButton('Close', self)
        quit.setGeometry(10, 10, 64, 35)

        quit.clicked.connect(self.fuck)
        quit.clicked.connect(self.fuck2)

        self.centerOnScreen()

    def fuck(self):
        print('fuck')
        #self.close()

    def fuck2(self):
        print('fuck2')
        self.close()

    def centerOnScreen (self):
        resolution = QtWidgets.QDesktopWidget().screenGeometry()
        self.move((resolution.width() / 2) - (self.frameSize().width() / 2),
                  (resolution.height() / 2) - (self.frameSize().height() / 2))


class TableWidgetItem(QTableWidgetItem):
    def __init__(self, *args, **kwarg):
        super().__init__(*args, **kwarg)

    def paintEvent(self, event):
        super().paintEvent(event)

        paint = QPainter(self)
        paint.setPen(Qt.blue)
        paint.drawText(rect(), Qt.AlignCenter, "The Text")

        print('fuck')

class FuckStyle(QStyle):
    def __init__(self, *args, **kwarg):
        super().__init__(*args, **kwarg)

    def drawPrimitive(self, element, option, painter, widget):
        super().drawPrimitive(element, option, painter, widget)

class TableView(QTableWidget):
    class NoFocusDelegate(QStyledItemDelegate):
        def __init__(self, *args, **kwarg):
            super().__init__(*args, **kwarg)

        def paint(self, painter, option, index):
            option.state &= ~QStyle.State_HasFocus
            return super().paint(painter, option, index)

    def __init__(self, *args, **kwarg):
        super().__init__(*args, **kwarg)

        self.setFrameShape(QFrame.NoFrame)
        self.setShowGrid(False)
        self.setColumnCount(3)
        self.setHorizontalHeaderLabels(('Address', 'Disassemble', 'Comment'))

        self.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.setStyleSheet("selection-background-color:lightblue;")
        self.setWordWrap(False)
        # self.setFocusPolicy(Qt.NoFocus)
        self.setItemDelegate(self.NoFocusDelegate())

        hheader = self.horizontalHeader()
        vheader = self.verticalHeader()

        # font = hheader.font()
        # font.setBold(True)
        # hheader.setFont(font)

        hheader.setDefaultSectionSize(150)
        hheader.setSectionsClickable(False)

        hheader.setStretchLastSection(True)
        hheader.setFixedHeight(25)
        hheader.resizeSection(0,150)
        hheader.setStyleSheet("QHeaderView::section{background:gray;}")
        hheader.setStyleSheet('''
            QScrollBar{background:transparent; height:10px;}
            QScrollBar::handle{background:lightgray; border:2px solid transparent; border-radius:5px;}
            QScrollBar::handle:hover{background:gray;}
            QScrollBar::sub-line{background:transparent;}
            QScrollBar::add-line{background:transparent;}'''
        )

        vheader.setSectionResizeMode(QHeaderView.ResizeToContents)
        vheader.setDefaultSectionSize(10)
        vheader.setVisible(False)

        vheader.setStyleSheet('''
            QScrollBar{background:transparent; width: 10px;}"
            QScrollBar::handle{background:lightgray; border:2px solid transparent; border-radius:5px;}
            QScrollBar::handle:hover{background:gray;}
            QScrollBar::sub-line{background:transparent;}
            QScrollBar::add-line{background:transparent;}'''
        )

        self.addLine(0x5DBA49A0, 'mov     eax, dword ptr [esp+0x8]')
        self.addLine(0x5DBA49A4, 'sub     eax, 0x0')
        self.addLine(0x5DBA49A7, 'je      short 5DBA49C5')

        self.resizeColumnsToContents()

    def addLine(self, addr, asm):
        addr = TableWidgetItem('%08X' % addr)
        asm = TableWidgetItem(asm)

        row = self.rowCount()
        self.insertRow(row)
        self.setItem(row, 0, addr)
        self.setItem(row, 1, asm)

def main():
    app = QApplication(sys.argv)

    qb = TableView()
    qb.resize(800, 600)
    qb.show()

    return app.exec_()

if __name__ == '__main__':
    TryInvoke(main)
