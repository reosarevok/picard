# -*- coding: utf-8 -*-

# Automatically generated - don't edit.
# Use `python setup.py build_ui` to update it.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(720, 320)
        self.vboxlayout = QtWidgets.QVBoxLayout(Dialog)
        self.vboxlayout.setContentsMargins(9, 9, 9, 9)
        self.vboxlayout.setSpacing(6)
        self.vboxlayout.setObjectName("vboxlayout")
        self.results_view = QtWidgets.QStackedWidget(Dialog)
        self.results_view.setObjectName("results_view")
        self.results_page = QtWidgets.QWidget()
        self.results_page.setObjectName("results_page")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.results_page)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label = QtWidgets.QLabel(self.results_page)
        self.label.setObjectName("label")
        self.verticalLayout_4.addWidget(self.label)
        self.release_list = QtWidgets.QTreeWidget(self.results_page)
        self.release_list.setObjectName("release_list")
        self.release_list.headerItem().setText(0, "1")
        self.verticalLayout_4.addWidget(self.release_list)
        self.results_view.addWidget(self.results_page)
        self.no_results_page = QtWidgets.QWidget()
        self.no_results_page.setObjectName("no_results_page")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.no_results_page)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.no_results_label = QtWidgets.QLabel(self.no_results_page)
        self.no_results_label.setStyleSheet("margin-bottom: 9px;")
        self.no_results_label.setObjectName("no_results_label")
        self.verticalLayout_3.addWidget(self.no_results_label, 0, QtCore.Qt.AlignHCenter)
        self.submit_button = QtWidgets.QToolButton(self.no_results_page)
        self.submit_button.setStyleSheet("")
        icon = QtGui.QIcon.fromTheme("media-optical")
        self.submit_button.setIcon(icon)
        self.submit_button.setIconSize(QtCore.QSize(128, 128))
        self.submit_button.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.submit_button.setObjectName("submit_button")
        self.verticalLayout_3.addWidget(self.submit_button, 0, QtCore.Qt.AlignHCenter)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem1)
        self.results_view.addWidget(self.no_results_page)
        self.vboxlayout.addWidget(self.results_view)
        self.hboxlayout = QtWidgets.QHBoxLayout()
        self.hboxlayout.setContentsMargins(0, 0, 0, 0)
        self.hboxlayout.setSpacing(6)
        self.hboxlayout.setObjectName("hboxlayout")
        spacerItem2 = QtWidgets.QSpacerItem(111, 31, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.hboxlayout.addItem(spacerItem2)
        self.ok_button = QtWidgets.QPushButton(Dialog)
        self.ok_button.setEnabled(False)
        self.ok_button.setObjectName("ok_button")
        self.hboxlayout.addWidget(self.ok_button)
        self.lookup_button = QtWidgets.QPushButton(Dialog)
        self.lookup_button.setObjectName("lookup_button")
        self.hboxlayout.addWidget(self.lookup_button)
        self.cancel_button = QtWidgets.QPushButton(Dialog)
        self.cancel_button.setObjectName("cancel_button")
        self.hboxlayout.addWidget(self.cancel_button)
        self.vboxlayout.addLayout(self.hboxlayout)

        self.retranslateUi(Dialog)
        self.results_view.setCurrentIndex(0)
        self.ok_button.clicked.connect(Dialog.accept)
        self.cancel_button.clicked.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.submit_button, self.release_list)
        Dialog.setTabOrder(self.release_list, self.ok_button)
        Dialog.setTabOrder(self.ok_button, self.lookup_button)
        Dialog.setTabOrder(self.lookup_button, self.cancel_button)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_("CD Lookup"))
        self.label.setText(_("The following releases on MusicBrainz match the CD:"))
        self.no_results_label.setText(_("No matching releases found for this disc."))
        self.submit_button.setText(_("Submit disc ID"))
        self.ok_button.setText(_("&Load into Picard"))
        self.lookup_button.setText(_("Lookup in &Browser"))
        self.cancel_button.setText(_("&Cancel"))
