from PyQt5.QtMultimedia import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import static
import geo


class MapsAPI(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(900, 600)

        self.search_input = QLineEdit()

        self.search_button = QPushButton("Искать", clicked=self.search)

        self.name_adress = QTextEdit()

        self.type_of_map = QComboBox()
        self.type_of_map.addItem("Схема")
        self.type_of_map.addItem("Спутник")
        self.type_of_map.addItem("Гибрид")
        self.type_of_map.currentIndexChanged.connect(self.choise_type)

        self.scale = QScrollBar(Qt.Orientation.Horizontal)

        self.index = QCheckBox("Приписывание почтового индекса")

        self.adress = geo.Get("Москва Красная площадь, 1")
        self.size_map = "600,400"
        self.spn = 0.004
        self.x, self.y = self.adress.Get_Coords().split(",")
        self.cur_type = "map"

        static.get_image(
            "test.png",
            self.size_map,
            self.adress.Get_Coords(),
            self.spn,
            self.cur_type,
        )
        self.curr_image = QImage("test.png")
        self.curr_image.convertTo(17)
        self.label = QLabel()
        self.label.setPixmap(QPixmap.fromImage(self.curr_image))

        layout = QHBoxLayout(self)
        hbox = QHBoxLayout()
        hbox.addWidget(self.label)

        vbox = QVBoxLayout()
        vbox.addWidget(self.search_input)
        vbox.addWidget(self.search_button)
        vbox.addWidget(self.name_adress)
        vbox.addStretch()
        vbox.addWidget(self.type_of_map)
        vbox.addWidget(self.scale)
        vbox.addWidget(self.index)

        layout.addLayout(vbox)
        layout.addLayout(hbox, 2)

    def search(self):
        self.adress = geo.Get(self.search_input.text().lower())
        self.x, self.y = self.adress.Get_Coords().split(",")
        self.spn = 0.004
        self.coords = self.adress.Get_Coords().split(",")
        self.update_map()

    def choise_type(self):
        types_map = {"Схема": "map", "Гибрид": "sat,skl", "Спутник": "sat"}
        self.cur_type = types_map[self.type_of_map.currentText()]
        self.update_map()

    def update_map(self):
        self.coords = f"{str(self.x)},{str(self.y)}"
        static.get_image(
            "test.png", self.size_map, self.coords, self.spn, self.cur_type
        )
        self.curr_image = QImage("test.png")
        self.curr_image.convertTo(17)
        self.label.setPixmap(QPixmap.fromImage(self.curr_image))

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_PageUp:
            self.spn += self.spn / 2
            self.spn = min(self.spn, 78.80268954418264)
            self.update_map()

        elif event.key() == Qt.Key_PageDown:
            self.spn -= self.spn / 2
            self.spn = max(self.spn, 0.00032471191406243174)
            self.update_map()

        elif event.key() == Qt.Key_Left:
            self.x = float(self.x) - self.spn / 4
            self.update_map()

        elif event.key() == Qt.Key_Right:
            self.x = float(self.x) + self.spn / 4
            self.update_map()

        elif event.key() == Qt.Key_Up:
            self.y = float(self.y) + self.spn / 4
            self.update_map()

        elif event.key() == Qt.Key_Down:
            self.y = float(self.y) - self.spn / 4
            self.update_map()


app = QApplication([])
ex = MapsAPI()
ex.show()
app.exec()
