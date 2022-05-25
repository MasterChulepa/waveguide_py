from PyQt5.QtWidgets import *
import WaveguideGUI
import numpy as np
import Graphs_TM
import Graphs_TE


class MatplotlibWidget(QMainWindow, WaveguideGUI.Ui_MainWindow):

    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.setWindowTitle("Waveguide propagation")
        self.pushButton.clicked.connect(self.update_graph)
        self.h = 1.2901262746146271
        self.Bc_sq = 1.8886317799411532
        self.a = 2.286
        self.b = self.a / 2
        self.radioButton_2.setChecked(True)
        self.c = 3 * (10 ** 10)
        self.mu = 1  # Magnetic permeability
        self.eps = 1  # Electric permeability

    def update_graph(self):
        n = self.spinBox_2.value()
        m = self.spinBox.value()
        f = float(self.lineEdit.text())
        omega = 2 * np.pi * f
        fc = self.c / (2 * (np.sqrt(self.mu * self.eps))) * np.sqrt(
            (m / self.a) ** 2 + (n / self.b) ** 2) / 10 ** 9  # Cutoff frequency calculation in GHz
        fc_round = round(fc, 2)
        if f < fc:
            result = "Mode does not propagate"
            self.label_6.setText(result)
            return
        else:
            result = f"Cutoff frequency calculation in GHz: {fc_round} GHz"
            self.label_6.setText(result)
        flag = self.radioButton.isChecked()
        if flag:
            painter = Graphs_TM.Graphs_TM()
            name_of_wave = f'TM{m}{n}'
        else:
            painter = Graphs_TE.Graphs_TE()
            name_of_wave = f'TE{m}{n}'
        self.MplWidget1.canvas.axes.clear()
        self.MplWidget2.canvas.axes.clear()
        self.MplWidget3.canvas.axes.clear()
        if flag and (n == 0 or m == 0):
            result = "Mode does not exist"
            self.label_6.setText(result)
            return
        if n == 0:
            painter.TE(self.a, self.b, m, n, self.c, self.h, omega, self.MplWidget1.canvas, 'xy')
            painter.TE(self.a, self.b, m, n, self.c, self.h, omega, self.MplWidget3.canvas, 'yz')
            painter.findz(self.a, m, self.h, self.Bc_sq, self.MplWidget2.canvas)
        elif m == 0:
            painter.TE(self.a, self.b, m, n, self.c, self.h, omega, self.MplWidget1.canvas, 'xy', rotate=True)
            painter.TE(self.a, self.b, m, n, self.c, self.h, omega, self.MplWidget3.canvas, 'yz', rotate=True)
        else:
            painter.findH(self.a, self.b, n, m, self.MplWidget1.canvas)
            painter.findE(self.a, self.b, n, m, self.MplWidget1.canvas, 4)
            painter.findz(self.a, m, self.h, self.Bc_sq, self.MplWidget2.canvas)
            painter.findz_doted(self.a, self.MplWidget2.canvas)
            painter.findz(self.b, n, self.h, self.Bc_sq, self.MplWidget3.canvas)
            painter.findz_doted(self.b, self.MplWidget3.canvas)
        self.MplWidget1.canvas.axes.set_title(f'{name_of_wave} projected on the XY plane', fontsize=12, color='white')
        self.MplWidget2.canvas.axes.set_title(f'{name_of_wave} projected on the ZX plane', fontsize=12, color='white')
        self.MplWidget3.canvas.axes.set_title(f'{name_of_wave} projected on the ZY plane', fontsize=12, color='white')
        self.MplWidget1.canvas.draw()
        self.MplWidget2.canvas.draw()
        self.MplWidget3.canvas.draw()


app = QApplication([])
window = MatplotlibWidget()
window.show()
app.exec_()
