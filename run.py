import sys
import numpy as np
import matplotlib.patches as mpatches

from PyQt5 import uic
from PyQt5.QtCore import QObject, QThread, pyqtSignal, pyqtSlot
from PyQt5.QtWidgets import QMainWindow, QApplication, QProgressBar
from matplotlib.pyplot import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

from podalgorytmy import *


class Ui(QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('gui.ui', self)
        self.show()
        self.initWorker()
        self.initMatplotlib()
        self.tbCalculate.clicked.connect(self.runAlgorithm)
        self.working = False

    def startProgress(self):
        self.progressBar = QProgressBar()
        self.progressBar.setRange(0,0)
        self.statusbar.addPermanentWidget(self.progressBar)
        self.statusbar.showMessage('Obliczam entropię...')

    def initMatplotlib(self):
        self.fig = Figure(figsize=(9,7))
        self.canvas = FigureCanvas(self.fig)
        self.mapLayout.addWidget(self.canvas)

    def initWorker(self):
        self.worker = Worker()
        self.thread = QThread()
        self.worker.moveToThread(self.thread)
        self.worker.finished.connect(self.generateRaster)

    def runAlgorithm(self):
        if self.working:
            return
        self.statusbar.clearMessage()
        classes = self.sbClasses.value()
        expected_entropy = self.dsbEntropy.value()
        x, y = self.sbX.value(), self.sbY.value()
        size = x * y
        #Obsługa przypadku gdzie classes == 1:
        if classes == 1:
            if expected_entropy == 0.:
                values = np.asarray([1])
                self.statusbar.showMessage("Cały obrazek w jednym kolorze")
                self.generateRaster(values)
                return 
            else:
                self.statusbar.showMessage("Wartość niemożliwa do osiągnięcia")
                return 
        max_entropy_case = np.asarray([1/classes]*classes)
        if expected_entropy > calculate_entropy(max_entropy_case) or expected_entropy < 0:
            self.statusbar.showMessage("Wartość niemożliwa do osiągnięcia")
            return 
        if expected_entropy == 0:
            self.statusbar.showMessage("Wartość niemożliwa do osiągnięcia")
            return 
        min_entropy_case = [0] * size
        for class_ in range(classes):
            min_entropy_case[class_] = class_ 
        min_entropy = array_to_entropy(min_entropy_case)
        if min_entropy > expected_entropy:
            self.statusbar.showMessaget("Minimalna entropia dla " + str(classes) + " klas w macierzy o wielkości " + str(size) + " to " + str(min_entropy))
            return 
        self.startProgress()
        init_cases = random_results(200, classes, size)
        classes = list(set(init_cases[0]))
        best_cases = selection(init_cases, expected_entropy, 30)
        if len(best_cases) == 1:
            self.generateRaster(np.array(best_cases[0]))
            return 
        print(best_cases)
        #Async
        self.thread.started.connect(lambda: self.worker.findResult(
            best_cases, 
            classes, 
            expected_entropy))
        self.thread.start()
    
    def generateRaster(self, result):
        x, y = self.sbX.value(), self.sbY.value()
        self.fig.clear()
        self.ax = self.fig.add_subplot(111)
        found_ent = array_to_entropy(result)
        result = result.reshape(x,y)
        values = np.unique(result.ravel())
        im = self.ax.imshow(result, extent=[0,x, 0, y])
        colors = [im.cmap(im.norm(value)) for value in values]
        patches = [mpatches.Patch(color=colors[i], label="Class {l}".format(l=values[i]+1)) for i in range(len(values))]
        self.ax.legend(handles=patches, bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
        self.canvas.draw()
        self.statusbar.removeWidget(self.progressBar)
        self.statusbar.showMessage(f"Obliczona entropia: {found_ent}")
        self.working = False
        self.thread.quit()

        
class Worker(QObject):

    finished = pyqtSignal(object)

    def findResult(self, best_cases, classes, expected_entropy):
        count = 1
        best_min = min(abs(array_to_entropy(array)-expected_entropy) for array in best_cases)
        while True:
            parent_indexes = choose_parents(best_cases)
            childrens = create_children(parent_indexes, best_cases)
            m_children = mutate(childrens, classes)
            bests = choose_bests(best_cases, parent_indexes, m_children, expected_entropy)
            if len(bests) == 1:
                self.finished.emit(bests[0])
                return
            best_cases = replace_parents_with_bests(bests, parent_indexes, best_cases)
            if count%100000 == 0:
                min_idx = np.argsort(abs(array_to_entropy(array)-expected_entropy) for array in best_cases)[0]
                if best_min == array_to_entropy(best_cases[min_idx]):
                    self.finished.emit(best_cases[min_idx])
                    return
                best_min = array_to_entropy(best_cases[min_idx])
            count += 1
        

app = QApplication(sys.argv)
window = Ui()
app.exec_()


