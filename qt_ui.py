import sys
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import *
from process import search


class ui(QWidget):
    def __init__(self):
        super().__init__()
        self.path_pic = None
        self.text = None
        self.path_word = None
        self.submit = None
        self.pic_path = None
        self.doc_path = None
        self.btnPic = None
        self.btnWord = None
        self.initUI()

    def initUI(self):
        # 新建表格布局
        grid = QGridLayout()
        grid.setSpacing(50)
        # 新建标题
        title = QLabel("欢迎使用A文档搜图")
        grid.addWidget(title, 0, 1, 1, 2)
        # 新建按钮
        self.btnWord = QPushButton('选择 Word 文件', self)
        self.btnWord.setToolTip("Import your word here.")

        self.btnPic = QPushButton('选择要搜索的图片', self)
        self.btnPic.setToolTip("Import your pic here.")
        # 新建路径便签
        self.doc_path = QLabel("请选择文件")
        self.pic_path = QLabel("请选择文件")

        self.submit = QPushButton('开始检索', self)
        grid.addWidget(self.btnWord, 1, 0, 1, 1)
        grid.addWidget(self.btnPic, 2, 0, 1, 1)
        grid.addWidget(self.doc_path, 1, 1, 1, 3)
        grid.addWidget(self.pic_path, 2, 1, 1, 3)
        grid.addWidget(self.submit, 3, 1, 1, 2)

        self.submit.clicked.connect(self.process)
        self.btnWord.clicked.connect(self.get_word)
        self.btnPic.clicked.connect(self.get_pic)
        self.setLayout(grid)
        self.resize(500, 200)
        self.setWindowTitle('欢迎使用 A 文档搜图')
        self.setImage()
        self.center()
        self.show()

    def setImage(self):
        bg = QtGui.QImage()
        bg.load(r'./图片1.jpeg')
        pa = QtGui.QPalette()
        pa.setBrush(self.backgroundRole(), QtGui.QBrush(bg))
        self.setPalette(pa)
        self.setAutoFillBackground(True)

    def closeEvent(self, event):
        reply = QMessageBox.question(self, '退出', "确认退出吗？", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def get_word(self):
        self.path_word = str(QtWidgets.QFileDialog.getOpenFileUrl(self, "选择文件")[0]).split("'")[-2][7:]
        print(self.path_word)
        self.doc_path.setText(self.path_word)

    def get_pic(self):
        self.path_pic = str(QtWidgets.QFileDialog.getOpenFileUrl(self, "选择文件")[0]).split("'")[-2][7:]
        self.pic_path.setText(self.path_pic)

    def process(self):
        self.text = "已搜索到结果，该图片上下文为：\n"
        self.text += search(self.path_word, self.path_pic)
        QMessageBox.question(self, '结果', self.text, QMessageBox.Yes, QMessageBox.Yes)

    def center(self):
        # 获得窗口
        qr = self.frameGeometry()
        # 获得屏幕中心点
        cp = QDesktopWidget().availableGeometry().center()
        # 显示到屏幕中心
        qr.moveCenter(cp)
        self.move(qr.topLeft())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = ui()
    sys.exit(app.exec_())
