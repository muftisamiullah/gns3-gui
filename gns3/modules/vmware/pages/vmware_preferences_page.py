# -*- coding: utf-8 -*-
#
# Copyright (C) 2015 GNS3 Technologies Inc.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""
Configuration page for VMware preferences.
"""

import os
import sys
from gns3.qt import QtWidgets

from .. import VMware
from ..ui.vmware_preferences_page_ui import Ui_VMwarePreferencesPageWidget
from ..settings import VMWARE_SETTINGS


class VMwarePreferencesPage(QtWidgets.QWidget, Ui_VMwarePreferencesPageWidget):

    """
    QWidget preference page for VMware.
    """

    def __init__(self):

        super().__init__()
        self.setupUi(self)

        # connect signals
        self.uiUseLocalServercheckBox.stateChanged.connect(self._useLocalServerSlot)
        self.uiRestoreDefaultsPushButton.clicked.connect(self._restoreDefaultsSlot)
        self.uiVmrunPathToolButton.clicked.connect(self._vmrunPathBrowserSlot)

        if sys.platform.startswith("darwin"):
            self.uiHostTypeComboBox.addItem("VMware Fusion", "fusion")
        else:
            self.uiHostTypeComboBox.addItem("VMware Player", "player")
            self.uiHostTypeComboBox.addItem("VMware Workstation", "ws")

    def _vmrunPathBrowserSlot(self):
        """
        Slot to open a file browser and select vmrun.
        """

        path, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Select vmrun", ".")
        if not path:
            return

        if not os.access(path, os.X_OK):
            QtWidgets.QMessageBox.critical(self, "vmrun", "{} is not an executable".format(os.path.basename(path)))
            return

        self.uiVmrunPathLineEdit.setText(os.path.normpath(path))

    def _restoreDefaultsSlot(self):
        """
        Slot to populate the page widgets with the default settings.
        """

        self._populateWidgets(VMWARE_SETTINGS)

    def _useLocalServerSlot(self, state):
        """
        Slot to enable or not local server settings.
        """

        if state:
            self.uiVmrunPathLineEdit.setEnabled(True)
            self.uiVmrunPathToolButton.setEnabled(True)
            self.uiHostTypeComboBox.setEnabled(True)
        else:
            self.uiVmrunPathLineEdit.setEnabled(False)
            self.uiVmrunPathToolButton.setEnabled(False)
            self.uiHostTypeComboBox.setEnabled(False)

    def _populateWidgets(self, settings):
        """
        Populates the widgets with the settings.

        :param settings: VMware settings
        """

        self.uiVmrunPathLineEdit.setText(settings["vmrun_path"])
        index = self.uiHostTypeComboBox.findData(settings["host_type"])
        if index != -1:
            self.uiHostTypeComboBox.setCurrentIndex(index)
        self.uiUseLocalServercheckBox.setChecked(settings["use_local_server"])

    def loadPreferences(self):
        """
        Loads VMware preferences.
        """

        vmware_settings = VMware.instance().settings()
        self._populateWidgets(vmware_settings)

    def savePreferences(self):
        """
        Saves VMware preferences.
        """

        new_settings = {}
        new_settings["vmrun_path"] = self.uiVmrunPathLineEdit.text()
        new_settings["host_type"] = self.uiHostTypeComboBox.itemData(self.uiHostTypeComboBox.currentIndex())
        new_settings["use_local_server"] = self.uiUseLocalServercheckBox.isChecked()
        VMware.instance().setSettings(new_settings)