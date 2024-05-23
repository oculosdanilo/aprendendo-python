import sys

from PySide6.QtCore import Slot
from PySide6.QtWidgets import QApplication, QPushButton


@Slot()
def morri():
  print("o quee😨")


app = QApplication(sys.argv)
botao = QPushButton("e cadê o amor foi pra casa do caralho")
botao.clicked.connect(morri)
botao.show()
app.exec()
