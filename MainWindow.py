import sys
from ui.ui_main import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import ctypes


class MainWindow(QMainWindow,Ui_MainWindow):
    def __init__(self, parent = None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        icon_path = './icon/'
        self.uiInit(icon_path)

        # self.resize(600, 600)  # 背景图片的宽度和高度小于窗口的高度和宽度
        palette = QPalette()
        palette.setBrush(QPalette.Background, QBrush(QPixmap(r'img\background.png')))
        self.setPalette(palette)

#         self.treeWidgetInit()
#
#         #设置两个复选框都为选中状态
#         self.checkBoxAlga.setChecked(True)
#         self.checkBoxText.setChecked(True)
#
#         #窗口双击事件绑定
#         self.labelImgShow.installEventFilter(self)
#         #窗口双击放大标志
#         self.cnt = True
#
    def uiInit(self, icon_path):
#         #隐藏边框
#         self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
#         self.setWindowIcon(QIcon('{}siom.ico'.format(icon_path)))
        # self.setWindowTitle("环抛智能数据分析系统")   #第二个参数：窗口标题

#         #设置窗口渐变背景色
#         self.setStyleSheet(
#             '''
#             QMainWindow{
#             background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
#             stop:0 #253a4b ,stop:1 #507da0);
#             }'''
#         )
#         #
#         self.setFixedSize(self.width(), self.height())
#         #按钮样式
#         self.buttonStart.setStyleSheet(
#             '''
#             QPushButton{{border-image:url('{0}开始.png');}}
#             '''.format(icon_path)
#         )
#         self.buttonPause.setStyleSheet(
#             '''
#             QPushButton{{border-image:url('{0}暂停.png');}}
#             '''.format(icon_path)
#         )
#         self.buttonOpenSaveDir.setStyleSheet(
#             '''
#             QPushButton{{border-image:url('{0}输出文件目录.png');}}
#             '''.format(icon_path)
#         )
#         self.buttonImportJson.setStyleSheet(
#             '''
#             QPushButton{{border-image:url('{0}生成geojson.png');}}
#             '''.format(icon_path)
#         )
#         img_path = '{0}选择路径.png'.format(icon_path)
#         self.buttonImportVideo.setIcon(QtGui.QIcon(img_path))
#         self.buttonImportVideo.setStyleSheet(
#             '''
#             QPushButton{{background:transparent;}}
#             '''
#         )
#         img_path = '{0}选择路径.png'.format(icon_path)
#         self.buttonOutSet.setIcon(QtGui.QIcon(img_path))
#         self.buttonOutSet.setStyleSheet(
#             '''
#             QPushButton{{background:transparent;}}
#             '''
#         )
#         img_path = '{0}关闭.png'.format(icon_path)
#         self.buttonWindowClose.setIcon(QtGui.QIcon(img_path))
#         self.buttonWindowClose.setStyleSheet(
#             '''
#             QPushButton{background:transparent;}
#             QPushButton:hover{background:gray;}
#             '''
#         )
#         img_path = '{0}最小化.png'.format(icon_path)
#         self.buttonWindowMinimize.setIcon(QtGui.QIcon(img_path))
#         self.buttonWindowMinimize.setStyleSheet(
#             '''
#             QPushButton{background:transparent;}
#             QPushButton:hover{background:gray;}
#             '''
#         )
#         #label样式
#         self.lineEditVideoPath.setStyleSheet(
#                 '''
#                 QLineEdit{
#                         background:white;
#                         border:1px solid gray;
#                         width:300px;
#                         border-radius:10px;
#                         padding:2px 4px;
#                 }''')
#         self.labelOutPath.setStyleSheet(
#                 '''
#                 QLabel{
#                         background:white;
#                         border:1px solid gray;
#                         width:300px;
#                         border-radius:10px;
#                         padding:2px 4px;
#                 }''')
#         self.labelTitle.setStyleSheet(
#             '''
#             QLabel{
#             background:#121e26;
#             }
#             '''
#         )
#         self.labelLogo.setStyleSheet(
#             '''
#             QLabel{{
#             border-image:url('{0}logo.png');
#             }}
#             '''.format(icon_path)
#         )
        self.labelCompany.setStyleSheet(
            '''
            QLabel{
            background:transparent;
            color:white;
            font-weight:bold;
            font-size:18px;
            font-family:"黑体";
            }
            '''
        )
#         self.labelDataShow.setStyleSheet(
#             '''
#             QLabel{
#             background:#415161;
#             border-radius:10px;
#             padding:2px 4px;
#             font-size:12px;
#             font-family:"黑体";
#             }
#             '''
#         )
#         self.labelImgShow.setStyleSheet(
#             '''
#             QLabel{
#             background:white;
#             }
#             '''
#         )
#         self.labelOutHint.setStyleSheet(
#             '''
#             QLabel{
#             border-radius:5px;color:white;font-size:12px;font-family:"黑体";
#             }
#             '''
#         )
#         self.labelSpeedHint.setStyleSheet(
#             '''
#             QLabel{
#             border-radius:5px;color:white;font-size:12px;font-family:"黑体";
#             }
#             '''
#         )
#
#         #combobox样式设置
#         self.sourceSelect.setStyleSheet(
#             '''
#             QComboBox{
#             background:transparent;
#             color:white
#             }
#             '''
#         )
#         self.speedSelect.setStyleSheet(
#             '''
#             QComboBox{
#             background:transparent;
#             color:white
#             }
#             '''
#         )
#         #设置lineEdit不可编辑
#         self.lineEditVideoPath.setReadOnly(True)
#         #设置checkBox样式
#         self.checkBoxAlga.setStyleSheet(
#             '''
#             QCheckBox{
#             color:white
#             }
#             '''
#         )
#         self.checkBoxText.setStyleSheet(
#             '''
#             QCheckBox{
#             color:white
#             }
#             '''
#         )
#
#     #使得界面可以在无边框情况下被鼠标拖动
#     def mouseMoveEvent(self, e: QMouseEvent):  # 重写移动事件
#         try:
#             self._endPos = e.pos() - self._startPos
#             self.move(self.pos() + self._endPos)
#         except:
#             pass
#
#     def mousePressEvent(self, e: QMouseEvent):
#         if e.button() == Qt.LeftButton:
#             self._isTracking = True
#             self._startPos = QPoint(e.x(), e.y())
#
#     def mouseReleaseEvent(self, e: QMouseEvent):
#         if e.button() == Qt.LeftButton:
#             self._isTracking = False
#             self._startPos = None
#             self._endPos = None
#
#     def treeWidgetInit(self):
#         self.dataTreeWidget.setColumnCount(1)  # 制定树控件为两列
#         self.dataTreeWidget.setHeaderLabels(["图像列表"])  # 设置列标签
#
# #接受一个id参数和nodes参数，分别是图像名和检测框信息
#     def treeWidgetAppend(self,id,nodes):
#         root=QTreeWidgetItem(self.dataTreeWidget)
#         #传入两个参数，列，文本
#         root.setText(0,"图像{}".format(id))
#
#         #node中两个元素，第一个存放分类id，第二个存放经纬度信息
#         for node in nodes:
#             n=QTreeWidgetItem(root)
#             n.setText(0,node[1])
#             if node[0] == '0':
#                 n.setBackground(0,QBrush(QColor("pink")))
#             else:
#                 n.setBackground(0,QBrush(QColor("#87CEEB")))
#
#     def eventFilter(self, obj, event):
#         label_list = [self.labelImgShow]
#         for i in range(0, len(label_list)):
#             if obj == label_list[i]:
#                 if event.type() == QEvent.MouseButtonDblClick:
#                     if self.cnt is True:
#                         self.location = label_list[i].geometry()
#                         label_list[i].setWindowFlags(QtCore.Qt.Window)
#                         label_list[i].showFullScreen()
#                         self.cnt = False
#                     else:
#                         label_list[i].setWindowFlags(QtCore.Qt.SubWindow)
#                         label_list[i].resize(640, 360)
#                         label_list[i].showNormal()
#                         label_list[i].setGeometry(self.location)
#                         self.cnt = True
#
#         return QWidget.eventFilter(self, obj, event)

if __name__ == '__main__':
    # 此条命令用于解决代码执行冲突
    App = QApplication(sys.argv)
    win = MainWindow()
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("myappid")
    win.showNormal()
    sys.exit(App.exec_())