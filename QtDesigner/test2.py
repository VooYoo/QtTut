# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\GitHub\QtTut\QtDesigner\test.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(857, 530)
        self.verticalLayoutWidget = QtGui.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(450, 140, 175, 80))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.vert_1 = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.vert_1.setObjectName(_fromUtf8("vert_1"))
        self.hor_1 = QtGui.QHBoxLayout()
        self.hor_1.setObjectName(_fromUtf8("hor_1"))
        self.radioButton = QtGui.QRadioButton(self.verticalLayoutWidget)
        self.radioButton.setObjectName(_fromUtf8("radioButton"))
        self.hor_1.addWidget(self.radioButton)
        self.vert2 = QtGui.QVBoxLayout()
        self.vert2.setObjectName(_fromUtf8("vert2"))
        self.checkBox = QtGui.QCheckBox(self.verticalLayoutWidget)
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.vert2.addWidget(self.checkBox)
        self.hor_1.addLayout(self.vert2)
        self.vert_1.addLayout(self.hor_1)
        self.pushButton = QtGui.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(20)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setMaximumSize(QtCore.QSize(50, 16777215))
        self.pushButton.setAutoDefault(False)
        self.pushButton.setDefault(False)
        self.pushButton.setFlat(False)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.vert_1.addWidget(self.pushButton)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.radioButton.setText(_translate("Form", "RadioButton", None))
        self.checkBox.setText(_translate("Form", "CheckBox", None))
        self.pushButton.setText(_translate("Form", "PushButton", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

