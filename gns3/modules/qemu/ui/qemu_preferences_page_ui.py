# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/grossmj/PycharmProjects/gns3-gui/gns3/modules/qemu/ui/qemu_preferences_page.ui'
#
# Created: Mon Feb 16 18:38:41 2015
#      by: PyQt4 UI code generator 4.10.4
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

class Ui_QemuPreferencesPageWidget(object):
    def setupUi(self, QemuPreferencesPageWidget):
        QemuPreferencesPageWidget.setObjectName(_fromUtf8("QemuPreferencesPageWidget"))
        QemuPreferencesPageWidget.resize(432, 586)
        self.verticalLayout = QtGui.QVBoxLayout(QemuPreferencesPageWidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.uiTabWidget = QtGui.QTabWidget(QemuPreferencesPageWidget)
        self.uiTabWidget.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.uiTabWidget.setObjectName(_fromUtf8("uiTabWidget"))
        self.uiServerSettingsTabWidget = QtGui.QWidget()
        self.uiServerSettingsTabWidget.setObjectName(_fromUtf8("uiServerSettingsTabWidget"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.uiServerSettingsTabWidget)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.uiUseLocalServercheckBox = QtGui.QCheckBox(self.uiServerSettingsTabWidget)
        self.uiUseLocalServercheckBox.setChecked(True)
        self.uiUseLocalServercheckBox.setObjectName(_fromUtf8("uiUseLocalServercheckBox"))
        self.verticalLayout_3.addWidget(self.uiUseLocalServercheckBox)
        self.uiRemoteServersGroupBox = QtGui.QGroupBox(self.uiServerSettingsTabWidget)
        self.uiRemoteServersGroupBox.setObjectName(_fromUtf8("uiRemoteServersGroupBox"))
        self.horizontalLayout_11 = QtGui.QHBoxLayout(self.uiRemoteServersGroupBox)
        self.horizontalLayout_11.setObjectName(_fromUtf8("horizontalLayout_11"))
        self.uiRemoteServersTreeWidget = QtGui.QTreeWidget(self.uiRemoteServersGroupBox)
        self.uiRemoteServersTreeWidget.setEnabled(False)
        self.uiRemoteServersTreeWidget.setSelectionMode(QtGui.QAbstractItemView.NoSelection)
        self.uiRemoteServersTreeWidget.setObjectName(_fromUtf8("uiRemoteServersTreeWidget"))
        self.horizontalLayout_11.addWidget(self.uiRemoteServersTreeWidget)
        self.verticalLayout_3.addWidget(self.uiRemoteServersGroupBox)
        self.uiTabWidget.addTab(self.uiServerSettingsTabWidget, _fromUtf8(""))
        self.verticalLayout.addWidget(self.uiTabWidget)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem = QtGui.QSpacerItem(254, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.uiRestoreDefaultsPushButton = QtGui.QPushButton(QemuPreferencesPageWidget)
        self.uiRestoreDefaultsPushButton.setObjectName(_fromUtf8("uiRestoreDefaultsPushButton"))
        self.horizontalLayout_2.addWidget(self.uiRestoreDefaultsPushButton)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(QemuPreferencesPageWidget)
        self.uiTabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(QemuPreferencesPageWidget)

    def retranslateUi(self, QemuPreferencesPageWidget):
        QemuPreferencesPageWidget.setWindowTitle(_translate("QemuPreferencesPageWidget", "QEMU", None))
        self.uiUseLocalServercheckBox.setText(_translate("QemuPreferencesPageWidget", "Always use the local server", None))
        self.uiRemoteServersGroupBox.setTitle(_translate("QemuPreferencesPageWidget", "Remote servers", None))
        self.uiRemoteServersTreeWidget.headerItem().setText(0, _translate("QemuPreferencesPageWidget", "Host", None))
        self.uiRemoteServersTreeWidget.headerItem().setText(1, _translate("QemuPreferencesPageWidget", "Port", None))
        self.uiTabWidget.setTabText(self.uiTabWidget.indexOf(self.uiServerSettingsTabWidget), _translate("QemuPreferencesPageWidget", "Server settings", None))
        self.uiRestoreDefaultsPushButton.setText(_translate("QemuPreferencesPageWidget", "Restore defaults", None))

