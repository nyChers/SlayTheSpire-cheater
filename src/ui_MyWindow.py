# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_MyWindow.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1104, 849)
        Dialog.setAcceptDrops(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:/Users/Chers/.designer/backup/cute.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setToolTip("")
        Dialog.setStatusTip("")
        Dialog.setWhatsThis("")
        Dialog.setModal(False)
        self.gridLayoutWidget = QtWidgets.QWidget(Dialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(18, 18, 235, 191))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setHorizontalSpacing(9)
        self.gridLayout.setObjectName("gridLayout")
        self.writefile = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.writefile.setObjectName("writefile")
        self.gridLayout.addWidget(self.writefile, 1, 1, 1, 1)
        self.current_health = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.current_health.setObjectName("current_health")
        self.gridLayout.addWidget(self.current_health, 3, 1, 1, 1)
        self.energy = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.energy.setObjectName("energy")
        self.gridLayout.addWidget(self.energy, 5, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 2, 0, 1, 1, QtCore.Qt.AlignRight|QtCore.Qt.AlignVCenter)
        self.openfile = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.openfile.setObjectName("openfile")
        self.gridLayout.addWidget(self.openfile, 1, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 5, 0, 1, 1, QtCore.Qt.AlignRight|QtCore.Qt.AlignVCenter)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 1, QtCore.Qt.AlignRight|QtCore.Qt.AlignVCenter)
        self.max_health = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.max_health.setObjectName("max_health")
        self.gridLayout.addWidget(self.max_health, 2, 1, 1, 1)
        self.gold = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.gold.setObjectName("gold")
        self.gridLayout.addWidget(self.gold, 4, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 4, 0, 1, 1, QtCore.Qt.AlignRight|QtCore.Qt.AlignVCenter)
        self.gridLayoutWidget_2 = QtWidgets.QWidget(Dialog)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(30, 740, 175, 80))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.encodeJson = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.encodeJson.setObjectName("encodeJson")
        self.gridLayout_2.addWidget(self.encodeJson, 1, 0, 1, 1)
        self.decodeautosave = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.decodeautosave.setObjectName("decodeautosave")
        self.gridLayout_2.addWidget(self.decodeautosave, 0, 0, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(260, 10, 831, 421))
        self.groupBox.setObjectName("groupBox")
        self.curr_card_list = QtWidgets.QTableWidget(self.groupBox)
        self.curr_card_list.setGeometry(QtCore.QRect(10, 30, 690, 381))
        self.curr_card_list.setAutoFillBackground(True)
        self.curr_card_list.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.curr_card_list.setAlternatingRowColors(True)
        self.curr_card_list.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.curr_card_list.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.curr_card_list.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.curr_card_list.setRowCount(0)
        self.curr_card_list.setColumnCount(4)
        self.curr_card_list.setObjectName("curr_card_list")
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.curr_card_list.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.curr_card_list.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.curr_card_list.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.curr_card_list.setHorizontalHeaderItem(3, item)
        self.gridLayoutWidget_3 = QtWidgets.QWidget(self.groupBox)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(710, 70, 114, 251))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.card_cancelall = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.card_cancelall.setObjectName("card_cancelall")
        self.gridLayout_3.addWidget(self.card_cancelall, 1, 0, 1, 1)
        self.card_update = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.card_update.setObjectName("card_update")
        self.gridLayout_3.addWidget(self.card_update, 3, 0, 1, 1)
        self.card_add = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.card_add.setObjectName("card_add")
        self.gridLayout_3.addWidget(self.card_add, 6, 0, 1, 1)
        self.card_delete = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.card_delete.setObjectName("card_delete")
        self.gridLayout_3.addWidget(self.card_delete, 2, 0, 1, 1)
        self.card_selectall = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.card_selectall.setObjectName("card_selectall")
        self.gridLayout_3.addWidget(self.card_selectall, 0, 0, 1, 1)
        self.card_replace = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.card_replace.setObjectName("card_replace")
        self.gridLayout_3.addWidget(self.card_replace, 4, 0, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_2.setGeometry(QtCore.QRect(20, 230, 231, 461))
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.groupBox_2)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 30, 211, 361))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.potions1 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.potions1.setText("")
        self.potions1.setObjectName("potions1")
        self.verticalLayout.addWidget(self.potions1)
        self.potions2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.potions2.setText("")
        self.potions2.setObjectName("potions2")
        self.verticalLayout.addWidget(self.potions2)
        self.potions3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.potions3.setText("")
        self.potions3.setObjectName("potions3")
        self.verticalLayout.addWidget(self.potions3)
        self.potions4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.potions4.setText("")
        self.potions4.setObjectName("potions4")
        self.verticalLayout.addWidget(self.potions4)
        self.potions5 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.potions5.setText("")
        self.potions5.setObjectName("potions5")
        self.verticalLayout.addWidget(self.potions5)
        self.add_potion = QtWidgets.QPushButton(self.groupBox_2)
        self.add_potion.setGeometry(QtCore.QRect(10, 410, 211, 34))
        self.add_potion.setObjectName("add_potion")
        self.groupBox_3 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_3.setGeometry(QtCore.QRect(260, 440, 831, 371))
        self.groupBox_3.setObjectName("groupBox_3")
        self.curr_relics_list = QtWidgets.QTableWidget(self.groupBox_3)
        self.curr_relics_list.setGeometry(QtCore.QRect(10, 30, 690, 331))
        self.curr_relics_list.setAutoFillBackground(True)
        self.curr_relics_list.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.curr_relics_list.setAlternatingRowColors(True)
        self.curr_relics_list.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.curr_relics_list.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.curr_relics_list.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.curr_relics_list.setRowCount(0)
        self.curr_relics_list.setColumnCount(4)
        self.curr_relics_list.setObjectName("curr_relics_list")
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.curr_relics_list.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.curr_relics_list.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.curr_relics_list.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.curr_relics_list.setHorizontalHeaderItem(3, item)
        self.gridLayoutWidget_4 = QtWidgets.QWidget(self.groupBox_3)
        self.gridLayoutWidget_4.setGeometry(QtCore.QRect(710, 50, 114, 191))
        self.gridLayoutWidget_4.setObjectName("gridLayoutWidget_4")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.gridLayoutWidget_4)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.relics_add = QtWidgets.QPushButton(self.gridLayoutWidget_4)
        self.relics_add.setObjectName("relics_add")
        self.gridLayout_4.addWidget(self.relics_add, 4, 0, 1, 1)
        self.relics_selectall = QtWidgets.QPushButton(self.gridLayoutWidget_4)
        self.relics_selectall.setObjectName("relics_selectall")
        self.gridLayout_4.addWidget(self.relics_selectall, 0, 0, 1, 1)
        self.relics_cancelall = QtWidgets.QPushButton(self.gridLayoutWidget_4)
        self.relics_cancelall.setObjectName("relics_cancelall")
        self.gridLayout_4.addWidget(self.relics_cancelall, 1, 0, 1, 1)
        self.relics_delete = QtWidgets.QPushButton(self.gridLayoutWidget_4)
        self.relics_delete.setObjectName("relics_delete")
        self.gridLayout_4.addWidget(self.relics_delete, 2, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.openfile, self.writefile)
        Dialog.setTabOrder(self.writefile, self.max_health)
        Dialog.setTabOrder(self.max_health, self.current_health)
        Dialog.setTabOrder(self.current_health, self.gold)
        Dialog.setTabOrder(self.gold, self.energy)
        Dialog.setTabOrder(self.energy, self.decodeautosave)
        Dialog.setTabOrder(self.decodeautosave, self.encodeJson)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "GodSlayTheSpire"))
        self.writefile.setText(_translate("Dialog", "写回存档"))
        self.label.setText(_translate("Dialog", "血量上限:"))
        self.openfile.setText(_translate("Dialog", "读取存档"))
        self.label_3.setText(_translate("Dialog", "能量上限:"))
        self.label_2.setText(_translate("Dialog", "当前血量:"))
        self.label_4.setText(_translate("Dialog", "金钱数量:"))
        self.encodeJson.setText(_translate("Dialog", "Json编码为autosave"))
        self.decodeautosave.setText(_translate("Dialog", "存档解码到Json"))
        self.groupBox.setTitle(_translate("Dialog", "卡牌管理"))
        item = self.curr_card_list.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Card ID"))
        item = self.curr_card_list.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "lv."))
        item = self.curr_card_list.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Card Name"))
        item = self.curr_card_list.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "description"))
        self.card_cancelall.setText(_translate("Dialog", "全部取消"))
        self.card_update.setText(_translate("Dialog", "升级选中"))
        self.card_add.setText(_translate("Dialog", "添加卡牌"))
        self.card_delete.setText(_translate("Dialog", "删除选中"))
        self.card_selectall.setText(_translate("Dialog", "全部选中"))
        self.card_replace.setText(_translate("Dialog", "替换选中"))
        self.groupBox_2.setTitle(_translate("Dialog", "药水管理"))
        self.add_potion.setText(_translate("Dialog", "添加药水"))
        self.groupBox_3.setTitle(_translate("Dialog", "遗物管理"))
        item = self.curr_relics_list.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Relics ID"))
        item = self.curr_relics_list.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Name"))
        item = self.curr_relics_list.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "FLAVOR"))
        item = self.curr_relics_list.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "DESCRIPTIONS"))
        self.relics_add.setText(_translate("Dialog", "添加遗物"))
        self.relics_selectall.setText(_translate("Dialog", "全部选中"))
        self.relics_cancelall.setText(_translate("Dialog", "全部取消"))
        self.relics_delete.setText(_translate("Dialog", "删除选中"))

