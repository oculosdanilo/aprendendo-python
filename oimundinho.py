import sys

from PySide6.QtCore import Slot
from PySide6.QtWidgets import QApplication, QPushButton


@Slot()
def morri():
  print("foi pra casa do caralho")


app = QApplication(sys.argv)
botao = QPushButton("e cadê o amor?")
botao.clicked.connect(morri)
botao.show()
app.exec()
