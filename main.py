# -*- coding: utf-8 -*-

import sys, os, cv2, xlwt
import numpy as np
from sys import exit, argv
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from Recognition import TesPlateRecognition
big = False

class Ui_MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.RowLength = 0
        self.Data = [['文件名称', '录入时间', '车牌号码', '车牌颜色', '车牌信息']]
        # self.setupUi(MainWindow())

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1213, 670)
        MainWindow.setFixedSize(1213, 670)  # 设置窗体固定大小
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(690, 40, 511, 460))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 500, 489))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.label_0 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_0.setGeometry(QtCore.QRect(10, 10, 111, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_0.setFont(font)
        self.label_0.setObjectName("label_0")
        self.label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label.setGeometry(QtCore.QRect(10, 40, 481, 420))
        self.label.setObjectName("label")
        self.label.setAlignment(Qt.AlignCenter)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.scrollArea_2 = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea_2.setGeometry(QtCore.QRect(10, 10, 671, 631))
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_1 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_1.setGeometry(QtCore.QRect(0, 0, 669, 629))
        self.scrollAreaWidgetContents_1.setObjectName("scrollAreaWidgetContents_1")
        self.label_1 = QtWidgets.QLabel(self.scrollAreaWidgetContents_1)
        self.label_1.setGeometry(QtCore.QRect(10, 10, 111, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_1.setFont(font)
        self.label_1.setObjectName("label_1")
        self.tableWidget = QtWidgets.QTableWidget(self.scrollAreaWidgetContents_1)
        self.tableWidget.setGeometry(QtCore.QRect(10, 40, 651, 581))  # 581))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setColumnWidth(0, 140)  # 设置1列的宽度
        self.tableWidget.setColumnWidth(1, 130)  # 设置2列的宽度
        self.tableWidget.setColumnWidth(2, 110)  # 设置3列的宽度
        self.tableWidget.setColumnWidth(3, 90)  # 设置4列的宽度
        self.tableWidget.setColumnWidth(4, 181)  # 设置5列的宽度
        self.tableWidget.setHorizontalHeaderLabels(["图片名称", "录入时间", "车牌号码", "车牌颜色", "车牌信息"])
        self.tableWidget.setRowCount(self.RowLength)
        self.tableWidget.verticalHeader().setVisible(False)  # 隐藏垂直表头)

        b = '''
                     color:white;
                     background:#2B2B2B;
                    '''
        # self.tableWidget.setStyleSheet(b)
        # self.tableWidget.setAlternatingRowColors(True)

        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.raise_()
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_1)
        self.scrollArea_3 = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea_3.setGeometry(QtCore.QRect(690, 510, 341, 131))
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollArea_3.setObjectName("scrollArea_3")
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 339, 129))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.label_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 111, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.label_3.setGeometry(QtCore.QRect(10, 40, 321, 81))
        self.label_3.setObjectName("label_3")
        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)
        self.scrollArea_4 = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea_4.setGeometry(QtCore.QRect(1040, 510, 161, 131))
        self.scrollArea_4.setWidgetResizable(True)
        self.scrollArea_4.setObjectName("scrollArea_4")
        self.scrollAreaWidgetContents_4 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_4.setGeometry(QtCore.QRect(0, 0, 159, 129))
        self.scrollAreaWidgetContents_4.setObjectName("scrollAreaWidgetContents_4")
        self.pushButton_2 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_4)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 40, 120, 30))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents_4)
        self.pushButton.setGeometry(QtCore.QRect(20, 70, 120, 30))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_3 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_4)
        self.pushButton_3.setGeometry(QtCore.QRect(20, 100, 120, 30))
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_4 = QtWidgets.QLabel(self.scrollAreaWidgetContents_4)
        self.label_4.setGeometry(QtCore.QRect(10, 10, 111, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.scrollArea_4.setWidget(self.scrollAreaWidgetContents_4)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.pushButton.clicked.connect(self.__openimage)  # 设置点击事件
        self.pushButton.setStyleSheet('''QPushButton{background:#222225;border-radius:5px;}QPushButton:hover{background:#2B2B2B;}''')
        self.pushButton_2.clicked.connect(self.__writeFiles)  # 设置点击事件
        self.pushButton_2.setStyleSheet('''QPushButton{background:#222225;border-radius:5px;}QPushButton:hover{background:#2B2B2B;}''')
        self.pushButton_3.clicked.connect(self.opencarmera)  # 设置点击事件
        self.pushButton_3.setStyleSheet( '''QPushButton{background:#222225;border-radius:5px;}QPushButton:hover{background:#2B2B2B;}''')
        self.retranslateUi(MainWindow)


        self.close_widget = QtWidgets.QWidget(self.centralwidget)
        self.close_widget.setGeometry(QtCore.QRect(1130, 0, 90, 50))
        self.close_widget.setObjectName("close_widget")
        self.close_layout = QGridLayout()  # 创建左侧部件的网格布局层
        self.close_widget.setLayout(self.close_layout)  # 设置左侧部件布局为网格

        self.left_close = QPushButton("")  # 关闭按钮
        self.left_close.clicked.connect(self.close)
        self.left_visit = QPushButton("")  # 空白按钮
        self.left_visit.clicked.connect(MainWindow.big)
        self.left_mini = QPushButton("")  # 最小化按钮
        self.left_mini.clicked.connect(MainWindow.mini)
        self.close_layout.addWidget(self.left_mini, 0, 0, 1, 1)
        self.close_layout.addWidget(self.left_close, 0, 2, 1, 1)
        self.close_layout.addWidget(self.left_visit, 0, 1, 1, 1)
        self.left_close.setFixedSize(15, 15)  # 设置关闭按钮的大小
        self.left_visit.setFixedSize(15, 15)  # 设置按钮大小
        self.left_mini.setFixedSize(15, 15)  # 设置最小化按钮大小
        self.left_close.setStyleSheet(
            '''QPushButton{background:#F76677;border-radius:5px;}QPushButton:hover{background:red;}''')
        self.left_visit.setStyleSheet(
            '''QPushButton{background:#F7D674;border-radius:5px;}QPushButton:hover{background:yellow;}''')
        self.left_mini.setStyleSheet(
            '''QPushButton{background:#6DDF6D;border-radius:5px;}QPushButton:hover{background:green;}''')

        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.ProjectPath = os.getcwd()  # 获取当前工程文件位置

        self.centralwidget.setStyleSheet('''
             QWidget#centralwidget{
             color:white;
             background:#222225;
             border-top:1px solid #222225;
             border-bottom:1px solid #222225;
             border-right:1px solid #222225;
             border-left:1px solid #444444;
             border-top-left-radius:10px;
             border-top-right-radius:10px;
             border-bottom-left-radius:10px;
             border-bottom-right-radius:10px;
             }
             ''')
        sc = '''
             QWidget{
             color:white;
             background:#2B2B2B;
             border-top:1px solid #222225;
             border-bottom:1px solid #222225;
             border-right:1px solid #222225;
             border-left:1px solid #444444;
             border-top-left-radius:10px;
             border-top-right-radius:10px;
             border-bottom-left-radius:10px;
             border-bottom-right-radius:10px;
             }

             '''

        self.scrollAreaWidgetContents_1.setStyleSheet('''
             QWidget{
             color:black;
             background:#2B2B2B;
             border-top:1px solid #222225;
             border-bottom:1px solid #222225;
             border-right:1px solid #222225;
             border-left:1px solid #444444;
             border-top-left-radius:10px;
             border-top-right-radius:10px;
             border-bottom-left-radius:10px;
             border-bottom-right-radius:10px;
             }
                      QListWidget{background-color:#2B2B2B;color:#222225}
         /*垂直滚动条*/
         QScrollBar:vertical{
             width:12px;
             border:1px solid #2B2B2B;
             margin:0px,0px,0px,0px;
             padding-top:0px;
             padding-bottom:0px;
         }
         QScrollBar::handle:vertical{
             width:3px;
             background:#4B4B4B;
             min-height:3;
         }
         QScrollBar::handle:vertical:hover{
             background:#3F3F3F;
             border:0px #3F3F3F;
         }
         QScrollBar::sub-line:vertical{
             width:0px;
             border-image:url(:/Res/scroll_left.png);
             subcontrol-position:left;
         }
         QScrollBar::sub-line:vertical:hover{
             height:0px;
             background:#222225;
             subcontrol-position:top;
         }
         QScrollBar::add-line:vertical{
             height:0px;
             border-image:url(:/Res/scroll_down.png);
             subcontrol-position:bottom;
         }
         QScrollBar::add-line:vertical:hover{
             height:0px;
             background:#3F3F3F;
             subcontrol-position:bottom;
         }
         QScrollBar::add-page:vertical{
             background:#2B2B2B;
         }
         QScrollBar::sub-page:vertical{
             background:#2B2B2B;
         }
         QScrollBar::up-arrow:vertical{
             border-style:outset;
             border-width:0px;
         }
         QScrollBar::down-arrow:vertical{
             border-style:outset;
             border-width:0px;
         }

         QScrollBar:horizontal{
             height:12px;
             border:1px #2B2B2B;
             margin:0px,0px,0px,0px;
             padding-left:0px;
             padding-right:0px;
         }
         QScrollBar::handle:horizontal{
             height:16px;
             background:#4B4B4B;
             min-width:20;
         }
         QScrollBar::handle:horizontal:hover{
             background:#3F3F3F;
             border:0px #3F3F3F;
         }
         QScrollBar::sub-line:horizontal{
             width:0px;
             border-image:url(:/Res/scroll_left.png);
             subcontrol-position:left;
         }
         QScrollBar::sub-line:horizontal:hover{
             width:0px;
             background:#2B2B2B;
             subcontrol-position:left;
         }
         QScrollBar::add-line:horizontal{
             width:0px;
             border-image:url(:/Res/scroll_right.png);
             subcontrol-position:right;
         }
         QScrollBar::add-line:horizontal:hover{
             width:0px;
             background::#2B2B2B;
             subcontrol-position:right;
         }
         QScrollBar::add-page:horizontal{
                    background:#2B2B2B;
         }
         QScrollBar::sub-page:horizontal{
                     background:#2B2B2B;
         }
             ''')
        self.scrollAreaWidgetContents.setStyleSheet(sc)
        self.scrollAreaWidgetContents_3.setStyleSheet(sc)
        self.scrollAreaWidgetContents_4.setStyleSheet(sc)
        b =             '''
             color:white;
             background:#2B2B2B;
            '''
        self.label_0.setStyleSheet(b)
        self.label_1.setStyleSheet(b)
        self.label_2.setStyleSheet(b)
        self.label_3.setStyleSheet(b)


        MainWindow.setWindowOpacity(0.95)  # 设置窗口透明度
        MainWindow.setAttribute(Qt.WA_TranslucentBackground)
        MainWindow.setWindowFlag(Qt.FramelessWindowHint)  # 隐藏边框


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "车牌识别系统"))
        self.label_0.setText(_translate("MainWindow", "原始图片："))
        self.label.setText(_translate("MainWindow", ""))
        self.label_1.setText(_translate("MainWindow", "识别结果："))
        self.label_2.setText(_translate("MainWindow", "车牌区域："))
        self.label_3.setText(_translate("MainWindow", ""))
        self.pushButton.setText(_translate("MainWindow", "打开文件"))
        self.pushButton_2.setText(_translate("MainWindow", "导出数据"))
        self.pushButton_3.setText(_translate("MainWindow", "实时识别"))
        self.label_4.setText(_translate("MainWindow", "事件："))
        self.scrollAreaWidgetContents_1.show()

    # 识别
    def __vlpr(self, path):
        PR = TesPlateRecognition()
        img, color = PR.plate_cut(path)
        result = PR.TesOCR(img, color)
        return result

    def opencarmera(self):
        result={}
        cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)  # 打开摄像头
        while (1):
            # get a frame
            ret, frame = cap.read()
            # frame = cv2.flip(frame, 1)  # 摄像头是和人对立的，将图像左右调换回来正常显示
            # show a frame
            cv2.imshow("capture", frame)  # 生成摄像头窗口

            if cv2.waitKey(1) & 0xFF == ord('q'):  # 如果按下q 就截图保存并退出
                cv2.imwrite("temp.jpg", frame)  # 保存路径
                break
        cap.release()
        cv2.destroyAllWindows()
        size = cv2.imdecode(np.fromfile("temp.jpg", dtype=np.uint8), cv2.IMREAD_COLOR).shape
        if size[0] / size[1] > 1.0907:
            w = int(size[1] * self.label.height() / size[0])
            h = self.label.height()
            jpg = QtGui.QPixmap("temp.jpg").scaled(w, h)
        elif size[0] / size[1] < 1.0907:
            w = self.label.width()
            h = int((size[0] * self.label.width()) / size[1])
            jpg = QtGui.QPixmap("temp.jpg").scaled(w, h)
        else:
            jpg = QtGui.QPixmap("temp.jpg").scaled(self.label.width(), self.label.height())

        self.label.setPixmap(jpg)
        result = self.__vlpr("temp.jpg")
        if result is not None:
            self.Data.append(
                ["temp.jpg", result['InputTime'], result['Number'], result['Type'],
                    result['From']])
            self.__show(result, "temp.jpg")
        else:
            QMessageBox.warning(None, "Error", "无法识别此图像！", QMessageBox.Yes)

    def __show(self, result, FileName):
        # 显示表格
        self.RowLength = self.RowLength + 1
        if self.RowLength > 18:
            self.tableWidget.setColumnWidth(5, 157)
        self.tableWidget.setRowCount(self.RowLength)

        self.tableWidget.setItem(self.RowLength - 1, 0, QTableWidgetItem(FileName))
        self.tableWidget.setItem(self.RowLength - 1, 1, QTableWidgetItem(result['InputTime']))
        self.tableWidget.setItem(self.RowLength - 1, 2, QTableWidgetItem(result['Number']))
        self.tableWidget.setItem(self.RowLength - 1, 3, QTableWidgetItem(result['Type']))
        if result['Type'] == '蓝色牌照':
            self.tableWidget.item(self.RowLength - 1, 3).setBackground(QBrush(QColor(3, 128, 255)))
        elif result['Type'] == '绿色牌照':
            self.tableWidget.item(self.RowLength - 1, 3).setBackground(QBrush(QColor(98, 198, 148)))
        elif result['Type'] == '黄色牌照':
            self.tableWidget.item(self.RowLength - 1, 3).setBackground(QBrush(QColor(242, 202, 9)))
        self.tableWidget.setItem(self.RowLength - 1, 4, QTableWidgetItem(result['From']))

        self.tableWidget.item(self.RowLength - 1, 0).setBackground(QBrush(QColor(255, 255, 255)))
        self.tableWidget.item(self.RowLength - 1, 1).setBackground(QBrush(QColor(255, 255, 255)))
        self.tableWidget.item(self.RowLength - 1, 2).setBackground(QBrush(QColor(255, 255, 255)))
        self.tableWidget.item(self.RowLength - 1, 4).setBackground(QBrush(QColor(255, 255, 255)))

        # 显示识别到的车牌位置
        size = (int(self.label_3.width()), int(self.label_3.height()))
        shrink = cv2.resize(result['Picture'], size, interpolation=cv2.INTER_AREA)
        shrink = cv2.cvtColor(shrink, cv2.COLOR_BGR2RGB)
        self.QtImg = QtGui.QImage(shrink[:], shrink.shape[1], shrink.shape[0], shrink.shape[1] * 3,
                                  QtGui.QImage.Format_RGB888)
        self.label_3.setPixmap(QtGui.QPixmap.fromImage(self.QtImg))

    def __writexls(self, DATA, path):
        wb = xlwt.Workbook();
        ws = wb.add_sheet('Data');
        # DATA.insert(0, ['文件名称','录入时间', '车牌号码', '车牌类型', '车牌信息'])
        for i, Data in enumerate(DATA):
            for j, data in enumerate(Data):
                ws.write(i, j, data)
        wb.save(path)
        QMessageBox.information(None, "成功", "数据已保存！", QMessageBox.Yes)

    def __writecsv(self, DATA, path):
        f = open(path, 'w')
        # DATA.insert(0, ['文件名称','录入时间', '车牌号码', '车牌类型', '车牌信息'])
        for data in DATA:
            f.write((',').join(data) + '\n')
        f.close()
        QMessageBox.information(None, "成功", "数据已保存！", QMessageBox.Yes)

    def __writeFiles(self):
        path, filetype = QFileDialog.getSaveFileName(None, "另存为", self.ProjectPath,
                                                     "Excel 工作簿(*.xls);;CSV (逗号分隔)(*.csv)")
        if path == "":  # 未选择
            return
        if filetype == 'Excel 工作簿(*.xls)':
            self.__writexls(self.Data, path)
        elif filetype == 'CSV (逗号分隔)(*.csv)':
            self.__writecsv(self.Data, path)

    def __openimage(self):
        path, filetype = QFileDialog.getOpenFileName(None, "选择文件", self.ProjectPath,
                                                     "JPEG Image (*.jpg);;PNG Image (*.png);;JFIF Image (*.jfif)")  # ;;All Files (*)
        if path == "":  # 未选择文件
            return
        filename = path.split('/')[-1]

        # 尺寸适配
        size = cv2.imdecode(np.fromfile(path, dtype=np.uint8), cv2.IMREAD_COLOR).shape
        if size[0] / size[1] > 1.0907:
            w = int(size[1] * self.label.height() / size[0])
            h = self.label.height()
            jpg = QtGui.QPixmap(path).scaled(w, h)
        elif size[0] / size[1] < 1.0907:
            w = self.label.width()
            h = int((size[0] * self.label.width()) / size[1])
            jpg = QtGui.QPixmap(path).scaled(w, h)
        else:
            jpg = QtGui.QPixmap(path).scaled(self.label.width(), self.label.height())

        self.label.setPixmap(jpg)
        result = self.__vlpr(path)
        if result is not None:
            self.Data.append(
                [filename, result['InputTime'], result['Number'], result['Type'],
                 result['From']])
            self.__show(result, filename)
        else:
            QMessageBox.warning(None, "Error", "无法识别此图像！", QMessageBox.Yes)

    def close(self):
        reply = QtWidgets.QMessageBox.question(self, '提示',
                                               "是否要退出程序？\n提示：退出后将丢失所有识别数据",
                                               QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                               QtWidgets.QMessageBox.No)
        if reply == QtWidgets.QMessageBox.Yes:
            sys.exit()
        else:
            pass



