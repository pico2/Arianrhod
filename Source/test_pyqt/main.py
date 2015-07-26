from mlqt import *
from Docker import *

class MainWindow(DockerContainer):
    def __init__(self):
        super().__init__()

        for dockName in 'First Second Third Fourth'.split():
            docker = self.mgr.createDocker(dockName)
            docker.setWidget(QListWidget())
            docker.setTitleBarVisible(False)

            # self.addDockWidget(Qt.TopDockWidgetArea, docker)
            self.tab.addTab(docker, dockName)

def main():
    app = QApplication(sys.argv)

    wnd = MainWindow()

    wnd.show()
    return app.exec_()

if __name__ == '__main__':
    TryInvoke(main)
