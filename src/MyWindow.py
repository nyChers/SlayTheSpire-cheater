#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Author:  NingYu Zhang
# @Date:    Created on 2018/6/27 18:01
import json
from copy import deepcopy

from PyQt5.QtGui import QCursor
from PyQt5.QtWidgets import QFileDialog, QTableWidgetItem, QTableWidget, QTableWidgetSelectionRange, QMenu, QAction
from ui_MyWindow import Ui_Dialog
from PyQt5 import QtWidgets
from ui_selectcard import Ui_selectcard
from ui_sel_relics import Ui_ui_sel_relics
from PyQt5.QtCore import Qt
import decode_encode

realdata = {}
cards_data = {}
relics_data = {}
potions_data = {}

cards = []
len_cards = 0
potions = []
len_potions = 0
relics = []
len_relics = 0


class MyWindow(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        qdialog_sel_card = QtWidgets.QDialog()
        ui_sel_card = Ui_selectcard()
        ui_sel_card.setupUi(qdialog_sel_card)

        # 设置按钮连接
        self.ui.decodeautosave.clicked.connect(self.decodeautosave)
        self.ui.encodeJson.clicked.connect(self.encodeJson)
        self.ui.openfile.clicked.connect(self.openfile)
        self.ui.writefile.clicked.connect(self.writefile)

        self.ui.card_selectall.clicked.connect(self.card_selectall)
        self.ui.card_cancelall.clicked.connect(self.card_cancelall)
        self.ui.card_delete.clicked.connect(self.card_delete)
        self.ui.card_update.clicked.connect(self.card_update)
        self.ui.card_replace.clicked.connect(self.card_replace)
        self.ui.card_add.clicked.connect(self.card_add)

        self.ui.relics_selectall.clicked.connect(self.relics_selectall)
        self.ui.relics_cancelall.clicked.connect(self.relics_cancelall)
        self.ui.relics_delete.clicked.connect(self.relics_delete)
        self.ui.relics_add.clicked.connect(self.relics_add)

        # 设置cardstable
        # 列宽
        self.ui.curr_card_list.setColumnWidth(0, 170)
        self.ui.curr_card_list.setColumnWidth(1, 50)
        self.ui.curr_card_list.setColumnWidth(2, 140)
        self.ui.curr_card_list.setColumnWidth(3, 300)

        # 设置relicstable的列宽
        self.ui.curr_relics_list.setColumnWidth(0, 150)
        self.ui.curr_relics_list.setColumnWidth(1, 100)
        self.ui.curr_relics_list.setColumnWidth(2, 200)
        self.ui.curr_relics_list.setColumnWidth(3, 300)
        # 不可编辑
        self.ui.curr_card_list.setEditTriggers(QTableWidget.NoEditTriggers)
        self.ui.curr_relics_list.setEditTriggers(QTableWidget.NoEditTriggers)

        # 读取数据
        global cards_data, relics_data, potions_data
        import data
        cards_data = data.allcards
        relics_data = data.allrelics
        potions_data = data.allpotions

        # 设置存档未读标记
        self.is_saver_read = 0
        for w in self.findChildren((QtWidgets.QPushButton, QtWidgets.QTableWidget, QtWidgets.QLineEdit)):
            w.setEnabled(0)
        self.ui.openfile.setEnabled(1)

        self.m = QMenu()
        self.m.triggered.connect(self.potions_add)
        for k, v in potions_data.items():
            qa = QAction(v['NAME'] + '\t\t' + str(v['DESCRIPTIONS']) + '\t\t' + k, self)
            self.m.addAction(qa)
        self.ui.potions1.customContextMenuRequested.connect(self.set_potions_menu)
        self.ui.potions2.customContextMenuRequested.connect(self.set_potions_menu)
        self.ui.potions3.customContextMenuRequested.connect(self.set_potions_menu)
        self.ui.potions4.customContextMenuRequested.connect(self.set_potions_menu)
        self.ui.potions5.customContextMenuRequested.connect(self.set_potions_menu)
        self.p_potions = 0

    # 读取存档写到json文件
    def decodeautosave(self):
        fileName1 = QFileDialog.getOpenFileName(self, "选取存档", "./", "存档 (*.autosave)")  # 设置文件扩展名过滤,注意用双分号间隔
        if fileName1[0] == '':
            return
        with open(fileName1[0], "rb") as f:
            old_autosave = f.read()
        # print(old_autosave)

        old_json = decode_encode.decode(old_autosave, "key")
        old_json = str(old_json, 'utf-8')
        # print(old_json)

        data = json.loads(old_json)
        # print(data)

        fileName2 = QFileDialog.getSaveFileName(self, "选取存档", "./", "存档 (*.json)")
        if fileName2[0] == '':
            return
        with open(fileName2[0], 'w') as f:
            json.dump(data, f, indent=2)

    # 将json文件转回autosave
    def encodeJson(self):
        fileName2 = QFileDialog.getOpenFileName(self, "选取Json", "./", "数据 (*.json)")
        if fileName2[0] == '':
            return
        with open(fileName2[0], 'r') as f:
            data = f.read()

        resave = decode_encode.encode(data, "key")
        resave = str(resave, encoding='utf-8')

        fileName3 = QFileDialog.getSaveFileName(self, "保存存档", "./", "存档 (*.autosave)")
        if fileName3[0] == '':
            return
        with open(fileName3[0], 'w') as f:
            f.write(resave)

    # 打开存档解码并读入数据到realdata
    def openfile(self):
        fileName = QFileDialog.getOpenFileName(self, "选取存档", "./", "存档 (*.autosave)")
        if fileName[0] == '':
            return
        with open(fileName[0], "rb") as f:
            old_autosave = f.read()

        b_realdata = decode_encode.decode(old_autosave, "key")
        s_realdata = str(b_realdata, 'utf-8')
        global realdata
        realdata = json.loads(s_realdata)

        self.is_saver_read = 1
        for w in self.findChildren((QtWidgets.QPushButton, QtWidgets.QTableWidget, QtWidgets.QLineEdit)):
            w.setEnabled(1)
        self.read_display()

    # 写回存档
    def writefile(self):
        self.modify_4Attributes()
        global realdata
        s_realdata = json.dumps(realdata, indent=2)
        new_autosave = decode_encode.encode(s_realdata, "key")
        resave = str(new_autosave, encoding='utf-8')
        fileName = QFileDialog.getSaveFileName(self, "保存存档", "./", "存档 (*.autosave)")
        if fileName[0] == '':
            return
        with open(fileName[0], 'w') as f:
            f.write(resave)

    # 读取并显示数据
    def read_display(self):
        global cards_data, relics_data

        self.ui.max_health.setText(str(realdata['max_health']))
        self.ui.current_health.setText(str(realdata['current_health']))
        self.ui.gold.setText(str(realdata['gold']))
        self.ui.energy.setText(str(realdata['red']))

        global cards, len_cards
        cards = realdata['cards']
        global relics, len_relics
        relics = realdata['relics']
        global potions, len_potions
        potions = realdata['potions']

        len_relics = len(relics)
        len_cards = len(cards)
        len_potions = len(potions)

        self.display_cards()
        self.display_relics()
        self.display_potions()

    # 显示卡牌
    def display_cards(self):
        ui_cardtable = self.ui.curr_card_list
        ui_cardtable.setRowCount(len_cards)
        for i in range(len_cards):
            ui_cardtable.setItem(i, 0, QTableWidgetItem(cards[i]['id']))
            ui_cardtable.setItem(i, 1, QTableWidgetItem(str(cards[i]['upgrades'])))
            ui_cardtable.setItem(i, 2, QTableWidgetItem(cards_data[cards[i]['id']]['NAME']))
            ui_cardtable.setItem(i, 3, QTableWidgetItem(cards_data[cards[i]['id']]['DESCRIPTION']))

    def display_relics(self):
        ui_relicstable = self.ui.curr_relics_list
        ui_relicstable.setRowCount(len_relics)
        for i in range(len_relics):
            ui_relicstable.setItem(i, 0, QTableWidgetItem(relics[i]))
            ui_relicstable.setItem(i, 1, QTableWidgetItem(relics_data[relics[i]]['NAME']))
            ui_relicstable.setItem(i, 2, QTableWidgetItem(relics_data[relics[i]]['FLAVOR']))
            ui_relicstable.setItem(i, 3, QTableWidgetItem(str(relics_data[relics[i]]['DESCRIPTIONS'])))

    def display_potions(self):
        self.ui.potions1.setText('')
        self.ui.potions1.setToolTip('')
        self.ui.potions2.setText('')
        self.ui.potions2.setToolTip('')
        self.ui.potions3.setText('')
        self.ui.potions3.setToolTip('')
        self.ui.potions4.setText('')
        self.ui.potions4.setToolTip('')
        self.ui.potions5.setText('')
        self.ui.potions5.setToolTip('')

        self.ui.potions1.setText(potions[0])
        self.ui.potions1.setToolTip(potions_data[potions[0]]['NAME'] + str(potions_data[potions[0]]['DESCRIPTIONS']))
        self.ui.potions2.setText(potions[1])
        self.ui.potions2.setToolTip(potions_data[potions[1]]['NAME'] + str(potions_data[potions[1]]['DESCRIPTIONS']))
        self.ui.potions3.setText(potions[2])
        self.ui.potions3.setToolTip(potions_data[potions[2]]['NAME'] + str(potions_data[potions[2]]['DESCRIPTIONS']))
        if len_potions > 3:
            self.ui.potions4.setText(potions[3])
            self.ui.potions4.setToolTip(
                potions_data[potions[3]]['NAME'] + str(potions_data[potions[0]]['DESCRIPTIONS']))
            self.ui.potions5.setText(potions[4])
            self.ui.potions5.setToolTip(
                potions_data[potions[4]]['NAME'] + str(potions_data[potions[0]]['DESCRIPTIONS']))

    # 修改基础四属性
    def modify_4Attributes(self):
        global realdata
        realdata['max_health'] = int(self.ui.max_health.text())
        realdata['current_health'] = int(self.ui.current_health.text())
        realdata['gold'] = int(self.ui.gold.text())
        realdata['red'] = int(self.ui.energy.text())

    # 全选卡牌
    def card_selectall(self):
        ui_cardtable = self.ui.curr_card_list
        ui_cardtable.setRangeSelected(QTableWidgetSelectionRange(0, 0, len_cards - 1, 3), True)

    # 取消全选卡牌
    def card_cancelall(self):
        ui_cardtable = self.ui.curr_card_list
        ui_cardtable.setRangeSelected(QTableWidgetSelectionRange(0, 0, len_cards - 1, 3), False)

    # 获取选中卡牌
    def get_cardselect(self):
        ui_cardtable = self.ui.curr_card_list
        list_items = ui_cardtable.selectedItems()
        cnt_items = len(list_items)
        cnt_cards = int(cnt_items / 4)
        index = []
        for i in range(cnt_cards):
            index.append(ui_cardtable.row(list_items[4 * i]))
        return index

    # 删除选中卡牌
    def card_delete(self):
        ui_cardtable = self.ui.curr_card_list
        index = self.get_cardselect()
        index.reverse()
        global len_cards
        len_cards -= len(index)
        for i in index:
            cards.pop(i)

        self.display_cards()
        self.card_cancelall()

    # 升级选中卡牌
    def card_update(self):
        ui_cardtable = self.ui.curr_card_list
        index = self.get_cardselect()
        for i in index:
            cards[i]['upgrades'] = 1
        self.display_cards()

    # 替换选中卡牌
    def card_replace(self):
        ui_cardtable = self.ui.curr_card_list
        index = self.get_cardselect()
        SelDialog.is_add = 0
        seldialog = SelDialog()
        seldialog.exec()
        if not seldialog.is_ok:
            return
        global cards, len_cards
        for i in index:
            cards[i]['id'] = seldialog.id_add
        self.display_cards()
        seldialog.destroy()

    # 添加卡牌
    def card_add(self):
        SelDialog.is_add = 1
        seldialog = SelDialog()
        seldialog.exec_()
        if not seldialog.is_ok:
            return
        global cards, len_cards
        for i in range(seldialog.num_sel):
            cards.insert(0, {'upgrades': 0, 'misc': 0, 'id': seldialog.id_add})
        len_cards = len(cards)
        self.display_cards()
        seldialog.destroy()

    # 全选遗物
    def relics_selectall(self):
        self.ui.curr_relics_list.setRangeSelected(QTableWidgetSelectionRange(0, 0, len_relics - 1, 3), True)

    # 取消全选遗物
    def relics_cancelall(self):
        self.ui.curr_relics_list.setRangeSelected(QTableWidgetSelectionRange(0, 0, len_relics - 1, 3), False)

    # 删除选中遗物
    def relics_delete(self):
        r_table = self.ui.curr_relics_list
        list_items = r_table.selectedItems()
        cnt_items = len(list_items)
        cnt_relics = int(cnt_items / 4)
        index = []
        for i in range(cnt_relics):
            index.append(r_table.row(list_items[4 * i]))
        index.reverse()
        global relics, len_relics
        len_relics -= len(index)
        for i in index:
            relics.pop(i)

        self.display_relics()
        self.relics_cancelall()

    # 添加遗物
    def relics_add(self):
        adddia = Addrelics()
        adddia.exec_()
        self.display_relics()

    def set_potions_menu(self, pos):
        m = self.m
        m.exec_(QCursor.pos())

    def potions_add(self, qa):
        global potions, len_potions
        name = qa.text().split('\t')[4]
        if self.p_potions == 3 and len_potions < 5:
            len_potions = 5
            potions.append('Potion Slot')
            potions.append('Potion Slot')
        potions[self.p_potions] = name
        self.p_potions = (self.p_potions + 1) % 5
        self.display_potions()

# 添加选择卡牌Dialog
class SelDialog(QtWidgets.QDialog):
    is_add = 1
    id_add = ''
    dict_curr_display = {}

    def __init__(self, parent=None):
        super(SelDialog, self).__init__(parent)
        self.ui = Ui_selectcard()
        self.ui.setupUi(self)
        self.setWindowFlags(Qt.MSWindowsFixedSizeDialogHint | Qt.WindowStaysOnTopHint)
        self.ui.sel_card_list.setSelectionMode(QTableWidget.SingleSelection)
        self.ui.cancel_sel_card.clicked.connect(self.close)
        self.ui.ok_sel_card.clicked.connect(self.btn_ok)
        self.ui.color_sel_card.activated.connect(self.sel_color)
        self.ui.type_sel_card.activated.connect(self.sel_type)

        # 是否确认
        self.is_ok = 0

        # 设置num初值为1
        if self.is_add:
            self.ui.num_sel_card.setText('1')
            self.num_sel = int(self.ui.num_sel_card.text())
        else:
            self.ui.num_sel_card.setEnabled(0)

        # 默认显示所有卡牌数据
        self.ui.sel_card_list.setColumnWidth(0, 170)
        self.ui.sel_card_list.setColumnWidth(1, 140)
        self.ui.sel_card_list.setColumnWidth(2, 370)
        global cards_data
        self.all_cards = deepcopy(cards_data)
        lens = len(cards_data)
        self.ui.sel_card_list.setRowCount(lens)
        i = -1
        for k, v in cards_data.items():
            i += 1
            self.ui.sel_card_list.setItem(i, 0, QTableWidgetItem(k))
            self.ui.sel_card_list.setItem(i, 1, QTableWidgetItem(v['NAME']))
            self.ui.sel_card_list.setItem(i, 2, QTableWidgetItem(v['DESCRIPTION']))

    def btn_ok(self):
        self.is_ok = 1
        items = self.ui.sel_card_list.selectedItems()
        self.id_add = items[0].text()
        if self.is_add:
            self.num_sel = int(self.ui.num_sel_card.text())
        # print(self.id_add, self.num_sel)
        self.close()

    def btn_cancel(self):
        pass

    def sel_color(self, s):
        global cards_data
        self.dict_curr_display.clear()
        if s == 0:
            self.ui.type_sel_card.clear()
            lens = len(self.all_cards)
            self.ui.sel_card_list.setRowCount(lens)
            i = -1
            for k, v in self.all_cards.items():
                i += 1
                self.ui.sel_card_list.setItem(i, 0, QTableWidgetItem(k))
                self.ui.sel_card_list.setItem(i, 1, QTableWidgetItem(v['NAME']))
                self.ui.sel_card_list.setItem(i, 2, QTableWidgetItem(v['DESCRIPTION']))
        elif s == 1:
            self.ui.type_sel_card.clear()
            self.ui.type_sel_card.addItem('ALL')
            self.ui.type_sel_card.addItem('Attack')
            self.ui.type_sel_card.addItem('Skill')
            self.ui.type_sel_card.addItem('Power')
            for k, v in self.all_cards.items():
                if v.get('color') == 'red':
                    self.dict_curr_display[k] = v
            lens = len(self.dict_curr_display)
            self.ui.sel_card_list.setRowCount(lens)
            i = -1
            for k, v in self.dict_curr_display.items():
                i += 1
                self.ui.sel_card_list.setItem(i, 0, QTableWidgetItem(k))
                self.ui.sel_card_list.setItem(i, 1, QTableWidgetItem(v['NAME']))
                self.ui.sel_card_list.setItem(i, 2, QTableWidgetItem(v['DESCRIPTION']))



        elif s == 2:
            self.ui.type_sel_card.clear()
            self.ui.type_sel_card.addItem('ALL')
            self.ui.type_sel_card.addItem('Attack')
            self.ui.type_sel_card.addItem('Skill')
            self.ui.type_sel_card.addItem('Power')
            for k, v in self.all_cards.items():
                if v.get('color') == 'blue':
                    self.dict_curr_display[k] = v
            lens = len(self.dict_curr_display)
            self.ui.sel_card_list.setRowCount(lens)
            i = -1
            for k, v in self.dict_curr_display.items():
                i += 1
                self.ui.sel_card_list.setItem(i, 0, QTableWidgetItem(k))
                self.ui.sel_card_list.setItem(i, 1, QTableWidgetItem(v['NAME']))
                self.ui.sel_card_list.setItem(i, 2, QTableWidgetItem(v['DESCRIPTION']))

        elif s == 3:
            self.ui.type_sel_card.clear()
            self.ui.type_sel_card.addItem('ALL')
            self.ui.type_sel_card.addItem('Attack')
            self.ui.type_sel_card.addItem('Skill')
            self.ui.type_sel_card.addItem('Power')
            for k, v in self.all_cards.items():
                if v.get('color') == 'green':
                    self.dict_curr_display[k] = v
            lens = len(self.dict_curr_display)
            self.ui.sel_card_list.setRowCount(lens)
            i = -1
            for k, v in self.dict_curr_display.items():
                i += 1
                self.ui.sel_card_list.setItem(i, 0, QTableWidgetItem(k))
                self.ui.sel_card_list.setItem(i, 1, QTableWidgetItem(v['NAME']))
                self.ui.sel_card_list.setItem(i, 2, QTableWidgetItem(v['DESCRIPTION']))

        elif s == 4:
            self.ui.type_sel_card.clear()
            self.ui.type_sel_card.addItem('ALL')
            self.ui.type_sel_card.addItem('Attack')
            self.ui.type_sel_card.addItem('Skill')
            self.ui.type_sel_card.addItem('Power')
            for k, v in self.all_cards.items():
                if v.get('color') == 'colorless':
                    self.dict_curr_display[k] = v
            lens = len(self.dict_curr_display)
            self.ui.sel_card_list.setRowCount(lens)
            i = -1
            for k, v in self.dict_curr_display.items():
                i += 1
                self.ui.sel_card_list.setItem(i, 0, QTableWidgetItem(k))
                self.ui.sel_card_list.setItem(i, 1, QTableWidgetItem(v['NAME']))
                self.ui.sel_card_list.setItem(i, 2, QTableWidgetItem(v['DESCRIPTION']))

        else:
            self.ui.type_sel_card.clear()
            for k, v in self.all_cards.items():
                if v.get('color') == 'curse':
                    self.dict_curr_display[k] = v
            lens = len(self.dict_curr_display)
            self.ui.sel_card_list.setRowCount(lens)
            i = -1
            for k, v in self.dict_curr_display.items():
                i += 1
                self.ui.sel_card_list.setItem(i, 0, QTableWidgetItem(k))
                self.ui.sel_card_list.setItem(i, 1, QTableWidgetItem(v['NAME']))
                self.ui.sel_card_list.setItem(i, 2, QTableWidgetItem(v['DESCRIPTION']))

    def sel_type(self, s):
        self.ui.sel_card_list.setRowCount(len(self.dict_curr_display))
        if s == 0:
            i = -1
            for k, v in self.dict_curr_display.items():
                i += 1
                self.ui.sel_card_list.setItem(i, 0, QTableWidgetItem(k))
                self.ui.sel_card_list.setItem(i, 1, QTableWidgetItem(v['NAME']))
                self.ui.sel_card_list.setItem(i, 2, QTableWidgetItem(v['DESCRIPTION']))
        else:
            self.ui.sel_card_list.clearContents()
            self.ui.sel_card_list.setRowCount(0)
            i = -1
            for k, v in self.dict_curr_display.items():
                if v.get('type') == self.ui.type_sel_card.currentText().lower():
                    i += 1
                    self.ui.sel_card_list.insertRow(i)
                    self.ui.sel_card_list.setItem(i, 0, QTableWidgetItem(k))
                    self.ui.sel_card_list.setItem(i, 1, QTableWidgetItem(v['NAME']))
                    self.ui.sel_card_list.setItem(i, 2, QTableWidgetItem(v['DESCRIPTION']))


# 添加遗物Dialog
class Addrelics(QtWidgets.QDialog):

    def __init__(self, parent=None):
        super(Addrelics, self).__init__(parent)
        self.ui = Ui_ui_sel_relics()
        self.ui.setupUi(self)

        self.setWindowFlags(Qt.MSWindowsFixedSizeDialogHint | Qt.WindowStaysOnTopHint)
        self.ui.sel_relics_list.setSelectionMode(QTableWidget.MultiSelection)

        self.ui.sel_relics_list.setColumnWidth(0, 150)
        self.ui.sel_relics_list.setColumnWidth(1, 100)
        self.ui.sel_relics_list.setColumnWidth(2, 200)
        self.ui.sel_relics_list.setColumnWidth(3, 300)
        # 不可编辑
        self.ui.sel_relics_list.setEditTriggers(QTableWidget.NoEditTriggers)

        self.ui.text_search.textEdited.connect(self.search)
        self.ui.btn_back.clicked.connect(self.close)
        self.ui.btn_add.clicked.connect(self.add)

        self.search('')

    def search(self, s):
        ui_relicstable = self.ui.sel_relics_list
        ui_relicstable.setRowCount(0)
        if s == '':
            i = -1
            ui_relicstable.setRowCount(len(relics_data))
            for k, v in relics_data.items():
                i += 1
                ui_relicstable.setItem(i, 0, QTableWidgetItem(k))
                ui_relicstable.setItem(i, 1, QTableWidgetItem(v['NAME']))
                ui_relicstable.setItem(i, 2, QTableWidgetItem(v.get('FLAVOR')))
                ui_relicstable.setItem(i, 3, QTableWidgetItem(str(v['DESCRIPTIONS'])))
        else:
            i = 0
            for k, v in relics_data.items():
                if s in k or s in v['NAME']:
                    ui_relicstable.insertRow(i)
                    ui_relicstable.setItem(i, 0, QTableWidgetItem(k))
                    ui_relicstable.setItem(i, 1, QTableWidgetItem(v['NAME']))
                    ui_relicstable.setItem(i, 2, QTableWidgetItem(v.get('FLAVOR')))
                    ui_relicstable.setItem(i, 3, QTableWidgetItem(str(v['DESCRIPTIONS'])))
                    i += 1

    def add(self):
        global relics, len_relics
        relics_table = self.ui.sel_relics_list
        sel_items = relics_table.selectedItems()
        cnt_items = len(sel_items)
        cnt_relics = int(cnt_items / 4)
        name = ''
        cnt = 0
        for i in range(cnt_relics):
            id = sel_items[4 * i].text()
            relics.append(id)
            len_relics += 1
            cnt += 1
            name = sel_items[4 * i + 1].text()
        self.ui.msg.setText(name + '等 ' + str(cnt) + '件已添加')
