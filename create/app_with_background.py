import sys
import csv
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt6.QtGui import QPixmap, QPainter, QPen, QColor
from PyQt6.QtCore import QSize, Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.points = []
        self.stroke_id = 0
        self.stroke_point_id = 0

        self.setFixedSize(400,400)
        self.setWindowTitle("Drawing App")
        
        self.previousPoint = None

        self.label = QLabel()

        self.canvas = QPixmap('background.png')

        self.pen = QPen()
        self.pen.setWidth(6)
        self.pen.setCapStyle(Qt.PenCapStyle.RoundCap)

        self.label.setPixmap(self.canvas)
        self.setCentralWidget(self.label)

    def mouseMoveEvent(self, event):
        position = event.pos()

        painter = QPainter(self.canvas)
        painter.setPen(self.pen)

        if self.previousPoint: 
            painter.drawLine(self.previousPoint.x(), self.previousPoint.y(), position.x(), position.y())
        else: 
            painter.drawPoint(position.x(), position.y())
        
        self.points.append([self.stroke_id, self.stroke_point_id, position.x(), position.y()])
        self.stroke_point_id +=1
        
        painter.end()

        self.label.setPixmap(self.canvas)
        self.previousPoint = position

    def mouseReleaseEvent(self, event):
        self.previousPoint = None
        self.stroke_id += 1

    def closeEvent(self, event):
        print("closing")
        
        print(self.points)
        n = len(sys.argv)
        if n == 2:
            filename = sys.argv[1]
            print(filename)
            with open(filename, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["Stroke Id", "Stroke Point Id", "X Position", "Y Position"])
                writer.writerows(self.points)
        
        event.accept() # let the window close

if __name__ == "__main__":
        app = QApplication([])
        window = MainWindow()
        window.show()
        app.exec()
