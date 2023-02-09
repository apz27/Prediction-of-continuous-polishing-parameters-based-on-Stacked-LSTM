from MainWindow import MainWindow
from PyQt5.QtWidgets import *
import sys
import numpy as np
import pandas as pd
from sklearn.svm import SVR
from sklearn.preprocessing import MinMaxScaler
import joblib
import ctypes
import openpyxl



class MyWindow(MainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.pushButton.clicked.connect(self.processStart)

        # self.label_nextPV.setText(self.getNextTime_process)

        self.state = self.comboBox.currentText()
        self.Time = self.lineEdit_Time.text()
        self.PXJ = self.lineEdit_PXJ.text()
        self.RS = self.lineEdit_RS.text()
        self.PV = self.lineEdit_PV.text()
        self.Power = self.lineEdit_Power.text()
        self.Astmag = self.lineEdit_Astmag.text()
        self.expectPV = self.lineEdit_expectPV.text()
        self.expectPower = self.lineEdit_expectPower.text()
        self.expectAstmag = self.lineEdit_expectAstmag.text()

        self.nextTime = self.lineEdit_nextTime
        self.nextPXJ = self.lineEdit_nextPXJ
        self.nextRS = self.lineEdit_nextRS


    def getVaue(self):
        self.state = self.comboBox.currentText()
        self.Time = self.lineEdit_Time.text()
        self.PXJ = self.lineEdit_PXJ.text()
        self.RS = self.lineEdit_RS.text()
        self.PV = self.lineEdit_PV.text()
        self.Power = self.lineEdit_Power.text()
        self.Astmag = self.lineEdit_Astmag.text()
        self.expectPV = self.lineEdit_expectPV.text()
        self.expectPower = self.lineEdit_expectPower.text()
        self.expectAstmag = self.lineEdit_expectAstmag.text()


    def processStart(self):
        self.getVaue()
        self.getNextTime()
        self.getNextPXJ()
        self.getNextRS()

        self.nextTime = self.lineEdit_nextTime.text()
        self.nextPXJ = self.lineEdit_nextPXJ.text()
        self.nextRS = self.lineEdit_nextRS.text()

        self.getNextPV()
        self.getNextPower()
        self.getNextAstmag()


    def getNextTime(self):
        # 读取数据
        if self.state == 'T':
            # df = pd.read_excel('T.xlsx')
            df = pd.read_excel(r"data\T.xlsx")
        elif self.state == 'L':
            # df = pd.read_excel('L.xlsx')
            df = pd.read_excel(r"data\L.xlsx")

        # 建立特征数据和标签数据
        X = df.drop(['Time', 'PXJ', 'RS'], axis=1)
        y = df['Time']

        # 归一化
        scaler_x = MinMaxScaler()
        scaler_y = MinMaxScaler()

        scaler_x = scaler_x.fit(X)
        X_train = scaler_x.transform(X)

        scaler_y = scaler_y.fit(np.array(y).reshape(-1, 1))
        y_train = scaler_y.transform(np.array(y).reshape(-1, 1))

        # 保存归一化参数
        joblib.dump(scaler_x, "scaler_x1.pkl")
        joblib.dump(scaler_y, "scaler_y1.pkl")

        # 构建SVR回归模型
        # 通过for循环来选择最好的核函数

        # for k in ['linear', 'poly', 'rbf', 'sigmoid']:
        #     clf = svm.SVR(kernel=k)
        #     clf.fit(X_train, y_train)
        #     confidence = clf.score(X_train, y_train)
        #     print('*************k, confidence*****************')
        #     print(k, confidence)

        # 建模
        Svr = SVR(kernel='rbf', C=1, gamma=0.5)

        Svr.fit(X_train, y_train)  # 拟合

        scaler_input = joblib.load('scaler_x1.pkl')
        scaler_output = joblib.load('scaler_y1.pkl')
        a = [[self.Time, self.PXJ, self.RS, self.PV, self.Power, self.Astmag, self.expectPV, self.expectPower,
              self.expectAstmag]]
        nextTime = Svr.predict(scaler_input.transform(a))
        # print('***Time***')
        # print(scaler_output.inverse_transform(np.array(nextTime).reshape(-1, 1)))
        # print(nextTime)
        # self.lineEdit_nextTime.setText('101')

        out = scaler_output.inverse_transform(np.array(nextTime).reshape(-1, 1))
        self.lineEdit_nextTime.setText(str(round(out[0][0], 3)))


    def getNextPXJ(self):
        # 读取数据
        if self.state == 'T':
            # df = pd.read_excel('T.xlsx')
            df = pd.read_excel(r"data\T.xlsx")
        elif self.state == 'L':
            # df = pd.read_excel('L.xlsx')
            df = pd.read_excel(r"data\L.xlsx")

        # 建立特征数据和标签数据
        X = df.drop(['Time', 'PXJ', 'RS'], axis=1)
        y = df['PXJ']

        # 归一化
        scaler_x = MinMaxScaler()
        scaler_y = MinMaxScaler()

        scaler_x = scaler_x.fit(X)
        X_train = scaler_x.transform(X)

        scaler_y = scaler_y.fit(np.array(y).reshape(-1, 1))
        y_train = scaler_y.transform(np.array(y).reshape(-1, 1))

        # 保存归一化参数
        joblib.dump(scaler_x, "scaler_x2.pkl")
        joblib.dump(scaler_y, "scaler_y2.pkl")

        # 构建SVR回归模型
        # 通过for循环来选择最好的核函数

        # for k in ['linear', 'poly', 'rbf', 'sigmoid']:
        #     clf = svm.SVR(kernel=k)
        #     clf.fit(X_train, y_train)
        #     confidence = clf.score(X_train, y_train)
        #     print('*************k, confidence*****************')
        #     print(k, confidence)

        # 建模
        Svr = SVR(kernel='rbf', C=1, gamma=0.5)

        Svr.fit(X_train, y_train)  # 拟合

        scaler_input = joblib.load('scaler_x2.pkl')
        scaler_output = joblib.load('scaler_y2.pkl')
        a = [[self.Time, self.PXJ, self.RS, self.PV, self.Power, self.Astmag, self.expectPV, self.expectPower,
              self.expectAstmag]]
        nextPXJ = Svr.predict(scaler_input.transform(a))
        # print('***PXJ***')
        # print(scaler_output.inverse_transform(np.array(nextPXJ).reshape(-1, 1)))
        # print(nextPXJ)
        # self.lineEdit_nextPXJ.setText('102')

        out = scaler_output.inverse_transform(np.array(nextPXJ).reshape(-1, 1))
        self.lineEdit_nextPXJ.setText(str(round(out[0][0], 3)))


    def getNextRS(self):
        # 读取数据
        if self.state == 'T':
            # df = pd.read_excel('T.xlsx')
            df = pd.read_excel(r"data\T.xlsx")
        elif self.state == 'L':
            # df = pd.read_excel('L.xlsx')
            df = pd.read_excel(r"data\L.xlsx")

        # 建立特征数据和标签数据
        X = df.drop(['Time', 'PXJ', 'RS'], axis=1)
        y = df['RS']

        # 归一化
        scaler_x = MinMaxScaler()
        scaler_y = MinMaxScaler()

        scaler_x = scaler_x.fit(X)
        X_train = scaler_x.transform(X)

        scaler_y = scaler_y.fit(np.array(y).reshape(-1, 1))
        y_train = scaler_y.transform(np.array(y).reshape(-1, 1))

        # 保存归一化参数
        joblib.dump(scaler_x, "scaler_x3.pkl")
        joblib.dump(scaler_y, "scaler_y3.pkl")

        # 构建SVR回归模型
        # 通过for循环来选择最好的核函数

        # for k in ['linear', 'poly', 'rbf', 'sigmoid']:
        #     clf = svm.SVR(kernel=k)
        #     clf.fit(X_train, y_train)
        #     confidence = clf.score(X_train, y_train)
        #     print('*************k, confidence*****************')
        #     print(k, confidence)

        # 建模
        Svr = SVR(kernel='rbf', C=1, gamma=0.5)

        Svr.fit(X_train, y_train)  # 拟合

        scaler_input = joblib.load('scaler_x3.pkl')
        scaler_output = joblib.load('scaler_y3.pkl')
        a = [[self.Time, self.PXJ, self.RS, self.PV, self.Power, self.Astmag, self.expectPV, self.expectPower,
              self.expectAstmag]]
        nextRS = Svr.predict(scaler_input.transform(a))
        # print('***RS***')
        # print(scaler_output.inverse_transform(np.array(nextRS).reshape(-1, 1)))
        # print(nextRS)
        # self.lineEdit_nextRS.setText('103')

        out = scaler_output.inverse_transform(np.array(nextRS).reshape(-1, 1))
        self.lineEdit_nextRS.setText(str(round(out[0][0], 3)))


    def getNextPV(self):
        # 读取数据
        if self.state == 'T':
            # df = pd.read_excel('T.xlsx')
            df = pd.read_excel(r"data\T.xlsx")
        elif self.state == 'L':
            # df = pd.read_excel('L.xlsx')
            df = pd.read_excel(r"data\L.xlsx")

        # 建立特征数据和标签数据
        X = df.drop(['PV', 'Power', 'Astmag'], axis=1)
        y = df['PV']

        # 归一化
        scaler_x = MinMaxScaler()
        scaler_y = MinMaxScaler()

        scaler_x = scaler_x.fit(X)
        X_train = scaler_x.transform(X)

        scaler_y = scaler_y.fit(np.array(y).reshape(-1, 1))
        y_train = scaler_y.transform(np.array(y).reshape(-1, 1))

        # 保存归一化参数
        joblib.dump(scaler_x, "scaler_x11.pkl")
        joblib.dump(scaler_y, "scaler_y11.pkl")

        # 构建SVR回归模型
        # 通过for循环来选择最好的核函数

        # for k in ['linear', 'poly', 'rbf', 'sigmoid']:
        #     clf = svm.SVR(kernel=k)
        #     clf.fit(X_train, y_train)
        #     confidence = clf.score(X_train, y_train)
        #     print('*************k, confidence*****************')
        #     print(k, confidence)

        # 建模
        Svr = SVR(kernel='rbf', C=2.7, gamma=1)

        Svr.fit(X_train, y_train)  # 拟合

        scaler_input = joblib.load('scaler_x11.pkl')
        scaler_output = joblib.load('scaler_y11.pkl')
        a = [[self.Time, self.PXJ, self.RS, self.PV, self.Power, self.Astmag, self.nextTime, self.nextPXJ, self.nextRS]]
        nextPV = Svr.predict(scaler_input.transform(a))
        # print('***PV***')
        # print(scaler_output.inverse_transform(np.array(nextPV).reshape(-1, 1)))
        # print(nextPV)
        # self.lineEdit_nextPV.setText('1')

        out = scaler_output.inverse_transform(np.array(nextPV).reshape(-1, 1))
        self.lineEdit_nextPV.setText(str(round(out[0][0], 3)))


    def getNextPower(self):
        # 读取数据
        if self.state == 'T':
            # df = pd.read_excel('T.xlsx')
            df = pd.read_excel(r"data\T.xlsx")
        elif self.state == 'L':
            # df = pd.read_excel('L.xlsx')
            df = pd.read_excel(r"data\L.xlsx")

        # 建立特征数据和标签数据
        X = df.drop(['PV', 'Power', 'Astmag'], axis=1)
        y = df['Power']

        # 归一化
        scaler_x = MinMaxScaler()
        scaler_y = MinMaxScaler()

        scaler_x = scaler_x.fit(X)
        X_train = scaler_x.transform(X)

        scaler_y = scaler_y.fit(np.array(y).reshape(-1, 1))
        y_train = scaler_y.transform(np.array(y).reshape(-1, 1))

        # 保存归一化参数
        joblib.dump(scaler_x, "scaler_x22.pkl")
        joblib.dump(scaler_y, "scaler_y22.pkl")

        # 构建SVR回归模型
        # 通过for循环来选择最好的核函数

        # for k in ['linear', 'poly', 'rbf', 'sigmoid']:
        #     clf = svm.SVR(kernel=k)
        #     clf.fit(X_train, y_train)
        #     confidence = clf.score(X_train, y_train)
        #     print('*************k, confidence*****************')
        #     print(k, confidence)

        # 建模
        Svr = SVR(kernel='rbf', C=2.7, gamma=0.5)

        Svr.fit(X_train, y_train)  # 拟合

        scaler_input = joblib.load('scaler_x22.pkl')
        scaler_output = joblib.load('scaler_y22.pkl')
        a = [[self.Time, self.PXJ, self.RS, self.PV, self.Power, self.Astmag, self.nextTime, self.nextPXJ, self.nextRS]]
        nextPower = Svr.predict(scaler_input.transform(a))
        # print('***Power***')
        # print(scaler_output.inverse_transform(np.array(nextPower).reshape(-1, 1)))
        # print(nextPower)
        # self.lineEdit_nextPower.setText('2')

        out = scaler_output.inverse_transform(np.array(nextPower).reshape(-1, 1))
        self.lineEdit_nextPower.setText(str(round(out[0][0], 3)))


    def getNextAstmag(self):
        # 读取数据
        if self.state == 'T':
            # df = pd.read_excel('T.xlsx')
            df = pd.read_excel(r"data\T.xlsx")
        elif self.state == 'L':
            # df = pd.read_excel('L.xlsx')
            df = pd.read_excel(r"data\L.xlsx")

        # 建立特征数据和标签数据
        X = df.drop(['PV', 'Power', 'Astmag'], axis=1)
        y = df['Astmag']

        # 归一化
        scaler_x = MinMaxScaler()
        scaler_y = MinMaxScaler()

        scaler_x = scaler_x.fit(X)
        X_train = scaler_x.transform(X)

        scaler_y = scaler_y.fit(np.array(y).reshape(-1, 1))
        y_train = scaler_y.transform(np.array(y).reshape(-1, 1))

        # 保存归一化参数
        joblib.dump(scaler_x, "scaler_x33.pkl")
        joblib.dump(scaler_y, "scaler_y33.pkl")

        # 构建SVR回归模型
        # 通过for循环来选择最好的核函数

        # for k in ['linear', 'poly', 'rbf', 'sigmoid']:
        #     clf = svm.SVR(kernel=k)
        #     clf.fit(X_train, y_train)
        #     confidence = clf.score(X_train, y_train)
        #     print('*************k, confidence*****************')
        #     print(k, confidence)

        # 建模
        Svr = SVR(kernel='rbf', C=2.3, gamma=0.5)

        Svr.fit(X_train, y_train)  # 拟合

        scaler_input = joblib.load('scaler_x33.pkl')
        scaler_output = joblib.load('scaler_y33.pkl')
        a = [[self.Time, self.PXJ, self.RS, self.PV, self.Power, self.Astmag, self.nextTime, self.nextPXJ, self.nextRS]]
        nextAstmag = Svr.predict(scaler_input.transform(a))
        # print('***Astmag***')
        # print(scaler_output.inverse_transform(np.array(nextAstmag).reshape(-1, 1)))
        # print(nextAstmag)
        out = scaler_output.inverse_transform(np.array(nextAstmag).reshape(-1, 1))
        self.lineEdit_nextAstmag.setText(str(round(out[0][0], 3)))




if __name__ == '__main__':
    # 此条命令用于解决代码执行冲突
    App = QApplication(sys.argv)
    win = MyWindow()
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("myappid")
    win.showNormal()
    sys.exit(App.exec_())