from urllib.request import urlopen
from bs4 import BeautifulSoup
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QToolButton,QLayout, QApplication, QWidget, QLabel, QGridLayout
import collections
class findall():

    def __init__(self):
        html = urlopen("https://cs.kookmin.ac.kr/")
        bsObject = BeautifulSoup(html, "html.parser")

        self.strong = []
        for p in bsObject.find_all('div', {'id': 'tab-item1'}):
            self.strong = p.select('strong')
        index = 0
        for i in self.strong:
            #self.strong[index] = str(i)#[8:-9]
            self.strong[index] = i.text
            index += 1


class kookminnotice(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        title = QLabel()
        title.setText("국민대학교 공지사항 리스트")
        self.labels = collections.OrderedDict()

        for i in range(1, 9 + 1):
            self.labels['label' + str(i)] = QLabel()

        '''
        self.label1 = QLabel()
        self.label2 = QLabel()
        self.label3 = QLabel()
        self.label4 = QLabel()
        self.label5 = QLabel()
        self.label6 = QLabel()
        self.label7 = QLabel(){ label1 : qlabellkjk , 
        self.label8 = QLabel()
        self.label9 = QLabel()
        '''
        '''self.label_list = [self.label1, self.label2, self.label3, self.label4, self.label5, self.label6, self.label7,
                           self.label8, self.label9]'''
        self.go_Button = QToolButton()
        self.go_Button.setText("Search")
        self.go_Button.clicked.connect(self.Button)

        self.allgrid = QGridLayout()
        self.allgrid.addWidget(title, 0, 0)

        self.line = QLabel()
        self.line.setText("-----")
        self.labelgrid = QGridLayout()
        for k in range(1 , 10):
            self.labelgrid.addWidget(self.label_list[k-1], k-1 , 0)
        self.allgrid.addWidget(self.line,1,0)
        self.allgrid.addLayout(self.labelgrid,2,0)
        self.allgrid.addWidget(self.go_Button, 3, 0)

        self.setLayout(self.allgrid)
        self.setWindowTitle('kookmin_sw_notice')

    def Button(self):
        searchlaunch = findall()
        for i in range(8):
            self.label_list[i].setText(searchlaunch.strong[i])


import sys

app = QApplication(sys.argv)
search = kookminnotice()
search.show()
sys.exit(app.exec_())
