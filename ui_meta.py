# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'meta.ui'
#
# Created: Wed Nov 25 10:34:35 2009
#      by: PyQt4 UI code generator 4.4.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import ma_data_table_view

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(985, 621)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        MainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/meta.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        self.centralwidget.setFont(font)
        self.centralwidget.setCursor(QtCore.Qt.ArrowCursor)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setContentsMargins(2, -1, 2, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.nav_frame = QtGui.QFrame(self.centralwidget)
        self.nav_frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.nav_frame.setFrameShadow(QtGui.QFrame.Plain)
        self.nav_frame.setObjectName("nav_frame")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.nav_frame)
        self.verticalLayout_2.setSpacing(1)
        self.verticalLayout_2.setContentsMargins(0, 1, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setContentsMargins(-1, -1, -1, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tableView = ma_data_table_view.MADataTable(self.nav_frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableView.sizePolicy().hasHeightForWidth())
        self.tableView.setSizePolicy(sizePolicy)
        self.tableView.setAlternatingRowColors(True)
        self.tableView.setObjectName("tableView")
        self.verticalLayout.addWidget(self.tableView)
        self.frame = QtGui.QFrame(self.nav_frame)
        self.frame.setMinimumSize(QtCore.QSize(0, 65))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame_2 = QtGui.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(10, 0, 181, 61))
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.nav_left_btn = QtGui.QToolButton(self.frame_2)
        self.nav_left_btn.setGeometry(QtCore.QRect(0, 10, 20, 41))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/images/left_arrow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.nav_left_btn.setIcon(icon1)
        self.nav_left_btn.setIconSize(QtCore.QSize(64, 64))
        self.nav_left_btn.setAutoRaise(True)
        self.nav_left_btn.setObjectName("nav_left_btn")
        self.nav_up_btn = QtGui.QToolButton(self.frame_2)
        self.nav_up_btn.setGeometry(QtCore.QRect(40, 0, 51, 20))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/images/up_arrow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.nav_up_btn.setIcon(icon2)
        self.nav_up_btn.setIconSize(QtCore.QSize(64, 64))
        self.nav_up_btn.setAutoRaise(True)
        self.nav_up_btn.setObjectName("nav_up_btn")
        self.nav_down_btn = QtGui.QToolButton(self.frame_2)
        self.nav_down_btn.setGeometry(QtCore.QRect(40, 40, 51, 20))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/images/down_arrow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.nav_down_btn.setIcon(icon3)
        self.nav_down_btn.setIconSize(QtCore.QSize(64, 64))
        self.nav_down_btn.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.nav_down_btn.setAutoRaise(True)
        self.nav_down_btn.setArrowType(QtCore.Qt.NoArrow)
        self.nav_down_btn.setObjectName("nav_down_btn")
        self.nav_lbl = QtGui.QLabel(self.frame_2)
        self.nav_lbl.setGeometry(QtCore.QRect(20, 20, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(50)
        font.setBold(False)
        self.nav_lbl.setFont(font)
        self.nav_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.nav_lbl.setObjectName("nav_lbl")
        self.nav_right_btn = QtGui.QToolButton(self.frame_2)
        self.nav_right_btn.setGeometry(QtCore.QRect(110, 10, 20, 41))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/images/right_arrow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.nav_right_btn.setIcon(icon4)
        self.nav_right_btn.setIconSize(QtCore.QSize(64, 64))
        self.nav_right_btn.setAutoRaise(True)
        self.nav_right_btn.setObjectName("nav_right_btn")
        self.nav_add_btn = QtGui.QToolButton(self.frame_2)
        self.nav_add_btn.setGeometry(QtCore.QRect(130, 10, 51, 41))
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/images/function_icon_set/add_48.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.nav_add_btn.setIcon(icon5)
        self.nav_add_btn.setIconSize(QtCore.QSize(64, 64))
        self.nav_add_btn.setAutoRaise(True)
        self.nav_add_btn.setObjectName("nav_add_btn")
        self.layoutWidget = QtGui.QWidget(self.frame)
        self.layoutWidget.setGeometry(QtCore.QRect(190, 0, 171, 61))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtGui.QGridLayout(self.layoutWidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtGui.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.cur_outcome_lbl = QtGui.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.cur_outcome_lbl.setFont(font)
        self.cur_outcome_lbl.setObjectName("cur_outcome_lbl")
        self.gridLayout.addWidget(self.cur_outcome_lbl, 0, 1, 1, 1)
        self.label_3 = QtGui.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.cur_time_lbl = QtGui.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.cur_time_lbl.setFont(font)
        self.cur_time_lbl.setObjectName("cur_time_lbl")
        self.gridLayout.addWidget(self.cur_time_lbl, 1, 1, 1, 1)
        self.verticalLayout.addWidget(self.frame)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout.addWidget(self.nav_frame)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menu_bar = QtGui.QMenuBar(MainWindow)
        self.menu_bar.setGeometry(QtCore.QRect(0, 0, 985, 21))
        self.menu_bar.setObjectName("menu_bar")
        self.menu_file = QtGui.QMenu(self.menu_bar)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        self.menu_file.setFont(font)
        self.menu_file.setObjectName("menu_file")
        self.menuAnalysis = QtGui.QMenu(self.menu_bar)
        self.menuAnalysis.setObjectName("menuAnalysis")
        MainWindow.setMenuBar(self.menu_bar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action_save = QtGui.QAction(MainWindow)
        self.action_save.setObjectName("action_save")
        self.action_open = QtGui.QAction(MainWindow)
        self.action_open.setObjectName("action_open")
        self.action_quit = QtGui.QAction(MainWindow)
        self.action_quit.setObjectName("action_quit")
        self.action_go = QtGui.QAction(MainWindow)
        self.action_go.setObjectName("action_go")
        self.menu_file.addAction(self.action_save)
        self.menu_file.addAction(self.action_open)
        self.menu_file.addAction(self.action_quit)
        self.menuAnalysis.addAction(self.action_go)
        self.menu_bar.addAction(self.menu_file.menuAction())
        self.menu_bar.addAction(self.menuAnalysis.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "OpenMeta[analyst]", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "outcome:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("MainWindow", "follow-up:", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_file.setTitle(QtGui.QApplication.translate("MainWindow", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.menuAnalysis.setTitle(QtGui.QApplication.translate("MainWindow", "Analysis", None, QtGui.QApplication.UnicodeUTF8))
        self.action_save.setText(QtGui.QApplication.translate("MainWindow", "save", None, QtGui.QApplication.UnicodeUTF8))
        self.action_open.setText(QtGui.QApplication.translate("MainWindow", "open...", None, QtGui.QApplication.UnicodeUTF8))
        self.action_quit.setText(QtGui.QApplication.translate("MainWindow", "quit", None, QtGui.QApplication.UnicodeUTF8))
        self.action_go.setText(QtGui.QApplication.translate("MainWindow", "Go", None, QtGui.QApplication.UnicodeUTF8))

import icons_rc