# 重写MainWindow类
class MainWindow(QtWidgets.QMainWindow):

    def closeEvent(self, event):
        reply = QtWidgets.QMessageBox.question(self, '提示',
                                               "是否要退出程序？\n提示：退出后将丢失所有识别数据",
                                               QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                               QtWidgets.QMessageBox.No)
        if reply == QtWidgets.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def mousePressEvent(self, event):
        global big
        big = False
        self.setWindowState(Qt.WindowNoState)
        self.m_flag = True
        self.m_Position = event.globalPos() - self.pos()  # 获取鼠标相对窗口的位置
        event.accept()

    def mouseMoveEvent(self, QMouseEvent):
        global big
        big = False
        self.setWindowState(Qt.WindowNoState)
        self.move(QMouseEvent.globalPos() - self.m_Position)  # 更改窗口位置
        QMouseEvent.accept()

    def mouseReleaseEvent(self, QMouseEvent):
        global big
        big = False
        self.setWindowState(Qt.WindowNoState)
        self.m_flag = False

    def mousePressEvent(self, event):
        global big
        big = False
        self.setWindowState(Qt.WindowNoState)
        self.m_flag = True
        self.m_Position = event.globalPos() - self.pos()  # 获取鼠标相对窗口的位置
        event.accept()

    def mouseMoveEvent(self, QMouseEvent):
        global big
        big = False
        self.setWindowState(Qt.WindowNoState)
        self.move(QMouseEvent.globalPos() - self.m_Position)  # 更改窗口位置
        QMouseEvent.accept()

    def mouseReleaseEvent(self, QMouseEvent):
        global big
        big = False
        self.setWindowState(Qt.WindowNoState)
        self.m_flag = False

    def big(self):
        global big
        print('最大化：{}'.format(big))
        if not big:
            self.setWindowState(Qt.WindowMaximized)
            big = True
        elif big:
            self.setWindowState(Qt.WindowNoState)
            big = False

    def mini(self):

        self.showMinimized()




if __name__ == "__main__":
    if os.path.exists('provinces.json'):
        if os.path.exists('cardtype.json'):
            if os.path.exists('Prefecture.json'):
                if os.path.exists('config.js'):
                    app = QtWidgets.QApplication(sys.argv)
                    MainWindow = MainWindow()  # QtWidgets.QMainWindow()
                    ui = Ui_MainWindow()
                    ui.setupUi(MainWindow)
                    MainWindow.show()
                    sys.exit(app.exec_())
                    # app = QApplication(argv)
                    # gui = Ui_MainWindow()
                    # gui.setupUi(MainWindow)
                    # MainWindow.show()
                    # exit(app.exec_())
                else:
                    print('未找到参数文件 config.js')
                    RuntimeError('未找到参数文件 config.js')
            else:
                print('未找到 Prefecture.json 文件')
                RuntimeError('未找到 Prefecture.json 文件')
        else:
            print('未找到 cardtype.json 文件')
            RuntimeError('未找到 cardtype.json 文件')
    else:
        print('未找到 provinces.json 文件')
        RuntimeError('未找到 provinces.json 文件')
