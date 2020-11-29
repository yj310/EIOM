import sys
from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2 import QtCore

from BasicInfo import BasicInfo


class noticeList(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.basicInfo = BasicInfo()

        self.w = QWidget(self)
        layout = QVBoxLayout()
        self.setWindowTitle('EIOM')
        self.w.resize(self.basicInfo.WindowWidth, self.basicInfo.WindowHeight)
        self.move(self.basicInfo.WindowX, self.basicInfo.WindowY)
        self.setFixedSize(self.basicInfo.WindowWidth, self.basicInfo.WindowHeight)
        palette = QPalette()
        palette.setBrush(QPalette.Background, QBrush(QPixmap("../img/background.png")))
        self.setPalette(palette)

        title = QLabel("EIOM", self.w)
        title.setFont(QFont(self.basicInfo.titleFont, 25))
        title.setAlignment(QtCore.Qt.AlignCenter)
        layout.addWidget(title)
        title.setGeometry(100, 10, 1000, 50)

        stateBtn = QPushButton('통계', self.w)
        stateBtn.setFont(QFont(self.basicInfo.font1, 13))
        stateBtn.setGeometry(0, 70, 200, 50)
        stateBtn.setStyleSheet('background-color: rgb(255,255,255); border:1px solid lightgray; ')

        noticeBtn = QPushButton('공지', self.w)
        noticeBtn.setFont(QFont(self.basicInfo.font1, 13))
        noticeBtn.setGeometry(200, 70, 200, 50)
        noticeBtn.setStyleSheet('background-color: rgb(255,255,255); border:1px solid lightgray; ')

        companyBtn = QPushButton('회사', self.w)
        companyBtn.setFont(QFont(self.basicInfo.font1, 13))
        companyBtn.setGeometry(400, 70, 200, 50)
        companyBtn.setStyleSheet('background-color: rgb(255,255,255); border:1px solid lightgray; ')

        postBtn = QPushButton('취업의뢰', self.w)
        postBtn.setFont(QFont(self.basicInfo.font1, 13))
        postBtn.setGeometry(600, 70, 200, 50)
        postBtn.setStyleSheet('background-color: rgb(255,255,255); border:1px solid lightgray; ')

        pfBtn = QPushButton('포트폴리오', self.w)
        pfBtn.setFont(QFont(self.basicInfo.font1, 13))
        pfBtn.setGeometry(800, 70, 200, 50)
        pfBtn.setStyleSheet('background-color: rgb(255,255,255); border:1px solid lightgray; ')

        infoBtn = QPushButton('내 정보', self.w)
        infoBtn.setFont(QFont(self.basicInfo.font1, 13))
        infoBtn.setGeometry(1000, 70, 200, 50)
        infoBtn.setStyleSheet('background-color: rgb(255,255,255); border:1px solid lightgray; ')

        contTitle=QLabel('제목 \n',self.w)
        contTitle.setFont(QFont(self.basicInfo.font1,13))
        contTitle.setGeometry(100,150,1000,90)
        contTitle.setStyleSheet('border-top:1px solid black; border-bottom:1px solid black; ')
        contTitle.setAlignment(QtCore.Qt.AlignCenter)

        writer=QLabel('유병석 선생님 | 2020.12.01',contTitle)
        writer.setFont(QFont(self.basicInfo.font1, 10))
        writer.setGeometry(0,60,1000,20)
        writer.setStyleSheet('color:gray; border:0px;')
        writer.setAlignment(QtCore.Qt.AlignCenter)

        content=QTextBrowser(self.w)
        content.setFont(QFont(self.basicInfo.font1, 12))
        content.setGeometry(100, 240, 1000, 300)
        content.setStyleSheet('border:0px;border-bottom:1px solid black; ')

        file = QLabel('첨부파일',self.w)
        file.setFont(QFont(self.basicInfo.font1, 12))
        file.setGeometry(100, 540, 1000, 50)
        file.setStyleSheet('border:0px;border-bottom:1px solid black; ')

        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    ex = noticeList()
    sys.exit(app.exec_())
