from MainWindow import Ui_mainWindow
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QFileDialog, QMessageBox
from PyQt5 import QtCore
import sys
import utils
import os


class myWidget(QWidget, Ui_mainWindow):
    def __init__(self, parent=None):
        super(myWidget, self).__init__(parent)
        self.setupUi(self)
        self.file_list = []
        self.convert_btn.setVisible(False)

    @QtCore.pyqtSlot()
    def on_file_btn_clicked(self):
        path = QFileDialog.getExistingDirectory(self, "Open", "./")
        if not path:
            return
        self.file_list.clear()

        filter_name = "bin"
        self.file_list = utils.getfile(path, filter_name)
        for file in self.file_list:
            utils.convert_bin_file_to_img(file, self.wdith_spinBox.value(), self.height_spinBox.value(),
                                          self.frame_spixBox.value())

        QMessageBox.information(self, "information", ("%d file found" % len(self.file_list)))

    @QtCore.pyqtSlot()
    def on_convert_btn_clicked(self):
        path = QFileDialog.getExistingDirectory(self, "Save", "./")
        if not path:
            return

        for file in self.file_list:
            utils.copyfile(file, path + "/" + file.replace("/", "_").replace(":", "_"))

        QMessageBox.information(self, "information", ("%d files saved" % len(self.file_list)))

    @QtCore.pyqtSlot()
    def on_open_btn_clicked(self):
        print("open..")
        path = QFileDialog.getExistingDirectory(self, "Open", "./")
        if not path:
            return
        self.file_list.clear()

        filter_name = ""
        if self.name_checkBox.isChecked():
            filter_name = self.lineEdit.text()
        self.file_list = utils.getfile(path, filter_name)

        QMessageBox.information(self, "information", ("%d file found" % len(self.file_list)))

    @QtCore.pyqtSlot()
    def on_save_btn_clicked(self):
        path = QFileDialog.getExistingDirectory(self, "Save", "./")
        if not path:
            return

        for file in self.file_list:
            utils.copyfile(file, path + "/" + file.replace("/", "_").replace(":", "_"))

        QMessageBox.information(self, "information", "convert done!")
        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWin = myWidget()
    myWin.show()
    sys.exit(app.exec_())