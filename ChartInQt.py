import requests
import sys
from PyQt5.QtWidgets import QWidget, QApplication , QPushButton, QGridLayout , QLabel
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from bs4 import BeautifulSoup
import numpy as np

req = requests.get('http://www.inven.co.kr/board/autochess/5416?category=%EC%A0%95%EB%B3%B4')
html = req.text
pars = BeautifulSoup(html, 'html.parser')
notice_list = pars.select(
    "td.bbsSubject > a"
)

views_list = pars.select(
    "td.hit"
)
view_list = []

for j in range(5,10):
    notice_list[j-5] = str(j-4) + '. ' + notice_list[j].get_text()
    view_list.append(int(views_list[j].get_text()))

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.initUi()
        self.setWindowTitle("오토체스 게시판 조회수 차트")
        self.setLayout(self.GridLayout)
        self.setGeometry(200,200,400,400)

    def initUi(self):
        self.pushButton = QPushButton("Go Gragh")
        self.pushButton.clicked.connect(self.buttonClicked)

        self.GridLayout = QGridLayout()

        self.labels = {}

        for i in range(1, 6):
            self.labels[i] = QLabel()
            self.labels[i].setText(notice_list[i-1])
            self.GridLayout.addWidget(self.labels[i],i-1,0)

        self.fig = plt.Figure()
        self.fig.suptitle('Views Graph')
        self.canvas = FigureCanvas(self.fig)


        self.GridLayout.addWidget(self.canvas , 5 , 0)
        self.GridLayout.addWidget(self.pushButton, 6, 0)

    def buttonClicked(self):
         N = 5
         ind = np.arange(N)
         width = 0.2

         ax = self.fig.add_subplot(111)
         ax.bar(ind, view_list, width)
         ax.set_xticks(ind + width / 20)
         ax.set_xticklabels(['1', '2', '3', '4', '5'])
         '''
        ax = self.fig.add_subplot(1,1,1)
        ax.bar(ind , view_list , width)
        ax.xticts(ind,('1','2','3','4','5'))
        ax.title('views')
        ax.set_xticks(ind + width/20)
        #ax.set_xticklabels(['1','2','3','4','5'])
        ax.grid()'''
         self.canvas.draw()
         self.canvas.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    app.exec_()
'''
print(views_list)
for i in range(5,10):
    print(notice_list[i].get_text())
for j in range(5,10):
    print(views_list[j].get_text())
'''
#powerbbsBody > table > tbody > tr > td > div > table > tbody > tr > td > table > tbody > tr:nth-child(3) > td > form > table > tbody > tr:nth-child(7) > td.hit
#powerbbsBody > table > tbody > tr > td > div > table > tbody > tr > td > table > tbody > tr:nth-child(3) > td > form > table > tbody >
#powerbbsBody > table > tbody > tr > td > div > table > tbody > tr > td > table > tbody > tr:nth-child(3) > td > form > table > tbody > tr:nth-child(7) > td.bbsSubject > a