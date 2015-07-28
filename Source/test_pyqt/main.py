from mlqt import *
from Docker import *

class MainWindow(DockerContainer):
    def __init__(self):
        super().__init__()

        for dockName in 'First Second Third Fourth Fifth'.split():
            docker = self.createDocker(dockName)
            docker.setWidget(QListWidget())

            self.addDockWidget(Qt.TopDockWidgetArea, docker)

def main():
    app = QApplication(sys.argv)

    wnd = MainWindow()

    wnd.show()
    return app.exec_()

if __name__ == '__main__':
    TryInvoke(main)
